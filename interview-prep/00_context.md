# Motorway BI Data Analyst: Stage 2 Interview Context

## Logistics

| Item | Detail |
|---|---|
| Company | Motorway (UK's largest online car-selling platform) |
| Role | BI Data Analyst, Analytics team, London (Hybrid) |
| Stage | 2nd stage: **Live Task Interview** ("AI Proficiency Tests") |
| Interviewer | **Shuma**, BI Team Lead (same person as stage 1) |
| Recruiter | Dan Gurhey |
| Format | **30 min** live task on provided data → **30 min** presenting findings/analysis |
| Tools expected | **SQL**, **Excel/Sheets**, possibly **Looker**, and **Claude** is allowed |
| Ground rules | Nothing to prepare in advance. Shuma is on hand for questions and guidance during the first 30 min, so **ask clarifying questions**. |

## Stage 1 feedback (what already landed)

- Building dashboards tailored to different user needs.
- TrackMyMachines work: improved KPI calculations, shipped tested solutions.
- **Deliberate use of AI tools like Claude Code** stood out.
- Stage 2 aims to **validate data modelling and reporting skills**.

## What Shuma said the role needs (from stage 1 conversation)

1. **Understand KPIs**: what they mean, how they're calculated, and what moves them.
2. **Collaborate across teams**: Marketing, Finance, Product, Commercial, Operations.
3. **Build dashboards at different levels**:
   - **Manager level**: detailed drill-downs across all KPIs (by segment, region, channel, time).
   - **Executive / CEO level**: a high-level overview of what's happening (a few headline KPIs, trend, vs target, the "so what").
4. **Use AI** to speed all of this up while staying accurate.
5. **Storytelling**: analyse data and tell the story of what is happening, why, and what to do next. Give the business insights, not just numbers.

## Job description summary

**About Motorway**
- UK's largest online car-selling platform, founded 2017. Series C, £143m raised.
- **Two-sided marketplace**: private **sellers** ↔ **8,000+ dealers** nationwide.
- Value prop: sellers get great prices; dealers get fast, reliable access to stock.

**About the role**
- Own analytical projects end-to-end: scope the business problem, then deliver the insight.
- Build and maintain critical dashboards and reporting.
- Surface trends and **anomalies** in business performance.
- Use **data storytelling** to drive measurable outcomes.
- Use AI strategically: LLM-assisted query generation, analysis summarisation, code review.
- Act as **human-in-the-loop**: check accuracy and repeatability of AI-driven self-serve analysis done by other teams.

**What you'll do**
- Take business problems and structure them into well-defined analytical tasks.
- Own KPI monitoring and reporting for embedded stakeholder teams, with **data accuracy** as the priority.
- **Root-cause data discrepancies** and explain them in detail.
- Build **Looker dashboards** and **Hex notebooks** for deep dives and self-serve.
- Write production-quality **SQL and Python** that passes peer review, and help others review AI-generated output.
- Communicate insights and recommendations clearly, with narratives that drive action.
- Use AI tools for query generation, analysis drafts and documentation without losing quality.
- Work with Analytics Engineers to bring new data sources into the stack.

**Stack named:** Looker, Hex, SQL, Python, AI/LLM tools (Claude).

## What the live task is likely testing (inference)

| They'll be watching for | How to show it |
|---|---|
| Problem structuring | Restate the question, agree on scope and definitions with Shuma before touching data |
| Data modelling | Understand grain, keys and joins; spot duplicates, nulls, fan-out |
| KPI thinking | Define each metric precisely (numerator, denominator, time window) |
| Accuracy / human-in-the-loop | Sanity-check AI output: row counts, reconciling totals, spot-checking edge cases |
| Deliberate AI use | Use Claude out loud and with intent: prompt with schema and context, then verify the result |
| Reporting at two levels | Exec summary (3 headline numbers + so-what) **and** a manager drill-down |
| Storytelling | What happened → why → so what → recommended action |

## Motorway business context: likely KPIs (my inference, not from the JD)

Motorway is a marketplace, so the data will probably follow this funnel:

**Seller side (supply)**
- Valuations requested → vehicles listed (valuation-to-listing conversion)
- Listing → sold (sell-through rate), time to sell
- Seller price expectation vs final sale price; re-list / price-drop rate
- Seller acquisition cost (CAC) by marketing channel

**Dealer side (demand)**
- Active dealers, bidding dealers, buying dealers
- Bids per vehicle, auction competitiveness
- Dealer retention / repeat purchase rate

**Transaction / commercial**
- Vehicles sold, GMV (gross merchandise value), average sale price
- Revenue (dealer fees), take rate, contribution margin
- Cancellations / post-sale issues (e.g. vehicle not as described), collection/ops SLAs

**Common cuts for drill-downs:** region, make/model, vehicle age/mileage, price band, marketing channel, dealer segment, week/month.

---
*More instructions to come. This file is the base context for the rest of the prep.*
