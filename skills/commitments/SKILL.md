---
name: commitments
description: >
  Use when the user says "commitments ledger", "who promised what", "what did we agree to", "what are they on the hook for", "pull the promises out of this thread", "log the action items from this call". Produces a ledger of every firm promise on both sides (owner, what, due date and how it was derived, quote, status), a separate soft list, the three to close first and a nudge for their most overdue item. Not for the follow-up emails after a call (use call-recap) or a promise handover to a successor (use handoff).
---

# Commitments

A two-sided ledger of what was promised, by whom and by when, from a pasted transcript or thread, so nothing owed slips and nothing owed to you goes unchased.

## Start here

If the user pasted a transcript, thread or notes, go. Also useful: the date of the call or thread, who is who (ours vs theirs), and today's date. If the date is missing, say "dates resolved from today (assumed, confirm)". Otherwise ask for the text and the date in ONE message, then proceed with whatever comes back. If an "Account context" block exists, use it for names.

## Do this

1. **Find the binding sentences.** A firm promise has a named owner, a deliverable and no hedge. Quote the words, under 25.
2. **Sort the rest.** Hedged intent ("I'll try", "let us look at", "we should") goes on a soft list, not the ledger. Requests, deadlines and hopes are not promises: file them as context.
3. **Resolve every date from the call date.** Mark each `stated` or `implied`. Where a relative date has two readings ("next Wednesday"), list both and ask.
4. **Carry in older promises** that were mentioned ("last time you said"). Age runs from the first promise, not the latest restatement.
5. **Set status as of today:** open, due today, overdue (days), done, or blocked by whom.
6. **Pick three to close first** by consequence, not order: due today, then anything others are waiting on, then the overdue promise that gates their goal.
7. **Draft one short nudge** for the most overdue of theirs. Ours become one-line tasks with a date. Drafts only, the user sends.

## Output

```
COMMITMENTS: [Account] | source [call/thread, date] | as of [date]
[n] firm open ([n] ours, [n] theirs) | [n] soft | [n] overdue

| # | Side | Owner | What | Due | Date basis | Quote | Status |

Soft (not counted, watch)
- [who] "[words]" - why it is soft

Not promises
- [constraint, request or hope] - why it is not ours or theirs

Close first
1. [item] - [why now]

Our tasks: [one line each, with date]

Nudge to [name] (re: #[n])
[draft] 
Flag: [anything to verify before sending]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **A maybe is not a promise.** Upgrading "let us look at it" to a ledger line makes the user owe something nobody agreed, and the customer will remember it as agreed.
- **Never record a promise nobody made.** A customer deadline ("finance needs it by the 20th") is their constraint, not our commitment, until someone says "I will".
- **Implied dates get confirmed, not trusted.** Two people hear "next Wednesday" as two different days, and the miss is found only when it is late.
- **Age is a relationship cost.** Count from the first promise. A re-promise resets their clock but not the real one, and a third restatement means something else is going on.
- **Slip out loud.** If an ours item will miss, tell them before the date with a new date, because a quiet miss costs more than a late delivery.
- **Their overdue promise is leverage and a signal.** It often means their priorities moved. Tie the nudge to the goal it blocks and ask what changed before pressing.
- **Product, price, security and legal items are "verify before confirming".** The user checks them, never this ledger, because a confirmed untruth is worse than a late answer.
- **Every count names its measure:** "6 firm open", not "6 items".

## Related (only if installed)

`call-recap` for the emails the call generated. `handoff` to pass the open promises to a successor. `value-ledger` for proof of results.
