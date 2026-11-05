---
name: csm-ramp
description: >
  Use when the user says "ramp plan for a new CSM", "new CSM starts Monday", "30 60 90 for my new hire", "is my new CSM ramped", "what should my new CSM do in week one", "inherited a book as a new CSM". Produces a week by week ramp the manager runs and the CSM follows: a book split into own, shadow and hold, a manager checklist, and day 30, 60 and 90 checkpoints defined by observable outputs. Not for a customer's first 90 days (use onboarding-plan) or one account's handover (use handoff).
---

# CSM Ramp

A ramp plan for a new CSM and their manager: what to read, who to meet, what to own and when, and how both sides know the CSM is ramped.

## Start here

If the user gave a start date and a rough book (account count, ARR, renewals in the next 90 days), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Start date, and whether the previous owner is still reachable (and for how many hours a week)
2. The book: account count, total ARR, the 10 largest, and every renewal or notice date inside 120 days
3. The CSM's background (new to CS, new to the product, new to the segment) and the manager's weekly time

If an "Account context" block exists in the conversation, use it. Write the plan for the manager to run, and the CSM can follow it.

## Do this

1. **Find the clock before the curriculum.** List every notice date (renewal minus notice period) inside the first 90 days. These accounts cannot wait for the CSM to be ready, so they get a named cover owner.
2. **Split the book three ways.** Own now: small, stable, low-stakes accounts that build reps. Shadow: the 10 largest and any renewing inside 90 days, where the previous owner or manager leads and the CSM co-pilots. Hold: the worst accounts, kept by the manager or previous owner with a dated transfer.
3. **Write the weeks.** Week 1: access, context, the stories of the top accounts, no fires. Weeks 2 to 4: listen. Read the 10 largest histories, shadow calls, meet top customers alongside the previous owner. Weeks 5 to 8: own renewals and write the first account plans. Weeks 9 to 13: lead a QBR and a save conversation with support. Adjust the lengths for book size and complexity.
4. **Set what the CSM may not do yet.** No commitments on price, roadmap, security or dates they cannot verify, until they have checked with the manager or product. Say it in the plan so it reads as a rule, not a doubt.
5. **Build the manager checklist.** The weekly one to one agenda, what gets reviewed (early reads, call recaps, the first plans), and what the manager removes (access, a stuck internal ask, an intro).
6. **Define ramped by outputs.** Calls led, reads written, renewals owned, a plan in place, a recap sent within a day. Date the checkpoints at day 30, 60 and 90, each with a test that can fail and what happens if it does.

## Output

```
RAMP PLAN: [CSM] | starts [date] | book: [n] accounts, [ARR] | ramped by [date] if checkpoints hold

Shape: STANDARD / COMPRESSED / EXTENDED because [book size, complexity, background]
Clock: [accounts with notice dates inside 90 days, who covers each]

Book split
Own now: [n], [ARR] | Shadow: [n], [ARR] | Hold until [date]: [accounts, who, why]

Weeks
| Week | Focus | CSM does | Manager does | Done when |

Rules for the CSM until ramped
- [what not to commit to, who to check with]

Checkpoints
Day 30 [date]: [observable output] | if missed: [response]
Day 60 [date]: ... | Day 90 [date]: ...

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Do not hand over the fires on day one.** The worst accounts need the most judgement and the least tolerance for error, and a new CSM has neither the history nor the relationships. The dated transfer is how they earn it.
- **Week one is context, not customers.** Reading the top account stories first means the first call is informed. A new CSM who meets customers before knowing the history repeats questions the customer already answered.
- **Meet the biggest customers with the previous owner while that is still possible.** A warm introduction transfers trust in minutes. A cold one takes quarters, and the window closes when the previous owner moves on.
- **Ramped is a set of outputs, not a number of days.** Time served says nothing about judgement. Calls led, reads written and renewals owned can be reviewed, so the manager can say yes or not yet.
- **Review early reads before the CSM acts on them.** A first renewal read is where judgement errors show cheaply. Use the same format every time so the manager sees the gaps fast.
- **Listening before committing is a rule, not caution.** A promise made in week three on something the CSM could not verify becomes a first-90-day surprise for the customer and a problem the manager inherits.
- **Plan slack into holiday and leave weeks.** A ramp with every week full slips at the first absence, and the first accounts to drop are the ones nobody was watching.

## Related (only if installed)

`renewal-risk` and `portfolio-review` for the early reads the manager reviews. `handoff` for each inherited account. `account-plan` for the first plans. `coaching` for the weekly one to one.
