---
name: churn-postmortem
description: >
  Works out why an account actually left, separating the reason the customer gave from the mechanism that caused it, and checks whether the loss was one of a correlated set. Trigger whenever the user says "churn postmortem", "why did we lose them", "post mortem", "churn analysis", "they did not renew", "we lost the account", "what went wrong with", "lessons learned", or names an account in the past tense. Also trigger when several accounts have been lost for the same stated reason, or before a churn review. It reconstructs the timeline, separates the date the account was lost from the date anyone noticed, identifies the earliest signal that was genuinely detectable at the time rather than obvious in hindsight, and asks whether the loss was winnable and when it stopped being so. Runs on whatever record survives and marks what could not be reconstructed.
---

# Churn Postmortem

The reason a customer gives for leaving is the reason they are willing to say out loud to someone they are leaving. It is polite, it is usually partly true, and it is almost never the mechanism.

"Budget cuts" is what you are told. Whether the budget was cut because the value was never proved is the thing you needed to know.

The failure this exists to prevent: **"it was an acquisition" filed as a cause, concealing nine months of nobody calling.** A postmortem that produces a category rather than a mechanism produces no change.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first, particularly the value metric and what healthy usage looks like. A postmortem without those reaches for usage numbers and misreads them. Where it is absent, carry on and say so.

**Minimum: what the user remembers.** Memory is biased but it is not worthless, and a postmortem written from memory that says so beats one that never happens.

**Better with** the account's email and meeting history, the support record, and whatever the renewal conversation produced in writing.

**Best with** the original business case and the health-score history, which together show whether the account was ever delivering what it was bought for.

---

## Step 1: Record the stated reason, then set it aside

Write down what the customer actually said, in their words, and date it. Note who said it and to whom, because a reason given to a CSM and a reason given to an executive are frequently different reasons.

Then set it aside. It is evidence about the conversation, not yet evidence about the cause. You will come back to it in Step 5 and check whether it survives.

---

## Step 2: Reconstruct the timeline, with two separate dates

Build the sequence of what happened. Then mark two dates that get conflated and should not be:

- **The date the account was actually lost.** When the decision became effectively irreversible. Often a budget planning cycle, a sponsor's departure, or a competitor being selected
- **The date anyone on your side noticed**

**The gap between them is the finding.** A three-week gap is a save that was attempted late. A seven-month gap is a detection problem, and no amount of better save-playing fixes it.

Anchor the timeline on the customer's calendar rather than yours. Their budget cycle, their fiscal year, their reorganisation.

---

## Step 3: Find the earliest genuinely detectable signal

This is where postmortems go wrong, and the discipline matters more than the answer.

Hindsight makes everything look obvious. The question is not "what can we now see was a sign". It is: **what was visible at the time, to someone who was looking, without knowing how it ended?**

Two columns, kept honestly apart:

| Was actually detectable | Only obvious in hindsight |
| :--- | :--- |
| The sponsor stopped replying in March | The tone of the February email |
| A second vendor appeared in a meeting invite | They seemed less enthusiastic |
| Seat count was not renewed at the true-up | Usage was slightly down |

**Only the left column produces a change worth making.** The right column produces vigilance, which is not a system and does not survive a busy quarter.

If nothing was detectable, say so. Some accounts are lost for reasons that never reach you, and recording that honestly is more useful than inventing a signal to feel in control.

---

## Step 4: Write the mechanism as a causal chain

Not a category. A chain, in three or four sentences, from what happened to non-renewal.

Not this: *they churned due to low adoption.*

This: *the ops team that drove most of the usage was cut in January. The remaining team used only the reporting module, which the analytics tool they bought in March already covered. The incoming operations lead had a stated consolidation mandate and we never met her.*

The first is a label. The second tells you which of four different things to fix.

**If the chain cannot be constructed, say the mechanism is unknown.** An unknown mechanism is a legitimate finding. A fabricated one is worse than nothing, because it produces confident changes to the wrong thing.

---

## Step 5: Test the stated reason against the mechanism

Bring back Step 1. Three possibilities:

**They match.** The stated reason was the mechanism. Record it and move on, and note it, because it is less common than it should be.

**The stated reason is downstream.** "Budget cuts" where the budget was cut because no value metric was ever agreed. The stated reason is true and it is not the cause.

**The stated reason is a courtesy.** They did not want the conversation. Common with a sponsor who has moved on, or where the real answer would be personal.

Ask the diagnostic question: **would this account have been cut if the value had been provable?** If no, the mechanism is value realisation regardless of what the exit conversation said.

---

## Step 6: Ask when it stopped being winnable

Not whether. When.

Most churns pass through a point after which no amount of good work would have changed the outcome: a competitor selected, budget reallocated in planning, the notice date passed, the sponsor gone. Name it and date it.

Then the useful question, which is not "could we have saved it" but **"what would have had to be true three months before that date"**. That is where a change lives.

---

## Step 7: Check whether this was one of many

The highest-leverage step, and the one that gets skipped because it takes a portfolio view rather than an account view.

- **How many accounts have been lost with this mechanism in the last year?**
- Do they share a segment, a pricing model, an onboarding cohort, an industry, or a CSM?

Thirty accounts lost for the same mechanism are **one product or pricing decision**, not thirty individual failures. Treating a systemic loss as a series of individual ones produces thirty coaching conversations and no fix.

If this is the first, say so, and note what would make it a pattern worth watching.

---

## Step 8: Write the two lists

Fill `assets/postmortem-template.md`.

**What changes.** Specific, owned, dated. A detection change if the gap in Step 2 was long. A process change if the mechanism recurs. A product or pricing input if Step 7 found correlation.

**What does not change.** Equally important and almost never written. Some losses are correctly accepted: a customer who went out of business, a genuine strategic shift, an account that was never a fit. Writing this down stops a postmortem culture turning every loss into a process change nobody follows.

---

## Output

1. **The stated reason**, quoted and dated
2. **The timeline**, with both dates and the gap between them
3. **The mechanism**, as a causal chain, or the honest statement that it is unknown
4. **Detectable against hindsight**, kept apart
5. **When it stopped being winnable**
6. **Correlation**: one of how many
7. **What changes**, owned and dated, and **what does not**
8. **What could not be reconstructed**

---

## Failure modes

- **Producing a category.** "Low adoption" is where the analysis should start, not where it ends
- **Hindsight dressed as detection.** If it was only visible knowing the ending, it is not a signal
- **Laundering.** Attributing to an external event what nine months of neglect caused
- **Blaming the person who held the account**, which reliably ends honest postmortems for everyone
- **Skipping the correlation check** and fixing thirty times what should be fixed once
- **Every loss producing a process change.** A postmortem that always finds a fix is not analysing, it is performing
- **Never writing the postmortem** because the account is gone and it feels like archaeology. The account is gone. The mechanism is still running

---

## What good looks like

- The mechanism is specific enough to be wrong
- Detectable and hindsight are visibly separated
- The gap between losing and noticing has a number
- The correlation question got asked
- Something changes, and something is explicitly left alone
- The person who held the account would still be willing to write the next one

---

## Reference files

- `assets/postmortem-template.md` - the postmortem to fill
