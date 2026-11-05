---
name: hard-conversation
description: >
  Use when the user says "how do I tell them", "I have to tell the customer", "we missed the date", "I have been putting this off", "they are going to be angry", "how do I break this to". Produces the two opening sentences first, then the concession ladder with a walk-away, a line for each of three reactions, and the same-day written record. Not for an escalation already under way (use escalation) or a meeting whose point is a senior customer executive (use exec-conversation).
---

# Hard Conversation

The two sentences to say first, the limits of what to offer, and the record to send the same day.

## Start here

If the user said what happened and who it affects, go. Otherwise ask in ONE message, then proceed with whatever comes back:

1. What happened (or will happen) and what was promised, ideally in the customer's own written words
2. Who is affected and who knows already
3. What the user can offer without asking anyone

Anything missing becomes "(assumed, confirm)". If an "Account context" block exists in the conversation, use it. For a price change, roadmap no, missed commitment or costly failure, load `references/by-scenario.md` for the one that applies.

## Do this

1. **Decide timing.** Default is today. Wait only for hours, to learn something they will ask at once or to get authority from someone reachable today. Never wait for the fix.
2. **Sort three lists:** what is true (dates, including the unflattering part), what is not known yet and when it will be, and what can be offered and on whose authority.
3. **Write the opening two sentences literally.** Sentence one is the news, plainly. Sentence two is the impact in their terms. Then stop: no preamble, no thanks for the partnership, no "I hope you understand".
4. **Set the ladder:** first offer, second offer and its trigger, what will not be given and the sentence to say instead, and the walk-away.
5. **Write one line for each reaction:** anger, cold, negotiating.
6. **Pick channel and room.** Say it by voice first, then write it. Tell the champion before their boss. Add a colleague only if they change what can be decided, and brief them.
7. **Draft the same-day record** to survive being forwarded.

## Output

```
HARD CONVERSATION: [Account] | [scenario] | tell them by [day, time]

Open with (say these, then stop)
1. [The news.]
2. [What it means for them.]

Concession ladder
First: [offer] (authority: [who, by when])
Second: [offer], only if [trigger]
Will not give: [x]. Say instead: "[sentence]"
Walk-away: [point at which the user stops conceding]

If they react
- Angry: "[names the specific impact, no defense]"
- Cold: "[asks what happens next on their side]"
- Negotiating: "[goes to the ladder, not past it]"

Before the call
- True: [...]  Not yet known: [...] by [date]
- Channel and room: [voice, who, champion told first]

Same-day record (draft)
Subject: [...]
[Short: what is true, what we committed with names and dates, what is open and when they hear. Nothing softer than said aloud.]

What I could not check
- [gap]
```

A filled example (a missed date) is in `examples/sample.md`.

## Rules

- **Say the news in sentence one.** The customer knows by sentence two anyway, and every sentence of runway lowers trust in the delivery.
- **Own exactly the part that is yours.** Under-apologizing reads as indifference. Over-apologizing on a commercial decision tells them your own company was wrong, and the user cannot then hold the position.
- **Apology before explanation, and explanation only when asked.** An explanation first is an excuse, and one offered unasked defends the process nobody asked about.
- **Fix the concessions before the call.** A credit improvised to end an awkward minute becomes the baseline for the next incident.
- **Give the reason once.** Repeating it under pressure invites pushing to see what moves.
- **Silence after the news is correct.** Filling it recreates the runway aloud.
- **Cold is not fine.** The quiet customer has often already decided elsewhere, so ask what happens next on their side.
- **No theory of cause.** A guess offered under pressure is quoted back when the real cause differs.

## Related (only if installed)

`email-critic` to check the record before sending. `exec-conversation` if it escalates above the contact. `renewal-risk` if the account was already in question.
