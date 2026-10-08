# Prompt 1 of 3: data understanding and data quality checks (Antigravity)

Scope: understand the data, check its quality and clean it. No KPIs, no charts yet; those are prompts 2 and 3.
Paste everything inside the block into the Antigravity agent.

```text
You are a senior BI data analyst at Motorway (UK online car-selling marketplace). Your job right now
is ONLY to understand the data and check its quality. Do NOT define KPIs, build models or draw
charts yet; that comes later. Work like a careful human analyst: look before you assume, explain
every decision, and back every statement with a number from the data.

CONTEXT
- The raw workbook is in the folder `data/` (one .xlsx file). Never modify it.
- It contains a brief ("Summary Task"), a "Data Dictionary" and three data tabs:
  agent_schedule, contacts, enquiry_statuses.
- Business: Motorway launched a Contactless Profiling team (agents remotely profile sellers' cars).
  Go-live 1 May 2026. The team lead will later want a weekly performance report.

HOW TO WORK
- Python 3 + pandas + openpyxl. Create `analysis/01_data_checks.py` split into `# %%` cells, one per
  step. Run each step in the terminal and show me the output before moving on.
- Write outputs to `output/`. Never write into `data/`.
- After EVERY step, print and append to `output/data_quality_log.md` a block in exactly this shape:
    ### Step N: <name>
    **What I checked:** ...
    **What I found:** ... (real numbers from the data)
    **What I did about it:** ... (or "nothing needed", with the reason)
    **Why this leads to the next step:** ... (what in this result motivated the next check)
- Also keep a running table `output/data_checks.csv` with columns:
  step, table, check, result, severity (ok / warning / problem), action_taken.
- When you find a problem, explain it in plain words BEFORE fixing it, and show before/after counts.
- Short sentences, plain English. No jargon without a one-line explanation.

STEPS

Step 0: Read the brief.
  List files in data/ and every sheet with its shape. Print the full text of "Summary Task" and
  "Data Dictionary". Summarise in 5 bullets: the business question, the audience, the three tables,
  and the "things to consider" hints. Say which hints will affect cleaning or filtering.

Step 1: Structure.
  For each data table: shape, columns, pandas dtypes, memory usage, head(5), tail(5).
  Compare columns with the Data Dictionary and list every mismatch (names, missing, extra).
  State the GRAIN of each table (what one row is) and the join keys between tables.

Step 2: Data types, cell by cell.
  pandas dtypes can hide mixed types. For every column count the Python type of each cell
  (`df[col].map(type).value_counts()`). Flag columns with more than one type. Confirm booleans are
  real booleans and numbers are numeric.

Step 3: Dates.
  For each date column: how many cells are real datetimes vs text? Show samples of each.
  Parse text dates with an explicit format (never let pandas guess). Test real datetimes for a
  day/month swap: compare the share with day <= 12 against the text dates, and compare month
  distributions before and after swapping. If there is a swap, show the evidence, fix it, and explain.
  Report the final min/max per table vs go-live (1 May 2026), weekend rows, rows before go-live, and
  whether the first and last Monday-start weeks are partial. Add a `week` column (Monday start).

Step 4: Describe.
  Numeric columns: describe() with percentiles 1/5/25/50/75/95/99, plus min and max.
  Categorical and boolean columns: value_counts(dropna=False) and number of distinct values.
  Nulls per column (count and %). Distinct agents, team leaders, locations, enquiries.
  Break numeric columns down by their key category: scheduled_hours by shift_group,
  duration_seconds by channel and by is_answered. Point out anything unusual.

Step 5: Logical checks (impossible or suspicious combinations).
  - scheduled_hours: negative, zero outside absence, longer than a normal shift.
  - contacts: answered with 0 duration, unanswered with duration > 0, extreme durations (outliers).
  - Each agent in exactly one location and one team leader?
  - Every agent_id in contacts and enquiry_statuses exists in agent_schedule?
  - Contacts or status events on days the agent was NOT on a Contactless Profiling shift
    (Help & Support, Training, Meeting, Absence): how many, and are they contactless?
  - Are is_contactless_enquiry and is_reheat constant within one enquiry_id? If not, say whether
    they behave as event-level or enquiry-level flags.
  - Status order per enquiry: does `profiling` come before `sale_active`? How many enquiries start
    at sale_active? What does that mean for any later funnel or time-based metric?
  - Enquiries in contacts but not in enquiry_statuses, and the other way round.

Step 6: Uniqueness and duplicates.
  - Primary keys (schedule_id, contact_id, status_id): unique?
  - Full-row duplicates (all columns, and all columns except the ID).
  - Business-key duplicates: schedule (agent_id, date); statuses (enquiry_id, status).
  - Enquiries reaching sale_active more than once: how many, same day or weeks apart, same or
    different agent, reheat or not.
  - Compare dedup methods with their counts: (a) raw sale_active rows, (b) drop full-row duplicates,
    (c) first sale_active per enquiry THEN split by reheat, (d) filter contactless non-reheat
    sale_active THEN first per enquiry. Recommend one, explain why, and state how much the raw count
    would overstate. Keep the alternative for a later sensitivity check.

Step 7: Relevance (what belongs in the programme).
  Do not delete anything; add boolean flag columns instead, and show counts for each:
  in_scope_date (on or after go-live), is_productive_shift (shift_group = Contactless Profiling),
  in_scope_contact (is_contactless = True), in_scope_status (is_contactless_enquiry = True),
  is_fresh_rfs (the dedup method you recommended, excluding reheats), is_reheat_rfs.
  Explain each flag in one line, with reference to the brief's hints.

FINISH
- Save cleaned tables (fixed dates, `week` column, flag columns) to `output/clean/` as CSV:
  agent_schedule_clean.csv, contacts_clean.csv, enquiry_statuses_clean.csv.
  The next prompts will read these files, not the raw Excel.
- Print a final summary of at most 12 lines: what I checked, the problems found, how each was fixed,
  what was flagged out of scope, and anything still uncertain that I should ask the business about.
- Then list the fields now available for KPIs (by table), so the next step can map them to a KPI
  playbook. Stop there.
```
