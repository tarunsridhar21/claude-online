# From results to a spoken story

Use this when Tarun sends **insights or query results** (numbers, tables, chart screenshots). It applies `STORYTELLING_GUIDE.md` (metric trees, What → Why → So what → Now what) to Motorway, and produces something he can **read once and say out loud**.

---

## Part A: Evaluate the results first (silent checks, then a short verdict)

Run these on his numbers before writing any story. Report only what fails or matters.

1. **Context.** Change vs last period, vs last year, vs target. First drop or the third in a row? Is the latest period complete?
2. **Put it in a tree.** Which branch moved? Use the Motorway trees below.
3. **Identity check.** For × trees: (1 + change A) × (1 + change B) should equal 1 + topline change. If it doesn't, the numbers have a problem: say so before any story.
4. **Money bridge.** Volume effect = Δvolume × old price; price effect = Δprice × new volume. Turns "%" into "£ lost / £ gained".
5. **Mix vs within.** Did the share move between segments (mix), or did each segment itself change (within)? Slice by the dimension that matches the question.
6. **Concentration.** Is the movement in 1–2 slices ("72% of the lost cars were in X")? If every slice moved equally, that's a **negative result**. Say it, because it rules something out.
7. **Noise.** Small slices (under ~30 cars) bounce around. Don't build a story on them.
8. **Wording traps.** Percentage points (pts) for changes in a rate, % for relative change. A factor that cushioned a fall "partly offset" it; it didn't "drive" it.
9. **Confidence.** High (identity holds, concentrated, big sample), medium (directional, timing only), low (small sample, proxy data). Hypotheses stay hypotheses: "most likely", "to confirm this…".

### Motorway metric trees (starting points)

```
Revenue        = GMV × take rate
GMV            = cars sold × average sale price
Cars sold      = valuations × listing rate × sell-through × completion rate
Sell-through   = cars sold ÷ cars entered      ← bids per car, bidders per car (demand)
                                                ← supply mix, price vs guide (supply)
Avg sale price = Σ (segment share × segment price)   → mix vs within-segment price
Contribution per car = revenue per car − marketing − transport − support
Active dealers (end) = start + new − churned
```

How to read the first split:

| Volume | Price | Reading |
|---|---|---|
| ↓ | → | Pure volume problem: funnel or demand |
| ↓ | ↑ | Fewer cars but dearer ones, likely a mix shift |
| → | ↓ | Price problem: softer dealer demand, or cheaper mix |
| ↓ | ↓ | Broad weakness, so go to the top of the funnel |

---

## Part B: Write the story so it's easy to say

Tarun speaks Indian English and will deliver this live. Write the way he would naturally speak: clear, confident and professional. **No phonetic spellings, no forced dialect.** Make it easy to say by design:

- **Short sentences.** One idea per sentence, 8–15 words. Every full stop is a breathing point.
- **Common, plain words.** Prefer "dropped" to "declined precipitously", "mainly" to "predominantly", "check" to "ascertain", "mix" to "composition". Avoid long, stress-heavy words where a short one works ("particularly" → "especially", "statistically significant" → "a real change, not noise", "heterogeneous" → "mixed").
- **Natural Indian English connectors** he'd actually use: "So basically…", "What is happening here is…", "The main reason is…", "Now, the important point is…", "So my recommendation is…", "One more thing I noticed…".
- **No American idioms or sports metaphors** ("move the needle", "ballpark", "slam dunk", "low-hanging fruit"). Say it directly.
- **Numbers written as spoken**, UK style: "about eighteen thousand pounds", "around one in five cars", "down eight per cent", "two points". No "£18k" or "pp" in the spoken script. Round them.
- **Signpost the structure out loud**: "First, what happened. Then why. Then what it means, and what I would do."
- **British spelling** (Motorway is UK): analyse, organisation, programme.
- **Max three insights.** More than three, nobody remembers.

---

## Part C: Output format (return exactly this, briefly)

**1. Quick check:** 2–4 bullets: does it add up, what's concentrated, what's ruled out, confidence. Flag anything that would embarrass him if Shuma asked.

**2. 30-second version (for the exec / opening line):** So what first. Three to four sentences.

**3. Spoken script (~2 minutes):** What → Why → So what → Now what, each labelled, short sentences, numbers as spoken.

**4. Likely questions, with one-line answers:** 3 max.

---

## Example, using the guide's practice numbers (illustrative only, not Motorway data)

Inputs: revenue −8% QoQ (third fall, smallest of the three); orders −11%; AOV +3.4%; earbuds −79 of −110 lost orders; mix effect +5.53, price effect 0; regions all −6% to −9%.

**1. Quick check**
- Adds up: 1.034 × 0.89 = 0.92, so −8% ✓. Bridge: volume −18k, AOV +5k.
- Concentrated: earbuds are about 70% of lost orders. Region ruled out.
- AOV rise is pure mix, not price. Confidence: high.

**2. 30-second version**
> "Good news inside a bad number. Revenue is down eight per cent, but this is the smallest drop this year. We are mainly losing cheap orders, especially earbuds. And customers are moving to monitors and laptops, so each order is worth more. I want to find out what is driving that shift, so we can push it further."

**3. Spoken script**
> **What happened.** Revenue dropped eight per cent this quarter. But this is the third fall in a row, and it is the smallest one. So the decline is slowing down.
>
> **Why.** Basically, revenue is orders times average order value. Orders fell eleven per cent. But average order value went up about three per cent. That is the first increase this year. In money terms, we lost around eighteen thousand pounds from fewer orders. And we got back around five thousand from higher order values.
>
> Now, where did the orders go? Mainly earbuds. Earbuds alone are about seventy per cent of the lost orders. I also checked region. All regions fell by a similar amount. So region is not the reason.
>
> **So what.** The revenue we are losing is mostly low-value orders. And customers are shifting to more expensive products, like monitors and laptops. That is actually a positive sign.
>
> **Now what.** I would do two things. First, check with the product team why people are moving to monitors and laptops. Is it a promotion, or something else? If it is working, we should push it. Second, find out why earbud orders fell almost twenty per cent.

**4. Likely questions**
- *"How do you know it's mix and not a price increase?"* → "I split the change. All of it is mix. Prices within each product did not change."
- *"Is region really not a factor?"* → "Every region fell between six and nine per cent. If it was regional, one would stand out."
- *"What would you put on a dashboard?"* → "Orders and order value as headline numbers, with product mix underneath, so we catch this early next time."
