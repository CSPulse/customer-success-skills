---
name: csql-motion
description: >
  Use when the user says "CSQL", "CS sourced pipeline", "should CS sell", "hand expansion leads to sales", "CS to sales handoff for expansion", "how do we credit CS for expansion". Produces a filled design for passing expansion signals from customer success to sellers: the position, two or three written signals, a warm handoff with a context note, attribution, two measures and kill criteria. Not for the business case on one deal (use expansion-case) or the team's capacity (use coverage-model).
---

# CSQL Motion

A design for how CSMs surface expansion signals and hand them to sellers without spending the trust that produced them.

## Start here

If the user said who spots, who works the lead, and how each side is paid, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Who works expansion today (AE, account manager, expansion team) and what CS owns commercially.
2. Three to five recent expansions that happened, and what was visible beforehand.
3. How CSMs and sellers are paid on expansion and retention.

Missing items are assumed and listed under "What I could not check". If an "Account context" block exists in the conversation, use it for motion and segments.

## Do this

1. **Choose the position.** Spot and hand off, CS owns expansion end to end, or deliberately neither. Check it against pay and training. CSMs expected to sell who are neither trained nor paid for it is the worst option, and it is the default when nobody decides.
2. **Write two or three qualifying signals,** built from the recent wins. Behavioral or stated only: a named owner with a stated need, a usage boundary being hit, an organizational trigger (new team, region, merger, mandate), a repeated workaround, an explicit ask. The CSM names which one fired and quotes the evidence. Thresholds are a common default, set your own.
3. **Design the handoff as an introduction.** The CSM introduces, stays on the first call, and leaves only once the need is confirmed. A five-line context note travels first: signal, who said it, what was discussed, what to avoid, who the skeptic is. Set a response window, for example one business day to acknowledge and five to first contact (a common default, set your own).
4. **Protect the customer.** Value conversation and sales conversation never share a meeting. The CSM raises a possibility and does not negotiate. A "no" changes nothing about service.
5. **Settle attribution before the first lead moves.** Sourced versus influenced, with a test. Whether both teams can claim the deal. What the CSM gets, stated even if it is nothing. Who owns the number.
6. **Pick two measures.** Conversion of CSQLs against the sellers' other sources, and relationship cost: renewal behavior, engagement and satisfaction of passed accounts against comparable accounts not passed. Track how many CSMs contribute.
7. **Write kill criteria and a review date,** so the program is stopped on evidence instead of quietly ignored.

## Output

Lead with the position. Use this skeleton exactly:

```
CSQL MOTION: [company] | [n] CSMs | [n] sellers working expansion

Call: [the position, and the one precondition that must hold]

Position: [spot and hand off / CS owns / neither] and why, given pay and training
Signals (CSM names which fired, quotes evidence): 1. ... 2. ... 3. ...
Handoff: [who introduces, who stays, response window]
Context note (five lines, filled for one example account)
Customer protection: [separation of conversations, "no" is free]
Attribution: [sourced vs influenced test, double count, what the CSM gets, who owns the number]
Measures: [conversion vs other sources, relationship cost, contribution spread]
Kill criteria and review date

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its shape and length.

## Rules

- **One bad handoff ends the flow of signals.** A CSM whose flagged customer gets a cold call stops flagging, so reading the note before contact is a precondition, not a courtesy. If sellers cannot commit to it, do not start.
- **Qualify on behavior or a stated need, never satisfaction.** A happy customer has not said they need more, and a program built on happiness produces volume that does not convert.
- **The CSM stays in the room.** Disappearing at handoff confirms the customer's worst reading of what just happened.
- **No cold outreach to a warm account.** The introduction comes from someone the customer already trusts.
- **A "no" must be free.** If declining changes service, the customer notices, and everything the CSM says afterward is discounted.
- **Attribution disputes start after the first large deal.** Settle them while nothing is at stake. If the honest answer for CSMs is "nothing", say so and expect the volume that buys.
- **Measure relationship cost, not just conversion.** Unmeasured, the main risk is invisible by design.
- **A program with no end condition is never ended.** It is ignored while the slide remains, so write the thresholds and the date now.

## Related (only if installed)

`expansion-case` for the business case once a signal qualifies. `business-review` for keeping value and sales conversations apart. `coverage-model` for whether the team has capacity at all.
