---
name: book-triage
description: >
  Use when the user says "triage my book", "which accounts this week", "plan my week", "my book is too big", "who needs me this week", "I cannot cover them all", or pastes an account list. Produces this week's 5 to 8 accounts with what changed and the clock, one deliberately chosen silent account, a not-this-week list with the trigger that pulls each back, and a Monday to Friday shape. Not for the depth read on one account (use renewal-risk) or for designing who gets a CSM (use coverage-model).
---

# Book Triage

Paste the account list. Get this week's short list, the one quiet account to check on purpose, what you are not touching, and how the days run.

## Start here

If the user pasted a list with at least account, ARR and renewal date, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The list: account, ARR, renewal date, notice period
2. Last real contact per account (a human reply or a call, not an automated email)
3. Anything that moved in the last 2 to 4 weeks that the user already knows about

Optional CSV columns if the user wants to paste cleanly: `account, arr, renewal_date, notice_days, last_real_contact, usage_trend_4wk, champion_status, open_commitment, note`. If an "Account context" block exists in the conversation, use it to tell seasonal from real movement.

## Do this

1. **Rank by movement, not state.** For each account ask what changed in the last 2 to 4 weeks: a person, the shape of usage, a commercial request (utilization export, procurement question), support pattern, an event on their side. No change earns a lower rank, not a touch.
2. **Find the binding date.** Notice date (renewal date minus notice period), budget lock, or a dated commitment, whichever comes first. Never the renewal date.
3. **Ask "if I spend four hours here, does anything move?"** Only me / needs someone else (then the action is the 20 minute ask) / decision already made (name it, do not work it) / nothing wrong (leave it).
4. **Pick the silent account on purpose.** Sort by last real contact, take the oldest one not already on the list, and say whether it is quiet because it is fine or because it is being avoided.
5. **Weight by value last.** Value sets depth, not inclusion. Keep the list to 5 to 8 accounts including the silent one. If three accounts are half the ARR, say they carry standing attention outside triage.
6. **Write the not-this-week list.** Each account gets the trigger (a date, an event, a signal) that pulls it back, and a review date.
7. **Shape Monday to Friday.** Anything needing another person goes out Monday. Hardest conversation early. One protected two hour block for the silent account. Leave roughly a fifth of the week unscheduled (a common default, set your own). Friday: 15 minutes on what moved.

## Output

Use this skeleton. Keep it to one page.

```
BOOK TRIAGE: week of [date] | [n] accounts in book | [n] on the list

This week
1. [Account] | [ARR] | binding date [date] | [only me / needs X]
   Changed: [what, said / seen / inferred]
   Do: [action, by day]

Silent account: [Account], last real contact [date]
Why it is quiet: [fine / avoided / unknown]. Do: [action, day]

Nothing can move: [Account] - [why it is decided], instead I will [x]

Not this week
- [Account] | pulled back if [trigger] | review [date]

Shape: Mon [..] | Tue [..] | Wed [..] | Thu [..] | Fri [..]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Movement beats color and size.** Both are static, so the same accounts surface every week and everything else drifts.
- **The notice date is the deadline.** A renewal 90 days out with a 60 day notice period has 30 days left, not 90.
- **Nobody emailing is not the same as nothing wrong.** Whoever wrote loudest correlates with neither risk nor value, and the quiet accounts are disproportionately risky and disproportionately rated green.
- **Name the accounts where nothing can move.** Effort after a replacement is chosen or the notice date has passed feels like work and changes nothing.
- **A fifth of a week unscheduled is not slack, it is absorption.** A week booked solid breaks by Tuesday and the silent account is the first thing dropped.
- **An account on the list three weeks running with nothing moving is a signal about the action,** not the account. Change the action or move it to not-this-week.
- **A tail that is on the not-this-week list every week is a coverage problem.** Say so upward, because absorbing it quietly hides the evidence the model is wrong.
- **Triage weekly.** A quarterly version is a plan and is stale within a fortnight.

## Related (only if installed)

`renewal-risk` for the depth read on any account the list surfaces. `coverage-model` when the same tail is never reachable. `account-plan` for the few accounts that earn a durable plan.
