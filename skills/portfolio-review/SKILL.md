---
name: portfolio-review
description: >
  Use when the user says "portfolio review", "review my team's reads", "everything is green and I do not believe it", "someone is sandbagging", "calibrate my team", "how do I run the forecast call". Reviews the team's reads, not their accounts: draws a sample, tests each read against four questions, spots the tells, and returns a run of show plus the changes to leave with. Not for the forecast number itself (use renewal-forecast) or one-to-one development (use coaching).
---

# Portfolio Review

A review plan that finds which of a team's account reads are not supported by evidence, before they reach a forecast.

## Start here

If the user has pasted the team's reads (account, ARR, call, reason, last contact date), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The reads: account, ARR, the CSM's call (green, likely, at risk) and their reason, ideally with last logged touch.
2. Meeting length and team size.
3. What the user suspects: sandbagging, happy ears, or just "I do not believe it".

If an "Account context" block exists in the conversation, use it to tell a wrong read from an unusual account. Missing last-contact dates go under "What I could not check".

## Do this

1. **Name the meeting.** This one is calibration of reads. Coaching goes to a one-to-one, and fixing a single account goes to a separate, shorter, invited meeting. Say so in the first minute.
2. **Draw the sample by rule.** Exceptions (changed category, at risk, above a value threshold), a random five picked by a stated rule and not by eye (for example alphabetical, every nth from the first), and the quiet ones (longest since a logged touch). Announce that the random five exist.
3. **Test every sampled read on paper.** Four questions in this order: What is the mechanism? Who decides, and when did you last speak to them? Which part is said and which is your inference? What would make you wrong? Mark each read HOLDS, THIN (answers missing) or FAILS (no mechanism or no decider). The gaps become the live questions.
4. **Scan all reads for tells,** not just the sample: share green with no skeptic named, risk with no play, risk that never changes state, reads identical to the health score, green with no logged touch. Then ask whether the system rewards them: what a miss costs versus a wrong green.
5. **Look across the book.** The same mechanism on several reads is one problem. Add the dollars, name an owner, route it to the product or internal-ask path.
6. **Write the run of show** in minutes for the user's meeting length: framing, about three minutes per sampled read, the cross-book pattern, the changes, an audit of last review.
7. **Close on changes.** For each read that moved: from, to, what it needs, owner, date. Add one thing the manager takes on. Check last review's changes happened.

## Output

Lead with how many sampled reads survive. Use this skeleton exactly:

```
PORTFOLIO REVIEW: [team] | [n] reads | $[x] | [minutes] minutes

Verdict: [n] of [m] sampled reads hold on paper ($[x] of $[y] sampled do not).
Meeting: calibration. [One line on where coaching and account fixes go.]

Sample: [rule for the random five]
Account | ARR | Why sampled | Read as written | Result | Ask in the room

Tells: [what was seen, and system or person]
Across the book: [mechanism] | accounts | $ | owner | route
Run of show: [minutes per block]
Changes to leave with: read | from | to | needs | owner | date
Manager takes on: [action]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its shape and length.

## Rules

- **Review reads, not accounts.** One account worked in depth eats the hour, and the other reads go unexamined. Problem-solving moves to its own meeting.
- **Draw the random five by rule.** Exceptions show what the team already knows. A random draw shows what it does not. A hand-picked "random" group is neither.
- **Ask the same four questions in the same order.** A standard feels fair. An interrogation of whoever drew the short straw teaches everyone to write safer reads.
- **Pull green accounts with no logged touch, every time.** They are rated safe because nobody has spoken to them, which is the reverse of evidence.
- **Check the system before the person.** Sandbagging is rational when a miss is punished harder than an inaccurate green, so changing the person changes nothing.
- **Never downgrade a read in front of peers as criticism.** Bad news dries up quickly, and the forecast goes quiet with it. Thank the surfacing separately from the situation.
- **Coaching in front of peers is a performance.** It teaches the room to bring safe reads, so take it to a one-to-one.
- **Take an action off someone's plate.** A review that only examines becomes an exam. The manager's own action should not be zero.

## Related (only if installed)

`renewal-forecast` for the number these reads roll into. `renewal-risk` for the read itself. `coaching` for what the review surfaces about an individual. `book-triage` for what a CSM does with the accounts flagged.
