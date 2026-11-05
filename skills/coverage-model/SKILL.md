---
name: coverage-model
description: >
  Use when the user says "coverage model", "CSM ratio", "how many accounts per CSM", "do we need more headcount", "high touch low touch", "we cannot cover the long tail". Produces a filled tier model: who gets a named CSM, pooled or digital, the capacity gap in hours, what each tier will not see, and a back-test against accounts that actually churned. Not for working a book that is already tiered (use book-triage) or what coverage implies for the forecast (use renewal-forecast).
---

# Coverage Model

A tier model the user can defend to leadership: who gets a named CSM, who is pooled, who is digital, what that costs in hours, and what the team is choosing not to see.

## Start here

If the user gave an account count (or list), the ARR spread and the CSM headcount, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The book: account count and ARR by size band, or the list with ARR and complexity notes (integrations, business units, regulated).
2. The team: CSM headcount, and any pooled, support or digital capacity.
3. The last two years of churn: account, ARR, segment, stated reason.

Hours per account that the user cannot supply are assumed and tagged `(assumed, confirm)`. If an "Account context" block exists in the conversation, use its segments.

## Do this

1. **Segment on three axes:** value, complexity, potential. Complexity (integrations, business units, regulation, bespoke setup) drives cost to serve. List the accounts that change tier because of it.
2. **Estimate cost to serve** in CSM hours per account per year for each tier, bottom up: planned touches plus reactive load. About 1,400 productive hours per CSM per year is a common default, set your own.
3. **Compute the ratio as an output.** Hours per account x accounts / productive hours = FTE needed per tier. Compare to headcount. The gap in hours is the finding.
4. **Define each tier in five lines:** named, pooled or digital; cadence you can meet at the computed load; what the customer may ask for; response commitment; the trigger that moves them up. Then write what the tier will not get and what you therefore will not see.
5. **Close the gap by choice.** Move accounts down, reduce the promise, or invest in the mechanism that makes a lower tier work. Recompute hours after the moves; they must fit headcount. Never absorb the gap quietly.
6. **Design the transitions.** Downward moves get a reason and a warm handover. Temporary elevations get an owner and an end date.
7. **Back-test against churn.** Put each churned account in its tier under the new model. Ask what signal would have fired and who would have seen it. Report the losses the model would have missed and the trigger that closes each.

## Output

Lead with the call. Use this skeleton exactly:

```
COVERAGE MODEL: [company] | [n] accounts | $[x] ARR | [n] CSMs

Call: [the model in one line, the hours gap, the trade accepted]

Tier | Accts | ARR | Coverage | Cadence | Hrs/acct | FTE | Up-trigger
Entry rules: [value, complexity] and the accounts moved by complexity

Capacity: required [h] vs available [h], gap [h]. Closed by: [moves, each with hours]
Not served: [per tier: what it does not get, what we will not see]
Digital needs: instrumentation | content | triggers with owners | route to a human
Transitions: [down, up, temporary elevation with owner and end date]
Back-test: [n] churned, by tier, seen or not seen, trigger that closes the gap
Review date: [date]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its shape and length.

## Rules

- **The ratio is an output.** Headcount divided by accounts describes a budget. Cost to serve times accounts is what tells you what the book needs.
- **Tier on complexity as well as revenue.** A small multi-site account costs more than a large simple one, and revenue-only tiers misplace both.
- **A cadence you cannot meet is a promise to be broken quietly.** The CSMs discover it first, by dropping the tail. Size the cadence to the computed load.
- **Write down what each tier loses.** Digital has no relationship signal, pooled has no continuity, and a named CSM absorbs more than the model says. A model with no stated losses is described, not designed.
- **Call it unserved unless digital has four parts:** instrumentation, content, triggers with owners, and a route to a human. Without them the word "digital" hides the gap.
- **The downward move is the dangerous one.** The customer feels abandoned just as they were already unhappy, so the handover is part of the design.
- **Temporary elevation needs an end date.** Otherwise each escalation becomes permanent and the model erodes into everyone being high touch.
- **A model that fails the back-test is only plausible.** If most past losses land in a tier with no signal for how they left, change the triggers before launch.

## Related (only if installed)

`book-triage` for working inside the tiers. `handoff` for the tier-change handover. `renewal-forecast` for what the model implies about the number.
