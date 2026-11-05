---
name: expansion-case
description: >
  Use when the user says "expansion case", "they want to add seats", "second department", "build the business case for", "how do I get budget for", "my champion needs to sell this internally", or "upsell". Produces a verdict on whether to ask yet, then a one-page case written for the champion to carry into a meeting you are not in: the anchor, where the money comes from, three numbers, a first step one person can approve, and pre-answered objections. Not for the review meeting (use business-review) or price haggling (use renewal-negotiation).
---

# Expansion Case

A one-page case the champion can defend alone, in their words, against other requests for the same money.

## Start here

If the user gave the account, the proposed scope and the likely sponsor, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, current scope and value, and what they want to expand into
2. Who would sponsor it, and whose budget it would come from
3. What the first deployment has produced, in the customer's measure

Outcome data, the last review and any leadership quote are a bonus. If an "Account context" block exists in the conversation, use it for the value metric and pricing.

## Do this

1. **Earn the ask.** Can you name what the first deployment produced, in their unit, and would a named person on their side repeat it? If not, the verdict is FIX PHASE ONE FIRST and you stop after one paragraph on what to fix.
2. **Find the anchor.** A problem their leadership already named, quoted with source and date. No anchor means you have a capability and an assumption, not a case. Say so.
3. **Follow the money.** Pick one: an existing line extended, a new ask in the next planning cycle, another department's budget, or displacing something. Name who controls it and whether the user has met them. Work back from their planning deadline, not your quarter.
4. **Write three numbers in their units.** Cost all-in including internal effort, return as they measure it, payback conservatively. Use their realized numbers first. Every estimate carries its basis and is tagged `said`, `seen` or `inferred`.
5. **Size a first step** one person can approve without a committee, that shows a result inside one cycle. State the full picture behind it so nobody feels misled.
6. **Pre-answer the objections** (see Rules) in two lines each.
7. **Write it for the room you will not be in.** Ask in the first three lines, no logo, no tier names, plus the two sentences the champion says out loud. Have them say it back to you and fix where they go vague.

## Output

Use this skeleton. The case itself is written to be forwarded; draft only, the user sends.

```
EXPANSION CASE: [Account] | [scope] | decision needed by [their date]

Verdict: ASK NOW / FIX PHASE ONE FIRST
Anchor: "[their words]" - [who, where, when]
Money: [which of four] | Controlled by: [name, role] | Met: yes / no

THE CASE (carried by [champion] to [budget holder])
Ask: [3 lines, first step, cost, decision date]
Cost $[x] all-in | Return [their unit] | Payback [n months] | First result by [date]
What the first deployment did: [measure, before, now, owner]
Why now / if we do nothing: [in their cost]
First step: [small, one approver] | Full picture: [what comes after]
Questions and answers: [six, two lines each]
Two sentences for the corridor: 1. ... 2. ...

What I could not check
- [gap, marked (assumed, confirm) inline]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Do not ask on a deployment that is not working.** The ask tells the account you are not paying attention and puts the renewal at risk for revenue that was never available.
- **An unanchored case competes with every improvement.** One tied to a problem leadership already named competes with nothing.
- **When the money is another department's, the champion is a route, not the buyer.** Their job is an introduction, so the first action is meeting the budget holder.
- **A case that fits no committee fits no calendar.** If the champion cannot get a yes without a meeting, shrink it until they can.
- **Do not hand a champion optimistic numbers.** They quote them, miss them, and carry the damage. Use ranges with a stated assumption, which survives finance.
- **Show the implementation effort.** The person in the room who has done this before will find it, and the case dies on that discovery.
- **Answer these six in the document:** why now, what if we do nothing, can we do this with what we have (admit the part they can), what did the last purchase deliver, who else does this, what does it cost to stop. Refusing the last reads as a trap.
- **Do not bundle it into the renewal by accident.** One negotiation holding both of your asks usually ends with the expansion paying for a discount.

## Related (only if installed)

`business-review` to establish the value first. `stakeholder-map` if the budget holder is unmet. `renewal-negotiation` if scope and price are being agreed together.
