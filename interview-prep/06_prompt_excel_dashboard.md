# Prompt 3 of 3: the same dashboard in Excel (filterable, native charts)

Part A explains the design, for you. Part B is the prompt for Antigravity. Run it after prompts 1 and 2.

---

## Part A: how the Excel version mirrors Streamlit

**The goal:** someone opening the Excel file later sees the same KPIs, the same charts, the same titles and colours, and the same ⓘ explanations as in the Streamlit dashboard, and can filter it themselves.

**How filtering works.** Rates must be recalculated after filtering. A pivot table's "average" would average the rates, which is wrong. So the workbook works like this:
- **Fact tabs:** raw numerators and denominators per agent per week (hours, contacts, answered, Ready for Sale…).
- **Calc tabs:** formulas such as `SUMIFS` pick rows using the dropdowns at the top of the Dashboard (week range, location, team leader, agent, channel, de-dup method). They add up the numerators and the denominators, *then* divide. So every rate is a ratio of sums, exactly as in Streamlit.
- **Native Excel charts** are linked to the Calc tabs, so they redraw whenever a dropdown changes. "All" in a dropdown uses the `"*"` wildcard, so one formula handles both "All" and a single value.
- **Info buttons:** an ⓘ cell next to every KPI card and chart, with a hover note holding the same four lines as Streamlit.
- **Totals check:** with all filters set to "All", check cells compare the workbook's totals with the Python totals and show PASS or FAIL.

**How each Streamlit chart maps to Excel:**

| Streamlit | Excel |
|---|---|
| Headline number with change (st.metric) | KPI card: big value cell, change vs previous week, conditional green/red arrow |
| Stacked column (fresh + reheat RFS) | Stacked column chart |
| Line + dashed May baseline | Line chart + a second constant series formatted as a grey dashed line |
| Hours by shift group + utilisation underneath | Stacked column chart, with a separate line chart directly below (no second axis) |
| 100% stacked column (channel mix) | 100% stacked column chart |
| One line per channel or location | Line chart, one series each, fixed colours |
| Ranked horizontal bar (agents) | Bar chart fed by a formula-sorted table, plus team-rate reference series |
| Heatmap (agent × week) | Formula grid with a blue colour-scale conditional format |
| Agent table with progress bars | Table with data bars |
| Definitions and data checks tab | Definitions and Data Checks sheets |

**If Shuma prefers pivot tables:** the `Fact_AgentWeek` sheet is formatted as an Excel Table, so you can also go Insert → PivotTable → add Slicers for location, team leader and week. For rates, use **PivotTable Analyze → Fields, Items & Sets → Calculated Field**, for example `= fresh_rfs / productive_hours`. A calculated field divides the *sums*, which is correct. Never use "Average of rate".

---

## Part B: the prompt

```text
You are a senior BI data analyst at Motorway. Prompts 1 and 2 cleaned the data, computed the KPIs
(app/metrics.py) and built a Streamlit dashboard. Now build the SAME dashboard as an Excel workbook
so a team lead can open it later, filter it, and see exactly what the Streamlit app showed: same
KPIs, same definitions, same chart titles, same colours, same info text.

INPUTS (stop and tell me if missing)
- app/metrics.py, app/kpi_info.py (INFO, TITLES, COLOURS, KPI_DEFS). If kpi_info.py does not exist,
  first move those dicts out of app/dashboard.py into app/kpi_info.py and make the dashboard import
  them, then re-run the dashboard to confirm it still works.
- output/kpis/*.csv (agent x week with all numerators and denominators), output/clean/*.csv,
  output/data_checks.csv.

TOOLS
- Python + xlsxwriter (native Excel charts, data validation, comments, conditional formatting,
  Excel Tables). pip install xlsxwriter if missing.
- Script: app/build_excel.py. Output: output/contactless_weekly_dashboard.xlsx.
- Target Excel 365 (also check that every formula you use works in Google Sheets; list any that don't).

SHEETS (in this order)
1 "Read me": what the workbook is, how to use the filters, that rates are ratios of sums, the date
  fix and dedup from the data checks, and how to refresh (re-run build_excel.py).
2 "Dashboard": filters, KPI cards and all charts (see below).
3 "Calc_Weekly", 4 "Calc_Agents", 5 "Calc_Heatmap", 6 "Calc_HandleTime": formula tabs feeding the charts.
7 "Fact_AgentWeek": one row per agent x week, as an Excel Table named tblAgentWeek. Columns:
  week (real date), week_label (e.g. "w/c 04 May", with " (partial)" for partial weeks), is_partial,
  agent_id, location, team_leader_id, scheduled_hours, productive_hours, hours_training,
  hours_meeting, hours_help_support, hours_absence, contacts_call, contacts_chat, answered_call,
  answered_chat, talk_sec_call, talk_sec_chat, fresh_rfs_first_then_split,
  fresh_rfs_filter_then_first, reheat_rfs.
8 "Fact_Contacts": answered contactless contacts only (week, agent_id, location, team_leader_id,
  channel, duration_min), as Table tblContacts, for median handle time.
9 "Definitions": KPI_DEFS (name, formula, numerator, denominator, tier, playbook link) and the
  "not measurable with this data" list.
10 "Data Checks": output/data_checks.csv.
Freeze header rows, set column widths, number formats (0.00 for rates, 0% for shares, #,##0 counts).

DASHBOARD FILTERS (top of the Dashboard sheet, clearly labelled cells with dropdowns)
- Start week, End week (lists of week_label), Reporting week (default = latest full week),
  Location, Team leader, Agent (each list starts with "All"), Channel (All / call / live_chat),
  Dedup method (first_then_split / filter_then_first).
- Put the dropdown source lists on a hidden "Lists" sheet. Use named ranges for every filter cell
  (sel_start, sel_end, sel_week, sel_loc, sel_tl, sel_agent, sel_channel, sel_dedup).
- "All" handling: criteria = IF(sel_loc="All","*",sel_loc) inside SUMIFS (same for team leader and agent).
- Channel handling: contacts = IF(channel="All", call+chat, the chosen column) using CHOOSE/IF.
- Dedup handling: fresh_rfs = IF(sel_dedup="first_then_split", col A, col B).

CALC_WEEKLY (one row per week; every value is a formula)
- For each week: SUMIFS of every numerator and denominator, applying all filters, then the rates:
  fresh_rfs, reheat_rfs, productive_hours, scheduled_hours, hours by shift group, contacts, answered,
  rfs_per_prod_hour, contacts_per_rfs, utilisation, answer_rate, contacts_per_prod_hr, chat_share,
  reheat_share, agents_active (COUNTIFS of agents with productive_hours > 0).
- Rows outside the Start–End week range return NA() so charts skip them.
- May baseline columns (w/c 4 May to 25 May, same filters) as constants down the column, for
  the dashed reference series.
- Wrap divisions in IFERROR(..., NA()) so an empty filter shows a gap, not a #DIV/0!.

CALC_AGENTS (one row per agent, over the selected week range and filters)
- productive_hours, fresh_rfs, contacts, answered, rfs_per_prod_hour, contacts_per_rfs,
  answer_rate, utilisation; include only agents with >= 20 productive hours in the ranking (say so).
- A sorted block (highest rfs_per_prod_hour first) using RANK.EQ plus a COUNTIF tie-breaker and
  INDEX/MATCH, so the ranked bar chart re-sorts when filters change. Add the team rate as a
  constant column for the reference series.

CALC_HEATMAP: agent rows x week columns of rfs_per_prod_hour (formulas, same filters except agent),
  with a 3-colour scale in single-hue blue (#cde2fb low → #2a78d6 → #0d366b high); blanks for NA.
CALC_HANDLETIME: per week and channel, median duration_min of tblContacts with the filters
  (MEDIAN(FILTER(...)) in Excel 365). If it is too slow, precompute it in Python instead, and add a
  note on the chart that it follows only the location/channel filters.

KPI CARDS (top of Dashboard, 4 cards matching Streamlit)
Fresh RFS | RFS per productive hour | Contacts per RFS | Utilisation.
Each card: title, value for the Reporting week, change vs the previous full week (absolute and %),
an arrow with conditional formatting (green #0ca30c = better, red #d03b3b = worse; for Contacts per
RFS, up is worse), the May baseline underneath, and an "ⓘ" cell whose comment holds INFO[kpi].

CHARTS (native xlsxwriter charts, same order, titles and colours as Streamlit; group them under
section headers matching the Streamlit tab names: "Output & productivity", "Effort & contact
quality", "Capacity", "Agents & locations")
 - Fresh RFS per week: stacked column (fresh #2a78d6, reheat grey #b4b2a9).
 - RFS per productive hour: line #2a78d6 with markers, plus May baseline as a dashed #52514e series.
 - Contacts per productive hour: line, directly below the previous chart.
 - Contacts per RFS: line + May baseline (dashed).
 - Answer rate: line, y-axis 0.8–1.0, plus average (dashed).
 - Median handle time: two lines (call #2a78d6, live_chat #eb6834).
 - Channel mix: 100% stacked column (call, live_chat).
 - Scheduled hours by shift group: stacked column (Contactless Profiling #2a78d6, Training #eb6834,
   Meeting #1baf7a, Help & Support #eda100, Absence #e87ba4), and directly below it a separate
   utilisation line chart with the same week categories. NEVER use a secondary y-axis.
 - Agents active per week: column.
 - Agent ranking: horizontal bar of rfs_per_prod_hour from the sorted block, plus the team rate as a
   dashed reference series.
 - RFS per productive hour by location: one line per location (Cape Town #2a78d6, London #eb6834,
   Manchester #1baf7a). Build Calc rows per location for this.
 - Heatmap: link to or copy Calc_Heatmap onto the Dashboard.
 - Agent table: from Calc_Agents with data bars on rfs_per_prod_hour and fresh_rfs.
Every chart: title from TITLES, axis titles with units, legend at the bottom when 2+ series (none
for one), light gridlines, lines 2.25pt, markers size 7, category axis = week_label (partial weeks
already labelled "(partial)"). Next to every chart, put an "ⓘ" cell with a comment holding INFO[chart]
(comment box wide enough to read; comments visible on hover, not always shown).

RECONCILIATION (must PASS)
- On the Data Checks sheet, add a "Workbook vs Python" block: for the "All" filter state, the static
  totals from metrics.py (fresh_rfs, productive_hours, contacts, rfs_per_prod_hour for the full range)
  next to the live formula totals from Calc_Weekly, with =IF(ABS(a-b)<0.0001,"PASS","FAIL").
- Write cached formula results with xlsxwriter's `value=` argument using the "All" state values, so
  the file shows correct numbers even before Excel recalculates.
- After building, re-open the file with openpyxl and check: every sheet exists, every chart is
  present, no formula text contains a typo'd sheet or range name, and named ranges resolve.
  Print what you checked.

FINISH
- Run build_excel.py, fix all errors, then tell me: the sheet list, the chart list (in order), the
  filters and how to use them, and any formula that will not work in Google Sheets.
- Remind me to open the file in Excel and check the PASS cells, then change one filter (e.g. Location
  = London) and confirm the charts and cards update.
- Do NOT write insights. I will do that from the charts.
```
