---
name: nrr-narrative
description: >
  Use when the user says "NRR", "net revenue retention", "why did NRR drop", "retention slide for the board", "explain our retention numbers", "what is our NRR hiding". Produces a one-page, board-ready retention narrative: the bridge from starting to ending ARR, gross retention beside net, cohort or blended, concentration, what recurs, what the number hides, and three sentences for the slide. Not for the forward number (use renewal-forecast) or the account reads underneath it (use portfolio-review).
---

# NRR Narrative

A one-page retention story a board can follow and a CFO cannot poke a hole in, built by taking the number apart before explaining it.

## Start here

If the user gave a period and the ARR movements (or starting and ending ARR for the same customers), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The period, starting ARR from existing customers, and any of: expansion, price uplift, contraction, churn.
2. Cohort cuts if they exist, the three largest expansions, and where churn sat (segment, channel, cohort).
3. The audience, and the decision the number feeds.

Missing movements are estimated and tagged `(assumed, confirm)`; a movement that cannot be split goes under "What I could not check". If an "Account context" block exists in the conversation, use it for pricing model (consumption pricing changes the arithmetic).

## Do this

1. **Decompose before narrating.** Starting ARR + expansion + price - contraction - churn = ending ARR for the same customers. Check it adds. Keep price and expansion apart: one is demand, the other is a charge.
2. **Compute the pair.** GRR = (start - contraction - churn) / start. NRR = (start + expansion + price - contraction - churn) / start. Add NRR without price. Put GRR first, and put the prior period beside it.
3. **Say the basis.** Cohort or blended, and any definition change this period. If blended, say what it flatters: customers landed recently have not reached a renewal yet.
4. **Find the concentration.** Share of expansion from the top three accounts. Where contraction and churn sit. Concentrated loss is a segment problem. Even loss is a product or pricing problem.
5. **Separate what recurs.** A one-time price uplift does not repeat. Multi-year terms defer churn, so also compute GRR on the base that was free to leave this period.
6. **Name what the number hides,** in your own words before anyone asks. Add one leading indicator that moves ahead of the number, with its mechanism, and the decision or spend the narrative supports.
7. **Write three sentences first:** what happened, why, what we are doing. Then the page. If it cannot be said in three, the analysis is not done.

## Output

Lead with the headline. Use this skeleton exactly:

```
[Headline: GRR x%, NRR y% for the period, and the one-line story]

Bridge ($k): start | + expansion | + price | - contraction | - churn | = end
  GRR | NRR | NRR without price   (this period beside prior period)
Basis: cohort or blended. Definition changes: [none, or what changed and the restated figures]
Concentration: [expansion from top three; where loss sits; cohort cut]
What recurs and what does not: [price, multi-year deferral, GRR on the base free to leave]
What the number hides: [bullets, disclosed not defended]
Leading indicator: [metric, mechanism, current reading, cadence]
Ask or decision: [what the board is being asked to back, and the target]
Three sentences for the slide

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its shape and length.

## Rules

- **GRR before NRR, always together.** Expansion in a few accounts can hold NRR flat while the base shrinks, and the gap between the two is the story.
- **Price is not expansion.** Expansion shows customers want more. Price shows you charged more. A board that finds the merge later distrusts every other number.
- **Contraction gets its own number.** Accounts that stayed and shrank are easy to leave out and are often the larger negative.
- **Blended flatters a fast-growing base.** The faster new business lands, the more young customers sit in the denominator before their first renewal. Show a cohort cut.
- **Deferred churn is not avoided churn.** Customers on multi-year terms cannot leave this year, so show retention on the exposed base too.
- **A changed definition goes first.** If the audience finds it themselves, the rest of the deck stops being believed.
- **Disclose concentration yourself.** If three accounts supplied most of the expansion, the number is three renewals, and it will not repeat on its own.
- **Show dollars beside percents.** A drop of four points means little to a board until it sees the dollars behind it.
- **Report lagging and leading together.** Retention is lagging by quarters. A board deciding where to spend needs the indicator it can watch now.

## Related (only if installed)

`renewal-forecast` for the forward half. `portfolio-review` for the reads underneath. `coverage-model` when the pattern is a coverage decision showing up in the numbers.
