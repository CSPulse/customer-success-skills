---
name: usage-email
description: >
  Use when the user says "usage email", "monthly usage email", "send them their numbers", "usage recap for my champion", "how are they using it this month", "turn these usage numbers into an email". Produces a draft under 150 words to the champion: month against month, the people worth thanking, unused seats framed as an offer, one recommendation, one ask, plus internal notes on what was left out. Not for the quarterly review (use business-review) or a plan for low usage (use adoption-plan).
---

# Usage Email

A monthly note to the champion, drafted from pasted usage numbers, that they can forward without editing. Draft only, the user sends.

## Start here

If the user pasted this month and last month (active users, actions or logins, seats bought), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. This month against last: active users, total actions, seats bought
2. The top three users, anyone who went quiet, any team with no use at all
3. The champion's name, and one line of how the user writes (or "write plainly")

If an "Account context" block exists in the conversation, use it to judge what normal looks like for this account.

## Do this

1. **Fix the measure.** Write down what "active" means (a common default: at least one action in the month). Compare like with like: same definition, same scope, and per working day if the months differ in length. If unknown, mark "(assumed, confirm)".
2. **Call the month:** up, flat, down or mixed. With a small seat count a swing of a few users is noise (a common default: under about a tenth either way, set your own). Say which it is.
3. **Find the people story.** Who deserves thanks, and which team has not started. If the paste holds no outcome, do not invent one: thank the activity and ask for the outcome.
4. **Choose one recommendation and one ask.** The recommendation is one team, feature or habit the numbers support. The ask is one person, one time, one date. Cut everything else.
5. **Keep quiet users and unused seats in aggregate.** Counts and an offer to help, no names, no per-person figures. Names go only in the internal notes.
6. **Draft in under 150 words** in the user's voice. Subject carries the outcome. Headline first, ask last.
7. **Write the internal notes:** what was left out and why, what to confirm, and what to look at next month.

## Output

```
USAGE EMAIL: [Account] | [Month] | to [champion] | send by [day, date]
Month: UP / FLAT / DOWN / MIXED - [one line, with the measure]

Subject: [outcome, with a number]

[draft, under 150 words]

Internal notes (not in the email)
- Left out on purpose: [names, counts, why]
- Confirm before sending: [definition of active, any claim]
- Next month watch: [one thing]

What I could not check
- [gap]
```

A filled example, with a bad-month variant, is in `examples/sample.md`.

## Rules

- **Lead with their outcome and their people.** The champion forwards what makes their team look good, and a number about the tool is read once and dropped.
- **Thank named users for what they did, never rank the rest.** A leaderboard shames everyone below it in front of their boss, and the champion will stop sharing data if it embarrasses a colleague.
- **Unused seats are an offer to help, never a scolding.** Raised first by the vendor it builds trust, and raised as a count with no plan it reads as a revenue push before renewal.
- **One recommendation, one ask.** A second ask halves the chance of the first being answered, because the champion has one spare minute, not two.
- **If usage is bad, say so plainly and bring a plan.** The champion will be asked about it internally, and spin gets found out and spends the credibility the user needs for the renewal.
- **Never explain a movement you did not observe.** "Because of the new release" is a causal claim, and a wrong one tells the champion the vendor is guessing. Say what changed, then ask what they think drove it.
- **Say when the numbers are partial.** A missing team or a half month reads as a drop, and a champion who repeats it upward is repeating an error.
- **Counts name their measure.** "41 active users" without the definition cannot be defended when someone in finance asks.

## Related (only if installed)

`adoption-plan` when two bad months in a row point at a cause. `business-review` for the quarterly version. `email-critic` to check the draft before it goes.
