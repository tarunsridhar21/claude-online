# Prompt 2 of 3: derive the KPIs and build the Streamlit dashboard

Part A is the plan, for you to read and explain to Shuma. Part B is the prompt to paste into Antigravity.
It reads the cleaned files from prompt 1 (`output/clean/*.csv`).

---

## Part A: which KPIs, and why

The playbook is written for the whole marketplace. This task is one **operations team**, so I took the
playbook's method (5-criteria scoring, ratio-of-sums rule, visual library V1–V17) and mapped each KPI
to its nearest playbook card (§1.4 translation). Scores use the playbook weights: decision 30%,
goal link 25%, diagnostic 20%, early warning 15%, measurable 10%.

| Rank | KPI | Formula (cleaned columns) | Playbook link | Score | Tier | Main visual |
|---|---|---|---|---|---|---|
| 1 | **RFS per productive hour** | fresh RFS ÷ `scheduled_hours` where `shift_group` = Contactless Profiling | §1.4 output per head; F7 (output per active unit) | 4.50 | Headline | V1 scorecard + V2 line with May baseline |
| 2 | **Contacts per RFS** | contactless contacts ÷ fresh RFS | O4 (contacts per 100 completed sales) | 4.30 | Headline | V1 + V2 line with May baseline |
| 3 | **Fresh RFS (Ready for Sale)** | distinct enquiries, first `sale_active`, contactless, non-reheat | O6 (completed sales: the output count) | 4.15 | Headline | V1 + V5 stacked column (fresh + reheat) |
| 4 | **Utilisation** | productive hours ÷ all scheduled hours | general capacity metric (§1.4) | 3.95 | Core | V5 hours by shift group + V2 utilisation line (two charts, shared x) |
| 5 | **Median handle time** | median `duration_seconds` of answered contacts, by channel | O5/O7 rule: median for time | 3.40 | Core | V2 line per channel |
| 6 | **Answer rate** | answered contacts ÷ contactless contacts | M1-style reach rate | 3.35 | Core | V2 line with band |
| 7 | **Contacts per productive hour** | contactless contacts ÷ productive hours | activity rate | 3.35 | Core | V2 line |
| 8 | **Channel mix** | share of contacts that are live chat | M7-style mix over time | 3.15 | Supporting | V6 100% stacked column |
| 9 | **Reheat share of RFS** | reheat RFS ÷ (fresh + reheat RFS) | C-side supply quality | 2.55 | Supporting | V2 line |
| — | **Agent leaderboard** | KPIs 1–2 per agent, with hours shown | O2 (ranked bar with denominators) | view | Manager | V8 ranked bar + V17 table |
| — | **Location trend** | KPI 1 per location per week | drill-down dimension | view | Manager | V2, one line per location |
| — | **Agent × week heatmap** | KPI 1 per agent per week | P2 cohort grid | view | Manager | V13 heatmap |

**Not measurable with this data** (show this in the dashboard; it's a good talking point):
- funnel and time to RFS (P1, O5): status dates don't run in order per enquiry;
- completion after RFS (O1): no post-sale data;
- cost per RFS (F1, M2): no cost data;
- seller satisfaction (M5): no survey data.

**Design rules** (from the playbook and the dataviz skill):
- **Rates:** every rate is a ratio of sums after filtering, never an average of rates.
- **No dual-axis charts.** Playbook V9 combos become two charts that share the x-axis.
- **Fixed colours** per location and shift group.
- **Status colours** (green/red) only on the change shown under each headline number, never for series.
- **Median, not mean,** for time.
- **Partial weeks** are marked and left out of week-on-week comparisons.

---

## Part B: the prompt

```text
You are a senior BI data analyst at Motorway. Prompt 1 already checked and cleaned the data. Now:
(1) derive the KPIs below in a reusable metrics module, and (2) build a Streamlit dashboard for the
Contactless Profiling TEAM LEAD's weekly performance review. Do not invent numbers: everything must
be computed from the cleaned files. Explain every decision briefly in plain English.

INPUTS (from prompt 1; if missing, stop and tell me)
- output/clean/agent_schedule_clean.csv   (date, week, agent_id, team_leader_id, location, shift_group,
  scheduled_hours, flag columns such as is_productive_shift, in_scope_date)
- output/clean/contacts_clean.csv          (date, week, agent_id, channel, is_contactless, is_answered,
  duration_seconds, enquiry_id, flag columns)
- output/clean/enquiry_statuses_clean.csv  (date, week, agent_id, enquiry_id, status,
  is_contactless_enquiry, is_reheat, is_fresh_rfs, is_reheat_rfs, flag columns)
- output/data_checks.csv and output/data_quality_log.md
First print each file's columns and row count, and confirm the flag columns exist. If a column name
differs, adapt and tell me.

SETUP
- pip install streamlit plotly pandas (if missing). Files:
  app/metrics.py   pure pandas functions, no Streamlit imports (reused later for Excel)
  app/dashboard.py the Streamlit app
  app/test_metrics.py  reconciliation checks (run with: python app/test_metrics.py)
- Run: streamlit run app/dashboard.py. Fix every error until it loads, then tell me the local URL.

PART 1: METRICS (app/metrics.py)
Scope rules (apply before any metric):
- Dates on or after 1 May 2026. Weeks start Monday. Mark a week "partial" if it has fewer working
  days than a full week (w/c 27 Apr covers only 1–3 May).
- Contacts: is_contactless = True only.
- Statuses: is_contactless_enquiry = True only.
- Fresh RFS: the de-duplicated, non-reheat sale_active per enquiry from prompt 1 (is_fresh_rfs).
  Reheat RFS reported separately, never added to the headline.
- Productive hours: scheduled_hours where shift_group = "Contactless Profiling" only. Training,
  Meeting, Help & Support and Absence stay in total scheduled hours (for utilisation) but are NOT in
  any productivity denominator.
- Credit: RFS goes to the agent_id on the status row (the data dictionary says the status is
  attributed to the agent who worked it).
- Build agent x week first, aggregating EACH source on its own before joining (avoids double
  counting). Every rate = sum(numerator) / sum(denominator) AFTER filters. Never average rates.
- Provide a function `kpis(filters)` returning a team x week table with the columns below, and
  `agent_kpis(filters)`, `location_kpis(filters)` for the manager views.
- Add a dedup switch: method "first_then_split" (first sale_active per enquiry, then drop reheats)
  vs "filter_then_first" (drop reheats, then first sale_active per enquiry), so the dashboard can show
  the sensitivity.

KPIs (implement exactly; name columns as given):
 1 rfs_per_prod_hour     = fresh_rfs / productive_hours
 2 contacts_per_rfs      = contacts / fresh_rfs
 3 fresh_rfs             = count of fresh RFS enquiries; also reheat_rfs
 4 utilisation           = productive_hours / scheduled_hours
 5 median_handle_time    = median duration_seconds of ANSWERED contacts, in minutes, by channel
 6 answer_rate           = answered / contacts
 7 contacts_per_prod_hr  = contacts / productive_hours
 8 chat_share            = live_chat contacts / contacts
 9 reheat_share          = reheat_rfs / (fresh_rfs + reheat_rfs)
 Also keep: agents (distinct agent_id with productive hours), productive_hours, scheduled_hours,
 hours by shift_group, contacts, answered, talk_hours (sum duration / 3600).

app/test_metrics.py must check and print PASS/FAIL:
- agent-level fresh_rfs sums to team total; location totals sum to team total
- total fresh_rfs equals the count of is_fresh_rfs rows in scope
- productive_hours <= scheduled_hours every week; all rates between sensible bounds (0–1 for shares)
- no duplicate (agent_id, week) rows in the agent x week table
Run it and show the output before building the dashboard.

PART 2: DASHBOARD (app/dashboard.py)
General:
- st.set_page_config(layout="wide", page_title="Contactless Profiling – Weekly Performance").
- Load data with @st.cache_data. Plotly for all charts: st.plotly_chart(fig, use_container_width=True).
- Title, then a caption: data range, last refreshed, and "Partial weeks are shaded and excluded from
  week-on-week deltas".

Sidebar filters (one place, applied to everything):
- Week range (slider over week starts), Location (multiselect), Team leader (multiselect),
  Agent (multiselect, searchable), Channel (call / live_chat; affects contact metrics only; say so).
- "Reporting week" selectbox (default: latest full week). Headline numbers show that week, with a
  delta vs the previous full week.
- Toggle "Include partial weeks in charts" (default on, shaded grey).
- Radio "RFS de-dup method" (the two methods from metrics.py), with a caption explaining it.

INFO BUTTONS (required)
- Every headline number: use st.metric(..., help=INFO[kpi]) so a (?) icon shows the text on hover.
- Every chart: put a small st.popover("ⓘ") in the chart's header row (st.columns([12,1])).
- Each INFO entry has exactly 4 short lines:
    What it is: one sentence.
    How it's calculated: the formula in words, with the denominator spelled out.
    Why this chart: why this visual suits it.
    How to read it: what a rise or fall MEANS for the team (KPI-level reading, not a deep dive).
- Keep all INFO text, chart TITLES and COLOURS in one shared file, app/kpi_info.py
  (dicts INFO, TITLES, COLOURS, and KPI_DEFS for the definitions table). dashboard.py imports them.
  The Excel build (prompt 3) will reuse the same file, so both outputs say exactly the same thing.
  Write the INFO text from the specs below.

LAYOUT
Row 1: headline (4 st.metric with border=True, in st.columns(4)):
  Fresh RFS | RFS per productive hour | Contacts per RFS (delta_color="inverse": up is bad) |
  Utilisation. Under the row, a caption with the May baseline (w/c 4 May – 25 May) for each.

Then st.tabs: ["Output & productivity", "Effort & contact quality", "Capacity", "Agents & locations",
"Definitions & data quality"].

TAB 1 – Output & productivity
 a) Fresh RFS per week: stacked column (fresh = blue, reheat = grey), labelled total on top of each
    column. Info: output count; reheats shown but not in the headline; a dip can be capacity (check the
    Capacity tab) not performance.
 b) RFS per productive hour per week: line with markers, plus a dashed grey reference line at the May
    baseline, labelled. Info: productivity; the denominator removes training/meetings/absence so it's
    fair week to week; falling = less output per hour worked.
 c) Small multiple under (b): contacts per productive hour (line). Info: activity; read with (b):
    activity up + output per hour down = more effort per car, not less work.

TAB 2 – Effort & contact quality
 a) Contacts per RFS per week: line + May baseline. Info: effort needed per car; rising = each car
    needs more contacts.
 b) Answer rate per week: line, y-axis 0.8–1.0, with the overall average as a dashed line. Info: reach;
    stable answer rate rules out "we can't reach sellers".
 c) Median handle time per week, one line per channel (call, live_chat), minutes. Info: median, not
    mean, because durations are skewed; longer handle time with flat output = harder or longer conversations.
 d) Channel mix: 100% stacked column (call vs live_chat) per week. Info: a shift towards chat can
    change contacts per RFS without any change in performance.

TAB 3 – Capacity
 a) Scheduled hours per week stacked by shift_group (fixed colours, legend). Info: where scheduled
    time goes; a training week shows here first.
 b) Directly below, sharing the same x-axis (NOT a second y-axis): utilisation line with a dashed
    reference at the period average. Info: share of scheduled time spent profiling.
 c) Agents active per week (column). Info: headcount; separates "fewer people" from "less per person".

TAB 4 – Agents & locations (manager view)
 a) Ranked horizontal bar: RFS per productive hour per agent for the selected weeks, sorted, team rate
    as a dashed vertical line, productive hours printed at the end of each bar; hide agents with
    < 20 productive hours (say so in a caption). Info: fair comparison per hour; read with hours,
    since small denominators are noisy.
 b) Table (st.dataframe with column_config progress bars): agent, location, team leader,
    productive hours, fresh RFS, RFS per productive hour, contacts per RFS, answer rate, utilisation.
    Sortable. Download button (CSV).
 c) RFS per productive hour per week, one line per location (fixed colours). Info: tells you whether a
    change is team-wide or one site.
 d) Heatmap agent x week of RFS per productive hour (single-hue blue scale, light = low, dark = high),
    cell value on hover. Info: spot an agent who dropped, or ramp-up patterns.

TAB 5 – Definitions & data quality
 - Table of every KPI: name, formula, numerator, denominator, tier, playbook link.
 - Data checks table from output/data_checks.csv, and the exclusion counts (rows in/out of scope).
 - Dedup sensitivity: fresh RFS and RFS per productive hour under both methods, side by side.
 - "Not measurable with this data" list: funnel / time to RFS (status order not reliable),
   completion after RFS (no post-sale data), cost per RFS (no cost data), seller satisfaction (no survey).

CHART STYLE (apply to every chart)
- Fixed colours, never cycled. Locations: Cape Town #2a78d6, London #eb6834, Manchester #1baf7a.
  Shift groups: Contactless Profiling #2a78d6, Training #eb6834, Meeting #1baf7a,
  Help & Support #eda100, Absence - Planned #e87ba4. Channels: call #2a78d6, live_chat #eb6834.
  Single-series lines: #2a78d6. Reference lines: dashed #52514e with a text label.
- Green #0ca30c / red #d03b3b ONLY for deltas or status, never as a series colour.
- One y-axis per chart (never secondary_y). Lines 2px, markers 8px. Light grid, no chart junk.
- Legend whenever there are 2+ series; titles state the KPI and unit (e.g. "RFS per productive hour").
- Hover tooltips show week, value (2 decimals for rates, % for shares) and the numerator and denominator.
- Shade partial weeks with a light grey vrect and the label "partial".
- Use plotly_white template; the same layout helper function for every chart.

FINISH
- Run test_metrics.py (all PASS), launch the app, fix errors, and click through every tab and filter
  combination at least once (e.g. one location, one agent, chat only) to check nothing breaks or
  shows NaN.
- Then print, for the latest full reporting week and for the May baseline, the value of every headline
  and core KPI in a small table, so I can write the insights. Do NOT write the insights yourself.
- Save the team x week, location x week and agent x week tables to output/kpis/*.csv (needed for the
  Excel step later). The agent x week table must keep every numerator and denominator separately
  (hours by shift_group, contacts / answered / talk seconds split by channel, fresh_rfs under BOTH
  dedup methods, reheat_rfs), not just the rates, so Excel can recompute rates after filtering.
```
