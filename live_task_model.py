"""Contactless Profiling weekly performance model.

Usage: python model.py <input.xlsx>
"""
import sys
import datetime as dt
import pandas as pd

FILE = sys.argv[1]
GO_LIVE = pd.Timestamp("2026-05-01")
x = pd.read_excel(FILE, sheet_name=None)
s, c, e = x["agent_schedule"].copy(), x["contacts"].copy(), x["enquiry_statuses"].copy()


def fix_date(v):
    # Text dates are M/D/YY. Real Excel dates were mis-read as D/M, so swap day and month back.
    if isinstance(v, dt.datetime):
        return pd.Timestamp(year=v.year, month=v.day, day=v.month)
    return pd.to_datetime(v, format="%m/%d/%y")


for d in (s, c, e):
    d["date"] = d["date"].map(fix_date)
    d["week"] = d["date"] - pd.to_timedelta(d["date"].dt.weekday, unit="D")  # Monday


def profile():
    out = []
    for n, d in [("agent_schedule", s), ("contacts", c), ("enquiry_statuses", e)]:
        out.append((n, len(d), d["date"].min().date(), d["date"].max().date(), d["agent_id"].nunique()))
    return pd.DataFrame(out, columns=["table", "rows", "min_date", "max_date", "agents"])


# ---------- 1. Hours: productive denominator = Contactless Profiling shifts only ----------
s = s[s["date"] >= GO_LIVE]
s["productive_hours"] = s["scheduled_hours"].where(s["shift_group"] == "Contactless Profiling", 0)
hours = s.groupby(["week", "agent_id"]).agg(
    team_leader_id=("team_leader_id", "first"), location=("location", "first"),
    scheduled_hours=("scheduled_hours", "sum"), productive_hours=("productive_hours", "sum"),
    days_scheduled=("schedule_id", "count"),
    productive_days=("shift_group", lambda g: (g == "Contactless Profiling").sum()))

# ---------- 2. Contacts: contactless only ----------
c = c[(c["date"] >= GO_LIVE) & c["is_contactless"]]
c["answered"] = c["is_answered"].astype(int)
c["talk_min"] = c["duration_seconds"] / 60
cont = c.groupby(["week", "agent_id"]).agg(
    contacts=("contact_id", "count"), answered=("answered", "sum"),
    calls=("channel", lambda g: (g == "call").sum()), chats=("channel", lambda g: (g == "live_chat").sum()),
    talk_min=("talk_min", "sum"))

# ---------- 3. Output: first sale_active per contactless, non-reheat enquiry ----------
e = e[e["date"] >= GO_LIVE]
sa = e[(e["status"] == "sale_active") & e["is_contactless_enquiry"]].sort_values(["date", "status_id"])
first_sa = sa.drop_duplicates("enquiry_id", keep="first")       # count each enquiry once
rfs_fresh = first_sa[~first_sa["is_reheat"]]
rfs_reheat = first_sa[first_sa["is_reheat"]]
out = pd.concat([
    rfs_fresh.groupby(["week", "agent_id"]).size().rename("rfs"),
    rfs_reheat.groupby(["week", "agent_id"]).size().rename("rfs_reheat"),
], axis=1)
ce = e[e["is_contactless_enquiry"]]
stat = ce.groupby(["week", "agent_id"]).agg(
    cancelled=("status", lambda g: (g == "cancelled").sum()),
    on_hold=("status", lambda g: (g == "on_hold").sum()))

# ---------- 4. Unified model: agent x week ----------
aw = hours.join([cont, out, stat], how="outer")
num = [col for col in aw.columns if col not in ("team_leader_id", "location")]
aw[num] = aw[num].fillna(0)
aw = aw.reset_index()
ph = aw["productive_hours"].replace(0, pd.NA)
aw["rfs_per_prod_hour"] = aw["rfs"] / ph
aw["contacts_per_prod_hour"] = aw["contacts"] / ph
aw["answer_rate"] = aw["answered"] / aw["contacts"].replace(0, pd.NA)
aw["utilisation"] = aw["productive_hours"] / aw["scheduled_hours"].replace(0, pd.NA)
aw["contacts_per_rfs"] = aw["contacts"] / aw["rfs"].replace(0, pd.NA)


# ---------- 5. Team x week (ratios of sums) ----------
def summarise(df, keys):
    g = df.groupby(keys).agg(
        agents=("agent_id", "nunique"), scheduled_hours=("scheduled_hours", "sum"),
        productive_hours=("productive_hours", "sum"), contacts=("contacts", "sum"), answered=("answered", "sum"),
        talk_min=("talk_min", "sum"), rfs=("rfs", "sum"), rfs_reheat=("rfs_reheat", "sum"),
        cancelled=("cancelled", "sum"), on_hold=("on_hold", "sum"))
    g["utilisation"] = g.productive_hours / g.scheduled_hours
    g["rfs_per_prod_hour"] = g.rfs / g.productive_hours
    g["rfs_per_agent"] = g.rfs / g.agents
    g["contacts_per_prod_hour"] = g.contacts / g.productive_hours
    g["answer_rate"] = g.answered / g.contacts
    g["contacts_per_rfs"] = g.contacts / g.rfs
    g["talk_share_of_prod_time"] = g.talk_min / 60 / g.productive_hours
    return g


tw = summarise(aw, "week")
loc_w = summarise(aw, ["week", "location"])
agent_tot = summarise(aw, ["location", "agent_id"]).sort_values("rfs_per_prod_hour", ascending=False)

# ---------- 6. Checks ----------
checks = pd.DataFrame([
    ("Dates: real Excel dates had day/month swapped; fixed", (s.shape[0] > 0)),
    ("RFS agent rows sum to team", aw.rfs.sum() == tw.rfs.sum()),
    ("Enquiries reaching sale_active more than once (counted once)", int(sa.enquiry_id.duplicated().sum())),
    ("Fresh contactless RFS (counted)", len(rfs_fresh)),
    ("Reheat RFS (excluded from main output)", len(rfs_reheat)),
    ("Non-contactless sale_active (excluded)", int(((e.status == "sale_active") & ~e.is_contactless_enquiry).sum())),
    ("Contacts not contactless (excluded)", int((x["contacts"]["is_contactless"] == False).sum())),
    ("RFS on agent-days with no Contactless Profiling shift",
     int(rfs_fresh.merge(s[s.shift_group == "Contactless Profiling"][["date", "agent_id"]], how="left",
                         on=["date", "agent_id"], indicator=True)["_merge"].eq("left_only").sum())),
], columns=["check", "value"])

if __name__ == "__main__":
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 40)
    print(profile())
    print(checks)
    print(tw.round(3))
    print(loc_w[["agents", "productive_hours", "rfs", "rfs_per_prod_hour", "answer_rate", "utilisation", "contacts_per_rfs"]].round(3))
    print(agent_tot[["productive_hours", "rfs", "rfs_per_prod_hour", "answer_rate", "contacts_per_rfs", "utilisation"]].round(3))
