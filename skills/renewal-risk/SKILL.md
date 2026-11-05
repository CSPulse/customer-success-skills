---
name: renewal-risk
description: >
  Use when the user asks "will they renew", "is this account at risk", "renewal risk", "churn risk", "should I be worried about [account]", "what's the read on [account]", "they asked for our utilization numbers or the notice date", or names an account with a renewal date inside two quarters. Produces a one-page call (renew, contract or churn) with the dollar range, the decider, the mechanism and the next move. Not for scoring a health model (use health-score), planning the timeline (use renewal-runway) or a champion who just left (use champion-loss).
---

# Renewal Risk

A one-page read the user can act on or defend in a forecast call. Built on one idea: usage describes the user, the renewal is decided by the buyer.

## Start here

If the user gave an account, a renewal date and roughly what they pay, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, ARR, renewal date, and the notice or opt-out date if the contract has one
2. Who signs, and when the user last spoke to them
3. The one thing that is worrying the user (or "nothing, just checking")

Anything else the user pastes (usage, emails, notes, the contract) is a bonus. If an "Account context" block exists in the conversation, use it to judge what normal looks like for this business.

## Do this

1. **Set their clock, not yours.** Opt-out date = renewal date minus notice period. Find their budget planning and fiscal year end if known. Report time left in their terms ("three weeks to their notice date"), not "90 days to renewal".
2. **Name the decision and the decider.** Renew as is, smaller, on new terms, or replace. A named human with budget authority. Whether the user has ever spoken to them. If the decider cannot be named, that is the finding and it goes first.
3. **Read the signals by weight.** Decision mechanism first, then commercial, then usage shape, then support, then organizational. Load `references/signals.md` for the full list. A heavy signal outranks any amount of comfort from a light one.
4. **Tag every piece of evidence** as `said` (someone told us, and who), `seen` (we observed it, and where) or `inferred` (our reading). Never let an inference sit in the evidence list untagged.
5. **State the mechanism as a chain**, from what was observed to non-renewal. If no chain can be built, write "mechanism unknown" and make finding it the play.
6. **Argue against the read**, then price it: full renewal, likely contraction and its size, and the downside. Dollars, not a color.
7. **Name one play** matched to the mechanism, with an owner, a date, the ask of the user's own company, and a checkpoint that can fail.

## Output

Use this skeleton. Keep it under one page.

```
RENEWAL READ: [Account] | [ARR] | renews [date] | opt-out by [date]

Call: RENEW / CONTRACT / CHURN
Dollars: $[low] to $[high], expected $[x]   Confidence: low / medium / high

Decider: [name, role]. Met: yes / no / only through [intermediary]
Mechanism: [3 sentences, cause to effect]

Evidence
- [said / seen / inferred] [fact, source, date]

What would make me wrong
- [strongest evidence against the call]

Play: [action] | Owner: [who] | By: [date]
Need from my side: [exec time, discount authority, roadmap answer, services hours]
Checkpoint: "If [observable thing] has not happened by [date], [escalation]."

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **No decider, no green.** An account where the signer is unknown or unmet cannot be called safe, however good the usage looks. That one fact outranks the rest of the page.
- **Quiet is not healthy.** The accounts with the fewest logged touches are disproportionately risky and disproportionately rated green. Silence from the sponsor while the working team stays engaged usually means the decision moved above the user's line of sight.
- **Requests for data are negotiation prep.** Utilization reports, seat counts, contract copies, invoice history and "what is our notice date" are the buyer starting early, not admin. A downgrade request is lagging: the scope decision was made weeks ago.
- **A champion's optimism is evidence about the champion.** Mark it `said` and name whose mouth it came from.
- **Most at-risk accounts renew smaller, not never.** A binary flag hides contraction, which is where most of the dollars are. Always give a range.
- **Fix the window honestly.** Before an alternative is named, value and relationships can still be repaired. After a replacement is procured, budget is reallocated or the notice date passes, they mostly cannot. Say which side of the line the account is on.
- **Correlated risks are one bet.** Thirty accounts at risk for the same reason is one product or pricing decision. Flag it and suggest renewal-forecast.
- **Do not invent a mechanism.** "Mechanism unknown, find it by [date]" is a legitimate finding. A fabricated chain is not.

## Related (only if installed)

`stakeholder-map` when the decider or the bench is unclear. `renewal-runway` to turn the call into dated actions. `renewal-negotiation` when the read lands on contraction. `champion-loss` when the sponsor has left.
