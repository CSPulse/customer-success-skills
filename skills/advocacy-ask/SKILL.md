---
name: advocacy-ask
description: >
  Use when the user says "reference call", "case study", "testimonial", "sales wants a reference", "can we use them as a logo", "who can we ask for a review", "G2 review". Decides whether to ask this customer for advocacy now, who to ask, the smallest ask that does the job, what you owe back, and the register line. Not for proving the value that justifies the ask (use business-review) or trading a reference in a negotiation (use renewal-negotiation).
---

# Advocacy Ask

The user walks away with a call (ask now, wait, or do not ask), the person, one small bounded ask, and what goes back the other way.

## Start here

If the user gave an account and what is being asked for (a call, a quote, a case study), go. Otherwise ask in ONE message:

1. Account, renewal date, and anything open or broken for them
2. What was asked for, by whom (often sales), and for which prospect
3. What the customer has said worked, in their words

Never wait. If an "Account context" block exists in the conversation, use it.
Gaps become "(assumed, confirm)" and are listed under What I could not check.

## Do this

1. **Run the four disqualifiers.** Any one means not yet: an open escalation or unmet commitment, no value the customer would state themselves, a renewal or negotiation inside the next quarter (a common default, set your own), or recent asks from any team.
2. **Find the moment.** A time they said out loud that something worked: a finished rollout, their own results in a review, a well-handled escalation. Quote it back, dated.
3. **Pick the person who benefited, not the signer.** Match the prospect's industry, size and problem. Check they are allowed to speak publicly (regulated, listed, government, mid-acquisition).
4. **Choose the smallest rung that does the job**: peer-site review, a quote they approve, one bounded reference call, named case study, speaking slot. Word it as a specific, time-boxed ask answerable in one line.
5. **Surface the approval path before drafting**: who signs off (marketing, comms, legal, their manager) and what a forwardable note for them would need.
6. **Name what they get**: peer access, their own visibility, influence on the product, or something already owed. Never a discount.
7. **Write the register line**: asked by whom, for what, when, consent scope, expiry.

## Output

```
ADVOCACY READ: [Account] | renews [date]

Call: ASK NOW / WAIT UNTIL [date or event] / DO NOT ASK
Because: [the deciding fact in one sentence]

Disqualifiers: escalation [y/n] | stated value [y/n] | renewal near [y/n] | recent asks [y/n]
Moment: "[their words]" ([said / seen], [date])
Person: [name, role], why them. Can speak publicly: [yes / no / unknown]
Ask: [rung] - [specific, bounded ask] | Prospect: [who]
Approval path: [who signs off, what they need]
What they get: [item] | Owner: [who] | By: [date]
Draft: [the message, 4 to 6 lines]
Register: asked by [x] on [date] for [y]; consent for this use only; expires [date]

What I could not check
- [gap]
```

On WAIT, name the event that unlocks the ask. On DO NOT ASK, give the user one line to tell sales.

A filled example is in `examples/sample.md`.

## Rules

- **Never ask at renewal.** Timing turns a favor into a trade, and the customer learns a reference has leverage value.
- **An open problem outranks a good moment.** Asking while something of theirs is broken is remembered longer than the problem.
- **The signer writes vendor-management prose.** The person who got their evenings back means it, so convinces; a lukewarm specific match beats an enthusiastic generic one.
- **Small and bounded gets a yes.** "Would you be a reference" has no honest yes; "one 30-minute call in the next two weeks" does. Sales asks for the largest rung by default, and a case study pulls in their comms and legal teams.
- **Approval kills case studies late.** It surfaces after hours of drafting unless you ask on day one.
- **Consent is per use.** A yes last quarter is not standing permission, and learning they were reused from the prospect ends the advocate.
- **One register across all teams.** Sales, marketing and support each ask the same three friendly accounts, and the customer sees one company asking eleven times.
- **A no is data.** Ask why once, gently; a happy customer declining often signals a problem you did not know about.

## Related (only if installed)

`business-review` to establish the value first. `stakeholder-map` to find who benefited. `one-pager` for the note their comms team forwards.
