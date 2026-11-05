---
name: offboarding
description: >
  Use when the user says "offboarding", "they gave notice", "they have decided to leave", "wind down the account", "exit conversation", "data export request", or "how do I handle a clean exit". Produces a confirmation that the decision is final, a dated wind-down table (data, deletion, access, final invoice), five exit questions, the reason-versus-mechanism record, a door-open plan and a drafted last message. Not for saving an account still in play (use renewal-risk) or the internal analysis afterward (use churn-postmortem).
---

# Offboarding

A clean exit: their data out early, an honest account of why, and a relationship that can come back.

## Start here

If the user gave the account, the end date and who made the decision, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, contract end date, and when and how notice was served
2. Who decided, and what they said the reason is
3. Anything the contract says about data return, deletion, and a final invoice

The contract and account history are a bonus. If an "Account context" block exists in the conversation, use it for what the team owns at the end of a term.

## Do this

1. **Confirm it is over.** Was the decision made by the person who makes it, or did one person say something in a meeting? Has the mechanism passed the point of change (replacement chosen, budget moved, notice served)? If not, the verdict is NOT YET and the plan is a risk read, not this.
2. **Do the contractual work first and fast.** List data export (format, scope, date), deletion confirmed in writing, access and integrations switching off with warning, any wind-down period owed, and the final invoice. Each gets a date and an owner.
3. **Ask for the exit conversation separately.** Fifteen minutes, nothing to sell, not mixed with invoices. Prepare the five questions in Rules.
4. **Keep reason and mechanism apart.** Record the reason given and, separately, what you infer actually caused it, with the earliest moment it was detectable. Quote them verbatim where possible and tag each `said`, `seen` or `inferred`.
5. **Plan the open door.** What would have to change for them to reconsider (stated honestly, no pitch), who to stay in touch with as a person, and where the champion is likely to go next.
6. **Hand over internally once.** Who needs to know (support, product, sales on peer accounts), the honest record, and how many other accounts share the mechanism.
7. **Draft the last message.** Short, specific thanks, what is done and what is left, one line leaving the door open, no ask.

## Output

Use this skeleton. Draft only; the user sends anything.

```
OFFBOARDING: [Account] | [ARR] | term ends [date] | notice served [date]

Call: CONFIRMED OVER / NOT YET (reason: [one line])
Stop selling from today.

Wind-down
| Item | Detail | By | Owner |

Exit conversation: ask for [date], with [names]. Questions: [five]
Reason given (said): [verbatim]   Apparent mechanism (inferred): [chain]
Earliest detectable signal: [what, when]. Noticed: [when]

Door open: [what would change] | Stay in touch: [name, how, when]
Internal handover: [who, what] | Others with this mechanism: [n or unknown]

Last message (draft): [5 lines]

What I could not check
- [gap, marked (assumed, confirm) inline]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Stop selling.** Every save attempt after a final decision turns the goodwill you have left into irritation, and goodwill is all you are protecting.
- **Make the data export faster than required.** It is the most watched part of an exit, and people describe slow exports to others long after they forget why they left.
- **No surprise final invoice.** One unexpected charge undoes every other good thing you did.
- **Hold the exit conversation apart from the wind-down.** Mixed with invoices it reads as a last save and you get polite answers. Ask: "when did you first start thinking about this", "what did you need that you did not get", "was there a moment we could have changed it", "what is the new thing doing that we were not", "what did you tell your own leadership about why".
- **Do not defend, correct or badmouth the replacement.** One correction ends the honest part of the conversation, and criticizing their choice makes them defend a decision they have to live with.
- **The reason given is rarely the mechanism.** The gap between when they started thinking about leaving and when your systems noticed is the finding.
- **A departing champion is a future buyer.** People move and remember how an exit felt. One personal message in six months beats an automated win-back sequence.
- **The honest internal record is the only one that changes anything.** Thirty losses with one cause are one product or pricing decision, so ask how many others share this mechanism.

## Related (only if installed)

`churn-postmortem` for the analysis afterward. `renewal-risk` if the decision is still open. `email-critic` for the last message.
