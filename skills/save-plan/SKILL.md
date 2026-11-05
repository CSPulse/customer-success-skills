---
name: save-plan
description: >
  Use when the user says "save plan", "save this account", "can we still save them", "30 day rescue", "they are leaning toward leaving", "turnaround plan for". Produces a window verdict (launch a save or manage the exit), then a mechanism-matched 30 day plan by week, the executive sponsor, asks, a day 15 go or no-go and the contraction you would accept in advance. Not for judging whether they will renew (use renewal-risk), a customer who already gave notice (use offboarding) or a live angry escalation (use escalation).
---

# Save Plan

Turn an at-risk read into a 30 day plan with one owner, a checkpoint that can fail, and a landing you chose before the pressure started.

## Start here

If the user gave the account, ARR, renewal and notice dates, and what is going wrong, go straight to "Do this". A renewal-risk read already in the conversation counts.

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, ARR, renewal date, notice date, and what the user has been told by whom
2. Who decides and whether the user has met them
3. What the user's company can offer: executive time, price or term room, services hours

Usage, emails and the contract are a bonus. If an "Account context" block exists in the conversation, use it.

## Do this

1. **Decide if there is a window.** Any one of these closes it: the decider has said no, the notice date has passed, a replacement is procured, the budget is reallocated. Closed means do not launch; manage the exit. Narrow means count the working days left and say so.
2. **Name the mechanism and match the play.** Budget cut, failed rollout, sponsor lost or reorganized, competitor, price, service failure, product gap. Load `references/plays.md`. If the mechanism is unknown, week 1 is finding it.
3. **Set the people.** One owner on the user's side. An executive sponsor at the level of their decider. The decider on their side, met in week 1, not only the champion.
4. **Put the fix and one proof first, the price last.** One result in the decider's own measure, in writing, within two weeks. Commercial options come after, as trades.
5. **Pre-decide the landing.** The contraction, term and add-back right the user would accept, and the floor below which they let it go. Get finance authority before the first call.
6. **Write it by week** with the ask of the customer each week, the asks of the user's own company (name, action, date), and a day 15 checkpoint with a stated consequence if it fails.
7. **Log it** where the next owner will read it: window, mechanism, owner, floor, checkpoint.

## Output

Use this skeleton. Keep it to one page.

```
SAVE PLAN: [Account] | [ARR] | renews [date] | opt-out by [date]

Window: OPEN / NARROW / CLOSED (manage the exit)
Why: [the facts, said / seen / inferred]. Working days left: [n]
Mechanism: [3 sentences, cause to effect]. Play: [name]
Dollars: save at $[x]. Accept down to $[floor] if [terms]. Below that, let go.

People: Owner [name] | Our exec [name] | Their decider [name], met yes / no

| Week | Action | Owner | Ask of customer | Date |

Asks of my company: [name, action, by when]
Day 15 checkpoint ([date]): "If [observable] has not happened, [switch to fallback]."
Fallback (graceful landing): [contraction, terms, door-open step]
Log: [where the plan is recorded]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **No window, no plan.** A save launched after a replacement is bought wastes a month and spends the goodwill a clean exit or a later win-back needs.
- **Match the play to the mechanism.** A discount does not fix a failed rollout and training does not fix a cut budget. The wrong play feels busy and changes nothing.
- **Fix before price.** Opening with a discount teaches the customer that threatening to leave works, and it answers none of their reasons.
- **Protect the relationship with the decider, not only the champion.** A champion can be reorganized away overnight, and the signer is the one who reads the renewal.
- **One owner.** A plan owned by three people has nobody holding the day 15 checkpoint.
- **The day 15 checkpoint must be able to fail.** Half the runway is gone by then, and a test that cannot fail turns the plan into ritual while the notice date closes.
- **Choose the contraction in advance.** Under pressure people concede whatever is asked. A floor decided beforehand makes a smaller account that renews a win, not a failure.
- **Never trade the unverified.** Roadmap dates, price and security terms come from the user's company, not from this page. Flag them before they reach a draft.

## Related (only if installed)

`renewal-risk` for the read this plan starts from. `stakeholder-map` when the decider is unclear. `renewal-negotiation` for the commercial rungs. `offboarding` when the window is closed. `adoption-plan` when the mechanism is low usage.
