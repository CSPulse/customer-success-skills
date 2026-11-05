---
name: customer-update
description: >
  Use when the user says "customer update", "notify customers", "announcement to customers", "end of life notice", "maintenance window", "outage notice", "tell them about the delay", or has news that must reach a list of customers. Segments the list by impact and drafts the broadcast, subject line first, with a personal note for the badly affected. Not for bad news to one account in a live conversation (use hard-conversation) or an account already on fire (use escalation).
---

# Customer Update

The user walks away with a segmented send plan and a broadcast that tells each reader in two lines whether it affects them and whether to act.

## Start here

If the user has said what is changing, when, and roughly who it touches, go. Otherwise ask in ONE message:

1. What is changing, and the date
2. Which customers it touches and how many (a rough split is fine)
3. Anything contractual: notice period, credits, security or legal review

This skill is a written broadcast to a list. If the news is for one account and will be spoken live, say hard-conversation fits better (if installed) and draft only the written record.

Never wait. If an "Account context" block exists in the conversation, use its segments. Gaps become "(assumed, confirm)".

## Do this

1. **Segment by impact, not by mailing list.** Materially affected (named contact, a call before the notice), affected but no action (one clear line), not affected (usually do not write). Large accounts hear from a person before the broadcast goes.
2. **Write the subject line first and make it the news**, with the date: "Scheduled maintenance, 12 Mar, 30 minutes". No urgency the content does not carry.
3. **Lead with three lines**: what changes and when, what it means for them, what they must do. If nothing, write "No action is needed from you."
4. **Split known from unknown.** Confirmed, expected, and when the next update lands. State no cause until it is established.
5. **Make it survive a forward** to an executive, a security team or a lawyer: no internal shorthand, no blame, no liability wording, one topic only.
6. **Set the reply plan**: one owner, a response window, and the two or three questions you already expect.
7. **Pick the order of sends**: named accounts first, then the broadcast, then a reminder near the date if one applies. Load `references/by-update-type.md` for incident, delay, deprecation, pricing, maintenance or CSM-change specifics.

## Output

```
SEND PLAN: [what is changing] | [date] | [n] customers

Segments
- Materially affected ([n]): [who], channel: [person/call first]
- Affected, no action ([n]): [channel]
- Not affected ([n]): [no message / status page only]

Subject: [the news, with the date]

[Three opening lines]
[Detail, then contact, then timeline]

Confirmed: ... | Expected: ... | Next update: [date, only if you will send it]

Reply plan: owner [x], window [y], expected questions: [...]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **One message to the whole list fails twice.** It buries the few badly hit in general reassurance and alarms everyone else about something that is not theirs.
- **"No action is needed" is load-bearing.** Its absence reads as an ask and produces tickets from people checking whether they are safe.
- **A next-update date is a promise.** Only give one you will keep, even if the update says nothing has changed; missing your own date does more damage than the original problem.
- **No cause before it is established.** A guessed cause in writing is quoted back when the real one differs.
- **No credits or concessions in a broadcast.** It turns a service event into a commercial event across the whole base at once. Decide the offer before the reply thread.
- **Do not apologize for a decision, only for harm.** Apologizing for a price or packaging change tells them your company thinks it was wrong. Say what changes and what does not.
- **A CSM change is a relationship event.** Named accounts hear it from a person first, ideally the outgoing CSM, with a named replacement and what carries over.
- **Brief support before it sends.** Replies arrive within the hour, and an unanswered reply is worse than no update.

## Related (only if installed)

`email-critic` on the draft. `hard-conversation` for a named account. `handoff` for the internal side of a CSM change. `one-pager` for a forwardable summary.
