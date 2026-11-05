---
name: escalation
description: >
  Use when the user says "their VP is involved", "the account is on fire", "angry customer escalation", "they are threatening to churn", "they want a call today", "this has gone to their exec". Produces, from a one-line description, the holding statement to send within the hour, a forwardable answer for the contact's boss, the internal ask, a severity and update cadence, and a second-pass repair plan. Not for bad news not yet delivered (use hard-conversation) or an account that has already left.
---

# Escalation

The first message to send within the hour, written from one line, then the pieces that keep the relationship intact once the incident is fixed.

## Start here

If the user gave one line (what happened, who is angry), go. Do not wait for the cause. Otherwise ask in ONE message, then proceed with whatever comes back:

1. What happened and what it cost them, in their terms
2. Who is escalating, and who they answer to
3. What the user can commit alone

Anything missing becomes "(assumed, confirm)". If an "Account context" block exists in the conversation, use it. Drafts only: the user sends.

## Do this

1. **Type it:** failure (something broke), relationship (frustration found a trigger) or commercial (the destination is a negotiation). Ask "what specifically has to be true for this to be resolved?" A crisp answer means failure, a list or vague answer means relationship, an answer about terms means commercial.
2. **Draft the holding statement:** their specific impact, what is known and not known, a named owner, the next update time. No theory of cause, no apology for what is not established, no fix date that cannot be held.
3. **Draft the forwardable answer** for the contact's boss: standalone, facts and impact, what is being done, owner, next update. No internal shorthand, no blame, no liability wording.
4. **Draft the internal ask** in business terms: impact, revenue at stake, what is committed, what is needed, by when. Decide whether to pull in an executive and write their brief.
5. **Set severity and cadence,** one owner and one channel. Hold the cadence even with nothing new.
6. **Repair plan, second pass,** once the incident closes: root cause in writing when known, what it cost them, one repair commitment met visibly, the new people met, and an executive sponsor if this is a repeat.

## Output

```
ESCALATION: [Account] | [failure / relationship / commercial] | Severity [S1-S3]: update every [n] hours until [condition]

1. HOLDING STATEMENT (send within the hour)
[Draft to the contact.]

2. FORWARDABLE ANSWER for [contact's boss]
[Draft they can pass on unedited.]

3. INTERNAL ASK to [name or role]
[Impact, revenue at stake, committed, needed, by when.]
Pull in: [who, when, brief: facts / unknown / committed / must not be promised / what they want]

4. OWNER AND CHANNEL
Owner: [one named person]. Channel: [one]. Facts kept in: [one place]

5. REPAIR PLAN (second pass, after the incident closes)
- Root cause in writing by [date]  - Ask what it cost them
- Repair commitment: [specific, theirs] by [date]  - New people met: [...]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **Silence is the failure.** Customers fill gaps with the worst explanation, so "no change, next update at four" is worth sending.
- **Severity sets the cadence.** A common default, set your own: S1 (core work stopped or their exec involved) every 2 hours, S2 (degraded) every 4, S3 daily.
- **The contact usually needs cover, not just a fix.** They are exposed in front of their boss, so the forwardable answer is often the most useful thing sent.
- **One owner, one version of the facts.** Three people replying in parallel produce three versions, and every difference reads as evasion.
- **Hold the executive card.** Use it when theirs is involved, the need is above the user's authority, or the relationship is the problem. An unbriefed executive commits things nobody can unpick.
- **No theory of cause.** A guess is quoted back when the real cause differs, so write the root cause only when known.
- **A relationship escalation treated as a failure fix returns.** The fix lands, the cause is untouched, and the account leaves later.
- **Repeat escalations get an executive sponsor,** because the pattern is the problem, not the incident.
- **Quiet after resolution is not relief.** It is sometimes the decision being made elsewhere.

## Related (only if installed)

`internal-ask` for the internal ask. `exec-conversation` if their executive joins. `stakeholder-map` for the people surfaced. `renewal-risk` afterwards.
