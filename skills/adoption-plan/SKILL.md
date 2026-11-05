---
name: adoption-plan
description: >
  Use when the user says "low adoption", "they are not using it", "usage has stalled", "shelfware", "seats sitting idle", "adoption plan". Produces a diagnosis of why usage is low (evidence tagged said, seen or inferred), the one cohort to move first, a 30 day plan with a pass or fail exit test, and the fallback if the cause is product fit. Not for a new customer still onboarding (use onboarding-plan), the renewal call (use renewal-risk) or an expansion pitch (use expansion-case).
---

# Adoption Plan

Paste the usage you have. Get the cause of low usage, the one group to move first, and a 30 day plan that ends in a test, not a training invite.

## Start here

If the user gave seats bought, seats active and what the product is meant to do for them, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Seats or licenses bought against active, split by team or role if known, and what "active" means in the export (a login, or a real action)
2. What they bought it to do, and who owns that outcome on their side
3. What changed when usage stopped growing (a person left, a launch slipped, nothing known)

A usage export, the contract dates and the renewal date are a bonus. If an "Account context" block exists in the conversation, use it to judge what normal looks like for this product.

## Do this

1. **Pin the measure.** Write "[n] of [n] seats did [action] in [period]". Split breadth (teams and roles with any real use) from depth (frequency and features per user). They are different problems with different fixes.
2. **Diagnose one primary cause.** Choose from: never started, started and stalled, one team only, wrong people licensed, product fit gap, champion gone, integration broken, change-management failure. Load `references/causes.md` for the evidence that separates them. Tag each piece `said`, `seen` or `inferred`. If two fit, name the one question that tells them apart.
3. **Pick the cohort that can move first.** The group with a license, a real need, a manager who cares and one removable blocker. Not the biggest group.
4. **Define success as a behavior with a date.** "By [date], [n] of [n] [role] do [action] at least [n] times a week." Logins are not success.
5. **Plan 30 days by cause.** Week by week, an owner on each side, one ask of the customer per week. Put the exit test before the notice date if that falls inside the 30 days.
6. **Decide the seat conversation.** If paid seats far exceed the realistic cohort, state the right-sized number and raise it yourself, before the notice window.
7. **Write the fallback.** If the cause is product fit, scope down honestly and log the gap instead of planning training for it.

## Output

Use this skeleton. Keep it to one page.

```
ADOPTION READ: [Account] | [ARR] | renews [date] | opt-out by [date]

Call: FIXABLE / PARTLY FIXABLE / FIT PROBLEM / TOO LITTLE DATA
Shape: [n] of [n] seats [action] in [period]. Breadth: [..] Depth: [..]
Cause: [primary], then [secondary or "none seen"]

Evidence
- [said / seen / inferred] [fact, source, date]

Cohort to move first: [who, how many, why them]
Success test: "By [date], [n] of [n] [role] [behavior]."

30 days
| Week | Action | Ours | Theirs | Ask of customer |
Exit test: [date] pass = [..] / partial = [..] / fail = [..]

Seat position: [realistic seats, dollars, who raises it, by when]
Fallback if the cause is fit: [scope, what to log, who to tell]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Count people doing the work, not logins.** A login is the cheapest event to produce, so a reminder email inflates it and the number falls back the next week.
- **"Offer training" fixes one cause in eight.** Training helps people who want to use it and cannot. It does nothing for a missing owner, a broken integration or a product that cannot do the job.
- **Breadth before depth.** Teaching advanced features to a team that never started spends the effort where the least is at stake.
- **Move the cohort with one removable blocker.** A single visible win gives the sponsor a story to tell upward, and other teams follow a team that works. Effort spread over every seat moves none.
- **Raise unused seats yourself.** A vendor who offers to right-size before the customer asks builds trust. The same conversation raised by the customer is a negotiation. A seat count the customer resents gets cut at renewal anyway.
- **A gone champion or a broken integration comes first.** Usage lags a people change by weeks, so the dip is a symptom. Fix the cause (champion-loss, a support ticket with a date) before planning adoption.
- **Check the calendar before calling it stalled.** Seasonal work, a freeze or a migration fakes a stall. Ask what the same month looked like last year (assumed, confirm).
- **Do not plan around a fit gap.** Training on something the product cannot do spends trust, and the sponsor remembers it at renewal.

## Related (only if installed)

`onboarding-plan` when the customer never went live. `champion-loss` when the owner left. `renewal-risk` for what low usage means for the renewal. `internal-ask` to log a fit gap with product.
