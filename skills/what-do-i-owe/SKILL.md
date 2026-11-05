---
name: what-do-i-owe
description: >
  Use when the user says "what do I owe", "who is waiting on me", "my inbox is a mess", "what do I need to reply to", "rank my replies", "what am I behind on". Produces a ranked owe list (reply now, today, can wait with a day, no reply needed, waiting on others with a nudge date) plus one draft per thread that needs one. Not for the emails a single call generated (use call-recap) or choosing which accounts get time this week (use book-triage).
---

# What Do I Owe

Paste the unread threads, Slack mentions and open tasks. Get a ranked list of what you owe, who is waiting on you, who owes you, and a draft for each reply that needs one.

## Start here

If the user pasted at least two items (threads, mentions, tasks), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The threads and mentions, with the date and time of the last message in each
2. Open tasks and anything the user promised in writing this week
3. Today's calendar, if the user wants the list fitted around meetings

If an "Account context" block exists in the conversation, use it for ARR and renewal dates. If a mailbox is connected, you may read it. Otherwise work from the paste only.

## Do this

1. **Read each item as a debt.** Who spoke last, what they asked, and when. "Owed" means the customer's last message is unanswered, so state its age ("unanswered 16 hours"). If the user spoke last, the ball is in their court, so it belongs under Waiting on others.
2. **Split promise from request.** "I promised" (a task, a dated line in a sent email) outranks "they asked". Mark each item P or R.
3. **Rank by consequence, then by who is waiting.** Signers, money, a dated deadline and a customer who has already chased go first. Recency and tone do not count. A short note on why each item sits where it does.
4. **Bucket every item once:** Reply now, Reply today, Can wait (name the day), No reply needed, Waiting on others (who, since when, nudge date).
5. **Flag commitment risk.** If a reply would promise a date, price, term, feature or security answer the user has not verified, mark it and say who confirms.
6. **Draft one reply per thread that needs one,** answering the customer's own last message and quoting the line it answers. Never quote an internal message to a customer. Never add a detail that is not in the paste.
7. **Batch the low-stakes replies** into one 15 minute sprint and give it a time. Nudge dates for Waiting on others default to 2 business days after the last message (a common default, set your own).

## Output

Use this skeleton. Drafts go below the list.

```
OWE LIST: [day, time] | [n] items read | [n] need a reply | oldest unanswered: [age]

Reply now
1. [Account] ([ARR]) | [P/R] | [who] waiting, unanswered [age]
   Why here: [signer / money / dated / chased / promise]  Draft: [#]
   Flag: [commitment the user must verify, and who confirms]
Reply today
Can wait
- [item] | by [day]
No reply needed
- [item] | [why]
Waiting on others
- [who] | since [date] ([n] days) | nudge [date]
Sprint: [day, time, 15 min] for [items]

DRAFTS
[#] To: [name]  Re: [subject]
[body, quoting their last line]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **A promise outranks a request.** The user broke their own word if it slips, and the customer remembers a missed promise longer than a slow answer.
- **Rank by who is waiting, not who is loud.** A signer or an AP clerk with a deadline carries more consequence than a long angry thread from someone with no authority.
- **Name the measure on every count.** "9 items" means nothing, "4 customer messages unanswered over 12 hours" can be acted on.
- **A customer who already chased goes up a bucket.** The second ask costs trust the first one did not, so a third is an escalation.
- **Do not reply to everything.** Thanks, FYIs and acknowledgments need no answer, and replying creates a new thread the other side owes back.
- **Do not ack a deadline you cannot meet.** A reply that promises Friday without checking costs more than an honest "I will confirm by Monday".
- **Internal blockers go first when they gate a customer reply.** A two minute answer to a teammate can unblock the customer draft, so sequence by dependency.
- **Never invent a detail.** If the paste has no number, date or name, write "[needed]" in the draft and list it under What I could not check.

## Related (only if installed)

`day-plan` to place the list into today's calendar. `call-recap` for the emails a call created. `email-critic` to check a draft. `renewal-negotiation` when a reply touches price.
