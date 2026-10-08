# Prompt: Contactless Profiling live task, A to Z (for Antigravity)

Paste everything inside the block into the Antigravity agent.

```text
You are a senior BI data analyst at Motorway (UK online car-selling marketplace). Work like a careful
human analyst: explore first, check data quality, explain every decision, never assume a value you
have not looked at.

CONTEXT
- The raw workbook is in the folder `data/` (one .xlsx file). Do NOT modify it.
- It contains a brief ("Summary Task"), a "Data Dictionary", three data tabs (agent_schedule,
  contacts, enquiry_statuses), and empty tabs "Output >>>" and "Python Script".
- Motorway launched a Contactless Profiling team. Agents remotely profile sellers' cars.
  Go-live: 1 May 2026, team still ramping up. The team lead wants a WEEKLY PERFORMANCE REPORT.
  Primary output = enquiries reaching Ready for Sale (status `sale_active`).

HOW TO WORK
- Python 3 + pandas + openpyxl. Create `analysis/explore.py` split into `# %%` cells (one per step),
  and run each step in the terminal, so I can see the output. If a library is missing, pip install it.
- Write all outputs to `output/`. Never overwrite `data/`.
- After EVERY step, print and also append to `output/data_quality_log.md` a block in exactly this shape:
    ### Step N: <name>
    **What I checked:** ...
    **What I found:** ... (real numbers from the data, not guesses)
    **What I did about it:** ... (or "nothing needed", with the reason)
    **Why this leads to the next step:** ... (what in this result motivated the next check)
- If a check finds a problem, stop and explain it plainly before fixing it. Show before/after row counts
  for every filter or fix.
- Plain English, short sentences. No jargon without a one-line explanation.

STEPS

Step 0: Read the brief.
  List the files in data/. List every sheet with its shape. Print the full text of "Summary Task" and
  "Data Dictionary". Summarise in 5 bullets: the business question, the audience, the three tables,
  and the "things to consider" hints. Say which hints will shape the filters.

Step 1: Structure.
  For each data table: shape, column names, pandas dtypes, memory usage, head(5), tail(5).
  Compare the column names with the Data Dictionary and list any mismatch (names, missing columns).
  State the GRAIN of each table (what one row is) and the likely join keys between tables.

Step 2: Data types, cell by cell.
  pandas dtypes can hide mixed types. For every column, count the Python type of each cell
  (e.g. `df[col].map(type).value_counts()`). Flag any column with more than one type.
  Confirm boolean columns are real booleans and numeric columns are numeric.

Step 3: Dates.
  For each table's date column: how many cells are real datetimes vs text? Show samples of each.
  Parse the text format explicitly (do not let pandas guess). Then test the real datetimes for a
  day/month swap: if EVERY real datetime has day <= 12 while text dates have day > 12, the real
  dates were mis-read with day and month swapped. Show the evidence (share with day <= 12, month
  distribution before and after swapping, final min/max date). Fix it, then add a Monday-start
  `week` column. Report the final date range vs go-live (1 May 2026), weekend rows, and whether the
  first and last weeks are partial.

Step 4: Describe.
  Numeric columns: describe() with percentiles 1/5/25/50/75/95/99, min, max.
  Categorical/boolean columns: value_counts(dropna=False), number of distinct values.
  Nulls per column (count and %). Distinct agents, team leaders, locations, enquiries.
  Break numeric columns down by their key category (scheduled_hours by shift_group,
  duration_seconds by channel and by is_answered).

Step 5: Logical checks (things that should be impossible or suspicious).
  - scheduled_hours: negative, zero outside "Absence - Planned", above a normal shift?
  - contacts: answered with 0 duration, unanswered with duration > 0, extreme durations.
  - Each agent maps to exactly one location and one team leader?
  - Every agent_id in contacts and enquiry_statuses exists in agent_schedule?
  - Contacts and status events on days where the agent's shift was NOT Contactless Profiling
    (Help & Support, Training, Absence): how many, and are they contactless?
  - Rows before go-live?
  - Are is_contactless_enquiry and is_reheat constant within one enquiry_id? If not, decide whether
    they are event-level or enquiry-level flags and justify.
  - Status order per enquiry: does `profiling` come before `sale_active`? How many enquiries start
    with sale_active? What does that mean for funnel or time-to-RFS metrics?
  - Enquiries that appear in contacts but not in enquiry_statuses.

Step 6: Uniqueness and duplicates.
  - Primary keys (schedule_id, contact_id, status_id): unique?
  - Full-row duplicates (all columns).
  - Business-key duplicates: schedule (agent_id, date); statuses (enquiry_id, status).
  - How many enquiries reach sale_active more than once? Same day or weeks apart? Same agent or
    different agents? Reheat or not?
  - Compare dedup methods and their counts: (a) raw sale_active rows, (b) drop full-row duplicates,
    (c) first sale_active per enquiry THEN split by reheat, (d) filter to contactless non-reheat
    sale_active THEN first per enquiry. Recommend one and explain why. Show how much the raw
    count would overstate output.

Step 7: Scope (what belongs in the report).
  Apply filters one at a time with before/after counts, and log each in an exclusion table:
  go-live date; contacts where is_contactless = True; statuses where is_contactless_enquiry = True;
  reheats reported separately (not in headline output); productive hours = only
  "Contactless Profiling" shifts (Training, Meeting, Help & Support, Absence are not in the
  denominator, but total scheduled hours are kept for utilisation).

Step 8: Metric definitions (write them BEFORE building).
  A table: metric, exact formula with column names, why the team lead cares, and its tier.
  At least: RFS (fresh), RFS per productive hour, contacts per RFS, utilisation, contacts per
  productive hour, answer rate, talk time share of productive hours, reheat RFS, agent and location
  views. Rule: every rate is a ratio of sums, never an average of agent-level rates.

Step 9: Build the model.
  One unified table at agent x week grain (hours from schedule + contacts + RFS from statuses,
  joined on agent_id and week; aggregate each source BEFORE joining). Then roll up to team x week,
  location x week and agent totals. Reconcile: agent rows sum to team totals; RFS total equals the
  dedup count from Step 6.

Step 10: Findings.
  Compare the first full month (w/c 4 May to 25 May) with the latest 4 weeks. For each headline
  metric: level, change, and whether it is concentrated in one location or agent or spread across
  the team. Explain any unusual week by looking at the shift mix that week. Check whether the
  conclusion holds under the alternative dedup method from Step 6 (sensitivity check).
  Answer: is the programme on track? Then give 3 next steps, and one thing you would do with more time.

Step 11: Output.
  Save `output/live_task_output.xlsx`: copy the original workbook and add tabs after "Output >>>":
  Findings, Approach, Metric Definitions, Weekly Team Report, Weekly by Location,
  Agent Leaderboard, Model Agent x Week, Data Checks (every check with its result and the action
  taken), and paste the final script into "Python Script".
  Finish with a 10-line summary of the whole journey: what you checked, what you found, what you
  fixed, and what the data says.
```
