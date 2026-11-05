---
name: champion-loss
description: >
  Use when the user says "my champion left", "sponsor left", "our contact changed roles", "my sponsor went dark", "new owner on the account", "they deactivated their account". Produces a 10 day plan (confirm, find the replacement and the real decider, reach each stakeholder, re-establish value per role, re-multithread, tie to the renewal clock) plus three short draft messages. Not for mapping a healthy account (use stakeholder-map) or the renewal call (use renewal-risk).
---

# Champion Loss

A first-10-days plan and three drafts for the moment the person who carried the account is gone, leaving, or quiet.

## Start here

If the user gave the account, who left or went quiet, and the renewal date, go straight to "Do this". If an "Account context" block exists in the conversation, use it for who signs and notice terms.

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, ARR, renewal date and notice period
2. Who left, went quiet or changed roles, how the user found out, and what they owned
3. Anyone else the user knows there, and who might replace them

Missing facts become "(assumed, confirm)" lines, never a reason to stop.

## Do this

1. **Confirm what happened, tag it.** Left, changed role, on leave, or just quiet? Tag `seen` (job-change alert, bounced email, deactivated account, usage drop) or `said`. Do not announce a departure on a rumor.
2. **Find the replacement and the real decider.** They are often different people. Ask the working team, not just management. If the decider cannot be named, that is the first finding.
3. **Reach each stakeholder with a message framed so they can answer either way** (a yes, a no or "not me, try X" all give the user information). Never ask them to confirm they are happy.
4. **Re-establish value per role.** What each person cares about, in the outcome terms of the original business case, not product features. The new owner has not seen why this was bought; do not assume they will find out.
5. **Re-multithread.** Aim for at least three relationships across two functions, learned from daily users first. Write down who each new contact is and what they own.
6. **Tie it to the clock.** Opt-out date = renewal minus notice. State days left to that date, and what must be true by day 10.
7. **Write the response down** (who, what was sent, what came back) so the next handoff does not lose it.

## Output

```
CHAMPION LOSS: [Account] | [ARR] | renews [date] | opt-out by [date]

Verdict: [Recoverable / at risk / likely lost] because [one sentence]
Status: [left / moved / quiet] - [seen/said] [source, date]
Decider: [name or "unknown"]. Replacement: [name or "unknown"]. Met: yes / no

Days 1 to 10
| Day | Action | Owner | Done when |

Drafts (you send)
1. To [their boss / remaining user]: [subject + 4 lines max]
2. To [new owner]: [subject + 4 lines max]
3. To [quiet contact]: [subject + 3 lines max]

Checkpoint: "If [observable] has not happened by day 10, [escalation]."

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length.

## Rules

- **Detect early.** Job-change alerts, a usage drop from one person, a deactivated account or an unanswered email are all signals; waiting for confirmation from the champion costs weeks of the clock.
- **Reach the replacement before they form a view.** A new owner reviews what the predecessor bought, and the first story they hear from someone else sticks.
- **The lost champion's optimism does not transfer.** Their enthusiasm was theirs; treat the account as unproven with the new owner until someone there says why it matters.
- **Frame every message so no answer is bad news.** "Not the right person" is useful; silence after "are you happy with us" is not.
- **Learn the new decider from daily users.** They know who really signs and what the new owner is being measured on, and they have no reason to guard it.
- **Do not forward the exit story as fact.** Hearing that someone left "on bad terms" is rumor until seen; repeating it to the new owner damages the user.
- **Never send, never post.** Drafts only. The user checks tone and facts, especially anything about the product, price or contract.

## Related (only if installed)


`stakeholder-map` to rebuild the bench. `renewal-runway` to date the weeks left. `renewal-risk` for the call once the picture is clear.
