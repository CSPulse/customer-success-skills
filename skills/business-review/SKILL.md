---
name: business-review
description: >
  Use when the user says "QBR", "EBR", "should I run a QBR", "prep the business review", "build the review deck", "what should I present to [account]", or "exec review next week". Produces a run-or-send-async verdict, then a slide-by-slide narrative with the decision or ask on slide 1, headline numbers in the customer's language, and a champion pre-brief. Not for deciding if the account will renew (use renewal-risk) or for a 15-minute exec slot (use exec-conversation).
---

# Business Review

A slide-by-slide story for a review that ends in a decision, or a clear call that this account should get a written report instead.

## Start here

If the user gave the account, the meeting date and who will attend, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, review date, and who is invited (is the person who signs coming)
2. The goal the customer stated at purchase or last review
3. Anything open or sore since the last review

Usage data, last deck and ticket history are a bonus. If an "Account context" block exists in the conversation, use it for the value metric and segment.

## Do this

1. **Run the gate first.** Check the "do not run" list in Rules. If any applies, the verdict is SEND ASYNC or DELAY, and you draft the written report outline instead of a deck.
2. **Write the ask and the belief.** One line for what you need the customer to decide, do or fund. One sentence for what they must leave believing. Everything that serves neither goes to the appendix.
3. **Pick 3 or 4 headline numbers in their outcome language**, not yours. Each needs a baseline, a source, the all-in cost on their side, and a conservative attribution stated out loud. Mark each `said`, `seen` or `inferred`. Activity metrics (logins, seats) go to the appendix.
4. **Write the slides as full-sentence headlines.** Slide 1 is the decision or ask. Then their goals restated, progress with the numbers, what is not working (raised by you first), and the recommendation. Three to five themes, one hour, roughly one third presenting.
5. **Shape for the room.** Executive: where we are against your goal, what I recommend, what I need. Champion: ammunition and no surprises. Users: workflow and what is coming.
6. **Pre-brief the champion** about 48 hours ahead: walk through the numbers, ask what they want from the meeting, offer them the slot to present their own result, send a one-page pre-read.
7. **Draft the 24 hour follow-up**: decisions, owners, dates, next meeting booked before anyone left.

## Output

Use this skeleton. Draft only; the user sends anything.

```
BUSINESS REVIEW: [Account] | [date] | [attendees]

Verdict: RUN / SEND ASYNC / DELAY. Reason: [one line]
Ask (slide 1): [decision, action or funding needed]
They leave believing: [one sentence]

Slides (60 min, about 20 presenting)
1. [Headline as a full sentence: the ask] - [minutes]
2. [Headline] - evidence: [number, baseline, source, tag] - [minutes]

Appendix, not presented: [activity data, ticket recap]
Champion pre-brief: [what to walk through, what to ask, who presents]
Raise before they do: [the thing that is not working]
Follow-up draft: [3 lines]

What I could not check
- [gap, marked (assumed, confirm) inline]
```

If the verdict is SEND ASYNC, replace the slides with a written-report outline (the ask, three numbers, one problem, one decision, a reply date) and offer a 15-minute call if they want one. A filled example is in `examples/sample.md`.

## Rules

- **Do not run a review when** there is no value baseline yet (run a success-planning session), an escalation is live (run the repair call), the decision maker will not attend and reaching them was the point, nothing changed since the last one, or the customer skipped the previous two. Cadence is not a reason: a review held to satisfy a calendar spends scarce access and teaches them the format is optional.
- **Send an async report to accounts where a meeting costs more than it returns.** Low contract value, stable operations and a user who never opens the deck are common cases. Ask the customer which they prefer.
- **The ask goes first.** Executives decide in the first five minutes whether to stay engaged, and a meeting with no ask only informs.
- **Activity is not value.** Logins prove the mechanism runs. A finance team forwards only a number it can rebuild: baseline, full cost, stated attribution.
- **When value cannot be measured**, have the champion say it themselves, record executive testimony, net it against their effort, or name the gap and propose instrumentation as the ask. Do not pad with benchmarks.
- **Never surprise the champion in front of their boss.** They stop advocating, and the sponsor you need next year is gone.
- **Do not disguise an expansion pitch as a review.** Customers forgive the ask and punish the disguise.
- **Data without context gets skipped.** Every chart answers "so what, and what do you want me to do".

## Related (only if installed)

`expansion-case` if the review earns an ask for more scope. `one-pager` for the leave-behind. `exec-conversation` for a short executive slot.
