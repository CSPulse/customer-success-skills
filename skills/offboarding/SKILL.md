---
name: offboarding
description: >
  Runs a departure well: the data handover, the honest exit conversation, and the door left open. Trigger whenever the user says "offboarding", "they are leaving", "we lost the account", "they gave notice", "churn process", "wind down", "transition them off", "they are not renewing", "how do I hand this back", "exit conversation", or names an account and a termination in the same breath. It separates what you owe them contractually from what you owe them professionally, gets the exit interview that nobody asks for, and treats the departing champion as a future pipeline event rather than a closed record. Use renewal-risk while the decision is still open and a save is possible, and churn-postmortem afterwards for the internal analysis of why it happened.
---

# Offboarding

The decision is made. Everything in this skill assumes that, and the single most damaging thing you can do here is keep trying to reverse it.

Three jobs, in order: get their data out cleanly, learn why in a way that is actually true, and leave the relationship in a state that can come back.

The failure this exists to prevent: **the account that goes cold the moment it is marked closed lost.** The last two weeks get no attention, the data export is slow, the final conversation never happens, and a customer who left for a solvable reason becomes a customer who tells people you were fine until you stopped caring.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first, particularly the contract shapes and what customer success owns at the end of a term. Where it is absent, carry on and name the assumption.

**Minimum: the account and the end date.** Enough for the wind-down plan, the questions and the handover.

**Better with** the contract, for notice, data retention and deletion obligations, the final invoice position and any wind-down period you already owe.

**Best with** the account history and the original business case, because the exit conversation is much sharper when you can ask about the specific thing they bought it to do.

---

## Step 0: Confirm it is actually over

Two checks, because running this skill on a live decision costs you the account you could still have kept.

- **Has the decision been made by the person who makes it**, or has one person said something in a meeting? Those are different, and `renewal-risk` handles the second
- **Has it passed the point where the mechanism can still be changed?** After a replacement has been procured, budget reallocated in planning, or the notice date passed, a save attempt is theatre. Before that, it is a live account

If it is genuinely over, stop selling. **Every further attempt to reverse it converts the goodwill you have left into irritation**, and goodwill is the only asset this skill is trying to protect.

---

## Step 1: Do the contractual work first, and do it fast

The part where a bad exit becomes a legal problem or a public complaint. Get it out of the way early so the rest of the relationship is not conducted through it.

- **Notice and dates.** What was served, when the term actually ends, and any wind-down or transition period you owe
- **Their data.** What format, by when, and whether it is complete. This is the single most watched thing in an offboarding and the one most often done slowly
- **Deletion obligations.** What you must delete, by when, and confirming it in writing. Regulated customers will ask, and having it ready is worth a great deal
- **Access and integrations.** What switches off and when, and warning them before anything stops working
- **The final invoice.** Any credits, any unused period, any true-up. An unexpected final invoice undoes every other good thing here

**Be faster than you have to be.** Slow data export is the thing people describe afterwards, more than the product problem that caused them to leave.

## Step 2: Ask for the exit conversation, separately

Ask for it explicitly, framed as what it is: fifteen minutes to understand what happened, with nothing to sell.

**Hold it separately from the commercial wind-down.** Mixed in with invoices and access dates, it reads as a last save attempt and you get polite answers.

The reason to bother: **this is the most honest conversation you will ever have with this customer.** They have no reason left to manage you. Everything they were too polite to say for two years is available for fifteen minutes, and nowhere else in the business can get it.

What to ask, and the phrasing matters:

- **"When did you first start thinking about this?"** Almost always far earlier than your systems show, and the gap is the finding
- **"What did you need that you did not get?"** Rather than what went wrong, which invites a tidy answer
- **"Was there a moment we could have changed it?"** They will name something specific, and it is usually not what you expected
- **"What is the new thing doing that we were not?"** Ask plainly. They will tell you
- **"What did you tell your own leadership about why?"** The internal story, which is often different from the one you were given and is the one that is true

Listen and record. Do not defend, do not correct, do not explain the roadmap. The moment you argue, the conversation ends and you get the polite version for the rest of it.

**Do not badmouth the replacement.** It reads as sour, it makes them defensive about a decision they have to live with, and it is the fastest way to close the door.

## Step 3: Separate the reason given from the mechanism

Whatever they say, the stated reason and the actual mechanism are usually different. Keep them apart in the record.

That analysis belongs in `churn-postmortem`, which is built for it and keeps what was detectable at the time apart from what is only obvious in hindsight. This skill's job is to capture the raw material accurately and hand it over without smoothing it.

**Record it verbatim where you can.** A quote from the exit conversation carries weight internally that a summary never does, and it is the thing most likely to change a product or pricing decision.

## Step 4: Leave the door open, deliberately

The most under-valued part, because it does not pay off this quarter.

- **Champions move.** The person leaving your product today is somewhere else in eighteen months, with a budget and a memory of how this ended. A clean exit is a pipeline event, and the industry knows this without acting on it
- **Say what would have to change** for them to reconsider, honestly, without a pitch attached. If the gap is real and you are not going to close it, say that too. It is more memorable than an assurance
- **Stay in touch as a person**, not as a lapsed record in a system. One genuine message in six months beats an automated win-back sequence
- **Ask for the connection**, not the reference. You are not owed a reference. You may well be owed the relationship

## Step 5: Hand over internally, once

- **Who needs to know**, and before they hear it elsewhere. Support, product where a feature gap drove it, sales where a peer account has the same shape
- **What goes in the record**, including the honest version rather than the sanitised one
- **The correlated question**: how many other accounts have this mechanism. Thirty losses with one cause are one decision, not thirty failures. `churn-postmortem` runs this properly
- **Close it properly in your systems.** A half-closed account distorts every forecast that touches it afterwards

## Step 6: Write the last message

It matters more than the first one, and it is usually written badly or not at all.

Short. Thanks that names something specific rather than the partnership in general. What is done and what is left. A door left open in one line, with no ask attached. Nothing about winning them back.

The test: **would they be glad to hear from you in a year.** If the last message makes that less likely, rewrite it.

`assets/offboarding-checklist.md` carries the wind-down, the questions and the handover in one page.

---

## Output

1. **The Step 0 confirmation** that it is genuinely over, and on what evidence
2. **The wind-down plan**: notice, data, deletion, access, final invoice, with dates and owners
3. **The exit conversation**: asked for, held, and recorded verbatim where possible
4. **The stated reason and the apparent mechanism**, kept separate, handed to `churn-postmortem`
5. **The door-open plan**, including what would have to change and who to stay in touch with
6. **The internal handover**, including the correlated-loss question
7. **The last message**, drafted
8. **What you could not check**

---

## Failure modes

- **Still selling.** Every save attempt after the decision converts goodwill into irritation
- **Slow data export.** The most watched thing in the whole process, and the thing they describe to others
- **A surprise final invoice.** Undoes every other good thing in one email
- **Bundling the exit conversation with the commercial wind-down**, so it reads as a save attempt and you get polite answers
- **Defending during the exit interview.** One correction and you get the tidy version for the rest of it
- **Badmouthing the replacement.** Sour, and it makes them defensive about a decision they now have to live with
- **Accepting the stated reason as the mechanism.** They are usually different, and the difference is the finding
- **Treating the champion as a closed record.** They move, they carry a memory of how this ended, and nobody follows up
- **Sanitising the internal handover.** The honest version is the only one that changes anything
- **No last message**, or one that asks for something

---

## What good looks like

- Their data was out early and complete, and deletion was confirmed in writing
- The exit conversation happened, separately, and was recorded in their words
- Nobody argued during it
- The stated reason and the mechanism are both written down, and marked as different things
- The correlated question was asked
- What would have to change was said honestly, with no pitch attached
- They would be glad to hear from you in a year

---

## Related skills

- `renewal-risk` while the decision is still open, which is the skill to run instead of this one
- `churn-postmortem` afterwards, for the analysis of why and whether it was one of a set
- `stakeholder-map` for who to stay in touch with, and where they go next
- `hard-conversation` where the exit is disputed or a failure caused it
- `email-critic` for the last message

---

## Supporting files

- `assets/offboarding-checklist.md` - wind-down, exit questions and handover on one page
