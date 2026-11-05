---
name: churn-postmortem
description: >
  Use when the user says "churn postmortem", "why did we lose them", "they did not renew", "post mortem on [account]", "what went wrong with [account]", "lessons learned from the loss". Produces a short written postmortem: the reason given versus the mechanism, the date it was lost versus the date anyone noticed, what was truly detectable then, and one change worth making. Not for an account still alive (use renewal-risk) or for running the exit conversation (use offboarding).
---

# Churn Postmortem

A one-page postmortem that separates what the customer said from what actually caused the loss, and ends in one owned change.

## Start here

If the user gave the account, what the customer said, and roughly what happened, go straight to "Do this". If an "Account context" block exists in the conversation, use its value metric and what healthy usage looks like.

Otherwise ask for these in ONE message, then proceed on memory. A postmortem from memory that says so beats none:

1. Account, ARR lost, date the notice or non-renewal arrived
2. The reason the customer gave, who they gave it to, and when
3. What the user remembers of the last six months: contacts, changes, silences

## Do this

1. **Quote the stated reason, date it, name who heard it, then set it aside.** A reason given to a CSM and one given to an executive are often different reasons.
2. **Build the timeline on the customer's calendar** (their budget cycle, reorganization, fiscal year). Mark two dates: when the loss became effectively irreversible, and when anyone on the user's side noticed. The gap is the finding.
3. **Split signals into two columns:** detectable then (visible to someone looking, not knowing the ending) and obvious only in hindsight. Only the first column produces a change worth making. If nothing was detectable, say so.
4. **Write the mechanism as a causal chain** in three or four sentences, from what happened to non-renewal. If it cannot be built, write "mechanism unknown" and say what would settle it.
5. **Test the stated reason against the mechanism:** match, downstream (true but not the cause), or courtesy. Ask: would they have cut it if the value had been provable?
6. **Name when it stopped being winnable** and what would have had to be true three months before.
7. **Check for a pattern.** How many accounts left with this mechanism in the last year, and do they share a segment, pricing model, cohort or CSM? Then write what changes (owned, dated) and what deliberately does not.

## Output

```
POSTMORTEM: [Account] | [ARR] | lost [date]

Verdict: [one sentence: mechanism, and whether it was preventable]
Stated reason: "[quote]" - [who], [date]
Lost on [date]. Noticed on [date]. Gap: [n weeks].
Mechanism: [3 to 4 sentences, or "unknown"]

Detectable then | Hindsight only
- [signal, date]   | - [observation]

Stated reason versus mechanism: match / downstream / courtesy
Stopped being winnable: [date, event]
Pattern: one of [n] with this mechanism; shared: [segment/etc.]

Changes: [change] | Owner | By
Not changing: [loss accepted, and why]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.
Match its length and specificity: real dates, real counts, no placeholders in the final output.

## Rules

- **A category is not a mechanism.** "Low adoption" is where analysis starts; it does not tell you which of four things to fix.
- **Hindsight is not detection.** If it was only visible knowing the ending, it builds vigilance, not a system, and vigilance does not survive a busy quarter.
- **Laundering is the common sin.** "It was an acquisition" can hide nine months of nobody calling. Ask what the contact history looks like before the event.
- **Do not blame the person who held the account.** It ends honest postmortems for everyone, and the process that let a gap persist is the thing to fix.
- **Thirty losses with one mechanism is one product or pricing decision.** Treating them as thirty cases produces thirty coaching talks and no fix.
- **Not every loss earns a process change.** A customer that went out of business was correctly lost; write that down so the next postmortem is not a performance.
- **Unknown is a legitimate finding.** A fabricated chain produces confident changes to the wrong thing.

## Related (only if installed)


`offboarding` to get the exit conversation while it is still possible. `internal-ask` when the mechanism was a product gap. `coverage-model` when losses share a touch level.
