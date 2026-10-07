# KPI playbook for a used-car marketplace

54 KPIs across Finance, Marketing, Operations, Commercial and Product, for a business in the style of Motorway. Each KPI is ranked inside its department, and each has its formula, the data it needs, the insights it can give, the best visual on each platform, and what to use when the data is thin.

## How to use this file

- **Ten minutes:** read Part 1. It shows how the KPIs connect, what to check when one moves, and the ranking for every department.
- **Building a chart:** find the KPI card in Part 4, then follow its visual number (V1 to V17) to Part 3 for the full recipe on your platform.
- **Explaining a KPI out loud:** use the card's formula, one line from "Insights it can give", and the sentence pattern in appendix C.

## Contents

- **Part 1: The map.** How the KPIs connect. What to check when one moves. The ranked tables.
- **Part 2: The method.** Evidence tags. How the ranking works. Rules for every KPI. Single value or chart. What to do when the data is thin.
- **Part 3: The visual library.** 17 visuals, each with when to use it and how to build it in Looker Studio, Streamlit, Python, SQL and the Antigravity IDE.
- **Part 4: The KPI cards.** Finance (F1 to F11), Marketing (M1 to M11), Operations (O1 to O10), Commercial (C1 to C11), Product (P1 to P11).
- **Appendices.** Platform limits. Drill-down terms. A sentence pattern for interviews. Sources and caveats.

Companion files in this folder: the KPI sheets (`1_finance_kpis.png` to `5_product_kpis.png`), the sample dashboards (`dashboard_1_finance.png` to `dashboard_5_product.png`), and `KPI_REFERENCE.md`. The images cover the first 40 KPIs.

---

# Part 1: The map

## 1.1 How the KPIs connect

No KPI stands alone. Profit breaks down into volume, price and cost, and each department owns part of that chain. When a number moves, the cause is usually one level down.

```
PRE-TAX RESULT  (Finance)
├── REVENUE = GMV × take rate
│   ├── GMV = completed sales × average sale price
│   │   ├── Completed sales = valuations started × valuation-to-sale conversion
│   │   │       valuations started ............ Marketing  (volume, channel mix, organic share)
│   │   │       conversion is three gates in a row:
│   │   │         1. the seller finishes the profile ... Product     (funnel completion)
│   │   │         2. a dealer buys the car ............. Commercial  (sell-through)
│   │   │         3. the agreed sale completes ......... Operations  (completion rate)
│   │   └── Average sale price ................ Commercial  (price against guide, bidders per car)
│   └── Take rate ............................. Finance     (fees, mix, Motorway Pay, paid listings)
└── COSTS
    ├── Variable, per car → CONTRIBUTION PER CAR = revenue per car − these
    │       marketing ......................... cost per car sold
    │       transport ......................... cost per move
    │       support ........................... contacts per 100 sales
    └── Fixed → operating costs as a share of revenue, adjusted EBITDA, cash burn and runway

WHAT FEEDS SELL-THROUGH AND PRICE  (the dealer side)
    verified dealers → active dealers → bids per car, bidders per car, time to first bid
    → retention cohorts, concentration

WHAT PROTECTS TRUST ON BOTH SIDES
    valuation accuracy → condition grade accuracy → price changed at collection → claims rate
    verification, problem vehicles stopped → seller satisfaction → review score
```

## 1.2 What to check when a number moves

Work down the chain. Check the cheap explanations (data and timing) before the interesting ones.

| If this moves | Check in this order |
|---|---|
| **Revenue falls** | GMV or take rate? If GMV: completed sales or average price? If sales: valuations, then conversion, then sell-through, then completion rate. |
| **Conversion falls** | Are the newest cohorts simply immature? Then channel mix. Then the funnel step. Then app version or device. |
| **Sell-through falls** | Bids per car and bidders per car (demand). If those hold: supply mix and price against guide. Then one region or segment. |
| **Contribution per car falls** | Revenue per car, then each cost bar: marketing, transport, support. Then the segment where it is negative. |
| **Completion rate falls** | Grouped by the right date? Then price changed at collection, on-time collection, region, dealer. |
| **Cost per car sold rises** | Cost per valuation or conversion? Then channel mix. Then cohort maturity. |
| **Support contacts rise** | Reason. Then release dates. Then days to seller payment. |
| **Claims rise** | A few dealers or all of them? Then condition grade accuracy and price changed at collection. |

## 1.3 The ranking, all five departments

Scores are out of 5. The method is in Part 2.

**Finance:** *Is the marketplace making money, and how far is it from profit?*

| # | KPI | Score | Tier | Format | Main visual | Evidence |
|---|---|---|---|---|---|---|
| F1 | Contribution per car | 4.65 | Headline | Single value + chart | Waterfall chart | S |
| F2 | GMV: value of cars sold | 4.30 | Headline | Single value + chart | Line chart against last year or last period | M |
| F3 | Net cash burn and runway | 4.15 | Headline | Single value + chart | Scorecard: one number with its change | I |
| F4 | Revenue (turnover) | 4.15 | Core | Single value + chart | Column chart | M |
| F5 | Take rate | 3.95 | Core | Single value + chart | Line chart with a target line or band | S |
| F6 | Average revenue per active dealer | 3.85 | Core | Single value + chart | Line chart against last year or last period | P |
| F7 | Adjusted EBITDA | 3.65 | Core | Chart | Column chart | P |
| F8 | Operating costs as a share of revenue | 3.50 | Supporting | Single value + chart | Stacked column chart | I |
| F9 | Pre-tax loss | 3.50 | Supporting | Single value + chart | Waterfall chart | M |
| F10 | Revenue per car sold | 3.45 | Supporting | Single value + chart | Line chart against last year or last period | P |
| F11 | Share of sales paid through Motorway Pay | 3.20 | Supporting | Single value + chart | Area chart | M |

**Marketing:** *Are we bringing in sellers who go on to sell, at a sensible cost?*

| # | KPI | Score | Tier | Format | Main visual | Evidence |
|---|---|---|---|---|---|---|
| M1 | Valuation-to-sale conversion | 4.75 | Headline | Chart | Funnel chart | S |
| M2 | Cost per car sold | 4.40 | Headline | Single value + chart | Ranked horizontal bar chart | S |
| M3 | Valuations started | 4.05 | Headline | Single value + chart | Area chart | I |
| M4 | CAC payback | 4.00 | Core | Single value + chart | Ranked horizontal bar chart | S |
| M5 | Seller satisfaction (NPS or CSAT) | 3.90 | Core | Single value + chart | Scorecard: one number with its change | S |
| M6 | Organic share of valuations | 3.80 | Core | Single value + chart | 100% stacked column chart (mix over time) | S |
| M7 | Cost per valuation (cost per lead) | 3.35 | Core | Single value + chart | Line chart against last year or last period | I |
| M8 | Review score | 2.70 | Supporting | Single value + chart | Scorecard: one number with its change | M |
| M9 | Seller price advantage | 2.65 | Supporting | Single value + chart | Scorecard: one number with its change | M |
| M10 | Visits and engagement | 2.55 | Supporting | Single value + chart | Combo chart with two axes (columns plus a line) | P |
| M11 | Brand awareness | 2.55 | Supporting | Single value + chart | Line chart with a target line or band | M |

**Operations:** *Does every agreed sale complete quickly, safely and without disputes?*

| # | KPI | Score | Tier | Format | Main visual | Evidence |
|---|---|---|---|---|---|---|
| O1 | Completion rate (and fall-through) | 4.55 | Headline | Single value + chart | Line chart with a target line or band | P |
| O2 | Claims (arbitration) rate by dealer | 4.20 | Headline | Chart | Ranked horizontal bar chart | P |
| O3 | Price changed at collection | 4.20 | Headline | Single value + chart | Ranked horizontal bar chart | I |
| O4 | Support contacts per 100 completed sales | 4.15 | Core | Chart | Line chart with a target line or band | I |
| O5 | Time to sell | 4.00 | Core | Single value + chart | Histogram with median and threshold lines | S |
| O6 | Completed sales | 4.00 | Core | Single value + chart | Column chart | I |
| O7 | Days to seller payment | 3.80 | Core | Single value + chart | Histogram with median and threshold lines | I |
| O8 | On-time collection and cost per move | 3.75 | Supporting | Chart | Combo chart with two axes (columns plus a line) | I |
| O9 | Problem vehicles stopped | 3.70 | Supporting | Chart | Stacked column chart | I |
| O10 | Seller verification coverage | 3.00 | Supporting | Single value + chart | Line chart with a target line or band | M |

**Commercial:** *Are enough dealers bidding, buying and coming back?*

| # | KPI | Score | Tier | Format | Main visual | Evidence |
|---|---|---|---|---|---|---|
| C1 | Sell-through | 4.75 | Headline | Single value + chart | Line chart with a target line or band | S |
| C2 | Active dealers | 4.65 | Headline | Single value + chart | Column chart | P |
| C3 | Bid volume and bids per car | 4.55 | Headline | Single value + chart | Combo chart with two axes (columns plus a line) | M |
| C4 | Cumulative sell-through curve | 4.20 | Core | Single value + chart | Line per cohort (cumulative curve by days since start) | S |
| C5 | Time to first bid | 4.15 | Core | Single value + chart | Histogram with median and threshold lines | S |
| C6 | Sale price against market guide | 4.00 | Core | Single value + chart | Histogram with median and threshold lines | M |
| C7 | Market depth: bidders per car | 3.90 | Core | Single value + chart | Histogram with median and threshold lines | S |
| C8 | Dealer concentration and retention | 3.85 | Supporting | Single value + chart | Cumulative share curve (Pareto or Lorenz) | S |
| C9 | Cars in the daily sale | 3.60 | Supporting | Single value + chart | Line chart against last year or last period | M |
| C10 | Motorway Pay adoption (dealers) | 3.20 | Supporting | Single value + chart | Area chart | M |
| C11 | Verified dealers | 2.55 | Supporting | Single value + chart | Line chart against last year or last period | M |

**Product:** *Is the journey easy to finish, and is the car information accurate?*

| # | KPI | Score | Tier | Format | Main visual | Evidence |
|---|---|---|---|---|---|---|
| P1 | Funnel completion by step | 4.85 | Headline | Chart | Funnel chart | I |
| P2 | Retention cohorts (dealers) | 4.60 | Headline | Chart | Heatmap (cohort grid) | S |
| P3 | Valuation accuracy | 4.40 | Headline | Single value + chart | Histogram with median and threshold lines | I |
| P4 | Verification pass rate and time | 4.00 | Core | Single value + chart | Column chart | I |
| P5 | Condition grade accuracy | 4.00 | Core | Chart | Column chart | I |
| P6 | Repeat seller rate | 3.75 | Core | Single value + chart | Line chart with a target line or band | S |
| P7 | App rating and stability | 3.50 | Core | Single value + chart | Line chart with a target line or band | I |
| P8 | Page speed (Core Web Vitals) | 3.35 | Supporting | Single value + chart | Bullet chart (value against a target and bands) | S |
| P9 | Dealer engagement curve (power users) | 3.25 | Supporting | Single value + chart | Histogram with median and threshold lines | S |
| P10 | Paid listing uptake | 3.10 | Supporting | Single value + chart | Line chart with a target line or band | I |
| P11 | Service-history extraction accuracy | 3.00 | Supporting | Single value + chart | Line chart with a target line or band | M |

---

# Part 2: The method

## 2.1 Evidence tags

| Tag | Meaning |
|---|---|
| **M** | Motorway has said this publicly |
| **P** | A listed peer reports or defines it |
| **S** | Standard metric from a recognised source (a16z for marketplaces, Google web.dev for web speed) |
| **I** | My inference. Nobody has published it for Motorway |

Motorway does not publish its KPI list. 16 of the 54 KPIs are tagged I. Do not say Motorway tracks an I KPI. Say it is the kind of measure such a business would watch.

## 2.2 How the ranking works

Each KPI is scored 1 to 5 on five questions. The score is the weighted average.

| Question | Weight | What a 5 means |
|---|---|---|
| **Decision value** | 30% | Someone would act differently depending on the number: spend, fix, stop, escalate. |
| **Link to the goal** | 25% | It moves directly with profit and marketplace liquidity. |
| **Diagnostic power** | 20% | When it moves, drilling down tells you why. |
| **Early warning** | 15% | It moves before revenue does. |
| **Measurable** | 10% | It can be computed reliably from data a company normally has. |

Ties are broken by early warning, then decision value, then goal link. The top three in a department are **Headline**, ranks four to seven are **Core**, and the rest are **Supporting**.

**This is a judgement.** The scores reflect a marketplace that reports a loss and aims for profit. A business chasing growth alone would rank volume measures higher. To change a score, edit `build_playbook.py` and run it again.

## 2.3 Rules for every KPI

1. **Define the grain first.** Say what one row means before you calculate.
2. **Define the measure once** and reuse it.
3. **A rate is a ratio of sums.** Never average monthly rates.
4. **Aggregate before you join.** Otherwise a total is counted once per joined row.
5. **Give every number a comparison:** a target, last year, last period or a threshold.
6. **Show the rows behind a rate.** 79% on 175 cars is weaker than 67% on 3,000.
7. **Allow time for outcomes.** Compare cohorts of the same age.
8. **Use the median for time and money.** Add the 90th percentile.
9. **Colour means status.** One chart answers one question.

## 2.4 Single value or chart

| Use a single value when | Use a chart when | Use both when |
|---|---|---|
| One number answers the question, and its meaning is a change or a gap to target. | The shape matters: a trend, a spread, a comparison across groups, a journey. | The reader needs the headline fast and the reason beneath it. This is the usual dashboard pattern. |

## 2.5 When the data is thin

Every KPI card has its own table of alternatives. The general ladder, from richest to barest:

| Situation | Step down to | What you keep | What you lose |
|---|---|---|---|
| Under about 6 periods | Columns, not a line | The levels | A trend you can trust |
| One period only | A scorecard or bullet against a target | Today's gap | Any direction |
| Under about 30 rows behind a rate | A wider period, grouped categories, and the count shown | A stable figure | Detail and timeliness |
| A dimension is missing (no channel, no region) | The total | The headline | The split that explains it |
| A field is missing (no guide price, no cost) | A labelled proxy, or a statement that the KPI cannot be computed | Honesty, and sometimes a rough signal | The KPI itself |

Never invent a missing field. A proxy must be named as a proxy on the chart.

---

# Part 3: The visual library

Each visual is defined once here. KPI cards refer to these by number.

### V1. Scorecard: one number with its change

- **Type:** Single value.
- **Use it for:** One number answers the question, and its meaning is a change or a gap to target.
- **Avoid it when:** The reader needs a trend or a spread. A lone number hides both.
- **Minimum data:** One period. Two periods for a change.
- **Step down to:** None. This is the bottom of the ladder.

| Platform | How |
|---|---|
| Looker Studio | Scorecard chart. Use a comparison date range for the change, and compact numbers for large values. |
| Streamlit | `st.metric(label, value, delta=, delta_color=, border=True)`. Add `chart_data=` for a small trend line inside the card. |
| Python | Plotly `go.Indicator(mode='number+delta')`, or a formatted f-string print. |
| SQL returns | One row: value and prior value. |
| Antigravity IDE | A printed line or Markdown in a notebook cell. No chart needed. |

### V2. Line chart with a target line or band

- **Type:** Chart.
- **Use it for:** A rate or level over time that has a target or a normal range.
- **Avoid it when:** Fewer than about 6 points, or a rate built on very few rows per point.
- **Minimum data:** About 6 or more periods, and roughly 30 or more rows behind each point.
- **Step down to:** Columns for a short history. A bullet or scorecard for one period.

| Platform | How |
|---|---|
| Looker Studio | Time series chart. Style tab: add a reference line (fixed value or parameter) or a reference band. |
| Streamlit | `st.line_chart` draws the line but has no target line. Use `st.plotly_chart(fig)` with `fig.add_hline()` or `add_hrect()`. |
| Python | `px.line(df, x, y)` then `fig.add_hline(y=target)`. Matplotlib: `ax.axhline()` and `ax.axhspan()`. |
| SQL returns | One row per period: numerator, denominator, rate. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V3. Line chart against last year or last period

- **Type:** Chart.
- **Use it for:** A total or level over time compared with last year, last period or another series.
- **Avoid it when:** Series on very different scales.
- **Minimum data:** Two series over the same periods. 13 months for year on year.
- **Step down to:** A moving average with the period-on-period change.

| Platform | How |
|---|---|
| Looker Studio | Time series chart with a comparison date range, or two metrics on one chart. |
| Streamlit | `st.line_chart(df)` with one column per series (wide format). Fully native. |
| Python | Pivot to one column per series, then `px.line(df, x=..., y=['this_year','last_year'])`. |
| SQL returns | One row per period, one column per series. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V4. Column chart

- **Type:** Chart.
- **Use it for:** Comparing a handful of categories, or a short run of periods.
- **Avoid it when:** More than about 12 bars, or long category names (use horizontal bars).
- **Minimum data:** One value per category.
- **Step down to:** A table.

| Platform | How |
|---|---|
| Looker Studio | Column chart. Add a breakdown dimension for stacks, or switch to 100% stacked for shares. |
| Streamlit | `st.bar_chart(df, x=, y=, color=)`. Fully native. |
| Python | `px.bar`, with `barmode='group'` for side by side. |
| SQL returns | One row per category. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V5. Stacked column chart

- **Type:** Chart.
- **Use it for:** A total over time and what it is made of.
- **Avoid it when:** More than about 5 segments, or when the middle segments must be compared precisely.
- **Minimum data:** A breakdown field that covers every row.
- **Step down to:** A total-only column chart.

| Platform | How |
|---|---|
| Looker Studio | Stacked column chart with a breakdown dimension. |
| Streamlit | `st.bar_chart(df, x=, y=, color=)` stacks by colour. Native. |
| Python | `px.bar(color=...)`. |
| SQL returns | One row per period per segment. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V6. 100% stacked column chart (mix over time)

- **Type:** Chart.
- **Use it for:** How the mix of a total changes over time.
- **Avoid it when:** When the size of the total also matters. It is hidden.
- **Minimum data:** A breakdown field and several periods.
- **Step down to:** One share as a line.

| Platform | How |
|---|---|
| Looker Studio | 100% stacked column chart or 100% stacked area chart. |
| Streamlit | Convert to shares in pandas first, then `st.area_chart` or `st.bar_chart`. |
| Python | `px.bar(..., barnorm='percent')` or `px.area(..., groupnorm='percent')`. |
| SQL returns | One row per period per segment, with its share. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V7. Area chart

- **Type:** Chart.
- **Use it for:** A share or volume that builds over time, optionally by segment.
- **Avoid it when:** Many overlapping series.
- **Minimum data:** About 6 or more periods.
- **Step down to:** A line.

| Platform | How |
|---|---|
| Looker Studio | Area chart (stacked area if there is a breakdown). |
| Streamlit | `st.area_chart`. Native. |
| Python | `px.area`. |
| SQL returns | One row per period (per segment). |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V8. Ranked horizontal bar chart

- **Type:** Chart.
- **Use it for:** Finding the best and worst among many items: dealers, channels, reasons.
- **Avoid it when:** Items with tiny denominators, unless you filter them out.
- **Minimum data:** A value and a denominator per item.
- **Step down to:** A table with bars, with items grouped into bands.

| Platform | How |
|---|---|
| Looker Studio | Bar chart sorted by the metric, with a row limit (top 10 or 20) and a reference line for a threshold. Pair it with a table with bars for the exact numbers. |
| Streamlit | `st.bar_chart(df, horizontal=True)` on a sorted frame. A threshold line needs Plotly. |
| Python | `px.bar(df.sort_values(...), orientation='h')` then `add_vline(threshold)`. |
| SQL returns | One row per item, sorted, with its denominator. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V9. Combo chart with two axes (columns plus a line)

- **Type:** Chart.
- **Use it for:** Two related measures with different units over the same periods.
- **Avoid it when:** When readers may compare the heights of the two series. The two scales are arbitrary.
- **Minimum data:** Both measures at the same grain.
- **Step down to:** Two small charts stacked on one x-axis.

| Platform | How |
|---|---|
| Looker Studio | Combo chart. Set one series to columns, one to a line, and put the line on the right axis. |
| Streamlit | No native two-axis chart. Use Plotly `make_subplots(specs=[[{'secondary_y': True}]])`, or two small charts stacked on one shared x-axis (clearer). |
| Python | Plotly `secondary_y=True`, or matplotlib `ax.twinx()`. |
| SQL returns | One row per period with both measures. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V10. Waterfall chart

- **Type:** Chart.
- **Use it for:** Showing how a starting amount becomes an end amount through additions and subtractions.
- **Avoid it when:** More than about 8 steps.
- **Minimum data:** Every step's amount, on the same basis.
- **Step down to:** Two columns (start and end) with the difference stated.

| Platform | How |
|---|---|
| Looker Studio | Waterfall chart. Feed it ordered steps with signed amounts. |
| Streamlit | `st.plotly_chart(go.Figure(go.Waterfall(...)))`. No native waterfall. |
| Python | `go.Waterfall(measure=['relative', ..., 'total'], x=..., y=...)`. Matplotlib: draw each bar with `bottom=`. |
| SQL returns | One signed row per step, in order. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V11. Funnel chart

- **Type:** Chart.
- **Use it for:** A fixed sequence of steps where people drop out.
- **Avoid it when:** Steps that can happen in any order.
- **Minimum data:** Distinct people at each step.
- **Step down to:** Start and end counts with one conversion rate.

| Platform | How |
|---|---|
| Looker Studio | Funnel chart (listed among Google's chart types). Fallback: a horizontal bar chart with steps in order. |
| Streamlit | `st.plotly_chart(px.funnel(df, x='users', y='step'))`. No native funnel. |
| Python | `px.funnel` or `go.Funnel`. |
| SQL returns | One row per step: order, name, distinct users. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V12. Histogram with median and threshold lines

- **Type:** Chart.
- **Use it for:** The spread of a measure: time, price, error.
- **Avoid it when:** Fewer than about 50 values.
- **Minimum data:** One value per record.
- **Step down to:** The median and 90th percentile as two numbers, or a boxplot.

| Platform | How |
|---|---|
| Looker Studio | No native histogram. Make a bin field (`FLOOR(value / width) * width`) and use a column chart of counts. A boxplot chart is native if you only need the spread. |
| Streamlit | No native histogram. Bin with `numpy.histogram` then `st.bar_chart`, or use `px.histogram` in `st.plotly_chart`. |
| Python | `px.histogram(df, x, nbins=...)` then `add_vline(median)`. Matplotlib: `ax.hist`. |
| SQL returns | One row per bin: bin start, count. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V13. Heatmap (cohort grid)

- **Type:** Chart.
- **Use it for:** Two dimensions and one measure, such as cohort by month.
- **Avoid it when:** Sparse grids with many empty cells.
- **Minimum data:** Several cohorts with several periods each.
- **Step down to:** One line per cohort, or a single retention line.

| Platform | How |
|---|---|
| Looker Studio | Pivot table with heatmap colouring on the metric. There is no separate heatmap chart. |
| Streamlit | `st.dataframe(pivot.style.background_gradient())`, or `st.plotly_chart(px.imshow(pivot))`. |
| Python | `px.imshow(pivot, text_auto=True)` or seaborn `heatmap`. |
| SQL returns | One row per cohort per period. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V14. Cumulative share curve (Pareto or Lorenz)

- **Type:** Chart.
- **Use it for:** Showing how concentrated something is.
- **Avoid it when:** Very few items.
- **Minimum data:** A value per item, for dozens of items.
- **Step down to:** A top-10 ranked bar with their combined share.

| Platform | How |
|---|---|
| Looker Studio | Table with bars and a running-sum column for the ranked list. For the curve itself, build the cumulative column in SQL and draw a line chart. |
| Streamlit | Compute the cumulative share in pandas, then `st.line_chart`. The 45 degree reference line needs Plotly. |
| Python | `px.line` of the cumulative share, plus a diagonal line for perfect equality. |
| SQL returns | One row per item with its running share (window function). |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V15. Line per cohort (cumulative curve by days since start)

- **Type:** Chart.
- **Use it for:** Comparing how fast different cohorts reach an outcome.
- **Avoid it when:** Cohorts that are not yet mature. Cut them.
- **Minimum data:** A start date and an outcome date per record.
- **Step down to:** The outcome by attempt, as columns.

| Platform | How |
|---|---|
| Looker Studio | Line chart (combo chart set to lines) with 'days since listing' as the dimension and one line per cohort. |
| Streamlit | Pivot to one column per cohort, then `st.line_chart`. |
| Python | `px.line(df, x='days_since', y='cumulative', color='cohort')`. |
| SQL returns | One row per cohort per day since start. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V16. Bullet chart (value against a target and bands)

- **Type:** Single value.
- **Use it for:** One value against a target and quality bands, in little space.
- **Avoid it when:** Showing a trend.
- **Minimum data:** A value and a target.
- **Step down to:** A scorecard with the gap to target.

| Platform | How |
|---|---|
| Looker Studio | Bullet chart. The docs also list a gauge, but a bullet chart reads more easily in a small space. |
| Streamlit | Plotly `go.Indicator(mode='number+gauge', gauge={'shape': 'bullet'})` in `st.plotly_chart`. |
| Python | Same Plotly indicator. |
| SQL returns | One row: value, target, band limits. |
| Antigravity IDE | Plotly figure in a notebook cell. If it does not show inline, save with `fig.write_html()` and open the file. |

### V17. Table with bars or heatmap

- **Type:** Table.
- **Use it for:** Exact numbers for a list that someone will act on.
- **Avoid it when:** Showing a pattern. Use a chart.
- **Minimum data:** Any.
- **Step down to:** None.

| Platform | How |
|---|---|
| Looker Studio | Table, with the bars or heatmap style turned on for the metric columns. |
| Streamlit | `st.dataframe(df)` with `column_config` (progress bars, small charts) or a pandas Styler. |
| Python | `df.style.bar()` or `background_gradient()`. |
| SQL returns | One row per item. |
| Antigravity IDE | A styled DataFrame shown in a notebook cell. |

---

# Part 4: The KPI cards

---

## FINANCE

*Is the marketplace making money, and how far is it from profit?*

**Suggested page layout**
- **Top row, single values:** Contribution per car, GMV: value of cars sold, Net cash burn and runway, Revenue (turnover). Each with its change against the last period.
- **Middle, the Headline charts:** Contribution per car (waterfall chart); GMV: value of cars sold (line chart against last year or last period); Net cash burn and runway (scorecard: one number with its change).
- **Lower, the Core diagnostics:** Revenue (turnover), Take rate, Average revenue per active dealer, Adjusted EBITDA.
- **Second page or drill through:** Operating costs as a share of revenue, Pre-tax loss, Revenue per car sold, Share of sales paid through Motorway Pay.

### F1. Contribution per car

`Headline` · rank 1 of 11 · score **4.65** · evidence **S** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 5, early warning 4, measurable 3.*

**Definition**
- **What it is:** Whether each sale pays for itself after the costs that rise with every sale.
- **Formula:** Revenue per car − variable cost per car (marketing, transport, payments, support, verification).
- **Data needed:** Revenue per completed sale. Variable costs per sale, or an allocation rule such as monthly cost ÷ monthly completed sales.
- **Evidence (S):** a16z lists unit economics as a core marketplace metric: whether the business is profitable per unit. Motorway does not publish it. The nearest listed peer measure is Carvana's total gross profit per unit, though Carvana owns the cars it sells.

**Why it ranks here:** It decides whether growth makes or loses money. With a stated aim of profit by mid-2026, this is the number that explains the pre-tax loss one level down, and the first one to check after any pricing or marketing change. It loses points only on measurability, because costs must be allocated to each car.

**Insights it can give**
- Positive and rising: each extra car adds profit, so growth closes the loss.
- Negative in one segment (a price band or a channel): that segment loses money however many cars it sells, so more volume there makes the loss bigger.
- Falling while revenue per car holds: a cost per car is rising. The waterfall shows which one, usually marketing or transport.
- **Read it with:** Cost per car sold (Marketing) and cost per move (Operations), its two largest cost bars.
- **Decision it supports:** Where to spend, which segments to grow or stop, and whether a price change is needed.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V10 Waterfall chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A waterfall shows how revenue per car is used up step by step, which one number cannot. The scorecard above it gives the headline and the change.
- **Build notes:** Bars in order: revenue per car, then one negative bar per variable cost, then a total bar for contribution. Costs orange, contribution navy. Put the unit in the title (£ per completed sale).

| Platform | Main (V10) | Companion (V1) |
|---|---|---|
| Looker Studio | Waterfall chart | Scorecard with comparison |
| Streamlit | `st.plotly_chart(go.Waterfall)` | `st.metric` (native) |
| Python | `go.Waterfall(measure=[...])` | `go.Indicator` or a printed number |
| SQL returns | one signed row per step, in order | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT step, gbp_per_car FROM (
  SELECT 'Revenue' AS step, 1 AS ord, SUM(revenue) * 1.0 / COUNT(*) AS gbp_per_car FROM completed_sales
  UNION ALL
  SELECT cost_type, 2, -SUM(amount) * 1.0 / (SELECT COUNT(*) FROM completed_sales)
  FROM variable_costs GROUP BY cost_type
) t ORDER BY ord;   -- one signed row per step, ready for a waterfall; the total bar is the sum
```

**Drill:** Drill down by price band, channel or region to find any segment that is negative. Drill through from a cost bar to that cost by month.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Costs per car | Monthly variable cost ÷ monthly completed sales, as a line | The trend, and whether contribution is positive overall | Which segment or cost line is responsible |
| Any cost data | Revenue per car sold only | The earning side of each sale | Everything about profitability. Say so plainly. |

**Trap:** Fixed costs do not belong here. Write the allocation rule under the chart, or two analysts will get two answers.

### F2. GMV: value of cars sold

`Headline` · rank 2 of 11 · score **4.30** · evidence **M** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 3, early warning 3, measurable 5.*

**Definition**
- **What it is:** The size of the marketplace. The total value of cars sold through it. It is not revenue.
- **Formula:** Sum of the final sale price of completed sales. Exclude all fees.
- **Data needed:** One row per completed sale with `sale_price` and `completed_date`.
- **Evidence (M):** Motorway reported £2.2bn of cars sold in 2023. ACV Auctions defines Marketplace GMV the same way in its 10-K.

**Why it ranks here:** Revenue is GMV multiplied by take rate, so volume starts here. It ranks below contribution because it measures size, not profit, and it can rise while the business loses more money per car.

**Insights it can give**
- Up while completed sales are flat: prices or mix moved (dearer cars), not activity.
- Up while take rate is down: more is sold but less of each sale is kept.
- A gap against last year in one region or price band shows where growth comes from or leaves.
- **Read it with:** Completed sales and average sale price, the two things GMV is made of.
- **Decision it supports:** Capacity and growth planning, and the size of the base that fees apply to.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V3 Line chart against last year or last period. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Time on the x-axis with last year overlaid shows growth and seasonality together. A scorecard gives the headline figure and its change.
- **Build notes:** Monthly points, this year in blue, last year in grey. Zoom the y-axis to the data range, but never cut a column chart.

| Platform | Main (V3) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + comparison range | Scorecard with comparison |
| Streamlit | `st.line_chart` (native) | `st.metric` (native) |
| Python | `px.line` with several y columns | `go.Indicator` or a printed number |
| SQL returns | one row per period, one column per series | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('month', completed_date) AS month, SUM(sale_price) AS gmv
FROM completed_sales
GROUP BY 1 ORDER BY 1;   -- last year: join this result to itself on month - INTERVAL '1 year'
```

**Drill:** Drill down month, week, day. Slice by region, make and price band.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| A full prior year | 4-week moving average with week-on-week change | Direction and momentum | Seasonality: a dip may be normal for the time of year |
| Sale price on some rows | Completed sales × median price, labelled as an estimate | Approximate size | Accuracy at the top end, where a few dear cars matter |

**Trap:** Count completed sales only, not agreed ones. Look for placeholder prices (a price of 1) that distort the sum.

### F3. Net cash burn and runway

`Headline` · rank 3 of 11 · score **4.15** · evidence **I** · added in round 2

*Scores: decision 5, goal link 5, diagnostic 2, early warning 4, measurable 4.*

**Definition**
- **What it is:** How much cash the business consumes each month, and how many months it can keep going.
- **Formula:** Net burn = cash out − cash in per month. Runway in months = cash balance ÷ average monthly net burn (use the last 3 months).
- **Data needed:** Monthly cash flow or bank balance series. This is management accounts data, not marketplace data.
- **Evidence (I):** Not published for Motorway. Motorway's public statement is an aim to be profitable by mid-2026 (M). Burn and runway are the standard way to judge any company that reports a loss.

**Why it ranks here:** A company with a pre-tax loss lives or dies on this. It ranks above revenue because it changes a decision sooner: cut spend, or raise money.

**Insights it can give**
- Burn falling while revenue grows: the path to profit is working.
- Burn rising faster than revenue: growth is being bought. Check contribution per car.
- Runway below the limit finance sets: the priority moves from growth to cost.
- **Read it with:** Adjusted EBITDA and operating costs as a share of revenue.
- **Decision it supports:** How much can be invested, and when.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V1 Scorecard: one number with its change. **Companion:** V2 Line chart with a target line or band.
- **Why:** One number answers the question 'how long have we got?', so a scorecard leads. The line beneath shows whether burn is falling.
- **Build notes:** Scorecard: runway in months, red below a limit your finance team sets. Line: closing cash balance with the 3-month burn on a second chart.

| Platform | Main (V1) | Companion (V2) |
|---|---|---|
| Looker Studio | Scorecard with comparison | Time series + reference line |
| Streamlit | `st.metric` (native) | `st.plotly_chart` (Plotly, for the target line) |
| Python | `go.Indicator` or a printed number | `px.line` + `add_hline` |
| SQL returns | one row: value and prior value | one row per period: numerator, denominator, rate |
| Antigravity IDE | printed value or DataFrame in a cell | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT month, closing_cash,
       AVG(operating_cash_out - operating_cash_in) OVER (ORDER BY month ROWS 2 PRECEDING) AS burn_3m,
       closing_cash / NULLIF(AVG(operating_cash_out - operating_cash_in) OVER (ORDER BY month ROWS 2 PRECEDING), 0) AS runway_months
FROM monthly_cash;   -- if burn is zero or negative, runway is not defined: show 'cash generative'
```

**Drill:** No drill down. Offer a table of the largest cash movements.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Monthly cash data | Year-end cash as columns | Whether cash shrinks year to year | Any sense of how many months remain |
| Cash data at all | Pre-tax loss per year as a proxy for burn | Rough scale of the yearly cash need | Timing, funding and working capital effects |

**Trap:** Funding inflows hide the burn. Use operating cash flow, not the change in the bank balance.

### F4. Revenue (turnover)

`Core` · rank 4 of 11 · score **4.15** · evidence **M** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 3, early warning 2, measurable 5.*

**Definition**
- **What it is:** The money Motorway keeps. Dealer fees on cars bought, seller service fees (£29.99 to £99.99 by sale price, charged only when the car is sold), transport fees and paid listings.
- **Formula:** Sum of all fee income in the period, by fee type.
- **Data needed:** A fee ledger with `date`, `fee_type`, `amount` and the sale it belongs to.
- **Evidence (M):** £60.9m in 2023, £66.4m in 2024 and £78.3m in 2025 (up 18%), from filed accounts reported by trade press.

**Why it ranks here:** It defines scale and growth and is easy to measure. It is a lagging figure and says nothing about profit on its own.

**Insights it can give**
- Growth from one fee type shows the driver: more cars (dealer fees) or new fees (seller fee, paid listing).
- Growing slower than GMV: take rate is falling.
- A step change on a known date usually marks a pricing change, not demand.
- **Read it with:** GMV and take rate.
- **Decision it supports:** Pricing, product mix, and whether growth targets are met.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V4 Column chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Yearly totals compare cleanly as columns, with the growth rate printed on each. A monthly stacked version splits the fee types.
- **Build notes:** Years as columns with growth labels. Second chart: stacked by month, one colour per fee type.

| Platform | Main (V4) | Companion (V1) |
|---|---|---|
| Looker Studio | Column chart | Scorecard with comparison |
| Streamlit | `st.bar_chart` (native) | `st.metric` (native) |
| Python | `px.bar` | `go.Indicator` or a printed number |
| SQL returns | one row per category | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('month', fee_date) AS month, fee_type, SUM(amount) AS revenue
FROM fees GROUP BY 1, 2;
```

**Drill:** Drill down year, quarter, month, then fee type.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Fee types | Total revenue with growth labels | Scale and growth | What is driving it |
| Monthly data | Annual columns | Long-run growth | Seasonality and the effect of recent changes |

**Trap:** Say which date the chart uses. Seller fees only exist once the car is collected and paid for.

### F5. Take rate

`Core` · rank 5 of 11 · score **3.95** · evidence **S** · from the first sheets

*Scores: decision 4, goal link 4, diagnostic 4, early warning 3, measurable 5.*

**Definition**
- **What it is:** The share of each sale that Motorway keeps.
- **Formula:** Revenue ÷ GMV for the same period and the same sales.
- **Data needed:** Revenue and GMV on the same date basis.
- **Evidence (S):** a16z marketplace metric. From the public 2023 figures, £60.9m ÷ £2.2bn is about 2.8%. That is my own calculation. Motorway does not state a take rate.

**Why it ranks here:** It shows pricing power and mix in one number. It tells you whether revenue grows because more is sold or because more is kept per sale.

**Insights it can give**
- Rising with a stable mix: pricing power. Fees went up and volume held.
- Rising only because the mix moved to higher-fee cars: no real pricing change.
- Falling: discounts, a move to cheaper fee tiers, or large dealers on better terms.
- **Read it with:** Revenue per car sold and the price-band mix.
- **Decision it supports:** Fee levels and discount policy.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A rate over time needs a trend line and a target. The y-axis is zoomed to a narrow band so small moves show.
- **Build notes:** Calculated field `SUM(revenue) / SUM(gmv)`. Never average the monthly rate column.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT r.month, r.revenue * 1.0 / g.gmv AS take_rate
FROM (SELECT DATE_TRUNC('month', fee_date) AS month, SUM(amount) AS revenue FROM fees GROUP BY 1) r
JOIN (SELECT DATE_TRUNC('month', completed_date) AS month, SUM(sale_price) AS gmv FROM completed_sales GROUP BY 1) g
  USING (month);
```

**Drill:** Light. By month and fee type. Deeper slices are noisy.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Monthly revenue | Annual take rate as columns | Level and long-run direction | When and why it changed |
| Revenue by sale | Company revenue ÷ GMV | One overall rate | Which fee or segment moved it |

**Trap:** A rising take rate may come from a mix shift to higher-fee cars, not a price change. Check the mix first.

### F6. Average revenue per active dealer

`Core` · rank 6 of 11 · score **3.85** · evidence **P** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 4, early warning 3, measurable 4.*

**Definition**
- **What it is:** How much dealer-side revenue each participating dealer brings in.
- **Formula:** Dealer fee revenue in the period ÷ active dealers in the period. Listed peers divide by the average of opening and closing paying dealers.
- **Data needed:** Dealer fee revenue by month, and the list of active dealers (bid or bought).
- **Evidence (P):** Auto Trader reports average revenue per retailer (£2,854 a month in FY2025). CarGurus reports quarterly average revenue per subscribing dealer, defined as quarterly marketplace revenue ÷ the average of opening and closing paying dealers. For Motorway the figure is my inference.

**Why it ranks here:** It separates two growth stories: more dealers, or more revenue from each. Peers treat it as a headline KPI.

**Insights it can give**
- Rising with a flat dealer count: existing dealers buy more or pay more.
- Falling while active dealers rise: growth is coming from small dealers, which dilutes the average.
- A wide gap between mean and median: a few large dealers carry the revenue.
- **Read it with:** Active dealers and dealer concentration.
- **Decision it supports:** Whether to grow by adding dealers or by deepening existing ones.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V3 Line chart against last year or last period. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A trend with last year as the comparison shows whether each dealer is worth more over time.
- **Build notes:** One line this year, one last year, monthly. Show the count of active dealers in a tooltip.

| Platform | Main (V3) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + comparison range | Scorecard with comparison |
| Streamlit | `st.line_chart` (native) | `st.metric` (native) |
| Python | `px.line` with several y columns | `go.Indicator` or a printed number |
| SQL returns | one row per period, one column per series | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
WITH rev AS (SELECT month, SUM(amount) AS dealer_revenue FROM dealer_fees GROUP BY month),
     act AS (SELECT month, COUNT(DISTINCT dealer_id) AS active_dealers FROM dealer_activity GROUP BY month)
SELECT month, dealer_revenue * 1.0 / active_dealers AS arpd FROM rev JOIN act USING (month);
```

**Drill:** Drill down by dealer size band and region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Revenue by dealer | Dealer fee revenue ÷ active dealers | The average | The spread, and who the big contributors are |
| Activity data | Revenue ÷ verified dealers | A lower-bound average | Meaning, because inactive dealers drag it down |

**Trap:** Auto Trader notes that smaller customers dilute the average. Report the median beside the mean.

### F7. Adjusted EBITDA

`Core` · rank 7 of 11 · score **3.65** · evidence **P** · from the first sheets

*Scores: decision 4, goal link 5, diagnostic 3, early warning 2, measurable 3.*

**Definition**
- **What it is:** Underlying profit before financing and one-off items.
- **Formula:** Operating result + depreciation + amortisation, plus or minus one-off and share-based items.
- **Data needed:** Quarterly operating result, depreciation, amortisation and a list of adjustments.
- **Evidence (P):** ACV Auctions reports it as a key metric ($58.8m in FY2025). Motorway does not publish it.

**Why it ranks here:** It shows whether the core business is nearing break-even, free of financing and one-offs. It ranks mid-table because it is company-defined and lagging.

**Insights it can give**
- Improving each quarter: operating leverage is real.
- Improving only because the adjustments grew: weak quality. Read the reconciliation.
- Crossing zero: the core business covers its running costs.
- **Read it with:** Pre-tax loss and cash burn.
- **Decision it supports:** Timing of the profitability goal.

**How to show it**
- **Format:** Chart.
- **Main visual:** V4 Column chart. **Companion:** V17 Table with bars or heatmap.
- **Why:** Quarterly columns coloured by sign show the climb towards zero. A small table beneath lists each adjustment so the number can be trusted.
- **Build notes:** Red below zero, green above, a zero line. Table: operating result, each add-back, adjusted EBITDA.

| Platform | Main (V4) | Companion (V17) |
|---|---|---|
| Looker Studio | Column chart | Table with bars or heatmap |
| Streamlit | `st.bar_chart` (native) | `st.dataframe` with `column_config` |
| Python | `px.bar` | pandas Styler |
| SQL returns | one row per category | one row per item |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT quarter, operating_result + depreciation + amortisation + one_offs AS adjusted_ebitda
FROM quarterly_accounts ORDER BY quarter;
```

**Drill:** No drill down. Use the reconciliation table.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Quarterly accounts | Annual columns | Direction year to year | The path within the year |
| The adjustments | Operating result only | A stricter view of profit | Comparability with peers who report the adjusted figure |

**Trap:** It is a company-defined measure. Always show what was added back.

### F8. Operating costs as a share of revenue

`Supporting` · rank 8 of 11 · score **3.50** · evidence **I** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 3, early warning 2, measurable 4.*

**Definition**
- **What it is:** How much of each pound of revenue is spent running the business, by cost line.
- **Formula:** Each cost line ÷ revenue, and total operating cost ÷ revenue.
- **Data needed:** A monthly or quarterly cost ledger by category, and revenue.
- **Evidence (I):** A standard financial ratio. Not published for Motorway.

**Why it ranks here:** It shows operating leverage: whether costs grow slower than revenue. That is how a loss closes. It ranks lower than contribution because it mixes fixed and variable costs.

**Insights it can give**
- Share falling as revenue grows: operating leverage.
- One line rising (often marketing): growth is being bought.
- People cost share flat while revenue grows: hiring keeps pace, so no leverage yet.
- **Read it with:** Adjusted EBITDA.
- **Decision it supports:** Budget setting by cost line.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V5 Stacked column chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Stacked columns show the total and each cost line's share together. A scorecard gives the total ratio.
- **Build notes:** One column per quarter, one colour per cost line, each as a share of revenue.

| Platform | Main (V5) | Companion (V1) |
|---|---|---|
| Looker Studio | Stacked column chart | Scorecard with comparison |
| Streamlit | `st.bar_chart(color=)` (native) | `st.metric` (native) |
| Python | `px.bar(color=)` | `go.Indicator` or a printed number |
| SQL returns | one row per period per segment | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT c.quarter, c.category, SUM(c.amount) * 1.0 / r.revenue AS share_of_revenue
FROM costs c JOIN quarterly_revenue r USING (quarter)
GROUP BY c.quarter, c.category, r.revenue;
```

**Drill:** Drill down quarter to month, and cost line to cost centre.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Cost by category | Total cost ÷ revenue as one line | Whether leverage exists overall | Which line is responsible |

**Trap:** Reclassified cost lines break comparisons over time. Note any change.

### F9. Pre-tax loss

`Supporting` · rank 9 of 11 · score **3.50** · evidence **M** · from the first sheets

*Scores: decision 4, goal link 5, diagnostic 2, early warning 1, measurable 5.*

**Definition**
- **What it is:** The distance from profit.
- **Formula:** Revenue − all operating costs − finance costs.
- **Data needed:** Annual or quarterly accounts: revenue, cost lines, finance costs.
- **Evidence (M):** £25.3m in 2025, down from £37.3m in 2024. Stated aim: profit by mid-2026. The cost split on the sample dashboard is invented.

**Why it ranks here:** It is the final verdict on the business model, but it is purely lagging and gives no clue why. Contribution per car and burn explain it.

**Insights it can give**
- Loss narrowing while revenue grows: scale is working.
- Loss narrowing while revenue is flat: cost cuts, which have a limit.
- The largest cost bar shows where the next saving or investment sits.
- **Read it with:** Contribution per car, which explains it per sale.
- **Decision it supports:** The top-level view of whether the model works.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V10 Waterfall chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A waterfall turns the income statement into a story: revenue falls through each cost line to the result.
- **Build notes:** First bar revenue (navy), each cost line orange, last bar the result (red if a loss).

| Platform | Main (V10) | Companion (V1) |
|---|---|---|
| Looker Studio | Waterfall chart | Scorecard with comparison |
| Streamlit | `st.plotly_chart(go.Waterfall)` | `st.metric` (native) |
| Python | `go.Waterfall(measure=[...])` | `go.Indicator` or a printed number |
| SQL returns | one signed row per step, in order | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT line, amount FROM annual_accounts WHERE year = 2025 ORDER BY display_order;
```

**Drill:** No drill down. Drill through from a cost bar to that cost by month.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Cost lines | Revenue and result as two columns per year | Scale of the loss against revenue | Any explanation of where the money goes |

**Trap:** Label estimates as estimates.

### F10. Revenue per car sold

`Supporting` · rank 10 of 11 · score **3.45** · evidence **P** · from the first sheets

*Scores: decision 3, goal link 4, diagnostic 3, early warning 3, measurable 5.*

**Definition**
- **What it is:** The earning power of one completed sale.
- **Formula:** Revenue ÷ number of completed sales.
- **Data needed:** Revenue by month and completed sales by month.
- **Evidence (P):** Peers report a per-customer version: Auto Trader's average revenue per retailer.

**Why it ranks here:** It is the revenue half of contribution per car. Useful, but on its own it ignores cost.

**Insights it can give**
- Up with the same mix: fees per sale rose.
- Up because dearer cars sold: mix. Check the price bands.
- Down after a promotion: the cost of the discount in revenue terms.
- **Read it with:** Take rate and average sale price.
- **Decision it supports:** Fee structure by price band.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V3 Line chart against last year or last period. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A monthly line with its 3-month average smooths noise so the trend shows.
- **Build notes:** Two series: the monthly value and its 3-month rolling mean.

| Platform | Main (V3) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + comparison range | Scorecard with comparison |
| Streamlit | `st.line_chart` (native) | `st.metric` (native) |
| Python | `px.line` with several y columns | `go.Indicator` or a printed number |
| SQL returns | one row per period, one column per series | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT month, SUM(revenue) * 1.0 / COUNT(*) AS revenue_per_car,
       AVG(SUM(revenue) * 1.0 / COUNT(*)) OVER (ORDER BY month ROWS 2 PRECEDING) AS avg_3m
FROM completed_sales GROUP BY month;
```

**Drill:** No drill down. If asked why it moved, use price band or fee type on a separate chart.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Exact sale counts | Revenue ÷ approximate sales | Rough level | Small real movements |

**Trap:** Seasonality. Compare with the same month last year.

### F11. Share of sales paid through Motorway Pay

`Supporting` · rank 11 of 11 · score **3.20** · evidence **M** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 3, early warning 3, measurable 5.*

**Definition**
- **What it is:** Adoption of the payments product.
- **Formula:** Sales paid through Motorway Pay ÷ all completed sales.
- **Data needed:** `payment_method` on each completed sale.
- **Evidence (M):** Motorway states over 50% of transactions and 2,000+ dealers. Earlier points on the sample line are invented.

**Why it ranks here:** It shows product adoption, but it is a means to an end. Rank is lowest because it does not change the profit decision.

**Insights it can give**
- Rising share: the product is becoming the default way to pay.
- Share stalled while dealer adoption rises: new adopters use it for few purchases.
- High among large dealers only: the product fits a segment, not the base.
- **Read it with:** Motorway Pay adoption by dealer (Commercial) and days to seller payment.
- **Decision it supports:** Product investment and dealer onboarding.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V7 Area chart. **Companion:** V16 Bullet chart (value against a target and bands).
- **Why:** A share that climbs towards a milestone suits an area chart. A bullet chart shows today's level against the 50% mark in a small space.
- **Build notes:** Quarterly area with a reference line at 50%.

| Platform | Main (V7) | Companion (V16) |
|---|---|---|
| Looker Studio | Area chart | Bullet chart |
| Streamlit | `st.area_chart` (native) | `st.plotly_chart(go.Indicator)` with a bullet gauge |
| Python | `px.area` | `go.Indicator(mode='number+gauge')` |
| SQL returns | one row per period (per segment) | one row: value, target, band limits |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT DATE_TRUNC('quarter', completed_date) AS quarter,
       AVG(CASE WHEN payment_method = 'pay' THEN 1.0 ELSE 0 END) AS pay_share
FROM completed_sales GROUP BY 1;
```

**Drill:** Drill down by dealer size band and region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Payment method on sales | The stated adoption figure as a scorecard | The current level only | Trend and segments |

**Trap:** This counts sales, not dealers. See the Commercial version.

---

## MARKETING

*Are we bringing in sellers who go on to sell, at a sensible cost?*

**Suggested page layout**
- **Top row, single values:** Cost per car sold, Valuations started, CAC payback, Seller satisfaction (NPS or CSAT). Each with its change against the last period.
- **Middle, the Headline charts:** Valuation-to-sale conversion (funnel chart); Cost per car sold (ranked horizontal bar chart); Valuations started (area chart).
- **Lower, the Core diagnostics:** CAC payback, Seller satisfaction (NPS or CSAT), Organic share of valuations, Cost per valuation (cost per lead).
- **Second page or drill through:** Review score, Seller price advantage, Visits and engagement, Brand awareness.

### M1. Valuation-to-sale conversion

`Headline` · rank 1 of 11 · score **4.75** · evidence **S** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 5, early warning 4, measurable 4.*

**Definition**
- **What it is:** How many sellers who start actually sell.
- **Formula:** Completed sales ÷ valuations started, for the same group of sellers (allow time for recent sellers to finish).
- **Data needed:** Valuation records with a timestamp or flag for each later step.
- **Evidence (S):** a16z match rate: how often the two sides of a marketplace successfully connect.

**Why it ranks here:** It is the yield of the whole seller funnel. A drop here points to the exact step that broke, so it is both an outcome and a diagnosis. It also drives cost per car sold.

**Insights it can give**
- Biggest drop at one step: that step is the problem (photos, profile, accepting the offer).
- Every channel falls equally in the newest weeks only: the cohorts are immature, not worse.
- One channel far below the rest: lead quality, not the product.
- **Read it with:** Funnel completion by step (Product) and sell-through (Commercial).
- **Decision it supports:** Which step to fix, and which channel to cut or grow.

**How to show it**
- **Format:** Chart.
- **Main visual:** V11 Funnel chart. **Companion:** V2 Line chart with a target line or band.
- **Why:** A funnel shows where sellers are lost. A line of mature cohorts shows whether the end-to-end rate is moving.
- **Build notes:** Count distinct sellers at each step and show the share of the first step. Compare cohorts of equal age only.

| Platform | Main (V11) | Companion (V2) |
|---|---|---|
| Looker Studio | Funnel chart | Time series + reference line |
| Streamlit | `st.plotly_chart(px.funnel)` | `st.plotly_chart` (Plotly, for the target line) |
| Python | `px.funnel` or `go.Funnel` | `px.line` + `add_hline` |
| SQL returns | one row per step: order, name, distinct users | one row per period: numerator, denominator, rate |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT DATE_TRUNC('week', created_at) AS cohort_week, COUNT(*) AS valuations,
       COUNT(profile_done_at) AS profile_done, COUNT(offer_accepted_at) AS accepted, COUNT(completed_at) AS completed
FROM valuations WHERE is_test = FALSE GROUP BY 1;
```

**Drill:** Drill down by channel, device and week cohort. Funnels hide big differences between channels.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Middle steps | One valuation-to-sale line by cohort | Whether end-to-end yield is moving | Where in the journey sellers are lost |
| Old enough cohorts | Funnel for mature weeks, plus profile completion for recent weeks | A fair comparison and an early read | The newest weeks' final outcome |
| Channel | Overall funnel | The leaking step | Whether it is a lead-quality problem |

**Trap:** Count each seller once per step. Recent cohorts look worse because they have not finished.

### M2. Cost per car sold

`Headline` · rank 2 of 11 · score **4.40** · evidence **S** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 4, early warning 3, measurable 4.*

**Definition**
- **What it is:** What it costs to win one completed sale.
- **Formula:** Marketing spend ÷ completed sales that came from those valuations.
- **Data needed:** Spend by channel and period, and completed sales traced to the channel of origin.
- **Evidence (S):** a16z unit economics. It is the honest test of a channel, more than cost per lead.

**Why it ranks here:** It turns marketing spend into a business outcome. A channel with cheap leads can be the dearest per sale.

**Insights it can give**
- Cheap per lead but dear per sale: the channel brings poor leads.
- Blended cost rising while each channel is flat: spend moved to dearer channels (a mix effect).
- Cost per sale above contribution per car: the channel loses money on every sale.
- **Read it with:** Contribution per car and cost per valuation.
- **Decision it supports:** Budget moves between channels.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V8 Ranked horizontal bar chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Channels compare by length, sorted cheapest to dearest, with a blended bar as the reference.
- **Build notes:** Colour the dearest channel red. Print the number of sales behind each bar.

| Platform | Main (V8) | Companion (V1) |
|---|---|---|
| Looker Studio | Bar chart, sorted, with reference line | Scorecard with comparison |
| Streamlit | `st.bar_chart(horizontal=True)`, Plotly for a threshold | `st.metric` (native) |
| Python | `px.bar(orientation='h')` + `add_vline` | `go.Indicator` or a printed number |
| SQL returns | one row per item, sorted, with its denominator | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
WITH sp AS (SELECT channel, SUM(spend) AS spend FROM spend_monthly GROUP BY channel),
     sa AS (SELECT origin_channel AS channel, COUNT(*) AS sales FROM completed_sales GROUP BY 1)
SELECT sp.channel, sp.spend, sa.sales, sp.spend / NULLIF(sa.sales, 0) AS cost_per_sale
FROM sp LEFT JOIN sa USING (channel);   -- aggregate both sides first, then join, or spend is counted once per sale
```

**Drill:** Drill down channel, then campaign.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Sale attribution to channel | Cost per valuation beside conversion by channel | Both halves of the answer | One trusted figure per channel |
| Mature cohorts | Cost per sale on cohorts older than the usual time to sell | A fair figure | The most recent campaigns |

**Trap:** The lag between valuation and sale makes the latest weeks look expensive. Use mature cohorts.

### M3. Valuations started

`Headline` · rank 3 of 11 · score **4.05** · evidence **I** · from the first sheets

*Scores: decision 4, goal link 4, diagnostic 3, early warning 5, measurable 5.*

**Definition**
- **What it is:** The top of the seller funnel.
- **Formula:** Count of sellers who enter a registration and receive a valuation in the period, by channel.
- **Data needed:** `valuation_id`, `created_at`, `channel`, `campaign`.
- **Evidence (I):** Follows Motorway's published seller journey: registration, valuation, profile, daily sale.

**Why it ranks here:** It is the earliest signal in the business: a fall here shows up in sales days later. It ranks below conversion because volume without yield means little.

**Insights it can give**
- A step up on a campaign date in one channel: paid volume. Check its quality.
- Organic falling while paid rises: paid may be buying sellers who would have come anyway.
- A fall across all channels: seasonality or a site problem. Check visits and app stability.
- **Read it with:** Conversion and cost per valuation.
- **Decision it supports:** An early signal for capacity: the cars that reach the sale next week.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V7 Area chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Volume by channel over time suits a stacked area: you see the total and who contributes.
- **Build notes:** Weekly, one colour per channel.

| Platform | Main (V7) | Companion (V1) |
|---|---|---|
| Looker Studio | Area chart | Scorecard with comparison |
| Streamlit | `st.area_chart` (native) | `st.metric` (native) |
| Python | `px.area` | `go.Indicator` or a printed number |
| SQL returns | one row per period (per segment) | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', created_at) AS week, channel, COUNT(*) AS valuations
FROM valuations WHERE is_test = FALSE GROUP BY 1, 2;
```

**Drill:** Drill down channel, then campaign. This is where a campaign that added volume shows up.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Channel | Total valuations with week-on-week change | Volume and direction | What is driving it |
| Daily data | Weekly or monthly totals | Trend | Fast reaction to a campaign or outage |

**Trap:** Remove test valuations. Normalise channel spellings first.

### M4. CAC payback

`Core` · rank 4 of 11 · score **4.00** · evidence **S** · added in round 2

*Scores: decision 5, goal link 5, diagnostic 3, early warning 3, measurable 2.*

**Definition**
- **What it is:** How long until the cost of winning a customer is earned back.
- **Formula:** Seller version: cost per car sold ÷ contribution per car (below 1 means the first sale repays the cost). Dealer version: dealer acquisition cost ÷ monthly contribution per active dealer, in months.
- **Data needed:** Spend by channel, contribution per car, dealer cohorts and their activity.
- **Evidence (S):** Unit-economics practice. Inovia defines CAC payback as the months needed to recover acquisition cost. One investor rule of thumb (net contribution about three times acquisition cost after 18 months) is one person's view, not a standard. Applying it to one-off sellers and repeat dealers is my adaptation.

**Why it ranks here:** It links marketing to profit directly. It ranks below conversion and cost per sale because it needs the hardest data: contribution per car and cohort tracking.

**Insights it can give**
- Ratio under 1 for sellers: the first sale repays the marketing cost.
- Dealer payback lengthening: new dealers are less active or dearer to win.
- A channel with fast payback and small volume: room to scale it.
- **Read it with:** Cost per car sold and contribution per car.
- **Decision it supports:** How much to pay to win a seller or a dealer.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V8 Ranked horizontal bar chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** The question is which channels pay back and which do not, so rank them against a line at 1.0.
- **Build notes:** Bars: payback ratio by channel, reference line at 1.0, red above it.

| Platform | Main (V8) | Companion (V1) |
|---|---|---|
| Looker Studio | Bar chart, sorted, with reference line | Scorecard with comparison |
| Streamlit | `st.bar_chart(horizontal=True)`, Plotly for a threshold | `st.metric` (native) |
| Python | `px.bar(orientation='h')` + `add_vline` | `go.Indicator` or a printed number |
| SQL returns | one row per item, sorted, with its denominator | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT channel, cost_per_sale / NULLIF(contribution_per_car, 0) AS payback_ratio
FROM channel_unit_economics;   -- a view built from the cost-per-sale and contribution queries
```

**Drill:** Drill down channel, then campaign.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Contribution per car | Cost per car sold ÷ revenue per car sold | A lower bound: a channel that fails here fails everywhere | Certainty that a passing channel is profitable |
| Dealer cohorts | Dealer acquisition spend ÷ new active dealers | The cost to win one dealer | How long it takes to earn that back |

**Trap:** Different costs in the numerator across teams. Fix one definition.

### M5. Seller satisfaction (NPS or CSAT)

`Core` · rank 5 of 11 · score **3.90** · evidence **S** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 4, early warning 4, measurable 3.*

**Definition**
- **What it is:** How likely sellers are to recommend Motorway, or how satisfied they are after a sale.
- **Formula:** NPS = % promoters (9 or 10) − % detractors (0 to 6) on a 0 to 10 'would you recommend' question. CSAT = % answering satisfied or very satisfied.
- **Data needed:** Post-sale survey responses with seller, date, score and, if possible, channel.
- **Evidence (S):** Marketplace guidance advises tracking buyer and seller NPS separately. OPENLANE reports a per-transaction satisfaction score (8.3 out of 10, company self-report). Aggregator NPS pages for auction firms disagree with each other and are not used.

**Why it ranks here:** Satisfaction moves before reviews and repeat behaviour do, so it is a leading indicator of both brand and retention.

**Insights it can give**
- Falling among sellers who completed: the post-sale experience (collection, payment, price change).
- Low among sellers who did not sell: valuation expectations or the offers.
- Detractors growing as passives shrink: a real problem, not noise.
- **Read it with:** Price changed at collection and support contacts.
- **Decision it supports:** Which part of the journey to fix first.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V1 Scorecard: one number with its change. **Companion:** V6 100% stacked column chart (mix over time).
- **Why:** One headline number leads. The mix of promoters, passives and detractors beneath shows why it moved.
- **Build notes:** Scorecard: NPS with response count. Beneath: 100% stacked columns by month.

| Platform | Main (V1) | Companion (V6) |
|---|---|---|
| Looker Studio | Scorecard with comparison | 100% stacked column or area |
| Streamlit | `st.metric` (native) | shares in pandas, then `st.area_chart` |
| Python | `go.Indicator` or a printed number | `px.area(groupnorm='percent')` |
| SQL returns | one row: value and prior value | one row per period per segment, with its share |
| Antigravity IDE | printed value or DataFrame in a cell | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT DATE_TRUNC('month', answered_at) AS month, COUNT(*) AS responses,
       100.0 * (AVG(CASE WHEN score >= 9 THEN 1.0 ELSE 0 END) - AVG(CASE WHEN score <= 6 THEN 1.0 ELSE 0 END)) AS nps
FROM seller_survey GROUP BY 1;
```

**Drill:** Drill down by channel and by the sale outcome (sold or not).

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Enough responses | Quarterly score with the response count | A stable figure | Month-to-month movement |
| Any survey | Review score and support contact rate | Indirect signals of satisfaction | The view of sellers who did not finish or review |

**Trap:** Survey bias: sellers who finished the sale answer differently from those who did not.

### M6. Organic share of valuations

`Core` · rank 6 of 11 · score **3.80** · evidence **S** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 3, early warning 4, measurable 4.*

**Definition**
- **What it is:** How much of the seller flow arrives without paid marketing.
- **Formula:** Valuations from unpaid sources (direct, organic search, referral) ÷ all valuations.
- **Data needed:** `channel` or source on every valuation, with paid and unpaid defined once.
- **Evidence (S):** a16z unit economics: watch whether acquisition cost falls and the organic share of users grows.

**Why it ranks here:** A rising organic share means growth is cheaper and a brand effect is working. A falling one means dependence on paid spend.

**Insights it can give**
- Rising: brand and word of mouth do more of the work.
- Falling as paid spend rises: growth depends on spend.
- Flat while totals rise: paid and organic grow together, a healthy pattern.
- **Read it with:** Brand awareness and cost per car sold.
- **Decision it supports:** The balance between brand and performance marketing.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V6 100% stacked column chart (mix over time). **Companion:** V1 Scorecard: one number with its change.
- **Why:** A share of a total, over time, is what a 100% stacked chart shows. The scorecard gives the headline organic share.
- **Build notes:** Weekly 100% stacked area, paid colours warm and unpaid colours cool.

| Platform | Main (V6) | Companion (V1) |
|---|---|---|
| Looker Studio | 100% stacked column or area | Scorecard with comparison |
| Streamlit | shares in pandas, then `st.area_chart` | `st.metric` (native) |
| Python | `px.area(groupnorm='percent')` | `go.Indicator` or a printed number |
| SQL returns | one row per period per segment, with its share | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', created_at) AS week,
       AVG(CASE WHEN channel IN ('organic', 'direct', 'referral') THEN 1.0 ELSE 0 END) AS organic_share
FROM valuations WHERE is_test = FALSE GROUP BY 1;
```

**Drill:** Drill down within the organic group (direct, search, referral).

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Source tracking | Share of valuations with no campaign tag | A rough organic share | The split between direct, search and referral |
| Any source data | Brand search volume trend | Whether interest in the brand is rising | Any link to actual valuations |

**Trap:** Attribution: a seller who saw a paid ad and later came direct is counted as organic.

### M7. Cost per valuation (cost per lead)

`Core` · rank 7 of 11 · score **3.35** · evidence **I** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 3, early warning 4, measurable 5.*

**Definition**
- **What it is:** The price of getting one seller to start.
- **Formula:** Marketing spend ÷ valuations started, per channel and week.
- **Data needed:** Spend by channel and week, and valuations by channel and week.
- **Evidence (I):** A standard marketing measure. Not published by Motorway.

**Why it ranks here:** It reacts first when a campaign changes, so it is a good early warning. It is the most misleading metric when read alone, because cheap leads are not good leads.

**Insights it can give**
- A jump in one channel on a date: a campaign changed targeting or bids.
- Rising everywhere: competition for the same audience, or seasonality.
- Falling with conversion falling: cheaper but worse leads.
- **Read it with:** Cost per car sold.
- **Decision it supports:** Day-to-day campaign tuning.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V3 Line chart against last year or last period. **Companion:** V1 Scorecard: one number with its change.
- **Why:** One line per paid channel on a shared axis shows which channel is getting dearer.
- **Build notes:** Weekly lines, one per channel. Mark campaign launches with a vertical line.

| Platform | Main (V3) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + comparison range | Scorecard with comparison |
| Streamlit | `st.line_chart` (native) | `st.metric` (native) |
| Python | `px.line` with several y columns | `go.Indicator` or a printed number |
| SQL returns | one row per period, one column per series | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
WITH sp AS (SELECT week, channel, SUM(spend) AS spend FROM spend_weekly GROUP BY 1, 2),
     v  AS (SELECT DATE_TRUNC('week', created_at) AS week, channel, COUNT(*) AS valuations FROM valuations GROUP BY 1, 2)
SELECT sp.week, sp.channel, sp.spend * 1.0 / v.valuations AS cost_per_valuation FROM sp JOIN v USING (week, channel);
```

**Drill:** Drill down channel, then campaign.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Weekly spend | Monthly points | Level by channel | Reaction to a campaign |
| Spend by channel | Total spend ÷ total valuations | Blended cost | Which channel is efficient |

**Trap:** Always show next to cost per car sold.

### M8. Review score

`Supporting` · rank 8 of 11 · score **2.70** · evidence **M** · from the first sheets

*Scores: decision 2, goal link 3, diagnostic 2, early warning 3, measurable 5.*

**Definition**
- **What it is:** Trust from past sellers.
- **Formula:** Average star rating across verified reviews.
- **Data needed:** Review ratings with dates, from an external review site.
- **Evidence (M):** Trustpilot shows about 4.4 to 4.5 out of 5 from over 100,000 reviews.

**Why it ranks here:** It is public proof of trust but it moves slowly and rarely drives a decision.

**Insights it can give**
- Share of 1-star rising while the average holds: an emerging issue the average hides.
- Reviews naming the same topic: a specific failure (price change, collection).
- Review volume falling: fewer completed sales or less prompting.
- **Read it with:** Seller satisfaction and support reasons.
- **Decision it supports:** Reputation management, and a check on internal surveys.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V1 Scorecard: one number with its change. **Companion:** V4 Column chart.
- **Why:** A single score for the headline, and the star distribution beneath because an average hides a split.
- **Build notes:** Scorecard for the average. Columns for the share at each star level.

| Platform | Main (V1) | Companion (V4) |
|---|---|---|
| Looker Studio | Scorecard with comparison | Column chart |
| Streamlit | `st.metric` (native) | `st.bar_chart` (native) |
| Python | `go.Indicator` or a printed number | `px.bar` |
| SQL returns | one row: value and prior value | one row per category |
| Antigravity IDE | printed value or DataFrame in a cell | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT stars, COUNT(*) AS reviews FROM reviews GROUP BY stars;   -- average: SELECT AVG(stars) FROM reviews;
```

**Drill:** No drill down. Link out to read the reviews.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| The distribution | Average with the review count | The headline | The split that explains it |
| History | Current score as a scorecard | Today's level | Trend |

**Trap:** An average of many 5s and some 1s differs from all 4s.

### M9. Seller price advantage

`Supporting` · rank 9 of 11 · score **2.65** · evidence **M** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 2, early warning 2, measurable 3.*

**Definition**
- **What it is:** The proof behind the promise.
- **Formula:** Share of sales above an independent market price guide, and the average £ gained against part exchange (customer survey).
- **Data needed:** `sale_price` and `guide_price` for each sale. The part exchange comparison comes from a survey.
- **Evidence (M):** Motorway claims 84% of sellers beat the market price and £1,600 more than part exchange. Self-reported.

**Why it ranks here:** It supports marketing claims but it is not an operational control. Rank is low because nothing changes if it moves a point.

**Insights it can give**
- Share above guide falling: softer dealer demand, or guide prices rose.
- High share but a small margin above guide: the claim is true but thin.
- Strong in some makes only: the advantage is specific to a segment.
- **Read it with:** Sale price against guide (Commercial) and bids per car.
- **Decision it supports:** Whether a marketing claim still holds.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V1 Scorecard: one number with its change. **Companion:** V12 Histogram with median and threshold lines.
- **Why:** The claim is one number. The histogram of price against guide, built from your own data, shows how robust it is.
- **Build notes:** Big percentage with the sale count beside it.

| Platform | Main (V1) | Companion (V12) |
|---|---|---|
| Looker Studio | Scorecard with comparison | Calculated bin + column chart, or Boxplot |
| Streamlit | `st.metric` (native) | `numpy.histogram` + `st.bar_chart`, or `px.histogram` |
| Python | `go.Indicator` or a printed number | `px.histogram` + `add_vline(median)` |
| SQL returns | one row: value and prior value | one row per bin: bin start, count |
| Antigravity IDE | printed value or DataFrame in a cell | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT AVG(CASE WHEN sale_price > guide_price THEN 1.0 ELSE 0 END) AS share_above_guide, COUNT(*) AS sales
FROM completed_sales WHERE guide_price IS NOT NULL;
```

**Drill:** No drill down on the card.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Guide price | Sale price against the median of similar cars | An internal fairness check | External credibility |
| Part exchange survey | Share above guide only | Half of the claim | The £ comparison with part exchange |

**Trap:** A company's own claim is evidence of what it says, not an audit.

### M10. Visits and engagement

`Supporting` · rank 10 of 11 · score **2.55** · evidence **P** · from the first sheets

*Scores: decision 2, goal link 2, diagnostic 3, early warning 3, measurable 4.*

**Definition**
- **What it is:** Audience reach.
- **Formula:** Monthly average visits across web and app, and minutes per visit.
- **Data needed:** Web and app analytics by day: `visits`, `engaged_minutes`, `source`.
- **Evidence (P):** Auto Trader reports cross-platform visits (81.6m a month) and minutes as KPIs.

**Why it ranks here:** Traffic is an input to the funnel but not an outcome. It matters more to a listings site than to Motorway.

**Insights it can give**
- Visits up, valuations flat: the wrong audience, or the page is not converting.
- Minutes per visit falling: less engaged traffic.
- App share rising: journeys are moving to the app.
- **Read it with:** Valuations started.
- **Decision it supports:** Channel and content choices.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V9 Combo chart with two axes (columns plus a line). **Companion:** V1 Scorecard: one number with its change.
- **Why:** Volume and quality (visits and minutes per visit) are different units, so two axes.
- **Build notes:** Columns for visits, line for minutes per visit. Do not truncate the column axis.

| Platform | Main (V9) | Companion (V1) |
|---|---|---|
| Looker Studio | Combo chart, line on the right axis | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly `secondary_y`) | `st.metric` (native) |
| Python | `make_subplots(secondary_y=True)` or `ax.twinx()` | `go.Indicator` or a printed number |
| SQL returns | one row per period with both measures | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('month', day) AS month, SUM(visits) AS visits, SUM(engaged_minutes) * 1.0 / SUM(visits) AS minutes_per_visit
FROM web_app_daily GROUP BY 1;
```

**Drill:** Drill down by traffic source, then landing page.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Engagement minutes | Visits only | Reach | Quality of the visit |
| Source | Total visits | Trend | Where the traffic comes from |

**Trap:** Web and app visitors overlap. Do not add them together as people.

### M11. Brand awareness

`Supporting` · rank 11 of 11 · score **2.55** · evidence **M** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 2, early warning 2, measurable 2.*

**Definition**
- **What it is:** Whether car owners think of Motorway.
- **Formula:** Survey: share of UK car owners who recognise the brand with prompting, and who name it without prompting.
- **Data needed:** Survey results by quarter with the sample size.
- **Evidence (M):** Motorway's TV campaigns name awareness as the aim. No figure is published, so the sample line is invented.

**Why it ranks here:** Strategic but slow, noisy and hard to attribute. Rank is lowest because it cannot guide weekly decisions.

**Insights it can give**
- Unprompted awareness rising after a campaign: it reached memory, not just recognition.
- Prompted up, unprompted flat: people recognise the name but do not think of it first.
- No change after spend: wrong audience or too little weight.
- **Read it with:** Organic share of valuations.
- **Decision it supports:** Brand budget.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Two survey series over time with campaign markers show whether awareness rises after spend.
- **Build notes:** Quarterly lines for prompted and unprompted, vertical markers for campaigns.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT quarter, AVG(prompted_aware::int) AS prompted, AVG(unprompted_aware::int) AS unprompted, COUNT(*) AS respondents
FROM brand_survey GROUP BY quarter;
```

**Drill:** No drill down. A survey cannot be sliced beyond its sample.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Several survey waves | Latest result with a margin of error | Current level | Any trend or campaign effect |
| Any survey | Brand search volume and direct traffic | A behavioural proxy | A true measure of the population |

**Trap:** Print the sample size. A 2 point move on a small sample is noise.

---

## OPERATIONS

*Does every agreed sale complete quickly, safely and without disputes?*

**Suggested page layout**
- **Top row, single values:** Completion rate (and fall-through), Price changed at collection, Time to sell, Completed sales. Each with its change against the last period.
- **Middle, the Headline charts:** Completion rate (and fall-through) (line chart with a target line or band); Claims (arbitration) rate by dealer (ranked horizontal bar chart); Price changed at collection (ranked horizontal bar chart).
- **Lower, the Core diagnostics:** Support contacts per 100 completed sales, Time to sell, Completed sales, Days to seller payment.
- **Second page or drill through:** On-time collection and cost per move, Problem vehicles stopped, Seller verification coverage.

### O1. Completion rate (and fall-through)

`Headline` · rank 1 of 10 · score **4.55** · evidence **P** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 4, early warning 4, measurable 4.*

**Definition**
- **What it is:** How many accepted offers finish.
- **Formula:** Completed sales ÷ offers accepted. Fall-through rate = 1 − completion rate.
- **Data needed:** One row per accepted offer with its final outcome and the date accepted.
- **Evidence (P):** ACV counts a unit once sold even if later unwound, so reversals are tracked separately.

**Why it ranks here:** Every fall-through wastes dealer, seller and logistics effort, and revenue is earned only on completion. It is the quality control of the whole post-sale process and it points to causes.

**Insights it can give**
- A fall concentrated in one region: logistics or a local dealer.
- A fall while 'price changed at collection' rises: profile accuracy.
- A fall in the newest weeks only, when grouped by completion date: an artefact. Regroup by acceptance date.
- **Read it with:** Price changed at collection and on-time collection.
- **Decision it supports:** Where to send operations effort.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A rate over time needs a target band so the reader sees the moment it leaves normal.
- **Build notes:** Weekly line with a shaded band (for example 93% to 95%). Group by the date the offer was accepted.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', accepted_at) AS week, COUNT(*) AS accepted,
       SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed,
       100.0 * SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) / COUNT(*) AS completion_pct
FROM offers GROUP BY 1;
```

**Drill:** Drill down by region, dealer, and reason for fall-through.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Fall-through reasons | Completion by region and dealer size | Where it happens | Why it happens |
| Acceptance dates | Completed ÷ accepted in the same month | An approximate rate | Fairness for recent periods |

**Trap:** Group by acceptance date. Grouping by completion date makes recent weeks look worse.

### O2. Claims (arbitration) rate by dealer

`Headline` · rank 2 of 10 · score **4.20** · evidence **P** · from the first sheets

*Scores: decision 5, goal link 4, diagnostic 4, early warning 4, measurable 3.*

**Definition**
- **What it is:** Disputes after purchase.
- **Formula:** Claims opened ÷ vehicles purchased, per dealer, per month.
- **Data needed:** `claim_id`, `dealer_id`, and purchases per dealer.
- **Evidence (P):** ACV Auctions defines the arbitration rate this way in its programme terms. The 25% review threshold on the sample dashboard mirrors an ACV term.

**Why it ranks here:** It protects the trust of both sides and points to specific dealers to act on, so it converts directly into decisions.

**Insights it can give**
- A few dealers far above the rest: the behaviour of those dealers.
- Rising across all dealers: listing accuracy or a policy change.
- Claims clustering on one reason: a specific inspection gap.
- **Read it with:** Condition grade accuracy.
- **Decision it supports:** Dealer review, and product fixes for listing accuracy.

**How to show it**
- **Format:** Chart.
- **Main visual:** V8 Ranked horizontal bar chart. **Companion:** V17 Table with bars or heatmap.
- **Why:** A ranked list highlights outliers at once. A table beside it gives purchases and claims behind each rate.
- **Build notes:** Highest first, threshold line, red above it. Filter out dealers with very few purchases.

| Platform | Main (V8) | Companion (V17) |
|---|---|---|
| Looker Studio | Bar chart, sorted, with reference line | Table with bars or heatmap |
| Streamlit | `st.bar_chart(horizontal=True)`, Plotly for a threshold | `st.dataframe` with `column_config` |
| Python | `px.bar(orientation='h')` + `add_vline` | pandas Styler |
| SQL returns | one row per item, sorted, with its denominator | one row per item |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
WITH p AS (SELECT dealer_id, COUNT(*) AS purchases FROM purchases WHERE purchased_at >= :start GROUP BY 1),
     c AS (SELECT dealer_id, COUNT(*) AS claims FROM claims WHERE opened_at >= :start GROUP BY 1)
SELECT p.dealer_id, p.purchases, COALESCE(c.claims, 0) AS claims, 100.0 * COALESCE(c.claims, 0) / p.purchases AS claims_pct
FROM p LEFT JOIN c USING (dealer_id) WHERE p.purchases >= 20 ORDER BY claims_pct DESC;
```

**Drill:** Drill through: click a dealer to open its claim list.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Enough purchases per dealer | Dealers grouped into size bands | Stable rates | Individual outliers |
| Purchases | Claims count by dealer | Who raises most claims | Fairness: big buyers will top the list |

**Trap:** A dealer with 2 purchases and 1 claim is 50%. Always show the denominator and set a minimum.

### O3. Price changed at collection

`Headline` · rank 3 of 10 · score **4.20** · evidence **I** · from the first sheets

*Scores: decision 4, goal link 4, diagnostic 5, early warning 4, measurable 4.*

**Definition**
- **What it is:** Friction between the profile and the real car.
- **Formula:** Sales where the price was adjusted after the dealer's inspection ÷ collections.
- **Data needed:** `price_at_listing`, `price_at_collection`, `adjustment_reason`.
- **Evidence (I):** Motorway says the dealer checks that the car matches its profile at collection. The KPI is inferred.

**Why it ranks here:** It is the root cause behind fall-through, claims and distrust. Reasons tell product and operations exactly what to fix, so it is highly diagnostic.

**Insights it can give**
- One reason dominating (undisclosed damage): the photo or question flow misses it.
- High with certain dealers: negotiating behaviour, not car condition.
- Rising after a product change: the change made profiles less accurate.
- **Read it with:** Condition grade accuracy and claims.
- **Decision it supports:** Product fixes to the profile, and dealer policy.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V8 Ranked horizontal bar chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** The overall rate is one number. The reasons are a ranking.
- **Build notes:** Scorecard: overall rate. Bars: reasons sorted largest first.

| Platform | Main (V8) | Companion (V1) |
|---|---|---|
| Looker Studio | Bar chart, sorted, with reference line | Scorecard with comparison |
| Streamlit | `st.bar_chart(horizontal=True)`, Plotly for a threshold | `st.metric` (native) |
| Python | `px.bar(orientation='h')` + `add_vline` | `go.Indicator` or a printed number |
| SQL returns | one row per item, sorted, with its denominator | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT adjustment_reason, COUNT(*) AS adjusted
FROM collections WHERE price_at_collection <> price_at_listing GROUP BY 1 ORDER BY 2 DESC;
```

**Drill:** Drill down reason, then dealer or region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Reasons | Rate by region and by dealer | Where | Why |
| Listing price | Count of adjusted collections | Volume | The size of the adjustment and the rate |

**Trap:** A rising rate may reflect a better inspection process, not worse sellers.

### O4. Support contacts per 100 completed sales

`Core` · rank 4 of 10 · score **4.15** · evidence **I** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 4, early warning 5, measurable 4.*

**Definition**
- **What it is:** How often customers need help, relative to volume.
- **Formula:** Support conversations ÷ completed sales × 100, split by reason.
- **Data needed:** Support tickets with date, reason tag and, if possible, the sale they relate to.
- **Evidence (I):** Standard e-commerce operations practice. Published benchmarks conflict because sources count tickets and contacts differently, so no benchmark is used.

**Why it ranks here:** It is the earliest alarm in operations. A rising contact rate shows up before reviews, claims or churn move.

**Insights it can give**
- A spike in one reason: a specific failure (payments, collection slots).
- Rising after a release: a product regression.
- Flat rate with rising volume: growth, not a problem.
- **Read it with:** App stability and days to seller payment.
- **Decision it supports:** Staffing, and which root cause to fix.

**How to show it**
- **Format:** Chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V8 Ranked horizontal bar chart.
- **Why:** A rate over time for the alarm, and a ranked bar of reasons for the cause.
- **Build notes:** Weekly line of total contacts per 100 sales. Companion bar: reasons for the latest four weeks.

| Platform | Main (V2) | Companion (V8) |
|---|---|---|
| Looker Studio | Time series + reference line | Bar chart, sorted, with reference line |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.bar_chart(horizontal=True)`, Plotly for a threshold |
| Python | `px.line` + `add_hline` | `px.bar(orientation='h')` + `add_vline` |
| SQL returns | one row per period: numerator, denominator, rate | one row per item, sorted, with its denominator |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
WITH t AS (SELECT DATE_TRUNC('week', created_at) AS week, reason, COUNT(*) AS contacts FROM support_tickets GROUP BY 1, 2),
     s AS (SELECT DATE_TRUNC('week', completed_date) AS week, COUNT(*) AS sales FROM completed_sales GROUP BY 1)
SELECT t.week, t.reason, 100.0 * t.contacts / s.sales AS contacts_per_100_sales FROM t JOIN s USING (week);
```

**Drill:** Drill down by reason, then sub-reason.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Reason tags | Total contacts per 100 sales | The alarm | The cause |
| A link to sales | Contacts ÷ that week's sales | An approximate rate | Accuracy where the contact follows the sale by days |

**Trap:** A new help-centre or form changes ticket volume without changing real problems.

### O5. Time to sell

`Core` · rank 5 of 10 · score **4.00** · evidence **S** · from the first sheets

*Scores: decision 4, goal link 4, diagnostic 4, early warning 4, measurable 4.*

**Definition**
- **What it is:** Speed for the seller.
- **Formula:** Days from profile complete to offer accepted, and from offer accepted to collection and payment.
- **Data needed:** A timestamp for each step.
- **Evidence (S):** a16z time to match. Seller reviews mention 2 to 8 days end to end (anecdotal).

**Why it ranks here:** Speed is the product promise to the seller. A long tail shows where sellers wait.

**Insights it can give**
- Median stable, 90th percentile growing: a tail of stuck cars.
- Longer in one price band: thin dealer demand there.
- Second stage (acceptance to payment) growing: logistics, not demand.
- **Read it with:** Time to first bid and on-time collection.
- **Decision it supports:** Service-level promises to sellers.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V12 Histogram with median and threshold lines. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Time data is skewed, so a distribution beats an average. The scorecard gives the median and the 90th percentile.
- **Build notes:** Bins of one day, a line at the median, a line at the service level.

| Platform | Main (V12) | Companion (V1) |
|---|---|---|
| Looker Studio | Calculated bin + column chart, or Boxplot | Scorecard with comparison |
| Streamlit | `numpy.histogram` + `st.bar_chart`, or `px.histogram` | `st.metric` (native) |
| Python | `px.histogram` + `add_vline(median)` | `go.Indicator` or a printed number |
| SQL returns | one row per bin: bin start, count | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT FLOOR(EXTRACT(EPOCH FROM (accepted_at - profile_done_at)) / 86400) AS days, COUNT(*) AS offers
FROM offers GROUP BY 1 ORDER BY 1;   -- median: PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY days)
```

**Drill:** No drill down on the histogram. Offer a second view by region or price band.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Step timestamps | Listing date to completed date, in days | End-to-end time | Which stage is slow |
| Enough records | Median by week | A stable central figure | The shape of the tail |

**Trap:** Report the median and the 90th percentile. The mean is pulled up by a few slow cars.

### O6. Completed sales

`Core` · rank 6 of 10 · score **4.00** · evidence **I** · from the first sheets

*Scores: decision 4, goal link 5, diagnostic 3, early warning 3, measurable 5.*

**Definition**
- **What it is:** The real output of operations: sales where the car was collected and the seller was paid.
- **Formula:** Count of sales with status completed in the period.
- **Data needed:** `sale_id`, `status`, `completed_date`, `region`.
- **Evidence (I):** Motorway charges its seller fee only once a car is sold, collected and paid for.

**Why it ranks here:** It is the unit of revenue. It ranks below rates because a count mostly follows demand and calendar days.

**Insights it can give**
- Up with completion rate flat: demand.
- Down with accepted offers flat: fall-through.
- A weekly pattern: use it for capacity planning.
- **Read it with:** Completion rate.
- **Decision it supports:** Staffing and transport capacity.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V4 Column chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Weekly volume against a target is a classic column chart.
- **Build notes:** Weekly columns with a target line.

| Platform | Main (V4) | Companion (V1) |
|---|---|---|
| Looker Studio | Column chart | Scorecard with comparison |
| Streamlit | `st.bar_chart` (native) | `st.metric` (native) |
| Python | `px.bar` | `go.Indicator` or a printed number |
| SQL returns | one row per category | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', completed_date) AS week, COUNT(*) AS completed_sales FROM completed_sales GROUP BY 1;
```

**Drill:** Drill down week, day; by region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| A target | 4-week average as the reference | Whether this week is unusual | Whether it is good enough |
| Region | Total | Volume | Where |

**Trap:** Compare like weeks. Working days change the count.

### O7. Days to seller payment

`Core` · rank 7 of 10 · score **3.80** · evidence **I** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 3, early warning 4, measurable 4.*

**Definition**
- **What it is:** How long the seller waits for the money after the car is collected.
- **Formula:** Median time from collection to payment received by the seller, and the share paid within a set time.
- **Data needed:** `collected_at` and `paid_at` on each completed sale.
- **Evidence (I):** Not published for Motorway. Payment speed is a stated part of the service, but I did not find a figure.

**Why it ranks here:** Fast payment is a main reason to sell this way. A slowing median hurts trust before it shows in reviews.

**Insights it can give**
- Median stable but a growing tail: specific cases stuck (finance settlements, banking).
- Slower for one payment method: process, not volume.
- Slower at weekends or month end: the calendar. Define the promise in working days.
- **Read it with:** Share of sales through Motorway Pay, and support contacts about payment.
- **Decision it supports:** The payment process and the promise made to sellers.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V12 Histogram with median and threshold lines. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A distribution reveals a tail of slow payments, and a scorecard gives the median and the share paid on time.
- **Build notes:** Bins of a few hours or one day, with the service level marked.

| Platform | Main (V12) | Companion (V1) |
|---|---|---|
| Looker Studio | Calculated bin + column chart, or Boxplot | Scorecard with comparison |
| Streamlit | `numpy.histogram` + `st.bar_chart`, or `px.histogram` | `st.metric` (native) |
| Python | `px.histogram` + `add_vline(median)` | `go.Indicator` or a printed number |
| SQL returns | one row per bin: bin start, count | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM (paid_at - collected_at)) / 3600) AS median_hours,
       AVG(CASE WHEN paid_at - collected_at <= INTERVAL '24 hours' THEN 1.0 ELSE 0 END) AS paid_within_24h
FROM completed_sales;
```

**Drill:** Drill down by payment method and region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Times of day | Whole days | Level | Same-day performance |
| Payment timestamps | Payment-related support contacts per 100 sales | A symptom | A direct measure |

**Trap:** Weekends and bank holidays stretch payment time. Use working days if that is the promise.

### O8. On-time collection and cost per move

`Supporting` · rank 8 of 10 · score **3.75** · evidence **I** · from the first sheets

*Scores: decision 4, goal link 3, diagnostic 4, early warning 4, measurable 4.*

**Definition**
- **What it is:** Transport performance.
- **Formula:** Collections made in the agreed slot ÷ all collections, and transport cost ÷ moves.
- **Data needed:** `slot_start`, `slot_end`, `actual_collection_time`, `transport_cost`, `region`.
- **Evidence (I):** Motorway Move launched in 2024 (dealer transport from about £89 to £99). The KPI is inferred.

**Why it ranks here:** Late collections create fall-through and complaints, and cost per move drives contribution.

**Insights it can give**
- Low on-time with high cost: wrong carrier or a hard region.
- High on-time with high cost: service is being bought.
- A sudden fall in one region: a carrier problem.
- **Read it with:** Completion rate.
- **Decision it supports:** Carrier choice and regional pricing.

**How to show it**
- **Format:** Chart.
- **Main visual:** V9 Combo chart with two axes (columns plus a line). **Companion:** V8 Ranked horizontal bar chart.
- **Why:** Service and cost have different units, and a region that is cheap and late is not good, so both need to be seen together.
- **Build notes:** Columns for on-time % by region, coloured by status, a line for cost per move.

| Platform | Main (V9) | Companion (V8) |
|---|---|---|
| Looker Studio | Combo chart, line on the right axis | Bar chart, sorted, with reference line |
| Streamlit | `st.plotly_chart` (Plotly `secondary_y`) | `st.bar_chart(horizontal=True)`, Plotly for a threshold |
| Python | `make_subplots(secondary_y=True)` or `ax.twinx()` | `px.bar(orientation='h')` + `add_vline` |
| SQL returns | one row per period with both measures | one row per item, sorted, with its denominator |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT region, AVG(CASE WHEN actual_time <= slot_end THEN 1.0 ELSE 0 END) AS on_time,
       SUM(transport_cost) * 1.0 / COUNT(*) AS cost_per_move
FROM collections GROUP BY region;
```

**Drill:** Drill down region, then depot or route.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Cost | On-time % by region | Service level | Value for money |
| Slot times | Days from acceptance to collection | Speed | Whether the promise was kept |

**Trap:** Read the two measures together.

### O9. Problem vehicles stopped

`Supporting` · rank 9 of 10 · score **3.70** · evidence **I** · from the first sheets

*Scores: decision 4, goal link 4, diagnostic 3, early warning 4, measurable 3.*

**Definition**
- **What it is:** Fraud and risk control.
- **Formula:** Listings stopped for stolen, clocked, cloned or outstanding-finance flags ÷ listings checked.
- **Data needed:** `flag_type` for each stopped listing, and the count of listings checked.
- **Evidence (I):** Motorway announced protections against clocked and cloned cars. No figure is published.

**Why it ranks here:** It guards the platform's reputation and shows risk trends. It ranks lower because a high count may mean better detection.

**Insights it can give**
- One flag type rising: a specific fraud pattern.
- Rate flat while the count rises: more listings, not more fraud.
- A jump after a new check went live: detection improved.
- **Read it with:** Seller verification coverage.
- **Decision it supports:** Fraud controls.

**How to show it**
- **Format:** Chart.
- **Main visual:** V5 Stacked column chart. **Companion:** V2 Line chart with a target line or band.
- **Why:** Stacked columns show volume by flag type. A rate line separates growth in volume from growth in risk.
- **Build notes:** Monthly stacked columns, plus a line of stopped ÷ checked.

| Platform | Main (V5) | Companion (V2) |
|---|---|---|
| Looker Studio | Stacked column chart | Time series + reference line |
| Streamlit | `st.bar_chart(color=)` (native) | `st.plotly_chart` (Plotly, for the target line) |
| Python | `px.bar(color=)` | `px.line` + `add_hline` |
| SQL returns | one row per period per segment | one row per period: numerator, denominator, rate |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT DATE_TRUNC('month', stopped_at) AS month, flag_type, COUNT(*) AS stopped FROM stopped_listings GROUP BY 1, 2;
```

**Drill:** Drill through to the list of stopped listings for review.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Listings checked | Counts by type | Volume and mix | Whether risk is truly rising |
| Flag type | Total stopped | Scale | What kind of risk |

**Trap:** More stops can mean better detection, not more fraud. Say which reading you believe and why.

### O10. Seller verification coverage

`Supporting` · rank 10 of 10 · score **3.00** · evidence **M** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 2, early warning 3, measurable 5.*

**Definition**
- **What it is:** The share of sales with checked identity.
- **Formula:** Sales with automated ID and document checks ÷ all sales.
- **Data needed:** `verification_status` on each sale.
- **Evidence (M):** Motorway's target was more than 95% of sales by the end of Q1 2026. Earlier points on the sample line are invented.

**Why it ranks here:** Important for fraud, but once it reaches the target it becomes a monitoring figure.

**Insights it can give**
- Plateau below target: a seller group the flow does not handle.
- A dip after an app release: a broken step.
- At target: move attention to pass rate and time.
- **Read it with:** Verification pass rate and time (Product).
- **Decision it supports:** Completing the rollout.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V16 Bullet chart (value against a target and bands).
- **Why:** A share climbing to a target is a line to a reference. A bullet shows the current level against the 95% target.
- **Build notes:** Monthly line with a 95% reference line.

| Platform | Main (V2) | Companion (V16) |
|---|---|---|
| Looker Studio | Time series + reference line | Bullet chart |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.plotly_chart(go.Indicator)` with a bullet gauge |
| Python | `px.line` + `add_hline` | `go.Indicator(mode='number+gauge')` |
| SQL returns | one row per period: numerator, denominator, rate | one row: value, target, band limits |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT DATE_TRUNC('month', completed_date) AS month,
       AVG(CASE WHEN verification_status = 'verified' THEN 1.0 ELSE 0 END) AS coverage
FROM completed_sales GROUP BY 1;
```

**Drill:** Light. By seller type if the data supports it.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| History | Bullet against the target | Today's gap | Whether it is closing |
| Status per sale | Share of sellers verified | Coverage of people | Coverage of transactions |

**Trap:** Coverage of sales is not coverage of sellers. Define the denominator.

---

## COMMERCIAL

*Are enough dealers bidding, buying and coming back?*

**Suggested page layout**
- **Top row, single values:** Sell-through, Active dealers, Bid volume and bids per car, Cumulative sell-through curve. Each with its change against the last period.
- **Middle, the Headline charts:** Sell-through (line chart with a target line or band); Active dealers (column chart); Bid volume and bids per car (combo chart with two axes (columns plus a line)).
- **Lower, the Core diagnostics:** Cumulative sell-through curve, Time to first bid, Sale price against market guide, Market depth: bidders per car.
- **Second page or drill through:** Dealer concentration and retention, Cars in the daily sale, Motorway Pay adoption (dealers), Verified dealers.

### C1. Sell-through

`Headline` · rank 1 of 11 · score **4.75** · evidence **S** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 5, early warning 4, measurable 4.*

**Definition**
- **What it is:** How often supply meets demand.
- **Formula:** Cars sold ÷ cars entered into the sale.
- **Data needed:** One row per listing with its outcome.
- **Evidence (S):** a16z match rate. Motorway does not publish it. ACV Auctions reports Marketplace Units and OPENLANE reports vehicles offered and sold, but I could not read a stated conversion formula for either.

**Why it ranks here:** This is marketplace liquidity itself. It is the point where seller, dealer and price meet, and a fall can be traced to a slice, so it is both an outcome and a diagnostic.

**Insights it can give**
- Falls with bids per car falling: a demand problem.
- Falls with bids per car steady: supply mix, or seller price expectations.
- Falls in one slice only: a local or segment issue, not the market.
- **Read it with:** Bids per car, bidders per car, and cars in the daily sale.
- **Decision it supports:** Whether to act on dealers (demand), sellers (pricing guidance) or the supply mix.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A rate over time with a target, and the number of cars behind it as a tooltip.
- **Build notes:** Weekly line, zoomed y-axis, target line. Show the count of cars on each point.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', sale_date) AS week, COUNT(*) AS cars_entered,
       SUM(CASE WHEN outcome = 'sold' THEN 1 ELSE 0 END) AS cars_sold,
       100.0 * SUM(CASE WHEN outcome = 'sold' THEN 1 ELSE 0 END) / COUNT(*) AS sell_through_pct
FROM daily_sale_entries GROUP BY 1;
```

**Drill:** Drill down by region, make, price band and age band. A fall often hides in one slice.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Weekly outcomes | Monthly rate | Level and slow trend | Early warning |
| Slices | Overall rate with the count | The headline | Where the fall is |
| Unsold listings | Cars sold count | Volume | The rate itself. It cannot be computed. |

**Trap:** A mix shift to harder-to-sell cars can lower the rate when nothing got worse. Compare like with like.

### C2. Active dealers

`Headline` · rank 2 of 11 · score **4.65** · evidence **P** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 4, early warning 4, measurable 5.*

**Definition**
- **What it is:** Dealers who actually take part.
- **Formula:** Dealers who bid on or bought at least one car in the period.
- **Data needed:** Bids and purchases with `dealer_id` and date.
- **Evidence (P):** ACV Auctions reports Marketplace Buyers (22,062 in FY2025).

**Why it ranks here:** Demand depends on participating dealers, not registered ones. The gap between verified and active is a main growth lever.

**Insights it can give**
- Verified rising, active flat: onboarding without activation.
- Active falling in one region: a local coverage gap.
- Active steady but purchases falling: dealers are bidding less.
- **Read it with:** Bids per car and dealer concentration.
- **Decision it supports:** Dealer activation and account management.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V4 Column chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Side-by-side columns of verified and active dealers show the gap. A scorecard gives the activity ratio.
- **Build notes:** Monthly, grey for verified, blue for active.

| Platform | Main (V4) | Companion (V1) |
|---|---|---|
| Looker Studio | Column chart | Scorecard with comparison |
| Streamlit | `st.bar_chart` (native) | `st.metric` (native) |
| Python | `px.bar` | `go.Indicator` or a printed number |
| SQL returns | one row per category | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('month', activity_date) AS month, COUNT(DISTINCT dealer_id) AS active_dealers
FROM dealer_activity WHERE action IN ('bid', 'purchase') GROUP BY 1;
```

**Drill:** Drill down by dealer size and region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Bid data | Buying dealers | Dealers who purchased | Those who bid and lost, so demand is understated |
| History | Activity ratio as a scorecard | Today's level | Trend |

**Trap:** Keep the activity window fixed (one calendar month).

### C3. Bid volume and bids per car

`Headline` · rank 3 of 11 · score **4.55** · evidence **M** · from the first sheets

*Scores: decision 5, goal link 4, diagnostic 4, early warning 5, measurable 5.*

**Definition**
- **What it is:** Strength of dealer demand.
- **Formula:** Total bids in the period, and bids ÷ cars in the daily sale.
- **Data needed:** One row per bid, and the count of cars offered.
- **Evidence (M):** Motorway reports bid volumes up about 20% in 2025, and EVs drew 29% more bids than the average car.

**Why it ranks here:** Bids lead sales. A fall in bids per car warns of a sell-through fall before it happens.

**Insights it can give**
- Bids per car falling while cars rise: demand is not keeping up with supply.
- Bids rising on one fuel type or make: shifting dealer appetite.
- Bids per car high but sell-through low: bids sit below seller expectations.
- **Read it with:** Sell-through and time to first bid.
- **Decision it supports:** Dealer engagement actions and supply targets.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V9 Combo chart with two axes (columns plus a line). **Companion:** V1 Scorecard: one number with its change.
- **Why:** Total and per-car measures are different units. Columns show volume, the line shows intensity.
- **Build notes:** Weekly columns for bids and a line for bids per car.

| Platform | Main (V9) | Companion (V1) |
|---|---|---|
| Looker Studio | Combo chart, line on the right axis | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly `secondary_y`) | `st.metric` (native) |
| Python | `make_subplots(secondary_y=True)` or `ax.twinx()` | `go.Indicator` or a printed number |
| SQL returns | one row per period with both measures | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
WITH b AS (SELECT DATE_TRUNC('week', bid_time) AS week, COUNT(*) AS bids FROM bids GROUP BY 1),
     c AS (SELECT DATE_TRUNC('week', sale_date) AS week, COUNT(*) AS cars FROM daily_sale_entries GROUP BY 1)
SELECT week, bids, cars, bids * 1.0 / cars AS bids_per_car FROM b JOIN c USING (week);
```

**Drill:** Drill down by make, fuel type and price band.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Cars offered | Total bids | Demand volume | Whether demand kept pace with supply |
| Bid-level data | Share of cars with at least one bid | Coverage | Depth |

**Trap:** Total bids can rise just because more cars were offered. Bids per car separates demand from supply.

### C4. Cumulative sell-through curve

`Core` · rank 4 of 11 · score **4.20** · evidence **S** · added in round 2

*Scores: decision 4, goal link 5, diagnostic 5, early warning 3, measurable 3.*

**Definition**
- **What it is:** How quickly cars sell after they are first listed, and how many never do.
- **Formula:** For each weekly cohort of newly listed cars, the share sold within 1, 2, 3 … days (or by first, second, third attempt).
- **Data needed:** `first_listed_at`, `sold_at`, and optionally `attempt_no`.
- **Evidence (S):** a16z describes the share of inventory that clears over time as a curve, called inventory turnover for product marketplaces.

**Why it ranks here:** A single sell-through rate hides speed. A curve shows both the speed and the final level, and comparing cohorts shows whether a change helped.

**Insights it can give**
- The curve rises faster for new cohorts: cars sell sooner.
- Same speed but a lower plateau: more cars never sell.
- Flat after day 3: relisting adds little.
- **Read it with:** Sell-through and time to first bid.
- **Decision it supports:** Relisting policy and seller messaging.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V15 Line per cohort (cumulative curve by days since start). **Companion:** V1 Scorecard: one number with its change.
- **Why:** Lines per cohort on a days-since-listing axis let you see whether newer cohorts sell faster.
- **Build notes:** Plot the last six weekly cohorts. Only show a cohort up to the day it has data for.

| Platform | Main (V15) | Companion (V1) |
|---|---|---|
| Looker Studio | Line chart, dimension = days since start | Scorecard with comparison |
| Streamlit | pivot, then `st.line_chart` | `st.metric` (native) |
| Python | `px.line(color='cohort')` | `go.Indicator` or a printed number |
| SQL returns | one row per cohort per day since start | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', first_listed_at) AS cohort_week, d AS days_since_listing,
       AVG(CASE WHEN sold_at IS NOT NULL AND sold_at <= first_listed_at + d * INTERVAL '1 day' THEN 1.0 ELSE 0 END) AS cumulative_sold
FROM listings CROSS JOIN generate_series(0, 14) AS d GROUP BY 1, 2;   -- Postgres; use a numbers table elsewhere
```

**Drill:** No drill down on the curve. Split by price band on a second chart.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Sale dates | Sold on first, second, third listing as columns | The value of relisting | Speed in days |
| Mature cohorts | Curve for cohorts older than 14 days | A fair comparison | The newest weeks |

**Trap:** Cut each cohort at its maturity. A recent cohort cannot show a day-14 value yet.

### C5. Time to first bid

`Core` · rank 5 of 11 · score **4.15** · evidence **S** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 4, early warning 5, measurable 4.*

**Definition**
- **What it is:** How quickly dealers respond to a newly listed car.
- **Formula:** Time from listing going live to the first bid, per car.
- **Data needed:** `listed_at` and the first `bid_time` per listing, including cars that never get a bid.
- **Evidence (S):** a16z time to match: for example, how long a user waits for a first quote.

**Why it ranks here:** It is the first sign of demand for a car, and a long wait predicts unsold cars. It also tells a seller how fast the market responds.

**Insights it can give**
- Longer for one segment: dealers are not watching that kind of car.
- A growing share with no bid: thin demand.
- Faster after an alert feature: the feature works.
- **Read it with:** Bidders per car.
- **Decision it supports:** Dealer alerts and listing timing.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V12 Histogram with median and threshold lines. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A distribution, because a few cars with no bids matter most and an average would hide them.
- **Build notes:** Bins of minutes or hours, median line, and a separate bar for cars with no bid.

| Platform | Main (V12) | Companion (V1) |
|---|---|---|
| Looker Studio | Calculated bin + column chart, or Boxplot | Scorecard with comparison |
| Streamlit | `numpy.histogram` + `st.bar_chart`, or `px.histogram` | `st.metric` (native) |
| Python | `px.histogram` + `add_vline(median)` | `go.Indicator` or a printed number |
| SQL returns | one row per bin: bin start, count | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT l.listing_id, MIN(b.bid_time) - l.listed_at AS time_to_first_bid
FROM listings l LEFT JOIN bids b ON b.listing_id = l.listing_id GROUP BY l.listing_id, l.listed_at;
```

**Drill:** No drill down on the histogram. Split by price band or make on a second chart.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Bid timestamps | Share of cars with a bid by the end of day one | Coverage | Speed |
| Zero-bid cars in the data | Median among cars with bids, flagged | Speed where demand exists | The cars that matter most |

**Trap:** Cars with no bid must stay in the data, or the median looks too good.

### C6. Sale price against market guide

`Core` · rank 6 of 11 · score **4.00** · evidence **M** · from the first sheets

*Scores: decision 4, goal link 5, diagnostic 4, early warning 3, measurable 3.*

**Definition**
- **What it is:** Whether dealers pay a fair price.
- **Formula:** Final sale price ÷ an independent market price guide.
- **Data needed:** `sale_price` and `guide_price` per sale.
- **Evidence (M):** Motorway claims 84% of sellers beat the market price (self-reported).

**Why it ranks here:** It connects dealer behaviour to seller value, which is the product promise. It is limited by the quality of the guide.

**Insights it can give**
- Distribution shifting left: softer demand or rising guide prices.
- Wide spread: the guide fits some cars poorly.
- Below guide for one make: a segment the dealer base undervalues.
- **Read it with:** Bidders per car.
- **Decision it supports:** Pricing guidance to sellers, and dealer recruitment by segment.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V12 Histogram with median and threshold lines. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A distribution around 100% shows both the average gap and the spread.
- **Build notes:** Bins of 1.5 percentage points, a line at 100%, bars above it coloured differently.

| Platform | Main (V12) | Companion (V1) |
|---|---|---|
| Looker Studio | Calculated bin + column chart, or Boxplot | Scorecard with comparison |
| Streamlit | `numpy.histogram` + `st.bar_chart`, or `px.histogram` | `st.metric` (native) |
| Python | `px.histogram` + `add_vline(median)` | `go.Indicator` or a printed number |
| SQL returns | one row per bin: bin start, count | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT FLOOR(100.0 * sale_price / guide_price / 1.5) * 1.5 AS pct_of_guide_bin, COUNT(*) AS sales
FROM completed_sales WHERE guide_price > 0 GROUP BY 1 ORDER BY 1;
```

**Drill:** No drill down on the histogram. A second view by make or age band.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Guide price | Sale price ÷ median of similar cars | Relative fairness | An external benchmark |
| Enough sales per segment | Overall share above guide | The headline | Segment differences |

**Trap:** The guide has its own error. Say which guide you used and who produced it.

### C7. Market depth: bidders per car

`Core` · rank 7 of 11 · score **3.90** · evidence **S** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 4, early warning 4, measurable 3.*

**Definition**
- **What it is:** Whether enough dealers compete for each car.
- **Formula:** Distinct dealers who bid per car, and the share of cars with at least three bidders (set your own threshold).
- **Data needed:** `listing_id`, `dealer_id` on every bid, and all listings so cars with zero bidders are counted.
- **Evidence (S):** a16z market depth: whether there is enough supply and demand that fits.

**Why it ranks here:** Competition sets the price. Cars with one bidder tend to sell near the reserve. It differs from bids per car, which can come from one dealer bidding repeatedly.

**Insights it can give**
- Many cars with one bidder: prices sit near the reserve.
- Thin in one region: recruit dealers there.
- Depth rising with flat bids: more dealers are taking part.
- **Read it with:** Sale price against guide.
- **Decision it supports:** Dealer recruitment by region and segment.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V12 Histogram with median and threshold lines. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A distribution of bidders per car shows the thin end where cars do not get competition.
- **Build notes:** Columns for 0, 1, 2, 3 and 4+ bidders. Scorecard: share with three or more.

| Platform | Main (V12) | Companion (V1) |
|---|---|---|
| Looker Studio | Calculated bin + column chart, or Boxplot | Scorecard with comparison |
| Streamlit | `numpy.histogram` + `st.bar_chart`, or `px.histogram` | `st.metric` (native) |
| Python | `px.histogram` + `add_vline(median)` | `go.Indicator` or a printed number |
| SQL returns | one row per bin: bin start, count | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT bidders, COUNT(*) AS cars FROM (
  SELECT l.listing_id, COUNT(DISTINCT b.dealer_id) AS bidders
  FROM listings l LEFT JOIN bids b ON b.listing_id = l.listing_id GROUP BY l.listing_id) t
GROUP BY bidders ORDER BY bidders;
```

**Drill:** Drill down by make, price band and region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Dealer identity on bids | Bids per car | Activity | Whether it is competition or one dealer bidding repeatedly |
| Listings without bids | Distribution among cars with bids, flagged | Depth where demand exists | The zero-bid share |

**Trap:** Left join from listings, or cars with no bids vanish.

### C8. Dealer concentration and retention

`Supporting` · rank 8 of 11 · score **3.85** · evidence **S** · from the first sheets

*Scores: decision 4, goal link 4, diagnostic 4, early warning 3, measurable 4.*

**Definition**
- **What it is:** How dependent the marketplace is on a few buyers, and whether dealers come back.
- **Formula:** Share of purchases made by the largest dealers, and the share of dealers who buy again within 30 or 90 days.
- **Data needed:** Purchases per dealer, and each dealer's first and later purchase dates.
- **Evidence (S):** a16z concentration of supply and demand, and retention cohorts.

**Why it ranks here:** It shows risk (loss of a large dealer) and health (repeat buying) at once.

**Insights it can give**
- Top 20% buying a rising share: growing dependence.
- Retention falling in new cohorts: onboarding quality.
- A large dealer's share falling: early churn risk.
- **Read it with:** Active dealers and retention cohorts.
- **Decision it supports:** Key account management.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V14 Cumulative share curve (Pareto or Lorenz). **Companion:** V1 Scorecard: one number with its change.
- **Why:** A cumulative curve shows how much of the demand a small group provides, in one picture.
- **Build notes:** Dealers ranked from largest on the x-axis, cumulative share of cars on the y-axis, with the equality diagonal.

| Platform | Main (V14) | Companion (V1) |
|---|---|---|
| Looker Studio | Table with running sum, or a line on a prepared column | Scorecard with comparison |
| Streamlit | `cumsum` in pandas, then `st.line_chart` | `st.metric` (native) |
| Python | `px.line` of the cumulative share | `go.Indicator` or a printed number |
| SQL returns | one row per item with its running share (window function) | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT dealer_id, purchases,
       SUM(purchases) OVER (ORDER BY purchases DESC) * 1.0 / SUM(purchases) OVER () AS cumulative_share,
       ROW_NUMBER() OVER (ORDER BY purchases DESC) * 1.0 / COUNT(*) OVER () AS dealer_rank_share
FROM (SELECT dealer_id, COUNT(*) AS purchases FROM purchases GROUP BY 1) t;
```

**Drill:** No drill down on the curve. Drill through to the top dealer list.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Enough dealers | Top-10 ranked bar with their combined share | Who matters | The full shape |
| First-purchase dates | Share of this month's buyers who also bought last month | A simple repeat rate | The cohort view |

**Trap:** State the retention window (30 or 90 days).

### C9. Cars in the daily sale

`Supporting` · rank 9 of 11 · score **3.60** · evidence **M** · from the first sheets

*Scores: decision 3, goal link 4, diagnostic 3, early warning 4, measurable 5.*

**Definition**
- **What it is:** Supply offered to dealers.
- **Formula:** Count of cars entered into each day's online sale.
- **Data needed:** `listing_id`, `sale_date`.
- **Evidence (M):** Motorway states up to 2,000 cars a day and more than 350,000 across 2025.

**Why it ranks here:** Supply is the raw material, but supply without sell-through is a cost, so it ranks mid-table.

**Insights it can give**
- Supply rising while sell-through falls: too much supply for demand.
- A fall a week after valuations fell: the expected lag.
- Weekday mix shifting: an operational pattern.
- **Read it with:** Valuations started and sell-through.
- **Decision it supports:** Dealer communications and the pace of marketing.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V3 Line chart against last year or last period. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Daily counts are noisy and weekly, so a 7-day average on top shows the trend.
- **Build notes:** Daily line in light colour, 7-day average in dark. Compare with the same weekday.

| Platform | Main (V3) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + comparison range | Scorecard with comparison |
| Streamlit | `st.line_chart` (native) | `st.metric` (native) |
| Python | `px.line` with several y columns | `go.Indicator` or a printed number |
| SQL returns | one row per period, one column per series | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT sale_date, COUNT(*) AS cars, AVG(COUNT(*)) OVER (ORDER BY sale_date ROWS 6 PRECEDING) AS avg_7d
FROM daily_sale_entries GROUP BY sale_date;
```

**Drill:** Drill down day, week; by region or make.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Daily data | Weekly columns | Trend | The weekday pattern |

**Trap:** Weekends are lower. Do not call that a drop.

### C10. Motorway Pay adoption (dealers)

`Supporting` · rank 10 of 11 · score **3.20** · evidence **M** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 3, early warning 3, measurable 5.*

**Definition**
- **What it is:** Take-up of a dealer product.
- **Formula:** Dealers using Motorway Pay ÷ buying dealers.
- **Data needed:** `dealer_id` and whether the dealer paid through Motorway Pay in the period.
- **Evidence (M):** Motorway states over 2,000 dealers use it. Earlier points on the sample line are invented.

**Why it ranks here:** A product adoption measure. It matters for revenue and stickiness, but it does not drive the marketplace's core outcomes.

**Insights it can give**
- Adoption rising but share of sales flat: trial without habit.
- High in large dealers: fit by segment.
- Dealers leaving the product: friction.
- **Read it with:** Share of sales paid through Motorway Pay.
- **Decision it supports:** Product rollout.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V7 Area chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A share climbing over time is an area or line chart.
- **Build notes:** Quarterly area.

| Platform | Main (V7) | Companion (V1) |
|---|---|---|
| Looker Studio | Area chart | Scorecard with comparison |
| Streamlit | `st.area_chart` (native) | `st.metric` (native) |
| Python | `px.area` | `go.Indicator` or a printed number |
| SQL returns | one row per period (per segment) | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('quarter', purchase_date) AS quarter,
       COUNT(DISTINCT CASE WHEN payment_method = 'pay' THEN dealer_id END) * 1.0 / COUNT(DISTINCT dealer_id) AS pay_adoption
FROM purchases GROUP BY 1;
```

**Drill:** Drill down by dealer size and region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Per-purchase payment data | The stated dealer count | Level | Trend and segments |

**Trap:** This counts dealers. The Finance version counts sales.

### C11. Verified dealers

`Supporting` · rank 11 of 11 · score **2.55** · evidence **M** · from the first sheets

*Scores: decision 2, goal link 3, diagnostic 2, early warning 2, measurable 5.*

**Definition**
- **What it is:** The size of the buying side.
- **Formula:** Count of dealers approved to bid.
- **Data needed:** `dealer_id`, `verified_date`, `status`.
- **Evidence (M):** Motorway states 7,500 to 8,000+ verified dealers (figures differ by page). The climb on the sample chart is invented.

**Why it ranks here:** It is a vanity figure on its own, because verified dealers who do not bid add nothing. It becomes useful beside active dealers.

**Insights it can give**
- Rising while active is flat: an activation problem.
- Flat: recruitment has stalled.
- Falling: removals or churn.
- **Read it with:** Active dealers.
- **Decision it supports:** Recruitment targets.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V3 Line chart against last year or last period. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A running total is a line.
- **Build notes:** Quarterly line.

| Platform | Main (V3) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + comparison range | Scorecard with comparison |
| Streamlit | `st.line_chart` (native) | `st.metric` (native) |
| Python | `px.line` with several y columns | `go.Indicator` or a printed number |
| SQL returns | one row per period, one column per series | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT month, SUM(new_dealers) OVER (ORDER BY month) AS verified_dealers
FROM (SELECT DATE_TRUNC('month', verified_date) AS month, COUNT(*) AS new_dealers FROM dealers GROUP BY 1) t;
```

**Drill:** Light. By region.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| History | Scorecard | Today's count | Growth |

**Trap:** Deactivated dealers must be removed from the running count.

---

## PRODUCT

*Is the journey easy to finish, and is the car information accurate?*

**Suggested page layout**
- **Top row, single values:** Valuation accuracy, Verification pass rate and time, Repeat seller rate, App rating and stability. Each with its change against the last period.
- **Middle, the Headline charts:** Funnel completion by step (funnel chart); Retention cohorts (dealers) (heatmap (cohort grid)); Valuation accuracy (histogram with median and threshold lines).
- **Lower, the Core diagnostics:** Verification pass rate and time, Condition grade accuracy, Repeat seller rate, App rating and stability.
- **Second page or drill through:** Page speed (Core Web Vitals), Dealer engagement curve (power users), Paid listing uptake, Service-history extraction accuracy.

### P1. Funnel completion by step

`Headline` · rank 1 of 11 · score **4.85** · evidence **I** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 5, early warning 4, measurable 5.*

**Definition**
- **What it is:** Where sellers drop out.
- **Formula:** Sellers reaching a step ÷ sellers at the step before (valuation, profile and photos, daily sale, offer accepted).
- **Data needed:** An event table: `user_id`, `step`, `timestamp`, plus `device` and `app_version`.
- **Evidence (I):** Follows Motorway's published how-it-works journey.

**Why it ranks here:** It is the product team's map of lost revenue. It gives a specific step to fix, and it can be cut by device, version and channel.

**Insights it can give**
- One step with the largest drop: fix that step.
- A drop in one app version or device: a bug, not design.
- A drop at 'accept offer': a price expectation gap, not usability.
- **Read it with:** Valuation accuracy and app stability.
- **Decision it supports:** Roadmap priority.

**How to show it**
- **Format:** Chart.
- **Main visual:** V11 Funnel chart. **Companion:** V4 Column chart.
- **Why:** Steps in order, with each drop visible, is exactly what a funnel is for.
- **Build notes:** Count distinct users per step in journey order. Show both the share of the first step and the share of the previous step.

| Platform | Main (V11) | Companion (V4) |
|---|---|---|
| Looker Studio | Funnel chart | Column chart |
| Streamlit | `st.plotly_chart(px.funnel)` | `st.bar_chart` (native) |
| Python | `px.funnel` or `go.Funnel` | `px.bar` |
| SQL returns | one row per step: order, name, distinct users | one row per category |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT step_order, step, COUNT(DISTINCT user_id) AS users
FROM seller_events GROUP BY step_order, step ORDER BY step_order;
```

**Drill:** Drill down by device, app version and channel. A drop often lives in one app version.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Step events | Start and finish counts | End-to-end rate | Where the loss is |
| Device or version | Overall funnel | The step | Whether it is a bug |

**Trap:** Count people who completed the earlier step, not anyone who appears at a later one.

### P2. Retention cohorts (dealers)

`Headline` · rank 2 of 11 · score **4.60** · evidence **S** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 5, early warning 3, measurable 4.*

**Definition**
- **What it is:** Whether dealers come back.
- **Formula:** Of dealers first active in a month, the share active again in each later month, by starting month.
- **Data needed:** `dealer_id`, `first_active_month`, `active_month`.
- **Evidence (S):** a16z user retention and core-action retention cohorts.

**Why it ranks here:** Demand depends on dealers staying. Cohorts show whether newer dealers are better or worse than older ones, which no average can.

**Insights it can give**
- Newer cohorts retain worse: recent recruits are weaker, or onboarding slipped.
- All cohorts dip in the same calendar month: a market or platform event.
- Retention flattens after month 3: those who stay, stay.
- **Read it with:** Active dealers and concentration.
- **Decision it supports:** Onboarding and account management.

**How to show it**
- **Format:** Chart.
- **Main visual:** V13 Heatmap (cohort grid). **Companion:** V2 Line chart with a target line or band.
- **Why:** A cohort grid gives start month against months since start, so one picture shows every cohort at once.
- **Build notes:** Rows are starting months, columns months since start. Read from M1 onward, since M0 is always 100%.

| Platform | Main (V13) | Companion (V2) |
|---|---|---|
| Looker Studio | Pivot table with heatmap | Time series + reference line |
| Streamlit | `st.dataframe` with a Styler gradient, or `px.imshow` | `st.plotly_chart` (Plotly, for the target line) |
| Python | `px.imshow` or seaborn `heatmap` | `px.line` + `add_hline` |
| SQL returns | one row per cohort per period | one row per period: numerator, denominator, rate |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
WITH first AS (SELECT dealer_id, DATE_TRUNC('month', MIN(purchase_date)) AS cohort FROM purchases GROUP BY 1),
     act AS (SELECT DISTINCT dealer_id, DATE_TRUNC('month', purchase_date) AS m FROM purchases)
SELECT f.cohort,
       (DATE_PART('year', a.m) - DATE_PART('year', f.cohort)) * 12 + DATE_PART('month', a.m) - DATE_PART('month', f.cohort) AS months_since,
       COUNT(DISTINCT a.dealer_id) AS dealers
FROM first f JOIN act a USING (dealer_id) GROUP BY 1, 2;   -- divide by the month-0 count of the same cohort
```

**Drill:** No drill down. A second grid by channel or region is clearer.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Six months of data | Month-1 and month-2 retention by cohort, as lines | Early retention | Long-run stickiness |
| Cohort dates | Share of last month's buyers who bought again | A simple repeat rate | Cohort comparison |

**Trap:** The triangle shape is expected. Compare columns down the rows.

### P3. Valuation accuracy

`Headline` · rank 3 of 11 · score **4.40** · evidence **I** · from the first sheets

*Scores: decision 5, goal link 5, diagnostic 4, early warning 3, measurable 4.*

**Definition**
- **What it is:** Whether the first estimate holds.
- **Formula:** (Final sale price − first estimate) ÷ first estimate.
- **Data needed:** `first_estimate` and `final_sale_price` per car.
- **Evidence (I):** Seller reviews mention valuations that change. Not published by Motorway.

**Why it ranks here:** A biased estimate makes sellers reject offers or feel misled, and it affects conversion and trust together.

**Insights it can give**
- Median below zero: estimates run high, so sellers are disappointed.
- Wide spread in older cars: the model lacks data there.
- A shift after a model release: the release changed the bias.
- **Read it with:** The funnel drop at 'accept offer'.
- **Decision it supports:** Valuation model priorities.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V12 Histogram with median and threshold lines. **Companion:** V1 Scorecard: one number with its change.
- **Why:** The shape of the error matters: a spread and a bias. A distribution shows both.
- **Build notes:** Bins of 2 percentage points, zero line, median line.

| Platform | Main (V12) | Companion (V1) |
|---|---|---|
| Looker Studio | Calculated bin + column chart, or Boxplot | Scorecard with comparison |
| Streamlit | `numpy.histogram` + `st.bar_chart`, or `px.histogram` | `st.metric` (native) |
| Python | `px.histogram` + `add_vline(median)` | `go.Indicator` or a printed number |
| SQL returns | one row per bin: bin start, count | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT FLOOR(100.0 * (final_price - first_estimate) / first_estimate / 2) * 2 AS error_bin_pct, COUNT(*) AS cars
FROM valuations_with_outcome GROUP BY 1 ORDER BY 1;
```

**Drill:** No drill down on the histogram. Second view by make and age band.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Final prices | Share of estimates revised before the sale | Instability of the estimate | Size and direction of the error |
| Enough cars per segment | Overall median error | Bias | Where it is worst |

**Trap:** A bias (median below zero) matters more than a wide spread.

### P4. Verification pass rate and time

`Core` · rank 4 of 11 · score **4.00** · evidence **I** · from the first sheets

*Scores: decision 4, goal link 4, diagnostic 4, early warning 4, measurable 4.*

**Definition**
- **What it is:** Ease of the identity check.
- **Formula:** Sellers passing ID and document checks first time ÷ sellers checked, and the minutes taken.
- **Data needed:** `check_type`, `result`, `started_at`, `finished_at`.
- **Evidence (I):** AI seller verification with face capture launched in 2026. The KPI is inferred.

**Why it ranks here:** A hard check loses honest sellers. A fast one that misses fraud loses dealers. This is where product friction meets risk.

**Insights it can give**
- One document type failing: guidance or capture for that document.
- Pass rate fine but time long: friction.
- Pass rate falling after stricter rules: the trade-off with fraud.
- **Read it with:** Seller verification coverage and problem vehicles stopped.
- **Decision it supports:** Fixes to the capture flow.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V4 Column chart. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Pass rate by check type is a category comparison, and the median time is a single number.
- **Build notes:** Columns by document type, coloured by status. Scorecard: median time.

| Platform | Main (V4) | Companion (V1) |
|---|---|---|
| Looker Studio | Column chart | Scorecard with comparison |
| Streamlit | `st.bar_chart` (native) | `st.metric` (native) |
| Python | `px.bar` | `go.Indicator` or a printed number |
| SQL returns | one row per category | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT check_type, AVG(CASE WHEN first_attempt_result = 'pass' THEN 1.0 ELSE 0 END) AS first_time_pass,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM (finished_at - started_at))) AS median_seconds
FROM verification_checks GROUP BY check_type;
```

**Drill:** Drill down check type, then failure reason.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Timestamps | Pass rates only | Where people fail | Effort |
| First-attempt flag | Eventual pass rate | Completion | Friction on the way |

**Trap:** A high pass rate with a slow median is still a poor experience. Show both.

### P5. Condition grade accuracy

`Core` · rank 5 of 11 · score **4.00** · evidence **I** · from the first sheets

*Scores: decision 4, goal link 5, diagnostic 4, early warning 3, measurable 3.*

**Definition**
- **What it is:** Trust in the car's description.
- **Formula:** Collections where the car matched its grade (1 to 5) ÷ all collections.
- **Data needed:** `listed_grade` and `collection_check_result` (ideally the grade found).
- **Evidence (I):** Motorway rolled out a 1 to 5 condition grading system. The accuracy KPI is inferred.

**Why it ranks here:** Grade accuracy decides whether dealers trust listings, which drives bids and prices.

**Insights it can give**
- Errors mostly one grade too high: sellers overrate.
- Worst at low grades: damage is hard to self-report.
- Improves after a guided photo step: the step works.
- **Read it with:** Price changed at collection and claims.
- **Decision it supports:** Grading guidance and photo capture.

**How to show it**
- **Format:** Chart.
- **Main visual:** V4 Column chart. **Companion:** V13 Heatmap (cohort grid).
- **Why:** Accuracy by grade is a comparison. A grid of listed against found grade shows the direction of the error.
- **Build notes:** Columns coloured by status. Grid: rows are the listed grade, columns the grade found.

| Platform | Main (V4) | Companion (V13) |
|---|---|---|
| Looker Studio | Column chart | Pivot table with heatmap |
| Streamlit | `st.bar_chart` (native) | `st.dataframe` with a Styler gradient, or `px.imshow` |
| Python | `px.bar` | `px.imshow` or seaborn `heatmap` |
| SQL returns | one row per category | one row per cohort per period |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT listed_grade, found_grade, COUNT(*) AS cars FROM collections GROUP BY 1, 2;
```

**Drill:** Drill down grade, then type of mismatch (panel, tyres, mileage).

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Grade found | Match rate by grade | Where accuracy is low | The direction of the error |
| Enough cars per grade | Overall match rate | The headline | Grade differences |

**Trap:** Low grades often have fewer cars. Show counts so a small group is not over-read.

### P6. Repeat seller rate

`Core` · rank 6 of 11 · score **3.75** · evidence **S** · added in round 2

*Scores: decision 4, goal link 4, diagnostic 4, early warning 3, measurable 3.*

**Definition**
- **What it is:** Whether sellers come back when they sell their next car.
- **Formula:** Of sellers whose first completed sale was in a quarter, the share who completed another within 12 months.
- **Data needed:** `seller_id` and `completed_date` for each completed sale.
- **Evidence (S):** a16z core-action retention: retention measured by the core action (for Motorway, a completed sale) rather than by logins.

**Why it ranks here:** It captures long-run value. Car sellers return rarely, so low values are normal and the trend matters more than the level.

**Insights it can give**
- Rising in recent cohorts: the experience is improving.
- Higher from referral channels: those sellers are worth more.
- Flat and low: normal for cars. Focus on referral instead.
- **Read it with:** Seller satisfaction.
- **Decision it supports:** Lifecycle marketing.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A rate by first-sale cohort as a line shows whether newer cohorts return more.
- **Build notes:** Quarterly cohorts, 12-month window. Use 24 months if 12 is too sparse.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
WITH first_sale AS (SELECT seller_id, MIN(completed_date) AS first_date FROM completed_sales GROUP BY 1)
SELECT DATE_TRUNC('quarter', f.first_date) AS cohort, COUNT(DISTINCT f.seller_id) AS sellers,
       COUNT(DISTINCT CASE WHEN s.completed_date > f.first_date
                             AND s.completed_date <= f.first_date + INTERVAL '12 months' THEN f.seller_id END) AS sold_again
FROM first_sale f JOIN completed_sales s USING (seller_id) GROUP BY 1;
```

**Drill:** Drill down by acquisition channel.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| 12 months of history | 90-day repeat, or a referral count | An early loyalty signal | True repeat behaviour |
| Stable seller IDs | Share of sales from a returning email or phone | A rough repeat share | Accuracy |

**Trap:** Dealer-sellers and private sellers behave differently. Separate them if the data allows.

### P7. App rating and stability

`Core` · rank 7 of 11 · score **3.50** · evidence **I** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 3, early warning 5, measurable 5.*

**Definition**
- **What it is:** Reliability of the app.
- **Formula:** Average app store rating, and crash-free sessions ÷ all sessions.
- **Data needed:** Session logs with a crash flag, `app_version`, and store ratings.
- **Evidence (I):** Motorway has iOS and Android seller apps. No figure is used here.

**Why it ranks here:** Crash-free sessions react within hours of a release, so this is the fastest early warning in product.

**Insights it can give**
- A dip starting on a release date: that release.
- A dip in one operating system: platform-specific.
- Rating falling with stable crashes: a usability complaint.
- **Read it with:** Funnel by app version and support contacts.
- **Decision it supports:** Release rollback or hotfix.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** A rate against a threshold, with release markers, shows the cause as well as the dip.
- **Build notes:** Weekly line, 99% reference line, release dates marked.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', session_start) AS week, app_version,
       100.0 * AVG(CASE WHEN crashed THEN 0.0 ELSE 1.0 END) AS crash_free_pct, COUNT(*) AS sessions
FROM app_sessions GROUP BY 1, 2;
```

**Drill:** Drill down app version and operating system.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Release dates | Crash-free rate by version | Which version is bad | Timing |
| Session logs | Store rating trend | Quality as users see it | Speed of detection |

**Trap:** A dip that starts on a release date points to the release. Check the version split before saying so.

### P8. Page speed (Core Web Vitals)

`Supporting` · rank 8 of 11 · score **3.35** · evidence **S** · added in round 2

*Scores: decision 3, goal link 3, diagnostic 3, early warning 4, measurable 5.*

**Definition**
- **What it is:** How fast and stable the web pages feel to real visitors.
- **Formula:** At the 75th percentile of page loads, split by mobile and desktop: LCP (loading), INP (responsiveness), CLS (layout shift).
- **Data needed:** Real-user performance data (a field-data source) with device and page.
- **Evidence (S):** Google's web.dev: good means LCP 2.5 seconds or less, INP 200 milliseconds or less, CLS 0.1 or less, at the 75th percentile.

**Why it ranks here:** Slow pages lose sellers before the funnel records them. It ranks mid-table because it is a hygiene factor with clear thresholds.

**Insights it can give**
- Mobile failing while desktop passes: page weight on mobile.
- LCP worse on one page: that page's images or scripts.
- Worse after a release: a regression.
- **Read it with:** The funnel entry step and visits.
- **Decision it supports:** Performance work.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V16 Bullet chart (value against a target and bands). **Companion:** V2 Line chart with a target line or band.
- **Why:** Three values each against a fixed threshold: three small bullet charts, not a full chart.
- **Build notes:** One bullet per metric against its threshold. Trend line for LCP below.

| Platform | Main (V16) | Companion (V2) |
|---|---|---|
| Looker Studio | Bullet chart | Time series + reference line |
| Streamlit | `st.plotly_chart(go.Indicator)` with a bullet gauge | `st.plotly_chart` (Plotly, for the target line) |
| Python | `go.Indicator(mode='number+gauge')` | `px.line` + `add_hline` |
| SQL returns | one row: value, target, band limits | one row per period: numerator, denominator, rate |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | notebook cell (test inline first), or Streamlit in a browser |

```sql
SELECT DATE_TRUNC('week', measured_at) AS week, device,
       PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY lcp_ms) AS lcp_p75,
       PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY inp_ms) AS inp_p75,
       PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY cls)    AS cls_p75
FROM page_performance GROUP BY 1, 2;
```

**Drill:** Drill down by page and device.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Field data | A lab test score, labelled | Technical health | Real visitors' experience |
| Device split | Overall 75th percentile | The headline | Where it is slow |

**Trap:** Averages hide the slow tail. Use the 75th percentile.

### P9. Dealer engagement curve (power users)

`Supporting` · rank 9 of 11 · score **3.25** · evidence **S** · added in round 2

*Scores: decision 3, goal link 4, diagnostic 3, early warning 3, measurable 3.*

**Definition**
- **What it is:** How engaged dealers are, and whether the most engaged group is growing.
- **Formula:** For each dealer, the number of days active in the last 30. The curve is how many dealers fall at each count.
- **Data needed:** `dealer_id` and `activity_date`.
- **Evidence (S):** a16z power user curves (L30 or L7 histograms).

**Why it ranks here:** It shows whether usage is concentrated in a few dealers or spread. A shift to the right is a sign of habit.

**Insights it can give**
- Curve shifting right: a habit is forming.
- A spike at 1 day: many dealers try once.
- Two humps: two dealer types.
- **Read it with:** Retention cohorts.
- **Decision it supports:** Features for heavy and light users.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V12 Histogram with median and threshold lines. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Distribution is the point: the shape shows a habit.
- **Build notes:** Columns for 0 to 30 active days, one colour, and a scorecard for the share active on 8 or more days.

| Platform | Main (V12) | Companion (V1) |
|---|---|---|
| Looker Studio | Calculated bin + column chart, or Boxplot | Scorecard with comparison |
| Streamlit | `numpy.histogram` + `st.bar_chart`, or `px.histogram` | `st.metric` (native) |
| Python | `px.histogram` + `add_vline(median)` | `go.Indicator` or a printed number |
| SQL returns | one row per bin: bin start, count | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT active_days, COUNT(*) AS dealers FROM (
  SELECT dealer_id, COUNT(DISTINCT activity_date) AS active_days
  FROM dealer_activity WHERE activity_date >= CURRENT_DATE - 30 GROUP BY dealer_id) t
GROUP BY active_days ORDER BY active_days;
```

**Drill:** No drill down. Compare cohorts on a second chart.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| Daily activity | Sessions or bids per dealer in 30 days | Intensity | Regularity |
| History | Current distribution | Today's shape | Whether it is improving |

**Trap:** Weekends. Dealers may buy on weekdays only.

### P10. Paid listing uptake

`Supporting` · rank 10 of 11 · score **3.10** · evidence **I** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 3, early warning 3, measurable 4.*

**Definition**
- **What it is:** Demand for a paid feature.
- **Formula:** Sellers buying the paid badge ÷ sellers offered it. Compare the sell rate with the badge and without.
- **Data needed:** `offered_badge`, `bought_badge`, and the sale outcome, ideally with a control group.
- **Evidence (I):** Motorway tested a £29.99 paid listing badge. The KPI is inferred.

**Why it ranks here:** A test read-out more than an ongoing KPI. It matters until the decision is made.

**Insights it can give**
- Uptake levelling off: natural demand reached.
- Sell rate higher with the badge in a controlled test: the badge works.
- Uptake in dearer cars only: segment the offer.
- **Read it with:** Sell-through.
- **Decision it supports:** Launch, reprice or drop the feature.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Uptake over time as a line, and two scorecards for the sell rates.
- **Build notes:** Weekly uptake line. Two cards: sell rate with and without. Test the difference in Python before calling it real.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT DATE_TRUNC('week', offered_at) AS week, COUNT(*) AS offered, SUM(bought_badge::int) AS bought,
       AVG(CASE WHEN bought_badge THEN sold::int END) AS sell_rate_with,
       AVG(CASE WHEN NOT bought_badge THEN sold::int END) AS sell_rate_without
FROM badge_offers GROUP BY 1;
```

**Drill:** No drill down. It is a test read-out.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| A control group | Uptake only | Willingness to pay | Whether the feature works |
| Enough sales | A wider period or pooled weeks | A more stable rate | Timeliness |

**Trap:** Sellers who pay may already be more likely to sell. Without randomisation the gap is not proof.

### P11. Service-history extraction accuracy

`Supporting` · rank 11 of 11 · score **3.00** · evidence **M** · from the first sheets

*Scores: decision 3, goal link 3, diagnostic 3, early warning 3, measurable 3.*

**Definition**
- **What it is:** Quality of document reading.
- **Formula:** Fields read correctly from service documents ÷ fields checked.
- **Data needed:** A sample audit: for each field, the machine value and the human-checked value.
- **Evidence (M):** Motorway's own blog claims 94.7%.

**Why it ranks here:** An internal quality measure for one feature. It matters for trust but affects a narrower part of the journey.

**Insights it can give**
- Accuracy rising by release: the model is improving.
- One document type lagging: train on it.
- Accuracy high but dealers still doubt: the display, not the extraction.
- **Read it with:** Condition grade accuracy.
- **Decision it supports:** Model priorities.

**How to show it**
- **Format:** Single value + chart.
- **Main visual:** V2 Line chart with a target line or band. **Companion:** V1 Scorecard: one number with its change.
- **Why:** Accuracy by model release as a line shows whether releases improve it.
- **Build notes:** Line by release, with labels and the audit sample size.

| Platform | Main (V2) | Companion (V1) |
|---|---|---|
| Looker Studio | Time series + reference line | Scorecard with comparison |
| Streamlit | `st.plotly_chart` (Plotly, for the target line) | `st.metric` (native) |
| Python | `px.line` + `add_hline` | `go.Indicator` or a printed number |
| SQL returns | one row per period: numerator, denominator, rate | one row: value and prior value |
| Antigravity IDE | notebook cell (test inline first), or Streamlit in a browser | printed value or DataFrame in a cell |

```sql
SELECT model_version, AVG(CASE WHEN machine_value = human_value THEN 1.0 ELSE 0 END) AS field_accuracy, COUNT(*) AS fields_audited
FROM extraction_audit GROUP BY model_version;
```

**Drill:** Drill down by document type and field.

**If the data is thin**

| If you are missing | Use instead | What that still tells you | What you lose |
|---|---|---|---|
| An audit | Share of extracted fields edited by a person | A proxy for errors | True accuracy, since unedited errors are missed |
| Sample size | Accuracy with a margin of error | An honest range | Precision |

**Trap:** Accuracy from a small audit has a wide margin. Show the sample size.

---

# Appendix A: what each platform can and cannot draw

**Looker Studio.** Native chart types in Google's documentation: scorecard, table (with bars or heatmap), pivot table, time series, bar and column (stacked and 100% stacked), pie and donut, combo, geo, Google Maps, area, scatter and bubble, bullet, gauge, tree map, Sankey, waterfall, boxplot, candlestick, timeline, funnel, and community visualisations. There is no native histogram: bin the value in a calculated field and use a column chart. Reference lines and bands go on line, bar, area, combo and scatter charts (Style tab). A heatmap is a style of table and pivot table. Menus change, so confirm in your own account.

**Streamlit.** Native chart elements: `st.line_chart`, `st.area_chart`, `st.bar_chart`, `st.scatter_chart`, `st.map`. Third-party renderers include `st.pyplot`, `st.altair_chart`, `st.vega_lite_chart`, `st.plotly_chart` and `st.pydeck_chart`. For a single value use `st.metric`: it takes a delta (`delta_color='inverse'` when down is good), a border, and an optional sparkline through `chart_data`. Native charts do not draw target lines, two axes, waterfalls, funnels, histograms or heatmaps, so use Plotly for those. These details are from the documentation for version 1.65.0. Check yours with `streamlit --version`.

**Python.** Plotly covers every visual in Part 3 and works in notebooks and Streamlit. Matplotlib and seaborn give static images. Altair is a good fit inside Streamlit.

**SQL.** SQL does not draw. Its job is to return the right shape, shown as "SQL returns" on each card. Snippets use common SQL (Postgres or BigQuery style). In SQLite, replace `DATE_TRUNC` with `strftime`. Table and column names are generic assumptions, not Motorway's schema.

**Antigravity IDE.** Antigravity is built on VS Code, and most VS Code extensions are reported to work. I could not verify from any source whether notebooks show charts inline there, and one user reported notebook problems. Test one cell before you rely on it. Fallbacks, in order: run Plotly in a notebook or a `# %%` cell; save with `fig.write_html("chart.html")` or `plt.savefig("chart.png")` and open the file; run `streamlit run app.py` and open the local address in a browser. The last is the most dependable.

# Appendix B: drill down, drill through, cross-filter

| Term | Meaning |
|---|---|
| **Drill down** | Click a bar or point to go one level deeper in the same chart (year to quarter to month). |
| **Drill through** | Click to open a separate detail page or table for that item (a dealer, a cost line). |
| **Cross-filter** | Click one chart and the others on the page filter to match. |

Give drill down to totals and rates that can be sliced by time and an attribute. Give none to a single headline number, a distribution, a survey, or a slice too small to trust. Use drill through when the next step is a list of records to act on.

# Appendix C: a sentence pattern for explaining any KPI

"[KPI] tells us [what], calculated as [formula]. I would show it as a [visual] against [comparison]. If it moved, I would first check [the line from 'Insights it can give'], and I would drill into [dimension]."

Example: "Sell-through tells us how often supply meets demand, calculated as cars sold divided by cars entered. I would show it as a weekly line against a target. If it fell, I would first check bids per car, because a fall with steady bids points to supply mix and not demand, and then I would drill into region, make and price band."

# Appendix D: sources and caveats

Fetched and read:
- Looker Studio chart types (Google Cloud documentation): https://docs.cloud.google.com/looker/docs/studio/types-of-charts
- Streamlit `st.metric` and chart elements: https://docs.streamlit.io/develop/api-reference/data/st.metric and https://docs.streamlit.io/develop/api-reference/charts
- Plotly funnel and waterfall charts: https://plotly.com/python/funnel-charts/ and https://plotly.com/python/waterfall-charts/
- a16z, 13 Metrics for Marketplace Companies: https://a16z.com/13-metrics-for-marketplace-companies/
- Google web.dev, Core Web Vitals: https://web.dev/articles/vitals

Read through search summaries only (primary pages not opened):
- CarGurus 10-K filings (paying dealers, quarterly average revenue per subscribing dealer): https://www.sec.gov/Archives/edgar/data/1494259/000095017024020157/carg-20231231.htm
- Carvana 10-K filings (retail units sold, total gross profit per unit; the definition I saw is from the FY2022 filing): https://www.sec.gov/Archives/edgar/data/1690820/000169082025000074/cvna-20241231.htm
- Auto Trader full-year results: https://data.fca.org.uk/artefacts/NSM/RNS/5672441.html
- Sharetribe on liquidity: https://www.sharetribe.com/marketplace-glossary/liquidity/
- Inovia on CAC payback: https://www.inovia.vc/?p=7848
- Bullet graph as a gauge replacement (Stephen Few's design, via secondary summaries): https://www.tableau.com/chart/what-is-bullet-graph
- The Motorway figures are sourced in `KPI_REFERENCE.md`.

Not found, so not claimed:
- OPENLANE's formula for its conversion rate.
- Any KPI list published by Motorway.
- A reliable benchmark for support contact rate. Sources conflict.
- Whether Antigravity shows notebook charts inline.

The "Insights it can give" lines are reasoning about how a marketplace works. They are patterns to test against the data, not findings.
