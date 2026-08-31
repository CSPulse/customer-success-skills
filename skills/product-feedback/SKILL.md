---
name: product-feedback
description: >
  Turns customer noise into something the product team will actually act on: the job to be done rather than the requested feature, how many accounts have it, what it is worth, and what happens if nothing changes. Trigger whenever the user says "product feedback", "feature request", "the customer wants", "raise this with product", "log this request", "they are asking for", "submit this to the roadmap", "product gap", "how do I get this built", or forwards a customer request expecting it to reach engineering. Also trigger when the user asks what happened to a request they raised, or says product ignores their input. It separates a request from a bug, a gap and a misunderstanding, refuses to inflate the revenue at stake, and closes the loop back to the customer including on a no. Use internal-escalation when the ask is urgent attention rather than roadmap consideration.
---

# Product Feedback

Product teams do not ignore customer success. They ignore feedback that arrives as a feature name with an account attached and no way to compare it against the forty other things asking for the same quarter.

The failure this exists to prevent: **forwarding a customer email into a channel.** It transfers the request and none of the information that would let anyone act on it, and it puts the translation work on the person least equipped to do it.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: what the product does, the segments and the contract shapes. That is what lets you say whether this is a gap for one segment or for all of them. Where it is absent, carry on and name the assumption.

**Minimum: what the customer asked for and who they are.** Enough to do the translation, size it honestly and write the submission.

**Better with** the other accounts that have raised something similar, the usage data behind the claim, and the contract value of each. Those turn an anecdote into a case.

**Best with** your product team's own intake format and prioritisation criteria, because a submission written in their frame gets read and one written in yours gets triaged.

---

## Step 1: Work out what kind of thing this actually is

A large share of what arrives as a feature request is not one. Sort it before writing anything, because each kind goes somewhere different:

- **A bug.** It is meant to work and does not. This goes to support, today, not onto a roadmap
- **A discoverability problem.** The product does this and the customer could not find it. Extremely common, and submitting it as a feature request wastes everyone's time and quietly tells product their product is worse than it is. Fix it with the customer and record it as a documentation or onboarding gap
- **A misunderstanding of the job.** They asked for X because they think it will produce Y, and it will not. Worth unpicking before it is passed on
- **A genuine gap.** The job is real, the product does not do it, and no reasonable workaround exists
- **A gap with a workaround.** Real, but survivable. Say so, because it changes the priority rather than the validity

Only the last two belong in a product submission, and they are different submissions.

## Step 2: Translate the request back into the job

Customers arrive having already designed a solution. That design is evidence about the problem, not a specification.

Write, in this order:

- **The job.** What they are trying to accomplish, in their words, with no product vocabulary in it
- **What they do today.** The workaround, including the manual steps, the spreadsheet, the person whose week it is
- **What it costs them.** Time, errors, risk, headcount, delay. In their unit
- **What they asked for**, recorded as their proposed solution rather than as the requirement

**Do not propose the solution.** It is not your job, it narrows the design before product has seen the problem, and a submission that leads with a design gets argued about on the design rather than considered on the problem.

## Step 3: Size it honestly, and never inflate

This is the step where customer success spends or earns its credibility with product.

- **How many accounts have this job**, not how many asked for this feature. Two customers asking for different features to solve the same problem are one case, and finding that is most of the value you add
- **The contract value attached**, stated plainly
- **The segment shape.** One enterprise account, or a pattern across mid-market, are different findings with different answers
- **What actually happens if nothing changes**, said honestly

That last one is where credibility is won or lost. **"They will churn over this" is a claim, and it is checkable.** Say it only when you would defend it at the renewal, because the CSM who says it three times and is wrong is ignored on the fourth, permanently and by everyone.

Where the honest answer is "they will be annoyed and renew anyway", write that. A submission that admits the account is not at risk is believed on the one where it is.

## Step 4: Bring evidence, not adjectives

- **Quotes**, dated and attributed by role rather than by name
- **Usage or support data** where it exists: how often the workaround runs, tickets filed, time in the manual step
- **Frequency across accounts**, listed
- **Anything they have already paid for or built** to work around it, which is the strongest signal available and the least often collected

"Strategic", "critical" and "major customer" are not evidence. They are what a submission says when it has none.

## Step 5: Write it in their format

Find out how the product team actually takes input and use that path. A perfect submission in the wrong channel is not a submission.

Ask, once, and record the answer: what fields they want, what counts as evidence, when the prioritisation cycle runs, and who owns the area. Submitting into a cycle that closed last week is why things appear to be ignored.

## Step 6: Close the loop, especially on a no

**The single reason customers stop telling you things.** They raise something, hear nothing, and conclude it went nowhere. They are usually right, and it takes about two rounds.

- **Tell the customer what happened**, including "we are not building this", which is a real answer and is respected far more than silence
- **Give the honest alternative** where one exists: a workaround, a partner, an integration, or the plain statement that this product does not do this
- **Never invent a timeline.** A hedged commitment on a team you cannot bind is how a roadmap conversation becomes a missed commitment. `hard-conversation` covers delivering the no properly
- **Record what you told them and when**, because they will ask again in a year and the answer needs to be consistent

## Step 7: Keep a register you can answer from

One list, per account and per theme: what was raised, when, what evidence went with it, what came back, and what the customer was told.

Two things it buys. You can answer "what happened to my request" without archaeology, which is the question that decides whether they keep telling you. And you can see the theme across accounts, which is the only way the fifth report of the same job becomes a case rather than a fifth anecdote.

---

## Output

1. **The classification**: bug, discoverability, misunderstanding, gap, or gap with a workaround
2. **The job**, in their words, with no product vocabulary
3. **What they do today** and what it costs them, in their unit
4. **The size**: accounts with this job, contract value, segment shape
5. **What happens if nothing changes**, said honestly
6. **The evidence**, quoted and dated
7. **The submission**, in the product team's own format
8. **What the customer will be told**, and when
9. **What you could not check**

`assets/feedback-submission.md` is the same structure as a fill-in submission and register entry.

---

## Failure modes

- **Forwarding the email.** Transfers the request and none of the information
- **Submitting a discoverability problem as a feature request.** Wastes a cycle and misrepresents the product
- **Leading with the customer's proposed solution**, so the discussion happens on the design instead of the problem
- **Counting feature names instead of jobs.** Two requests for the same job look like two problems and are one case
- **Inflating the risk.** The credibility cost is permanent and it is carried by every CSM after you
- **"Strategic" and "critical"** in place of evidence
- **Submitting into the wrong channel or a closed cycle**, then concluding product ignores you
- **Never closing the loop.** Two rounds of silence and the customer stops reporting anything
- **Inventing a timeline** to soften a no, which converts it into a missed commitment later
- **No register**, so the same job arriving for the fifth time still looks like the first

---

## What good looks like

- The submission names a job, not a feature
- The number of accounts is a count of the job, and someone else could verify it
- The churn claim is either absent or one you would defend at the renewal
- Evidence is dated and attributed, and no adjective is doing the work of a number
- It went in through the path product actually uses
- The customer was told what happened, including when the answer was no
- A year later, the register answers what happened without anyone digging

---

## Related skills

- `internal-escalation` when the ask is urgent attention now rather than roadmap consideration
- `hard-conversation` for delivering a roadmap no to the customer properly
- `renewal-risk` when the gap is genuinely part of the renewal decision
- `churn-postmortem` when a product gap was the mechanism of a loss
- `account-research` when the request turns out to be an unhonoured commitment from the original deal

---

## Supporting files

- `assets/feedback-submission.md` - the submission and register entry, usable without an assistant
