---
name: csm-hiring
description: >
  Use when the user says "interview kit for a CSM", "hiring a CSM", "CSM interview questions", "work sample for a CSM candidate", "scorecard for the CSM role", "how do I tell a good CSM from a nice one". Produces a role scorecard, eight structured questions with what strong and weak answers sound like, a 30 minute work sample with a rubric, red flags and a debrief template. Not for onboarding the hire (use csm-ramp) or coaching a current CSM (use coaching).
---

# CSM Hiring

An interview kit a hiring manager can run next week: the same questions for every candidate, a work sample that shows judgement, and a way to decide that does not depend on who liked whom.

## Start here

If the user gave the segment, the book size and the level, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Segment, rough book (accounts and ARR), and whether the hire owns renewals and expansion
2. Level and the experience the user expects
3. What the last strong hire and the last weak one did differently

If an "Account context" block exists in the conversation, use it for the product and the typical customer. Do not ask for anything protected or personal about candidates.

## Do this

1. **Write the scorecard from the outcomes.** Three to five outcomes the hire must deliver in year one (renewals owned, accounts led, quality of reads). Then weight the competencies for this segment. Common defaults, set your own: mid-market leans on prioritization and commercial judgement, enterprise on executive communication.
2. **Choose eight questions.** One per heavy competency, drawn from: commercial judgement, prioritization under load, ownership, hard customer, executive communication, written clarity, data comfort, technical fluency. Write what strong and weak answers sound like, and one probe for "what did you personally do, and what was the dollar figure".
3. **Assign who asks what.** Same questions, same order, every candidate. One interviewer owns each competency, and a second scorer sits in on the panel to calibrate.
4. **Build the work sample.** A fictional messy account of 8 to 10 facts with three planted traps: a signer nobody has met, a date that is not the renewal date, and a number whose measure is unclear. Thirty minutes to write a read, 15 to discuss. Score it against the renewal-risk format.
5. **Write the rubric.** A 1 to 4 scale per competency with a described anchor, a 0 to 2 score per line of the work sample, a hiring bar and the red flags.
6. **Write the debrief.** Scores in writing before anyone speaks, evidence beside each score, then discussion, then the decision and its one reason.

## Output

```
CSM INTERVIEW KIT: [role] | [segment] | [level]
Year-one outcomes: [3 to 5]

Scorecard | competency | why it matters here | weight (points of 100) |
Hiring bar: [no 1 on which competencies; weighted total of at least N]

Questions
[n]. [competency] [question]
   Strong: [what it sounds like]  Weak: [what it sounds like]  Probe: [follow-up]

Who asks what: [rounds, interviewers, second scorer]

Work sample: [brief, traps, time] | Rubric: [lines scored 0 to 2, pass mark]
Red flags: [list]
Debrief: [template]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Judgement and ownership outrank charm.** Relationship skill is the easiest thing to see in an interview and the weakest predictor of whether a book gets run well. A likable CSM who cannot prioritize loses accounts politely.
- **Ask every candidate the same job-related questions.** Different questions make candidates incomparable and let first impressions decide. Stay off age, family, health, origin and other protected topics, and have HR or legal confirm local rules.
- **The work sample is the best signal.** Interview answers are rehearsed, but a messy account shows how someone reads evidence under a clock. Use invented data, never a real customer.
- **Score before you discuss.** The first confident voice anchors the room. Written scores first keep the quiet interviewer's evidence in play.
- **Ask what went wrong, then who did it.** A candidate who cannot name a failure has not owned a book, or cannot see their part in it. Blaming customers is the commonest tell.
- **Listen for dollars.** A candidate who talks only about relationships and never ARR, notice dates or contraction will avoid the commercial half of the role.
- **Probe the "we".** Credit for team outcomes is fine when the candidate can say which part was theirs. If they cannot, they were present, not responsible.
- **Anchor scores to evidence, not to the person.** A 3 means a specific answer met the bar. Write the line they said, so the debrief argues about evidence.

## Related (only if installed)

`renewal-risk` as the format for the work sample rubric. `csm-ramp` for the first 90 days once hired. `coaching` for development after.
