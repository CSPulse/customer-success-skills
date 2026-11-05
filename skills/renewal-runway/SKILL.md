---
name: renewal-runway
description: >
  Use when the user says "renewal runway", "renewal timeline", "when do I start the renewal", "plan backward from the renewal date", "I am late on this renewal", "opt-out date". Builds a dated backward plan from the opt-out date (renewal minus notice) with checkpoints near T-180, T-120, T-90, T-60 and T-30, each with an action, an owner and a pass/fail test, plus a compressed version if the user is already late. Not for judging the account (use renewal-risk) or negotiating terms (use renewal-negotiation).
---

# Renewal Runway

A dated table, pasteable into a calendar or CRM tasks, that works back from the real deadline.

## Start here


If the user gave a renewal date and a notice period (or "no notice"), go straight to "Do this". Use today's date from the conversation. If an "Account context" block exists, use its notice terms.

Otherwise ask for these in ONE message, then proceed with whatever comes back (do not wait for all three):

1. Renewal date and notice or opt-out period (days)
2. ARR and whether it auto-renews
3. Who signs, and whether the user has met them

If notice is unknown, assume 60 days, mark it "(assumed, confirm)" and put it first under What I could not check.

## Do this


1. **Compute the opt-out date:** renewal date minus notice period. This, not the renewal date, is the deadline. Report days left to it.
2. **Set checkpoints** at roughly T-180, T-120, T-90, T-60 and T-30 days before the opt-out date. These are common defaults (a 90 day trigger with 60 and 30 day checkpoints is the most common style in CS playbooks); label them as defaults and let the user move them.
3. **Give each checkpoint** an action, an owner, and a pass/fail exit test that an observer could check ("signer named and a call booked", not "relationship good").
4. **Mark the status of each date:** done, due, or missed. Early on, every renewal should already carry a documented risk status; risk found at 90 days usually existed at 180.
5. **If the user is late, compress.** Merge every missed checkpoint into one "this week" block, ordered: confirm the decider, confirm the notice date, get a meeting on the calendar, then value proof. Drop anything not on the path to the opt-out date.
6. **End with a table** the user can paste: date, checkpoint, action, owner, exit test.
7. **Sanity check the spacing.** If the contract is short (under a year) or the account is large, tell the user to pull checkpoints earlier. If two checkpoints land within a week of each other, merge them.

## Output


```
RENEWAL RUNWAY: [Account] | [ARR] | renews [date] | opt-out [date]

Verdict: [On time / Late by N days]. [N] days to opt-out. Biggest risk to the plan: [one line]

| Date | Checkpoint | Action | Owner | Pass if |
| ...  | T-180 (default) | ... | ... | ... |

If late: this-week block
- [ordered actions, each with a date]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.
Match its length and specificity: real dates, real counts, no placeholders in the final output.

## Rules


- **The opt-out date is the deadline.** Past it, an auto-renew locks in or a silent notice ends the contract; the renewal date only matters if notice was not served.
- **Checkpoints are defaults, not law.** Short or monthly terms need tighter spacing, and a multi-year strategic account may need an earlier start; the user sets their own.
- **Every checkpoint needs a test that can fail.** "Check in with the champion" cannot fail, so it hides the miss until it is too late.
- **Late means compress, not repeat.** Running six weeks of steps in two produces noise; keep only what changes the outcome before the opt-out date.
- **Confirm the notice clause from the contract text.** A notice period remembered wrongly moves the real deadline, and the fix costs a year.
- **Count from the customer's calendar too.** Their budget planning usually closes well before your renewal, so a checkpoint after that point is too late to change the number.
- **Drafts and tasks only.** The user schedules and sends; this skill writes nothing into a calendar or CRM.

## Related (only if installed)


`renewal-risk` to read the account at each checkpoint. `stakeholder-map` when the decider is unknown. `champion-loss` when the sponsor left.
