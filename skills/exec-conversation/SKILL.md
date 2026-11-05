---
name: exec-conversation
description: >
  Use when the user says "I have fifteen minutes with their CFO", "meeting my champion's boss", "exec sponsor meeting", "new VP just joined", "what do I say to a C-level". Produces the first sentence with a number in it, the one ask, two questions only the executive can answer, the champion plan, an eight-minute running order and a five-line follow-up. Not for a QBR (use business-review) or when the point of the meeting is bad news (use hard-conversation).
---

# Exec Conversation

A short script for a senior customer who has no context and will leave early: first sentence, one ask, two questions, follow-up.

## Start here

If the user gave the executive's title and why the meeting exists, go. Otherwise ask in ONE message, then proceed with whatever comes back:

1. Their title, and who set up the meeting (the champion, the user's side, or the executive)
2. What the account has delivered, in any number the customer recognizes
3. What the user needs from this person

Anything missing becomes "(assumed, confirm)". If an "Account context" block exists in the conversation, use it. Ten minutes with the champion beforehand is the best preparation available, so suggest it.

## Do this

1. **Find out why the meeting exists.** The champion arranged it to look good, the user's side arranged it for coverage, the executive asked (something is under review), or a new executive is auditing what a predecessor bought. Each changes what to say.
2. **Name what they are measured on** this year: cost, risk, revenue or time. Translate the account's results into one of those, with a number they would recognize from their own reporting.
3. **Write the first sentence:** the outcome so far in their measure, then the one thing needed from them.
4. **Pick one ask** only they can do (sponsor, unblock, introduce, decide), small enough to answer in the room.
5. **Prepare two questions** only they can answer, and leave one thing in the first sentence incomplete so the question back is one the user is ready for.
6. **Protect the champion.** Agree who says what in advance. Nothing goes to the executive that the champion has not seen.
7. **Plan eight minutes and four,** with a cut line, then draft the five-line follow-up.

## Output

```
EXEC MEETING: [Name, title] | [Account] | [date] | plan for 8 minutes, not 15

Open with: "[Outcome in their measure, with a number. Then the ask.]"
Ask: [one specific request] by [date]

Why this meeting exists: [said / inferred, and who said it]
They are measured on: [cost / risk / revenue / time: the metric] ([said / seen / inferred])

Two questions only they can answer
1. / 2.
Planted: [the gap left in the opening and the answer ready]

Champion plan
- Already seen by [champion]: [what]. Split: champion covers [x], user covers [y]

Running order
8 min: opening and number, ask, question 1, question 2
4 min: opening and ask. Cut line: drop [x] first.

Follow-up (send same day, to them, not through the champion)
1. What we agreed 2. The ask and date 3. What we owe, by when
4. Link or number to check 5. Next step

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **Lead with the conclusion.** The executive decides in 30 seconds whether to give attention or look at their phone, so an agenda or company overview loses them.
- **One ask.** A busy person defers a list and acts on a single request.
- **No ask is also a failure.** Fifteen minutes with nothing requested gives no reason to grant another fifteen.
- **Drop the vendor vocabulary.** Product names, tiers and adoption rates each cost a sentence to explain and are inputs to what they care about, not the thing itself.
- **Plan for eight minutes.** They join late and leave early, so the ask goes before material that could be sent.
- **Never raise anything the champion has not seen,** because a champion surprised in front of their boss stops being one that afternoon.
- **A contradiction with the champion is the most valuable thing said.** Note it exactly and take it away. Resolving it in the room exposes the champion.
- **Finish early.** Handing back minutes to a full calendar is one of the few reliable ways to earn another meeting.

## Related (only if installed)

`call-prep` for the general shape. `stakeholder-map` to check this person is the buyer. `hard-conversation` if the meeting is bad news.
