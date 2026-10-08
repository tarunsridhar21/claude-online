# From schema to KPIs to story: the method

This is the procedure to run (playbook v2: 59 KPIs, F1–F13, M1–M12, O1–O11, C1–C12, P1–P11) when Tarun sends a schema screenshot, column names or a data brief. It sits on top of `KPI_PLAYBOOK.md` (the source of the KPI IDs F1–P11 and visuals V1–V17) and `00_context.md` (the role and interviewer).

The live task is 30 minutes. Everything here is built for speed: read the schema, then return a ranked list in one pass.

---

## Working from column names only (standing rule)

Tarun will send **column names and maybe data types, never the rows**. So:

- I can't see grain, nulls, value sets, date ranges, duplicates or test rows. I **infer** them from names and types, label every inference as an **assumption**, and never state a data fact as known.
- Ask for the cheap facts in one batch, as queries he can run in 2 minutes:
  - Grain: `SELECT COUNT(*), COUNT(DISTINCT <id_col>) FROM t;` (equal = one row per id)
  - Status/outcome values: `SELECT <status_col>, COUNT(*) FROM t GROUP BY 1 ORDER BY 2 DESC;`
  - Date range: `SELECT MIN(<date_col>), MAX(<date_col>) FROM t;`
  - Nulls: `SELECT COUNT(*) - COUNT(<col>) AS nulls FROM t;`
  - Join fan-out: row counts before and after the join.
- Rank KPIs by what the **column names make possible**, and mark each as *confirmed by schema* or *depends on assumption X*.
- SQL I write uses his column names exactly. Where a value is a guess (e.g. `status = 'sold'`), I say so and tell him to check it with the status query.
- I can't compute results. He runs the queries and sends me the numbers (pasted or screenshot), and I help interpret them and build the story from those. I never invent figures. Any example numbers I use are clearly labelled illustrative.
- Types help: a `timestamp` pair gives durations and funnels, `numeric` gives sums and averages, `boolean` is a flag/rate, a `string` with few values is a dimension, and an ID is a join key.

## Step 0: Read the brief before the columns

The brief decides the ranking more than the columns do. Before anything else, pin down:

1. **The question.** "How is the business doing?" (broad, so lead with headline KPIs) or "Why did X drop?" (narrow, so lead with diagnostic KPIs).
2. **The audience.** Exec (few numbers, a verdict) or manager (drill-downs, lists to act on). Shuma said both matter.
3. **The decision.** What someone would do differently depending on the answer.

If the brief is vague, suggest a question to ask Shuma (see Step 7).

## Step 1: Profile the data (2–3 minutes, out loud)

For each table, state:

| Check | Why |
|---|---|
| **Grain**: what one row is | Playbook rule 1. Decides every COUNT and SUM. |
| **Keys and joins**: which IDs link tables, one-to-many or many-to-many | Join fan-out is the classic double-count. Aggregate before joining (rule 4). |
| **Date range and date columns** | Which date to group by (accepted vs completed changes the answer). Is the latest period complete? |
| **Status / outcome fields and their values** | Sold vs unsold, completed vs fallen through. Needed for every rate. |
| **Nulls, test rows, placeholder values** (price = 1, test sellers) | Remove before counting. Say you did. |
| **Dimensions available** (region, make, channel, fuel, price band) | These are the drill-downs, not KPIs on their own. |

Say these out loud. This is the "human in the loop" part of the job description.

## Step 2: Map columns to KPIs (lookup index)

Scan the schema for these **signal columns**. Each one unlocks the KPIs on its row. "+" means it also needs the other column.

| If you see… | You can build | Notes |
|---|---|---|
| `sale_price` / `sold_price` + sale date + status | **F2** GMV, **O6** completed sales, **F8** average sale price (mean + median) | Completed only. Watch for placeholder prices. |
| fee / revenue / `amount` (+ `fee_type`) | **F4** revenue; + sale price → **F6** take rate; + count of sales → **F12** revenue per car | |
| + `dealer_id` on fees | **F7** revenue per active dealer; with 13+ months → **F5** dealer net revenue retention | Show the median beside the mean. NRR: exclude new dealers. |
| Any **variable cost** (marketing spend, `transport_cost`, support cost) | **F1** contribution per car (with revenue) | The #1 Finance KPI. Write down the allocation rule. |
| Company P&L lines (operating result, cost lines, cash) | **F9** adjusted EBITDA, **F10** opex share of revenue, **F11** pre-tax loss, **F3** burn and runway | Management-accounts data, rare in a live task. |
| marketing `spend` by `channel` | **M8** cost per valuation; + sales by origin channel → **M2** cost per car sold; + contribution → **M4** CAC payback | Use mature cohorts for cost per sale. |
| `valuation_id` + `created_at` (+ `channel`) | **M3** valuations started; + channel → **M7** organic share; + revenue of resulting sales → **M6** revenue per valuation | Remove tests, normalise channel names. M6 vs M8 = margin per lead. |
| Step timestamps / flags (`profile_done_at`, `listed_at`, `accepted_at`, `completed_at`) | **P1** funnel by step, **M1** valuation-to-sale, **O5** time to sell, **O1** completion rate | P1 and M1 overlap, so present them as one funnel. |
| `listing_id` + outcome (sold/unsold) + sale date | **C1** sell-through, **C10** cars in daily sale | Unsold rows are essential. Without them there is no rate. |
| `first_listed_at` + `sold_at` (or `attempt_no`) | **C4** cumulative sell-through curve | Cut cohorts at their maturity. |
| **Bids table** (`listing_id`, `dealer_id`, `bid_time`, `bid_amount`) | **C3** bids per car, **C5** time to first bid, **C7** bidders per car, **C2** active dealers | Left join from listings so zero-bid cars stay. |
| `dealer_id` on purchases with dates | **C2** active dealers, **C8** concentration and retention, **P2** retention cohorts, **P9** engagement curve | |
| + dealer contribution, churn and acquisition spend | **C9** dealer LTV and LTV:CAC | Stacks three estimates. State the churn assumption. |
| `verified_date` / dealer status | **C12** verified dealers (only useful beside C2) | |
| `guide_price` / market value | **C6** price vs guide, **M10** seller price advantage | No guide → proxy vs median of similar cars, labelled. |
| First estimate / `valuation_amount` vs final price | **P3** valuation accuracy | Bias (median ≠ 0) matters more than spread. |
| `price_at_listing` vs `price_at_collection` (+ reason) | **O3** price changed at collection | |
| Claims table (`dealer_id`) | **O2** claims rate by dealer; + `cost`, `opened_at`, `closed_at` → **O9** claim cost and resolution time | Minimum purchases per dealer. Report open claims beside O9. |
| `collected_at` + `paid_at` | **O7** days to seller payment | Working days. |
| Slot times + actual collection (+ transport cost) | **O8** on-time collection and cost per move | |
| Support tickets (+ reason) | **O4** contacts per 100 sales | |
| Survey score / reviews | **M5** NPS/CSAT, **M9** review score | |
| `payment_method` | **F13** Pay share of sales, **C11** Pay adoption by dealer | |
| `seller_id` with repeat sales | **P6** repeat seller rate | |
| `listed_grade` vs `found_grade` | **P5** condition grade accuracy | |
| Verification checks / fraud `flag_type` | **P4** verification pass rate, **O11** verification coverage, **O10** problem vehicles stopped | |
| Sessions, crashes, web vitals, visits | **P7**, **P8**, **M11** | |
| Brand survey | **M12** brand awareness | |
| `region`, `make`, `model`, `fuel_type`, `age`, `mileage`, `price` bands | **Drill-down dimensions** for everything above | A sell-through fall usually hides in one slice. |

**If the data is not marketplace-shaped** (e.g. SaaS, retail, logistics, generic sales or marketing data): use **playbook §1.4**, which translates general metrics (CAC, LTV, ARPU, AOV, churn, NRR, DAU/MAU, fill rate, on-time delivery, return rate…) to the playbook's KPIs. Use their formulas, visuals and rules, but name them in the dataset's own language. Anything not in §1.4: define it fresh and score it with the five criteria in Step 3.

**Use each card's extras:**
- **"Who uses it"** fills the stakeholder column (Marketing, Finance, Product, Commercial, Operations, Exec), which maps directly to the teams in the job description.
- **"In a sentence"** is a ready template for saying the KPI out loud. Swap in his real numbers. The card's numbers are samples: never quote them as Motorway figures.
- **Evidence tag G** = general business metric adapted to a marketplace. Like I, never say "Motorway tracks this".

## Step 3: Rank them

Start from the playbook score (out of 5), then adjust for *this* data and *this* brief. Show the adjustment so the ranking is defensible.

| Criterion | Weight |
|---|---|
| Decision value: someone acts differently based on it | 30% |
| Link to the goal: profit and marketplace liquidity | 25% |
| Diagnostic power: drilling down explains it | 20% |
| Early warning: moves before revenue | 15% |
| Measurable: with **this** dataset | 10% |

**Adjustments:**
- **+0.25 to +0.5** if it directly answers the brief.
- **−0.5** if it needs a proxy (say what the proxy is and label it on the chart).
- **Drop it** if a required field is missing. List it under "Can't build: would need X". That is a good talking point, not a weakness.
- **Merge duplicates** (P1 + M1 funnel; C2 + C12 active vs verified; M6 beside M8 per channel) instead of listing both.
- Ties: early warning, then decision value, then goal link.

**Tiers for a 30-minute task:**
- **Build now (3–5):** the top of the list, and what the presentation is built on.
- **If time:** the next 3–4, usually diagnostics for the headline.
- **Mention only:** the rest, plus what's not buildable.

## Step 4: Pick the visual, split exec vs manager

Use the KPI card's main and companion visual from the playbook. Choose by question:

| Question | Visual |
|---|---|
| One number vs target or last period | V1 scorecard, V16 bullet |
| Rate over time with a target | V2 line + target |
| Total over time vs last year | V3 line vs LY |
| Where do people drop out | V11 funnel |
| Best/worst among many (dealers, channels, regions) | V8 ranked bar (show denominators) |
| Spread of time/price/error | V12 histogram + median (P90 too) |
| How revenue becomes profit per car | V10 waterfall |
| Volume and intensity together | V9 combo |
| Cohorts | V13 heatmap or V15 line per cohort |
| Concentration | V14 Pareto |
| Exact list someone will act on | V17 table with bars |

**Exec page (CEO):** 3–4 scorecards with change vs last period + one trend chart + one sentence verdict. No drill-downs.
**Manager page:** the diagnostic charts: funnel by channel, rate by region/make, ranked bars, histograms, tables with drill-through.

### Excel / Google Sheets recipes (the playbook covers Looker Studio, not Sheets)

| Visual | Google Sheets | Excel (365) |
|---|---|---|
| V1 scorecard | Big cell + `SPARKLINE()` + conditional colour on the change cell | Same, or a card made from cells |
| V2 line + target | Line chart; add a constant "target" column as a second series | Same |
| V3 vs last year | Pivot by month with years as columns → line chart | Same |
| V4/V5/V6 columns | Column / stacked / 100% stacked column | Same |
| V8 ranked bar | Sort the data, then bar chart | Same |
| V9 combo | Combo chart, line on right axis | Combo chart, secondary axis |
| V10 waterfall | Native waterfall chart | Native waterfall chart |
| V11 funnel | No native: bar chart with steps in order | Native funnel chart |
| V12 histogram | Native histogram chart | Native histogram chart |
| V13 heatmap | Pivot table + colour-scale conditional formatting | Same |
| V14 Pareto | Cumulative % column + combo chart | Native Pareto chart |

Rates in Sheets: `=SUMIFS(...)/COUNTIFS(...)` per period, never `AVERAGE` of a rate column (rule 3). `QUERY()` is a quick SQL-like group-by.

**Looker (Motorway's tool) vs Looker Studio:** different products. Looker uses LookML explores. In an interview, describe the dashboard in Looker terms (single value tiles with comparison, line/column tiles, table with conditional formatting, drill fields on dimensions). Build in Sheets if Looker isn't set up.

## Step 5: Sanity-check before showing anything

Do this on any AI-generated query too. This is the human-in-the-loop part, so say it out loud.

- Row counts before and after each join match expectations (no fan-out).
- Parts add up to totals (regions sum to the total).
- Rates are ratios of sums, with the denominator shown.
- Latest period is complete. Immature cohorts excluded or flagged.
- Spot-check 2–3 individual rows by hand.
- One "does this make sense" check against something known (e.g. Motorway's ~2,000 cars/day).

## Step 6: Storytelling

### The shape of every insight

1. **Headline:** the answer in one plain sentence. "Sales are down 8%, and nearly all of it is the North."
2. **What happened:** the number with its comparison (vs last period, target, last year).
3. **Why:** one level down the KPI tree (playbook §1.2). **Rule out the boring explanations first**: data issue, calendar/timing, mix shift, immature cohorts. Then the real cause.
4. **So what:** size it in pounds, cars or dealers. "That's about 400 cars a week, roughly £X of GMV."
5. **Now what:** a specific recommendation with an owner. "Commercial should recruit dealers in the North for 4×4s."
6. **Confidence and next check:** what you'd verify before betting on it.

### Make it sound human

- Talk like a person explaining to a colleague, not a report. Use "I", "we", "my read is…".
- Round the numbers: "about 1 in 5", "roughly £2m". Give exact figures only when precision matters.
- Every chart title is the takeaway ("Sell-through fell because bids dried up in the North"), not a label ("Sell-through by region").
- One message per chart. Three insights max in a presentation; more dilutes them.
- Be honest about uncertainty: "This is consistent with X, but I can't rule out Y without Z data." Never claim causation from correlation; say what test would prove it.
- Name the assumption you made and why. Interviewers reward judgement more than certainty.
- Connect to the business: sellers want price and speed, dealers want stock they can sell, Motorway earns on completed sales.

### Logical and calculated, not just plausible

- Every claim traces to a number you computed. No invented figures, no "probably about".
- The story must reconcile: if GMV fell 10%, the volume effect and the price effect must explain that 10%.
- Distinguish **level** (we're at 62%) from **change** (down 4 points) from **cause** (because…).
- Watch Simpson's paradox: overall rate down while every segment is flat means a mix shift, not a decline.

### 30-minute presentation shape (aim for ~15 min talk, rest Q&A)

| Min | Section |
|---|---|
| 1–2 | The question and how I approached it |
| 2–4 | The data: what it is, what I checked, what I cleaned, how I used Claude and verified it |
| 4–12 | 2–3 insights, each in the shape above. Exec view first, then drill-down |
| 12–14 | Recommendations and what I'd monitor (the dashboard I'd build: exec page and manager page) |
| 14–15 | Limitations and next steps: what data I'd add |

### Questions Shuma is likely to ask; have an answer ready

- "How do you know it's not a data issue?" → your Step 5 checks.
- "What would you do next?" → the next drill-down, or the missing data.
- "How did you use AI, and how did you verify it?" → prompt with schema plus context, then row counts, reconciliation, spot checks.
- "What would the CEO see vs a manager?" → exec page vs manager page.
- "What would you put on a target / alert?" → the early-warning KPIs (bids per car, time to first bid, valuations started).

## Step 7: Questions to ask Shuma during the task

Pick 2–3, don't interrogate:
- "Who's the audience for this, exec or a team lead?"
- "Is there a specific question or decision behind it, or is it open?"
- "What does one row represent in this table?" (if unclear)
- "Is the most recent period complete?"
- "Are there test or cancelled records I should exclude?"
- "Is there a target I should compare against?"

---

## Output template (what I return when given a schema)

1. **What this data is**: tables, grain, joins, date range, first sanity flags (≤6 lines).
2. **Ranked KPI table**:

   | Rank | KPI (ID) | Formula with *your* column names | Score (adj.) | Why it matters here | Who uses it | Exec / Manager | Main visual + companion | Build in |
   |---|---|---|---|---|---|---|---|---|

3. **Can't build (and what's missing)**: each with the proxy, if any.
4. **Dashboard sketch**: exec page and manager page.
5. **Ready-to-run SQL** for the top 3 (plus Sheets formula if relevant).
6. **2–3 questions for Shuma.**
7. After the charts are built: **the story**, in Step 6 shape.

---

## Worked example (practice run on a made-up schema)

**Schema:**
- `valuations(valuation_id, seller_id, created_at, channel, make, model, year, mileage, region, estimated_price)`
- `listings(listing_id, valuation_id, listed_at, reserve_price, outcome, sold_price, sold_at)`
- `bids(bid_id, listing_id, dealer_id, bid_amount, bid_time)`
- `dealers(dealer_id, region, verified_date, size_band)`

**What it is:** a seller funnel (valuation → listing → sold) plus dealer demand (bids). One row per valuation, listing, bid and dealer respectively. `valuations` → `listings` is 1-to-0..many (relists?), so check that. `listings` → `bids` is one-to-many, so aggregate bids per listing before joining. No fees or costs, so no revenue or profit KPIs.

| Rank | KPI | Formula | Score | Why here | Level | Visual |
|---|---|---|---|---|---|---|
| 1 | Seller funnel (P1 + M1) | distinct valuations → listed → `outcome='sold'` | 4.85 | Shows where sellers are lost; cut by `channel` | Both | V11 funnel + V2 line |
| 2 | Sell-through (C1) | sold listings ÷ listings | 4.75 | Marketplace liquidity; drills by region/make | Both | V2 line + V1 |
| 3 | Active dealers (C2 vs C12) | distinct `bids.dealer_id` per month vs verified | 4.65 | Demand side; active vs verified gap | Both | V4 columns + V1 |
| 4 | Bids per car (C3) | bids ÷ listings | 4.55 | Leads sell-through | Manager | V9 combo |
| 5 | Valuation accuracy (P3) | (`sold_price` − `estimated_price`) ÷ `estimated_price` | 4.40 | Explains rejected offers | Manager | V12 histogram |
| 6 | GMV (F2) + average sale price (F8) | SUM(`sold_price`) where sold; mean and median `sold_price` | 4.30 / 3.65 | Size of the market, and whether it moved on volume or price | Exec | V3 line + V1 |
| 7 | Cumulative sell-through (C4) | share sold by day N since `listed_at` | 4.20 | Speed and plateau | Manager | V15 |
| 8 | Time to first bid (C5) | MIN(`bid_time`) − `listed_at` | 4.15 | Earliest demand signal | Manager | V12 |
| 9 | Bidders per car (C7) | distinct dealers per listing | 3.90 | Competition sets price | Manager | V12 |
| 10 | Dealer concentration (C8) | top-20% dealers' share of wins | 3.85 | Dependence risk | Manager | V14 |
| — | Sale vs reserve (proxy for C6) | `sold_price` ÷ `reserve_price` | 3.50 (−0.5 proxy) | Labelled proxy: no guide price | Manager | V12 |

**Can't build:** contribution per car, revenue, take rate, cost per car sold (no fees or costs). Completion rate (no post-sale status). All of Operations except time to sell.

**Exec page:** GMV · cars sold · sell-through · active dealers (scorecards vs last month) + GMV vs last year line + one-line verdict.
**Manager page:** funnel by channel · sell-through by region × make · bids per car combo · time-to-first-bid histogram · dealer Pareto · table of worst segments.
