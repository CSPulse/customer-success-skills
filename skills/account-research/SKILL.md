---
name: account-research
description: >
  Archaeology on an account you inherited or are meeting cold: what was sold, by whom, on what promise, what has happened since, and which of it nobody has questioned in two years. Trigger whenever the user says "account research", "I just inherited this account", "brief me on", "what do I need to know about", "first meeting with", "taking over the account", "get me up to speed on", "who are these people", "why did they buy", "what was promised", or names an account they have not worked before. Also trigger before a first call on a transferred book, and when an account's history stops explaining its present. It separates what is documented from what is folklore, finds the original promise the renewal will be judged against, and produces a list of what must be asked because it cannot be found. Use the sales plugin's own research skill when assessing a prospect you have no relationship with; this one is for an account that already exists.
---

# Account Research

This is not fit assessment. The deal is done, the money is spent, and somebody made promises you were not in the room for. The job is finding out what those were before you are held to them.

The failure this exists to prevent: **inheriting an account, reading the CRM, feeling briefed, and discovering in month four that the customer bought it to do something the product has never done.** That commitment is somewhere in an email from last March, and it is what the renewal will be decided on.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: the product, the segments, the contract shapes and the value metric. That is what lets you tell a normal deployment from an odd one here. Where it is absent, carry on and name the assumption.

**Minimum: the account name and whatever you were handed.** Even a CRM record and a contract produce the structure, the questions and an honest list of what is unknown.

**Better with** the original deal notes, the mailbox history, the support record and the contract. Between them they hold the promise, the sceptic and the pattern.

**Best with** the person who sold it or ran it before you, for twenty minutes. That conversation contains things no system holds, and it stops being available the day they leave.

---

## When this runs

An inherited account, a transferred book, a first meeting on an account someone else owned, a re-engagement after months of silence, or any account whose present has stopped being explained by its file.

**Not for a prospect.** The `sales` plugin covers research before a relationship exists, and the frame is opposite: it assesses whether to pursue. This one starts from the fact that they already bought, and asks what they bought and what they were told.

---

## Step 1: Find the original promise

The single highest-value artefact and the one least likely to be in the CRM. Somewhere there is a statement of what this customer would get. A business case, a proposal, a slide, an email answering "can it do X".

Look for it in this order: the original business case or proposal, the signed order form and any statement of work, the email thread around signature, the first onboarding plan, and the sales handover if one exists.

What you are extracting:

- **The outcome they were told they would get**, in the words used at the time
- **Any number attached to it**, and who attached it
- **Any commitment about future capability.** "That is on the roadmap" said in a deal cycle is the most expensive sentence in software, and it is never in the CRM
- **Who said it.** A commitment from a founder is a different object from one made by an SDR

**If you cannot find it, that is a finding, not a gap to move past.** Write "no documented promise" and put it at the top. An account with no recorded reason for existing is at risk in a way no usage number will show, because at renewal nobody on either side can say what it was for.

## Step 2: Separate the record from the folklore

Every inherited account arrives with a story attached. "They are a difficult customer." "They never adopted the second module." "The champion hates us."

For each claim you are handed, ask two questions: **who observed this, and when.** Most of it turns out to be one person's impression from an incident two years and three staff changes ago, repeated until it became a fact.

Mark every item as one of:

- **Documented** - it is written down somewhere you can point at
- **Reported** - a named person told you, recently, and they were there
- **Folklore** - it is in the air with no source, or the source has left

Folklore is not necessarily wrong. It is unverified, and it is dangerous precisely because it shapes how you approach the account before you have met anyone. The most common damage is inherited pessimism: a CSM avoids an account for a year on a reputation nobody can source.

## Step 3: Build the timeline, not the summary

A summary tells you where the account is. A timeline tells you how it got there, and that is what predicts what happens next.

Assemble, with dates:

- Signature, go-live, and how far apart they were. A long gap is usually the first sign of something
- Every contract event since: renewals, expansions, contractions, term changes, price changes
- Personnel changes on both sides, theirs and yours. **Count your own.** An account on its fourth CSM has been taught that nobody stays
- Escalations and major incidents
- The last time anyone from your side had a real conversation with them

Then find the quiet stretch. **Almost every inherited account has a period where nothing happened**, and what happened in that period is usually the answer to whatever question you are asking now.

## Step 4: Work out who is still here

Deal contacts age faster than anything else in the record. Check each name against reality before you rely on it.

- Who signed, and are they still there
- Who championed it, and are they still there and still in the same role
- Who was the sceptic. Deal notes almost always name one and nobody has thought about them since
- Who is new since signature, on their side, and whose predecessor's decisions they inherited

**A new executive above your contact is the single most important thing this step can find**, because they are reviewing everything their predecessor bought and you are on that list.

Where more than a couple of names need working out, `stakeholder-map` does this properly, including whether anyone has actually been met.

## Step 5: Read the usage against the promise, not against a benchmark

You are not asking whether usage is good. You are asking whether it matches what they bought it for.

- Is the thing from Step 1 the thing they actually use
- Which of the sold scope has never been switched on, and does anyone remember why
- Has usage moved with their business or against it
- Where is it concentrated, and is that one team, one person, or one workflow

An account using 40% of what it bought, happily, on the workflow it bought it for, is healthier than one at 90% on something nobody asked for. `health-read` audits the score itself; this step only asks whether the shape matches the story.

## Step 6: Find what nobody has questioned

The most useful output and the one that needs the most deliberate looking. Every inherited account carries assumptions that were true once and have been carried forward unexamined.

- A workaround introduced during onboarding that everyone still uses and nobody remembers is a workaround
- A "not for us" from three years ago on something that shipped since
- A contract term that made sense at the original size
- A reporting cadence nobody reads
- A named contact everyone copies who left the team

These are cheap wins, and more importantly they are the fastest way to demonstrate you are not the fourth person to read the same file.

## Step 7: Write the questions you have to ask

Research ends by naming what could not be found. Split it:

- **Ask your own side.** Whoever sold or ran it, before they leave. Time-limited, so do it first
- **Ask the customer**, in the first conversation, framed as wanting to get it right rather than as ignorance. "I want to check I have understood what you were originally trying to solve" is a strong opening on an inherited account and customers respond to it well
- **Cannot be answered.** Say so and move on

**Do not simulate knowledge you do not have in the first meeting.** The customer knows their own history and can tell instantly. Asking well reads as diligence; pretending reads as the fourth CSM in three years.

---

## Output

A brief someone else could pick up:

1. **The promise**: what they were told they would get, in the original words, with the source and date, or "not documented" stated plainly
2. **The timeline**, with the quiet stretch marked
3. **Who is still here**, and who arrived since
4. **Usage against the promise**, not against a benchmark
5. **Record against folklore**, with every claim marked documented, reported or folklore
6. **What nobody has questioned**
7. **The questions**, split into ask-your-side, ask-the-customer, and unanswerable
8. **What you could not check**

`assets/account-brief.md` is the same structure as a fill-in brief.

---

## Failure modes

- **Reading the CRM and calling it research.** The CRM holds what was recorded, which is rarely what was promised
- **Inheriting the folklore as fact.** Especially the negative kind, which produces a year of avoidance on an unsourced reputation
- **Skipping the handover conversation** with whoever had it before, which expires the day they leave
- **Never finding the original promise**, and discovering it at renewal in an email from last March
- **Trusting the contact list.** Deal contacts age faster than anything else in the file
- **Benchmarking usage** instead of reading it against what they bought it for
- **A summary instead of a timeline.** Where it is now, with no account of how it got there
- **Missing your own churn.** Four CSMs in three years is a fact about your company that the customer has definitely noticed
- **Pretending in the first meeting.** They know their own history and they can tell
- **Research with no questions at the end.** If everything was answered, the research was not thorough

---

## What good looks like

- The original promise is quoted, sourced and dated, or its absence is stated as the headline finding
- Every claim carries a mark: documented, reported or folklore
- The timeline has a quiet stretch and someone has asked what happened in it
- The list of who has left is as complete as the list of who is there
- At least one carried-forward assumption has been found and named
- The first meeting has real questions in it, and none of them pretend
- Someone else could take the account tomorrow from this brief alone

---

## Related skills

- `stakeholder-map` for the relationship picture in depth, once the names are established
- `health-read` for auditing the score rather than reading usage against the promise
- `renewal-risk` once the history is understood and the question becomes what happens next
- `call-prep` for the first conversation this research is preparing
- `account-context` for what normal looks like in this business
- `onboarding-plan` when the research shows the original onboarding never finished

---

## Supporting files

- `assets/account-brief.md` - the fill-in brief, usable without an assistant
