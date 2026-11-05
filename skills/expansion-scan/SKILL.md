---
name: expansion-scan
description: >
  Use when the user says "scan my book for expansion", "where is the upsell hiding", "who is ready to expand", "rank my expansion opportunities", "which accounts are outgrowing their plan", "seats are nearly full". Produces a ranked table scored on confidence, size and timing, a hold list of accounts that must not be asked yet, conservative sizing, and a first-conversation note for the top one. Not for the business case on one deal (use expansion-case) or passing a lead to sales (use csql-motion).
---

# Expansion Scan

Paste the book. Get the few accounts worth an expansion conversation, ranked, sized conservatively, with the first conversation written for the best one.

## Start here

If the user pasted a list with account, ARR and any seats or usage numbers, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The list: account, ARR, renewal date and notice period, seats bought and in use (or whatever unit you price on)
2. Usage movement over the last 30 to 60 days, plus health or open issues per account
3. Anything customers said: a new team asking, a new use case, a leader mentioning the product

If an "Account context" block exists in the conversation, use it for the pricing unit and what counts as expansion.

## Do this

1. **Gate first.** Move any account whose deployment is not demonstrably working to the hold list: open escalation, stalled adoption, sponsor gone, unmet decider inside the notice window. Name the fix and a rescan date.
2. **List the signals** per remaining account: capacity (seats nearly full), momentum (usage up by about a third on its own prior period), proof (a result the customer stated), demand (a new team or use case asked), executive mention. Tag each `said` (who, when), `seen` (where) or `inferred`, and name what else could explain it.
3. **Set confidence** using `references/sizing.md`. A behavioral signal alone is Low. A customer-stated need raises it. A known payer and scope make it High.
4. **Size from their side.** Their stated scope times today's unit price when they gave one, else a default from `references/sizing.md`. Show low and expected, and the basis for each.
5. **Rank** by expected size times confidence weight, ties broken on timing (a budget cycle opening, or distance to the notice date). Show the arithmetic once.
6. **Write the first conversation for the top account:** how it opens, two or three questions, what to listen for, who joins, and what not to do (quote a price, bring in sales before the need is stated).
7. **Say how to log it:** one line per opportunity, an estimate with basis and date, stage "identified", never "pipeline".

## Output

Verdict first. Keep it to one page.

```
EXPANSION SCAN: [date] | [n] scanned | [n] ranked | [n] on hold
Verdict: [where the real opportunity is, weighted estimate]

| # | Account | ARR | Conf | Low | Expected | Weighted | Timing |
Signals: [one tagged line per ranked account]

Hold (do not ask)
- [Account] | [signal] | [what blocks it] | fix by [date], rescan [date]

No signal: [n] accounts [names]
Sizing assumptions (defaults, set your own): [unit price, weights]

First conversation: [Account], [person]
Open: [..]  Ask: [..]  Listen for: [..]  Bring: [..]  Do not: [..]
Log as: estimate $[x], basis [..], stage identified, [date]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Expand only what is working.** An ask on a shaky deployment reads as chasing revenue, and the customer's answer ("fix this first") lands in the renewal.
- **A signal is a prompt, not an opportunity.** It becomes one when the customer states a need in their own words. Until then it is a hypothesis, and a pipeline built from usage curves is forecast fiction.
- **Rank by confidence times size times timing.** The biggest number is usually the least certain, and chasing it spends the best hours on the weakest lead.
- **Size the customer's cost of the problem, not the price list.** The champion must defend the number against other uses of their budget. List price times every possible seat is a wish.
- **Full seats are capacity, not demand.** They can be full from shared logins or one team's peak. Check that the next users exist and want it before counting.
- **Mind the notice date.** An ask inside the notice window competes with the renewal for the same attention and can turn a clean renewal into a negotiation. Sequence it after, unless the customer raises it.
- **Hand over without burning the relationship.** The champion gets a case they can carry first. Sales joins only after the customer states the need and agrees to the intro, and the CSM stays in the room. A customer who meets a seller before asking for one feels sold to.
- **Log estimates as estimates.** A number quoted later as a commitment becomes a target someone is measured against.

## Related (only if installed)

`expansion-case` to build the case the champion carries. `csql-motion` for the handoff to sales. `renewal-risk` on any account that lands on the hold list.
