# Turning Numbers Into Stories
### A hands-on guide to metric trees and the What → Why → So what → Now what framework

> Based on Christine Jiang's video **"The ONLY Data Storytelling Framework You Need (Real Demo)"** (YouTube, 11:05, published 17 Sep 2026), verified against the full transcript and expanded into a guide you can reuse with your own data. Every query, formula and number in this guide was run and checked on a practice dataset you can generate yourself (Part 6).

---

## How to read this guide

This guide is written like a conversation with a senior analyst sitting next to you. Each part builds on the one before, so it works best read in order the first time. After that, the cheat sheet in Part 10 is all you need.

You'll see two labels throughout:

- **[Video]** marks something Christine says or shows in the video. These points were checked against the transcript.
- **[Added]** marks something this guide adds to make the method reusable: the maths, code, extra trees, exercises and caveats.

Some sections end with **"Check yourself"** questions. Try them before opening the answer, because recalling something is much better for learning than rereading it.

### Contents

- [Part 0 · The whole idea in 60 seconds](#part-0--the-whole-idea-in-60-seconds)
- [Part 1 · The 4:35 pm Slack message](#part-1--the-435-pm-slack-message)
- [Part 2 · Metric trees: the mental model](#part-2--metric-trees-the-mental-model)
- [Part 3 · Finding the "why"](#part-3--finding-the-why)
- [Part 4 · The demo, step by step](#part-4--the-demo-step-by-step)
- [Part 5 · Telling the story](#part-5--telling-the-story)
- [Part 6 · Hands-on toolkit: reproduce everything](#part-6--hands-on-toolkit-reproduce-everything)
- [Part 7 · Practice exercises with model answers](#part-7--practice-exercises-with-model-answers)
- [Part 8 · Common mistakes](#part-8--common-mistakes)
- [Part 9 · Verification notes](#part-9--verification-notes)
- [Part 10 · Cheat sheet and glossary](#part-10--cheat-sheet-and-glossary)

---

## Part 0 · The whole idea in 60 seconds

When someone asks "why did this number change?", don't go hunting through all your data. Instead:

1. **Get context.** Is this change actually unusual or bad? Compare it to forecast and recent history.
2. **Draw a metric tree.** Break the number into the 2–3 smaller numbers that produce it. For example, *revenue = average order value × number of orders*.
3. **Check which branch moved.** Then slice that branch by **one** dimension (product, region, channel…) to see where the movement is concentrated.
4. **Log what you find** as you go.
5. **Tell it as a story:** **What** happened → **Why** it happened → **So what** (what it means) → **Now what** (what to do next).

The last two steps are where you add the most value. Describing a number is easy, and AI tools can do it. Judging what it means and what to do about it is the part people need you for.

---

## Part 1 · The 4:35 pm Slack message

**[Video]** Picture this. It's late on a Wednesday afternoon and your finance director messages you: revenue was down 8% this quarter, can you help us understand why?

Christine describes two kinds of analyst in that moment:

| Analyst 1 | Analyst 2 |
|---|---|
| Opens Excel and SQL and starts checking everything, hoping something jumps out | Already has a mental model of how revenue breaks down |
| Replies with something like "let me look into it and get back to you" | Replies with "let's start with average order value and order count. I want to know whether people are spending less, or fewer people are buying" |
| Sounds unsure, and risks a never-ending analysis | Sounds confident and experienced, and knows exactly where to look first |

The difference between them isn't technical skill. It's that Analyst 2 has a **metric tree** in their head.

> **Why this matters for you:** the same pattern shows up in interviews. "How would you investigate a drop in X?" is a very common analyst question. Answering with a tree immediately sounds like Analyst 2.

**[Video] About the presenter:** Christine Jiang led part of the data team at Vimeo, where she helped hire analysts. She now runs a mentorship program for people moving into data roles. The video links her free business metrics cheat sheet, which she suggests using alongside it.

---

## Part 2 · Metric trees: the mental model

### 2.1 What a metric tree is

**[Video]** A metric tree is a visual model that links a headline ("topline") metric to the smaller, more actionable metrics that actually drive it.

The key insight is that **revenue isn't a standalone number**. It's the output of two smaller numbers multiplied together:

```
Revenue  =  Average order value (AOV)  ×  Number of orders
            "how much each order is      "how many orders
             worth"                       there were"
```

So "why did revenue fall?" really means: **did people spend less per order, did fewer orders happen, or both?** That turns one vague question into two specific ones.

**[Video]** Christine's second example is from marketing:

```
Total clicks  =  Click-through rate  ×  Audience size
                 (quality of content)   (how many people you reach)
```

If clicks drop, you check whether the content got worse (CTR) or you reached fewer people (audience).

> **[Added] Small precision note:** strictly, click-through rate is *clicks ÷ impressions*, so the exact identity is *clicks = impressions × CTR*. "Audience size" is a friendly stand-in for impressions. It's fine for thinking, but use impressions when you calculate.

### 2.2 Every industry has its own trees

**[Video]** Every industry and North Star metric has its own tree. The more you understand the metrics neighbouring yours, the better your intuition gets for why a number moves. Christine's examples:

| Field | Typical topline metric to build a tree for |
|---|---|
| Finance | Revenue |
| SaaS | Active subscribers |
| Product | Retention |

**[Video]** Trees can have several layers, so you can trace a change down to its root cause.

### 2.3 Two kinds of trees [Added]

The video doesn't name this distinction, but it will make you much sharper.

| | **Identity tree** | **Driver tree** |
|---|---|---|
| How branches relate | Exact maths: A = B × C, or A = B + C | Cause and effect: B and C *influence* A |
| Example | Revenue = AOV × orders | Retention ← activation, engagement, support quality |
| Strength | The numbers must add up, so you can **prove** how much each branch contributed | Covers things that can't be written as a formula |
| Weakness | Can stop short of the real cause | You can only show correlation unless you test it |

**Rule of thumb:** use identity branches near the top, because they tell you *where* the change happened. Use driver branches lower down, because they suggest *why*.

> **[Added] This idea is old and proven.** Finance has used it for about a century in *DuPont analysis*, which breaks return on equity into profit margin × asset turnover × financial leverage. Metric trees apply the same trick to any business metric.

### 2.4 How to build your own tree

**[Video]** Start with the topline number you care about most, then identify the **two to three** numbers that directly contribute to it. It doesn't have to be perfect. A rough tree is better than no tree, because it's the difference between freezing on an open-ended question and knowing where to look.

**[Added]** A few rules that make trees easier to use:

1. **Prefer exact identities at the top.** If you can write it as × or +, do.
2. **Stop at actionable leaves.** A leaf is good when a team can influence it or you can investigate it directly.
3. **Expand only the branch that moved.** Don't draw the whole forest up front.
4. **Each split should answer a question.** Price or volume? New or existing customers? Quality or reach?

The common patterns:

| Pattern | Formula | Question it answers |
|---|---|---|
| Price × volume | Revenue = AOV × orders | Spending less, or fewer buyers? |
| Rate × base | Clicks = impressions × CTR | Worse quality, or less reach? |
| Funnel | Purchases = visitors × view rate × cart rate × checkout rate × payment rate | At which step are we losing people? |
| Segment sum | Total = segment A + segment B + … | Which segment moved? |
| Stock and flow | End = start + inflow − outflow | Gaining fewer, or losing more? |

### 2.5 A ready-made tree library [Added]

Treat these as starting points, not rules. They were checked so that every **=** really is an identity.

**E-commerce revenue**
```
Revenue = AOV × Orders
├── AOV = Σ (share of orders by product × that product's average order value)
│         → product mix, prices, discounts, items per order
└── Orders = Visitors × Conversion rate
             → slice by device, channel, landing page
```

**SaaS recurring revenue (MRR)**
```
MRR (end of month) = MRR (start)
                   + New MRR          (new customers × starting plan price)
                   + Expansion MRR    (upgrades, extra seats, add-ons)
                   − Contraction MRR  (downgrades)
                   − Churned MRR      (cancelled customers' MRR)
```

**SaaS active subscribers**
```
Subscribers (end) = Subscribers (start) + New subscribers − Churned subscribers
Churned subscribers = Churn rate × Subscribers (start)
```

**Paid acquisition**
```
New customers = Spend ÷ Cost per acquisition (CAC)
CAC = Cost per click ÷ Click-to-customer conversion rate
Clicks = Impressions × CTR
```

**Product retention (driver tree, not identity)**
```
Retention (e.g. day-30)
├── Activation  → % of new users completing the key first action
├── Engagement  → sessions per user, adoption of core features
└── Friction    → bugs, support tickets, time to first value
```

**Subscription churn (segment sum)**
```
Churned customers = Voluntary churn (chose to leave)
                  + Involuntary churn (failed payments, expired cards)
```

**Support ticket volume**
```
Tickets = Active customers × Tickets per customer
Tickets per customer → bug rate, onboarding clarity, outages
```

<details>
<summary><b>Check yourself:</b> Monthly ad revenue for a news site fell. Draw the first split.</summary>

One good tree is **ad revenue = page views × ads per page × fill rate × price per ad (RPM)**. The first question becomes: did we get less traffic, show fewer ads, or earn less per ad? A simpler first split is **page views × revenue per thousand page views**, which is traffic versus monetisation.
</details>

---

## Part 3 · Finding the "why"

### 3.1 Context first: is this change actually bad?

**[Video]** A falling metric sounds bad, but something completely different can be happening underneath. Christine's example: if revenue was *forecast* to fall 10%, then −8% is actually not so bad. But if this is the *first* quarter of decline, it's a big red flag. Establishing that context is part of your job.

**[Added]** Context checklist:

- [ ] What was the **forecast or target**?
- [ ] How does it compare with the **last 2–4 periods**? First decline, or the third in a row? Bigger or smaller than before?
- [ ] Is there **seasonality**? Compare with the same period last year.
- [ ] Were there **known events**, such as a launch, outage, price change, campaign or tracking change?
- [ ] Is the change bigger than **normal noise**? Small segments bounce around naturally.

> **[Added] Percent vs percentage points.** If churn goes from 5% to 7%, that's **+2 percentage points** but **+40%** relative. "Churn ticked up 2%" is ambiguous, so say which you mean. Use "points" (pp) for changes in rates and "%" for relative changes.

### 3.2 Check the neighbours, not everything

**[Video]** The common trap Christine sees in students is going broad straight away: traffic, seasonality, promotions. That spirals into analysis with no clear outcome. Instead:

1. Check the **one to three neighbouring metrics** in the tree to see what moved.
2. **Slice** those metrics by a **key dimension** to isolate the movement.

**[Added]** How to read the first split for price × volume:

| AOV | Orders | What it suggests |
|---|---|---|
| ↓ | → | Cheaper purchases, more discounting, or smaller baskets |
| ↑ | ↓ | Fewer buyers but higher-value ones, often a mix shift (this is the demo) |
| ↓ | ↓ | Broad weakness, so check the top of the funnel |
| → | ↓ | Pure volume problem: traffic or conversion |
| Opposite directions | | The headline hides two stories, so report both |

### 3.3 Put numbers on each branch [Added]

The video reads the branches as percentages. Two quick calculations make your answer airtight.

**1. The identity check.** For a × tree, the changes multiply:

```
(1 + AOV change) × (1 + orders change) = 1 + revenue change
(1 + 0.034)      × (1 − 0.11)          = 0.920   →  revenue −8.0% ✓
```

If this doesn't come out right, your numbers have a problem (wrong date range, double-counted orders…). Fix that before you tell any story.

**2. The money bridge.** This is how much each branch added or removed:

```
Revenue change  =  Volume effect                    +  AOV effect
                =  (change in orders) × (old AOV)    +  (change in AOV) × (new orders)
```

With the practice data (Part 6):

```
−13,151  =  (−110 orders × 164.29)  +  (+5.53 × 890 orders)
         =       −18,072            +       +4,921
```

Now you can say something precise: **lost volume cost about 18k, and higher order values clawed back about 5k.** Executives love this sentence.

> Why not "AOV explains X% of the change"? When the two branches pull in opposite directions, percentage shares come out strange (one branch "explains" more than 100%). A money bridge is always easy to read.

### 3.4 Slice by one dimension at a time

**[Added]** Pick the dimension that best fits your hypothesis:

| Your question | Slice by |
|---|---|
| What are people buying? | Product, category, price band |
| Who is it happening to? | Customer tier, new vs returning, cohort |
| Where? | Region, country, store |
| How did they arrive? | Channel, campaign, referrer |
| On what? | Device, browser, app version |
| When exactly? | Day, week, release date |

Go one at a time. Slicing five dimensions at once produces a wall of numbers and no story.

### 3.5 Mix effect vs within-segment effect [Added]

**[Video]** Christine explains that AOV is driven by **product mix**. If people buy more expensive products, AOV goes up, and if they buy cheaper ones, it goes down.

That's true, but there's a second way AOV can rise: **the same products got more expensive** (price increases, fewer discounts). A careful analyst checks both. The exact split is:

```
AOV change = Mix effect     + Within-segment effect
           = Σ (new share − old share) × old segment AOV
           + Σ new share × (new segment AOV − old segment AOV)
```

In the practice data, sliced by product: **AOV +5.53 = mix +5.53 + price 0.00**. That's a pure mix shift, which confirms Christine's explanation.

> **Watch out:** the "within" part depends on how you slice. Sliced by **product**, it's a genuine price effect. Sliced by **region**, the product mix changes hide *inside* each region. In the practice data the region slice shows mix 0.00 and within-region +5.53, even though nothing about prices changed. Slice by the dimension that matches your question.

### 3.6 How to know you've found it

You've found the driver when:

- the movement is **concentrated** in one or two slices, such as "79 of the 110 lost orders were earbuds";
- the other slices are roughly **flat**, or move in line with the total;
- the **timing** matches a known event, if there is one; and
- you can explain it in **one or two sentences**.

**[Added] Record negative results too.** "Checked region: every region fell 6–9%, so no single region explains it" is a real finding. It saves you and your stakeholder from re-checking, and it makes your story more convincing.

<details>
<summary><b>Check yourself:</b> AOV +3%, orders −11%. Without a calculator, roughly what happened to revenue?</summary>

For small changes, the percentages roughly add: +3% − 11% ≈ **−8%**. The exact figure is 1.03 × 0.89 − 1 = −8.3%. The demo's +3.4% AOV gives exactly −8.0%.
</details>

---

## Part 4 · The demo, step by step

**[Video]** Christine walks through the 8% revenue question in a spreadsheet, pretending it's the end of Q3 2026. Here is each step: what she did, what it showed, why it matters, and how to reproduce it with the practice data.

> The practice dataset (Part 6) is built to reproduce the video's headline numbers exactly: revenue −8%, AOV +3%, orders −11%, a Q2 mix of 19% gaming monitors and 41% earbuds, and the same direction of change for each product. The individual product counts are invented, because the video doesn't show them. Product names are generic ("Wireless earbuds" rather than AirPods).

### Step 1 · Confirm the headline and get context

- **[Video] What she found:** revenue really is down 8% versus last quarter, but this is the **smallest drop of the last two quarters**. So it might not all be bad.
- **Why it matters:** the story has already changed from "revenue is falling" to "the decline may be easing".
- **Reproduce:** practice data, Part 6.

| Quarter | Revenue | Change | Orders | Change | AOV | Change |
|---|---|---|---|---|---|---|
| 2025-Q4 | 220,545 | | 1,300 | | 169.65 | |
| 2026-Q1 | 190,650 | −13.6% | 1,140 | −12.3% | 167.24 | −1.4% |
| 2026-Q2 | 164,290 | −13.8% | 1,000 | −12.3% | 164.29 | −1.8% |
| **2026-Q3** | **151,139** | **−8.0%** | **890** | **−11.0%** | **169.82** | **+3.4%** |

### Step 2 · Check the two neighbouring metrics

- **[Video] What she found:** AOV is **up about 3%**, the first time all year that it has grown. Order count is **down 11%**, still a fall but slightly less steep than the previous two quarters.
- **Why it matters:** this is a volume problem, partly cushioned by people spending more per order.
- **[Added] Prove it:** identity check 1.034 × 0.89 = 0.920 ✓. Money bridge: −18,072 from volume and +4,921 from AOV.

### Step 3 · Start an insights log

**[Video]** She writes each finding down as she goes, which gives the analysis shape. Then she tackles AOV and order count separately. (The full log is in Part 6.5.)

### Step 4 · Explain the AOV rise with product mix

- **[Video] What she did:** broke each quarter's orders down by product. In Q2, about **19%** of orders were gaming monitors and **41%** were AirPods.
- **[Video] What she found:** customers bought slightly more gaming monitors and slightly fewer AirPods, plus a small uptick in MacBook Airs. The rest of the mix stayed about the same. So AOV rose because of a trade from cheaper earbuds towards pricier monitors (and a few more laptops).
- **Practice data:**

| Product | Q2 share | Q3 share | Change |
|---|---|---|---|
| Wireless earbuds ($149) | 41.0% | 37.2% | −3.8 pts |
| Gaming monitor ($300) | 19.0% | 21.6% | +2.6 pts |
| Laptop ($500) | 6.0% | 6.7% | +0.7 pts |
| Charging cable pack ($20) | 20.0% | 21.1% | +1.1 pts |
| Webcam ($80) | 9.0% | 8.1% | −0.9 pts |
| Keyboard ($100) | 5.0% | 5.3% | +0.3 pts |

- **[Added] Verify it's mix, not price:** mix effect +5.53, within-product price effect 0.00. The video assumes mix without checking prices, so do this check on real data.

### Step 5 · Explain the order drop with volume by product

- **[Video] What she did:** looked at order counts by product. The pivot table was a wall of numbers, so she weighed two options. One was to calculate exact growth rates. The other, because her audience is a senior finance director, was to go **directional** with a simple line chart.
- **[Video] What she found:** dips in AirPods, charging cable packs and the Samsung webcam, and a slight rise in gaming monitor purchases. In short, **the volume loss is concentrated in cheaper products**, while a pricier product grew.
- **Practice data, exact version:**

| Product | Q2 orders | Q3 orders | Change | % change |
|---|---|---|---|---|
| Wireless earbuds | 410 | 331 | −79 | −19.3% |
| Webcam | 90 | 72 | −18 | −20.0% |
| Charging cable pack | 200 | 188 | −12 | −6.0% |
| Keyboard | 50 | 47 | −3 | −6.0% |
| Laptop | 60 | 60 | 0 | 0.0% |
| Gaming monitor | 190 | 192 | +2 | +1.1% |

- **[Added] Find the biggest contributor:** earbuds alone account for 79 of the 110 lost orders, about **72%**. That's −7.9 of the −11 points.

### Step 6 · Stop when you have a story

**[Video]** At this point she has enough to take back to the stakeholder. You don't need to answer every possible question, just the one you were asked, with clear next steps. The story itself is in Part 5.3.

---

## Part 5 · Telling the story

### 5.1 The four parts

**[Video]** This is the structure Christine teaches for turning any metric into a story:

| Part | The question it answers | What goes in it |
|---|---|---|
| **What** | What happened? | The number, its direction and size, the period, and context |
| **Why** | What caused it? | The 1–3 drivers, with numbers and the slice that isolates them |
| **So what** | Why should anyone care? | Your judgement: good, bad or mixed? Temporary or structural? |
| **Now what** | What should we do next? | Specific next checks or actions, ideally with an owner |

### 5.2 Why most analysts stop too early

**[Video]** Christine notices that most analysts, in projects and interviews, stop after the first one or two parts. "Revenue was down 8% because AOV went up and order count went down" just describes the number, and AI can easily do that. The judgement call and what to do next is where your business knowledge and communication come in.

**[Added]** A useful test: *if your stakeholder could have produced your answer by looking at the dashboard, you haven't finished yet.*

### 5.3 The demo story

**[Video]** Christine's version, paraphrased: revenue fell 8%, driven by an 11% dip in volume alongside a 3% rise in AOV, the first AOV increase all year. The downturn isn't all bad, because customers are starting to buy pricier products like laptops and monitors, and lost volume is in cheaper items like headphones. Next steps: find out what is driving the shift to laptops and monitors (particular regions? last quarter's promotions?) and whether to push that further this quarter. That gives the finance director next steps to explore with the product team.

**[Added] Tightened version, ready to send:**

> **What:** Revenue fell 8% in Q3, our smallest quarterly decline this year.
> **Why:** Order volume dropped 11%, mostly in low-priced items. Earbuds alone account for about 70% of the lost orders. That was partly offset by a 3% rise in average order value, the first increase this year, as customers shifted towards gaming monitors and laptops. In money terms, lost volume cost us about 18k and higher order values recovered about 5k.
> **So what:** The decline is easing, and the revenue we're losing is mostly low-value. The shift towards higher-priced products is a genuinely positive signal.
> **Now what:** I'd like to check with the product team what's driving the move to monitors and laptops (specific regions, or last quarter's promotions?) so we can push it further this quarter. Separately, it's worth asking why earbud volume fell almost 20%.

> **Note:** the AOV increase **offset** the drop rather than **driving** it. It's a small wording point, but stakeholders notice.

### 5.4 Three more examples from the video, expanded

**[Video]** Christine gives three more short examples and suggests comparing your own project and interview answers against them. The stories below are paraphrased. The "how you'd get there" lines are **[Added]**, showing which tree and slice would produce each insight.

**A. Product analyst: conversion fell 6%**

> **What/Why:** Conversion dropped 6%, entirely on mobile. Desktop was flat.
> **So what:** It's probably related to the checkout redesign that shipped last Tuesday.
> **Now what:** Work with the marketing team to confirm exactly what changed and whether to roll some of it back.

*How you'd get there:* tree = conversion by device (a segment split). First slice = device. Timing check = release log. Note the hedge "probably": timing alone shows correlation, not proof. **[Added] Next level:** slice mobile by funnel step to confirm the drop is at checkout.

**B. Growth: signups up 20%**

> **What/Why:** Signups rose 20%, but almost all of the increase came from one paid channel where spend tripled. Organic and referrals were flat.
> **So what:** This may not be sustainable.
> **Now what:** Check the average cost of these new signups to see whether they're worth it.

*How you'd get there:* tree = signups as a sum of channels. Slice = channel. **[Added] Next level:** compare cost per signup and early retention for that channel against the others. Cheap signups that don't stick aren't growth.

**C. Subscriptions: churn ticked up 2%**

> **What/Why:** Churn rose, concentrated in customers on the lowest pricing tier in North America. Meanwhile, customers in Japan started buying more expensive plans and staying on them longer.
> **So what:** This is a local, low-tier problem, plus a promising trend elsewhere.
> **Now what:** Look into the trends in both regions and refine promotions there.

*How you'd get there:* slice churn by tier, then by region within that tier. **[Added]** Say whether "2%" means percentage points or relative change (Part 3.1).

### 5.5 Calibrate to your audience

**[Video]** Strong business communication means adjusting the story for who you're talking to: technical, non-technical, or other teams. Christine calls this one of the most important skills separating analysts who thrive in the age of AI from those who feel left behind. You saw it in the demo, where she used a simple chart rather than exact growth rates for the finance director.

| Audience | Lead with | Level of detail |
|---|---|---|
| Executive / director | So what + Now what | Directional chart, one or two numbers, the money bridge |
| Data team / technical peer | Why, with method | Exact rates, definitions, caveats, queries |
| Product or marketing team | The lever they own | Their slice, timing, and what to test |
| Interviewer | Your structure | Say the tree out loud, then walk What → Why → So what → Now what |

**[Added]** For senior audiences, consider **putting the So what first** ("Good news inside a bad number: …"). Busy readers decide whether to keep reading from the first sentence.

**[Video]** Knowing what to do next (the Now what) depends on domain knowledge of your industry. Christine's metrics cheat sheet is her suggested shortcut. **[Added]** Another is to read your company's earnings calls or board decks, which use exactly these trees.

### 5.6 Phrase bank [Added]

| Part | Sentence starters |
|---|---|
| What | "[Metric] was [up/down] X% in [period], which is [better/worse] than [forecast/trend]." |
| Why | "This was driven by … and partly offset by …" · "Almost all of the change came from …" · "[Other slices] were flat." |
| So what | "This means …" · "The good news inside this number is …" · "This is [one-off / a trend / not sustainable] because …" |
| Now what | "Next, I'd like to check … with [team]." · "I recommend we … by [date]." · "To confirm this, we could …" |

### 5.7 Quality checklist before you send

- [ ] **What** includes context, not just the raw number
- [ ] **Why** names specific drivers, with numbers
- [ ] The identity check adds up
- [ ] **So what** takes a position (good, bad, mixed, sustainable?)
- [ ] **Now what** has at least one specific, ownable next step
- [ ] Hypotheses are worded as hypotheses ("probably", "to confirm…")
- [ ] It would make sense to this particular reader
- [ ] They could repeat it in one sentence

---

## Part 6 · Hands-on toolkit: reproduce everything

Everything here was **run and checked**. Python with pandas 3.0, the SQL in DuckDB 1.5 using PostgreSQL-compatible syntax, and the spreadsheet formulas recalculated in LibreOffice Calc 24.2. All the numbers in Parts 3–5 come from these tools.

### 6.1 Generate the practice dataset (Python)

Save this as `make_practice_data.py` and run `python make_practice_data.py`. It writes `orders.csv`, which has 4,330 orders with one product each.

```python
"""Generate a practice dataset that reproduces the video's demo numbers.

One row per order (one product per order, quantity 1) from Q4 2025 to Q3 2026.
Q3 2026 vs Q2 2026: revenue -8%, AOV +3%, orders -11%.
Region is included on purpose with NO signal, so you can practise logging a negative result.
"""
import csv
import datetime as dt

PRICES = {
    "Wireless earbuds": 149,
    "Gaming monitor": 300,
    "Laptop": 500,
    "Charging cable pack": 20,
    "Webcam": 80,
    "Keyboard": 100,
}

# Orders per product per quarter: (quarter label, first day of quarter, counts)
QUARTERS = [
    ("2025-Q4", dt.date(2025, 10, 1), {"Wireless earbuds": 505, "Gaming monitor": 240, "Laptop": 100,
                                        "Charging cable pack": 245, "Webcam": 130, "Keyboard": 80}),
    ("2026-Q1", dt.date(2026, 1, 1),  {"Wireless earbuds": 450, "Gaming monitor": 212, "Laptop": 80,
                                        "Charging cable pack": 220, "Webcam": 110, "Keyboard": 68}),
    ("2026-Q2", dt.date(2026, 4, 1),  {"Wireless earbuds": 410, "Gaming monitor": 190, "Laptop": 60,
                                        "Charging cable pack": 200, "Webcam": 90, "Keyboard": 50}),
    ("2026-Q3", dt.date(2026, 7, 1),  {"Wireless earbuds": 331, "Gaming monitor": 192, "Laptop": 60,
                                        "Charging cable pack": 188, "Webcam": 72, "Keyboard": 47}),
]

REGIONS = ["North", "North", "South", "South", "South", "East", "East", "West", "West", "West"]

rows, order_id = [], 100000
for label, start, counts in QUARTERS:
    for product, n in counts.items():
        for i in range(n):
            order_id += 1
            day = start + dt.timedelta(days=(i * 89) // max(n, 1))  # spread across ~90 days
            rows.append({
                "order_id": order_id,
                "order_date": day.isoformat(),
                "quarter": label,
                "product": product,
                "region": REGIONS[i % len(REGIONS)],
                "quantity": 1,
                "unit_price": PRICES[product],
                "revenue": PRICES[product],
            })

with open("orders.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} orders to orders.csv")
```

**Make your own scenario:** change the counts in `QUARTERS` to invent a new situation. For example, make laptops the product that drops, and watch AOV fall while orders hold up. Then practise the full method on it.

### 6.2 Run the whole diagnosis (Python)

Save as `metric_tree_analysis.py`, then run `python metric_tree_analysis.py orders.csv`. It works on **any** order-line file with `order_id`, `order_date`, `product` and `revenue` columns. Change `DIMENSION` to slice by something else.

```python
"""Run the full metric-tree diagnosis on an orders file.

Usage:  python metric_tree_analysis.py orders.csv
Needs columns: order_id, order_date, product, revenue  (one row per order line).
Change DIMENSION to slice by something else (region, channel, device...).
"""
import sys
import pandas as pd

DIMENSION = "product"

df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else "orders.csv", parse_dates=["order_date"])
df["quarter"] = df["order_date"].dt.to_period("Q").astype(str)

# 1. Topline + neighbours: revenue = AOV x orders
q = df.groupby("quarter").agg(revenue=("revenue", "sum"), orders=("order_id", "nunique"))
q["aov"] = q["revenue"] / q["orders"]
for col in ["revenue", "orders", "aov"]:
    q[f"{col}_chg"] = q[col].pct_change()
print("== Topline and neighbour metrics ==")
print(q.round(3).to_string(), "\n")

cur, prev = q.index[-1], q.index[-2]

# 2. Sanity check: the identity must hold, (1 + AOV change) x (1 + orders change) = 1 + revenue change
lhs = (1 + q.loc[cur, "aov_chg"]) * (1 + q.loc[cur, "orders_chg"]) - 1
print(f"Identity check: (1+AOV)(1+orders)-1 = {lhs:.4f}  vs revenue change {q.loc[cur, 'revenue_chg']:.4f}\n")

# 3. Revenue bridge in money: how much did each branch add or remove?
#    volume effect = change in orders x OLD AOV ; AOV effect = change in AOV x NEW orders (adds up exactly)
d_rev = q.loc[cur, "revenue"] - q.loc[prev, "revenue"]
volume_effect = (q.loc[cur, "orders"] - q.loc[prev, "orders"]) * q.loc[prev, "aov"]
aov_effect = (q.loc[cur, "aov"] - q.loc[prev, "aov"]) * q.loc[cur, "orders"]
print(f"Revenue bridge: {d_rev:+,.0f} = volume effect {volume_effect:+,.0f} + AOV effect {aov_effect:+,.0f}\n")

# 4. Slice: mix (share of orders) and volume by dimension, previous vs current quarter
two = df[df["quarter"].isin([prev, cur])]
counts = two.pivot_table(index=DIMENSION, columns="quarter", values="order_id", aggfunc="nunique", fill_value=0)
mix = counts / counts.sum()
out = pd.DataFrame({
    f"orders_{prev}": counts[prev],
    f"orders_{cur}": counts[cur],
    "volume_chg": counts[cur] - counts[prev],
    f"share_{prev}": mix[prev].round(3),
    f"share_{cur}": mix[cur].round(3),
    "share_chg_pts": ((mix[cur] - mix[prev]) * 100).round(1),
}).sort_values("volume_chg")
print(f"== Slice by {DIMENSION}: {prev} vs {cur} ==")
print(out.to_string(), "\n")

# 5. Mix vs within-segment effect on AOV
#    mix effect    = AOV change caused by the SHARE of orders moving between segments
#    within effect = AOV change caused by each segment's own average order value changing
#    (when DIMENSION is product, the within effect is a true price/discount effect)
seg_aov = (two.groupby([DIMENSION, "quarter"])["revenue"].sum()
           / two.groupby([DIMENSION, "quarter"])["order_id"].nunique()).unstack()
mix_effect = ((mix[cur] - mix[prev]) * seg_aov[prev]).sum()
within_effect = (mix[cur] * (seg_aov[cur] - seg_aov[prev])).sum()
print(f"AOV change {q.loc[cur, 'aov'] - q.loc[prev, 'aov']:+.2f} = "
      f"mix effect {mix_effect:+.2f} + within-{DIMENSION} effect {within_effect:+.2f}")
```

**Expected output on the practice data** (abridged):

```
== Topline and neighbour metrics ==
         revenue  orders      aov  revenue_chg  orders_chg  aov_chg
2025Q4    220545    1300  169.650          NaN         NaN      NaN
2026Q1    190650    1140  167.237       -0.136      -0.123   -0.014
2026Q2    164290    1000  164.290       -0.138      -0.123   -0.018
2026Q3    151139     890  169.819       -0.080      -0.110    0.034

Identity check: (1+AOV)(1+orders)-1 = -0.0800  vs revenue change -0.0800
Revenue bridge: -13,151 = volume effect -18,072 + AOV effect +4,921

== Slice by product: 2026Q2 vs 2026Q3 ==
                     orders_2026Q2  orders_2026Q3  volume_chg  share_2026Q2  share_2026Q3  share_chg_pts
Wireless earbuds               410            331         -79          0.41         0.372           -3.8
Webcam                          90             72         -18          0.09         0.081           -0.9
Charging cable pack            200            188         -12          0.20         0.211            1.1
Keyboard                        50             47          -3          0.05         0.053            0.3
Laptop                          60             60           0          0.06         0.067            0.7
Gaming monitor                 190            192           2          0.19         0.216            2.6

AOV change +5.53 = mix effect +5.53 + within-product effect +0.00
```

With `DIMENSION = "region"`, every region's share of orders stays within about 0.6 points. That's your negative result: **region doesn't explain this**.

### 6.3 SQL version

Tested in DuckDB with PostgreSQL-compatible syntax. The table is called `order_lines` because each row is one line of an order. That's why the queries use `COUNT(DISTINCT order_id)`: a basket with three products is still **one** order.

**Query 1 · Topline and neighbours with % change**

```sql
WITH q AS (
  SELECT
    DATE_TRUNC('quarter', order_date)  AS quarter,
    SUM(revenue)::NUMERIC              AS revenue,
    COUNT(DISTINCT order_id)::NUMERIC  AS orders
  FROM order_lines
  GROUP BY 1
)
SELECT
  quarter,
  revenue,
  orders,
  ROUND(revenue / orders, 2)                                                  AS aov,
  ROUND(revenue / NULLIF(LAG(revenue) OVER w, 0) - 1, 4)                     AS revenue_chg,
  ROUND(orders  / NULLIF(LAG(orders)  OVER w, 0) - 1, 4)                     AS orders_chg,
  ROUND((revenue / orders) / NULLIF(LAG(revenue / orders) OVER w, 0) - 1, 4) AS aov_chg
FROM q
WINDOW w AS (ORDER BY quarter)
ORDER BY quarter;
```

Why it's written this way: `::NUMERIC` avoids **integer division**, where 890/1000 would become 0 in some databases. `NULLIF(…, 0)` avoids divide-by-zero errors.

**Query 2 · Product mix (share of orders) per quarter**

```sql
WITH t AS (
  SELECT
    DATE_TRUNC('quarter', order_date) AS quarter,
    product,
    COUNT(DISTINCT order_id)          AS orders
  FROM order_lines
  GROUP BY 1, 2
)
SELECT
  quarter,
  product,
  orders,
  ROUND(orders * 1.0 / SUM(orders) OVER (PARTITION BY quarter), 3) AS share_of_orders
FROM t
ORDER BY quarter, product;
```

> **Caveat:** if orders can contain several products, these shares add up to more than 100%, because one order counts once for each product in it. In that case, measure mix as **share of revenue** or **share of units** instead.

**Query 3 · Volume change by product, previous vs current quarter**

```sql
WITH p AS (
  SELECT
    product,
    COUNT(DISTINCT order_id) FILTER (WHERE order_date >= DATE '2026-04-01' AND order_date < DATE '2026-07-01') AS prev_qtr,
    COUNT(DISTINCT order_id) FILTER (WHERE order_date >= DATE '2026-07-01' AND order_date < DATE '2026-10-01') AS cur_qtr
  FROM order_lines
  GROUP BY product
)
SELECT
  product,
  prev_qtr,
  cur_qtr,
  cur_qtr - prev_qtr                                         AS abs_change,
  ROUND((cur_qtr - prev_qtr) * 1.0 / NULLIF(prev_qtr, 0), 3) AS pct_change
FROM p
ORDER BY abs_change;
```

If your database doesn't support `FILTER`, write `COUNT(DISTINCT CASE WHEN <condition> THEN order_id END)` instead. It gives the same result.

**Query 4 · Generic "slice by any dimension" template** (shown filled in for region)

```sql
SELECT
  region,                                   -- swap in any dimension
  SUM(CASE WHEN order_date >= DATE '2026-07-01' AND order_date < DATE '2026-10-01' THEN revenue ELSE 0 END) AS current_value,
  SUM(CASE WHEN order_date >= DATE '2026-04-01' AND order_date < DATE '2026-07-01' THEN revenue ELSE 0 END) AS previous_value,
  SUM(CASE WHEN order_date >= DATE '2026-07-01' AND order_date < DATE '2026-10-01' THEN revenue ELSE 0 END)
- SUM(CASE WHEN order_date >= DATE '2026-04-01' AND order_date < DATE '2026-07-01' THEN revenue ELSE 0 END) AS abs_change
FROM order_lines
GROUP BY region
ORDER BY abs_change;
```

Result on the practice data: West −9.0%, South −8.4%, East −8.4%, North −5.6%. All regions fell by a similar amount, so region isn't the story. The biggest **absolute** drops are simply in the biggest regions, which is why you should look at % change too.

**Dialect notes:** in BigQuery use `DATE_TRUNC(order_date, QUARTER)`. MySQL has no `DATE_TRUNC`, so build the quarter with `CONCAT(YEAR(order_date), '-Q', QUARTER(order_date))`.

### 6.4 Excel / Google Sheets version

Recalculated in LibreOffice and matching the Python figures. Assume the data is in columns **A** `order_id`, **B** `order_date`, **C** `product`, **D** `revenue`, with a helper column **E** for the quarter.

**1. Quarter label (E2, fill down):**
```
=YEAR(B2)&"-Q"&ROUNDUP(MONTH(B2)/3,0)          → "2026-Q3"
```

**2. Revenue per quarter (summary sheet, quarter label in A2):**
```
=SUMIFS(data!D:D, data!E:E, A2)
```

**3. Number of orders, counting each order once.** This is the step people most often get wrong, because `COUNT(order_id)` counts **lines**, not orders.

| Tool | Formula or method |
|---|---|
| Excel pivot table | Tick **"Add this data to the Data Model"** when creating the pivot, then set the value field to **Distinct Count** |
| Excel 365 | `=COUNTA(UNIQUE(FILTER(data!A2:A5000, data!E2:E5000=A2)))` |
| Google Sheets | `=COUNTUNIQUEIFS(data!A2:A5000, data!E2:E5000, A2)` |
| Any version (slow on big data) | `=SUMPRODUCT((data!E2:E5000=A2)/COUNTIFS(data!A2:A5000,data!A2:A5000,data!E2:E5000,data!E2:E5000))` |

**4. AOV and % change:**
```
AOV:       =B2/C2                  (revenue ÷ distinct orders)
% change:  =(B3-B2)/B2
```

**5. Contribution of one product to the total change, in points:**
```
=(product_orders_new - product_orders_old) / total_orders_old
```
Earbuds: (331 − 410) / 1000 = **−7.9 points** of the −11%.

**6. Product mix pivot:** Rows = quarter, Columns = product, Values = order count. Then go to **Value Field Settings → Show Values As → % of Row Total** (in Google Sheets: **Summarise by → Show as → % of row**).

**7. Directional view:** insert a **line chart** of order count by product over quarters, the same view Christine used for the finance director.

### 6.5 The insights log

**[Video]** Christine keeps a running log as she works. **[Added]** Here's a template, filled in with the practice data:

| # | Finding | Evidence | Meaning / hypothesis | Next check |
|---|---|---|---|---|
| 1 | Revenue −8% QoQ, smallest drop this year | −13.6%, −13.8%, −8.0% | Decline may be easing | Check neighbours |
| 2 | AOV +3.4%, first rise this year | 164.29 → 169.82 | Customers spending more per order | Mix vs price |
| 3 | Orders −11%, slightly less steep than before | −12.3%, −12.3%, −11.0% | Volume is the main problem | Slice by product |
| 4 | Identity holds | 1.034 × 0.89 = 0.920 | Numbers are consistent | none |
| 5 | Bridge: −18.1k volume, +4.9k AOV | money bridge | Headline for executives | none |
| 6 | AOV rise is pure mix | mix +5.53, price 0.00 | Shift to monitors and laptops | Why the shift? |
| 7 | Earbuds = 72% of lost orders | −79 of −110 | Biggest single driver | Why did earbuds fall? |
| 8 | Region is not the driver (negative result) | All regions −6% to −9% | Don't pursue region | none |

Rules for a good log: one finding per row, always with a number, negative results included, and a "next check" column so it doubles as your to-do list.

---

## Part 7 · Practice exercises with model answers

For each one: **(a)** draw the tree, **(b)** name the first check, **(c)** choose a slice, **(d)** write all four parts of the story using plausible invented numbers. Then open the model answer.

<details>
<summary><b>1. Streaming app:</b> monthly watch time fell 5%.</summary>

- **Tree:** watch time = active users × sessions per user × minutes per session.
- **First check:** which of the three moved? Fewer users is a reach problem. Fewer or shorter sessions is an engagement or content problem.
- **Slice:** if users are down, slice by new vs returning. If minutes per session are down, slice by content type or device.
- **Example story:** "Watch time fell 5%. Active users were flat, but minutes per session fell 6%, almost entirely on TV devices after the app update on the 3rd. So it's an engagement problem on one platform, not lost viewers. Next, work with the TV app team to check playback errors and autoplay since the update."
</details>

<details>
<summary><b>2. Food delivery:</b> gross order value is up 12%, but profit is flat.</summary>

- **Tree:** profit = gross order value × take rate − delivery costs − promotion costs − other costs.
- **First check:** did the take rate fall, or did costs grow faster than order value?
- **Slice:** by city or by promotion. Growth bought with discounts often shows up here.
- **Example story:** "Order value grew 12% but profit was flat, because promotion spend doubled and most of the growth came from discounted orders in two new cities. The growth is real but unprofitable so far. Next: compare repeat-order rates for promo vs non-promo customers before extending the campaign."
</details>

<details>
<summary><b>3. B2B SaaS:</b> net revenue retention dropped from 110% to 104%.</summary>

- **Tree:** NRR = (starting MRR + expansion − contraction − churned MRR) ÷ starting MRR.
- **First check:** did expansion shrink, or did contraction or churn grow? Express each as points of NRR.
- **Slice:** customer size or plan, then signup cohort.
- **Example story:** "NRR fell 6 points. Churn was stable, but expansion fell from 15 to 9 points as mid-size customers stopped adding seats, in line with hiring freezes in that segment. So existing customers aren't leaving, they're just growing more slowly. Next: test usage-based upsells with customer success for the mid-size segment."
</details>

<details>
<summary><b>4. Newsletter:</b> open rate is steady, but click-through fell by a quarter.</summary>

- **Tree:** clicks ÷ delivered = open rate × click-to-open rate (CTOR). Open rate is flat, so **CTOR** fell by about a quarter.
- **First check:** CTOR by issue, and by link position.
- **Slice:** content type, or template version.
- **Caveat:** open rates have been inflated since Apple's Mail Privacy Protection (2021) began pre-loading emails, so a "steady" open rate may hide real changes. Clicks are the more trustworthy signal.
- **Example story:** "Clicks fell 25% while opens held steady, so people are reading but not clicking. It started with the new template, which moved links below the fold. Next: A/B test the old link placement in the next two issues."
</details>

<details>
<summary><b>5. Retail chain:</b> same-store sales are up 3%, but foot traffic is down 8%.</summary>

- **Tree:** sales = foot traffic × conversion rate × average basket.
- **The maths:** 1.03 ÷ 0.92 = 1.12, so conversion × basket together rose about **12%**.
- **First check:** was it conversion (more visitors buying) or basket (each buyer spending more)?
- **Slice:** by store format, or category.
- **Example story:** "Sales grew 3% despite 8% less traffic, because the average basket rose 11% thanks to price increases in groceries. That growth depends on pricing, and fewer people are coming in. Next: check basket size excluding price changes, and whether traffic loss is concentrated in specific stores."
</details>

<details>
<summary><b>6. Mobile game:</b> day-7 retention improved, but revenue per user fell.</summary>

- **Tree:** revenue per user = payer rate × revenue per payer. Retention is a separate branch.
- **First check:** did fewer users pay, or did payers spend less?
- **Slice:** acquisition channel and cohort. A **mix effect** is likely: new low-intent users who stick around but rarely pay.
- **Example story:** "Retention rose but revenue per user fell 10%, because a new ad channel brought in many non-paying users who stay but rarely buy. Revenue per payer is unchanged. Not a monetisation problem, but a mix shift. Next: report metrics by channel so the overall average doesn't hide it, and decide whether those users are worth the acquisition cost."
</details>

### Interview drill

> "A key metric at a company you like dropped 10% last month. Walk me through how you'd investigate."

<details>
<summary><b>Model answer structure</b></summary>

1. **Clarify:** "Which metric exactly, compared with what? Last month, or the same month last year? Was a drop expected?"
2. **Context:** "Before diagnosing, I'd check the forecast, the recent trend, seasonality, and any launches or tracking changes."
3. **Say the tree out loud:** "Revenue is AOV × orders, so the first question is whether people spent less per order or fewer people bought."
4. **First check and why:** "I'd compare those two first, because it halves the search space."
5. **First slice and what would confirm it:** "Then I'd slice the branch that moved by product. If the drop is concentrated in one category, that's my lead. If it's spread evenly, I'd look at traffic and conversion instead."
6. **Sense-check:** "I'd confirm the components multiply back to the total."
7. **Communicate:** "I'd present What, Why, So what, Now what, with the So what first if it's going to an executive."
</details>

---

## Part 8 · Common mistakes

| Mistake | Why it hurts | Fix |
|---|---|---|
| Checking everything at once | Endless rabbit holes **[Video]** | Draw the tree, check the 1–3 neighbours |
| Assuming "down" means "bad" | Misses healthy shifts underneath **[Video]** | Get context, then check composition |
| Stopping at What and Why | Only describes the number **[Video]** | Always add So what and Now what |
| Vague next steps ("look into it") | Nobody can act on it | Name the check, the team and the question |
| Counting order lines as orders | AOV and order counts come out wrong | `COUNT(DISTINCT order_id)` / Distinct Count |
| Assuming mix when prices changed | Wrong explanation for AOV | Split mix vs within-product effect |
| Mixing up % and percentage points | Misleading sizes | "pts" for changes in rates |
| Reading only absolute changes | Big segments always look like the cause | Look at % change and shares too |
| Treating timing as proof | Correlation isn't causation | Hedge ("probably"), then propose a test |
| Slicing many dimensions at once | Noise, and false patterns | One dimension, chosen by hypothesis |
| Not recording findings | You lose the thread **[Video]** | Keep an insights log |
| Ignoring noise in small segments | Chasing random wobbles | Compare with normal period-to-period variation |
| One message for every audience | Loses the room **[Video]** | Adapt depth and order to the listener |

---

## Part 9 · Verification notes

### What was checked

1. **Every [Video] claim** in this guide was compared against the video's full English transcript and its official description, including the scenario, examples, demo numbers, framework and closing advice. Quotes are paraphrased.
2. **Every number** in Parts 3–6 was computed three independent ways (pandas, SQL in DuckDB, and spreadsheet formulas in LibreOffice), and all three agreed.
3. **Every formula and tree** marked with = was checked to be a true identity.

### Confirmed from the video

The 4:35 pm Wednesday Slack from a finance director about an 8% revenue drop · the two-analysts contrast · the definition of a metric tree · revenue = AOV × orders · clicks = CTR × audience size · trees for finance (revenue), SaaS (active subscribers) and product (retention) · start with 2–3 contributing numbers, and a rough tree beats none · the −10% forecast context example · the warning against broad rabbit holes (traffic, seasonality, promotions) · check 1–3 neighbours, then slice by a key dimension · demo set at the end of Q3 2026 · −8% being the smallest drop of the last two quarters · AOV +3% for the first time all year · orders −11% as a slight easing · Q2 mix of 19% gaming monitor and 41% AirPods · mix shift towards monitors and slightly more MacBook Airs · line-chart dips in AirPods, charging cable packs and the Samsung webcam, with a slight monitor uptick · choosing directional over exact for a senior audience · What / Why / So what / Now what · most analysts stopping after part one or two · AI can describe numbers · the three extra examples (conversion −6% on mobile, signups +20% from one paid channel, churn up in North America's lowest tier with Japan improving) · calibrating to the audience · domain knowledge driving the Now what.

### Nuances in the video, clarified here

| In the video | Clarification | Where |
|---|---|---|
| The demo story says the revenue fall was driven by the volume dip *and* the AOV rise | The AOV rise **offset** the fall, so say "partly offset by" | 5.3 |
| AOV rise attributed to product mix | Correct here, but the video didn't check prices or discounts. Verify mix vs price on real data | 3.5 |
| Mix measured as share of orders by product | Works when each order has one product. With multi-product baskets, use share of revenue or units | 6.3 |
| Clicks = CTR × audience size | The exact identity is impressions × CTR | 2.1 |
| "Churn ticked up by 2%" | Ambiguous between percentage points and relative %. State which | 3.1 |
| Volume lost "only" in cheaper products | Directionally right from a line chart. Confirm with exact numbers before stating it strongly | 4, Step 5 |

### Corrections to the previous version of this guide

| Previous version | Problem | Fixed to |
|---|---|---|
| Excel AOV `=SUM(revenue)/COUNT(order_id)` | Counts lines, not orders | Distinct-count methods (6.4) |
| SQL table named `orders` with a product column | Misleading. It's line-level data | `order_lines`, with `COUNT(DISTINCT order_id)` throughout |
| SQL used `COUNT(*)` for product volume | Counts lines | `COUNT(DISTINCT order_id)` |
| SQL had no protection against integer division or divide-by-zero | Could return 0 or errors | `::NUMERIC`, `NULLIF` |
| MRR tree listed components without starting MRR | Didn't add up | Full stock-and-flow identity |
| Paid acquisition "tree" mixed unrelated items | Not an identity | Spend ÷ CAC, with CAC = CPC ÷ conversion |
| Conversion example: "confirm with marketing/product" | Video says the **marketing** team | Corrected |
| Conversion example's "drop at checkout step" and "8 weeks" presented as if from the video | These were illustrative additions | Now labelled [Added] |
| Demo story said "driven by" both changes | AOV offset the drop | "Partly offset by" |

---

## Part 10 · Cheat sheet and glossary

### One-page cheat sheet

**1 · Clarify:** metric, direction, size, period, baseline.

**2 · Context:** forecast? trend? seasonality? events? noise?

**3 · Tree:** topline → 2–3 drivers (× or + where possible).

**4 · Neighbours:** % change for each driver. Check that the identity multiplies back to the total.

**5 · Bridge:** volume effect = Δorders × old AOV; AOV effect = ΔAOV × new orders.

**6 · Slice:** one dimension at a time. Look for concentration, use % and shares, and record negative results.

**7 · Mix vs price:** did the share move, or did the segment itself change?

**8 · Log:** finding · evidence · meaning · next check.

**9 · Story:**
- **What:** number + context
- **Why:** drivers with numbers ("partly offset by…")
- **So what:** take a position
- **Now what:** a specific next step, with an owner

**10 · Audience:** executives get So what first and a simple chart. Technical audiences get exact rates and method.

### Glossary

| Term | Meaning |
|---|---|
| **AOV (average order value)** | Revenue ÷ number of distinct orders |
| **QoQ** | Quarter over quarter, compared with the previous quarter |
| **Percentage point (pt / pp)** | The difference between two percentages (5% → 7% = +2 pts) |
| **Topline / North Star metric** | The headline number a team is judged on |
| **Metric tree** | A diagram linking a topline metric to the smaller metrics that produce it |
| **Identity tree** | A tree where branches combine exactly (× or +) |
| **Driver tree** | A tree where branches influence the parent but don't add up exactly |
| **Dimension** | A category you slice by: product, region, channel, device… |
| **Mix effect** | Change caused by the share of activity moving between segments |
| **Within-segment effect** | Change caused by segments themselves changing, such as prices |
| **Revenue bridge** | Splitting a revenue change into money amounts per driver |
| **CTR / CTOR** | Click-through rate (clicks ÷ impressions or delivered) / click-to-open rate (clicks ÷ opens) |
| **MRR / NRR** | Monthly recurring revenue / net revenue retention |
| **CAC** | Customer acquisition cost |
| **Insights log** | A running list of findings, with evidence and next checks |

---

*Credit: the metric-tree approach, the demo and the What / Why / So what / Now what framework come from Christine Jiang's video "The ONLY Data Storytelling Framework You Need (Real Demo)". Everything marked [Added] (the tree library, maths, code, practice data, exercises and verification) was written for this guide. Video content is paraphrased.*
