---
name: coverage-model
description: >
  Designs who gets a named CSM, who gets pooled, who gets digital only, and states what breaks at each line. Trigger whenever the user says "coverage model", "segmentation", "touch model", "CSM ratio", "how many accounts per CSM", "high touch low touch", "tech touch", "digital CS", "scaled CS", "pooled model", "we cannot cover the long tail", "do we need more headcount", or is designing or defending how a team is deployed across a book. It segments by what accounts need rather than only by what they pay, treats the ratio as an output rather than an input, names what each tier will not get, and tests the model against the accounts that actually churned. Use book-triage for working inside a coverage model that already exists, and renewal-forecast for what the model implies about the number.
---

# Coverage Model

A coverage model is a set of decisions about **who you are choosing not to serve properly**, and the reason most of them fail is that this is never said out loud. The tiers get named, the ratio gets set, and the part where the bottom forty per cent of accounts receive nothing is left implicit until it shows up as churn nobody predicted.

The failure this exists to prevent: **the model designed backwards from headcount.** Take the number of CSMs, divide by the number of accounts, call the result a ratio, and describe whatever that produces as a strategy.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: segments, contract shapes, motion and what healthy usage looks like. That is the raw material for segmentation. Where it is absent, carry on and name the assumption.

**Minimum: the account list with values, and your headcount.** Enough for a first model with the trade-offs stated.

**Better with** churn history by segment, product usage data, and support load per account, which is the cost side nobody counts.

**Best with** the last two years of churn including the reason and the segment, because a coverage model that would not have caught your actual losses is a plausible model rather than a working one.

---

## Step 1: Segment by need, not only by revenue

Revenue-only tiering is the default and it is wrong in a specific, expensive way: it puts a simple two-hundred-thousand-dollar account and a complex, high-risk, three-department fifty-thousand-dollar account in the wrong places.

Segment on three axes and then decide:

- **Value.** Contract value and its trajectory
- **Complexity.** Integrations, number of business units, regulatory exposure, how bespoke the deployment is. Complexity drives cost to serve, and cost to serve is what coverage is actually allocating
- **Potential.** Room to grow, strategic relevance, reference value

A small account with high complexity costs more than a large simple one and frequently gets tiered as though it costs nothing. That is where the surprise churn and the CSM burnout both come from.

## Step 2: Define each tier by what it gets, in specifics

Vague tiers are how models die. "High touch" means nothing operationally.

For each tier, write:

- **Named CSM or not.** This is the real dividing line, not the frequency
- **The cadence**, as a commitment you would actually meet at the stated ratio
- **What the customer is entitled to ask for**
- **The response commitment**, if any
- **What triggers escalation into a higher tier**, temporarily or permanently

Then check the arithmetic honestly. **A cadence you cannot meet at the ratio you are proposing is not a model, it is an aspiration**, and the people who will discover that are the CSMs, quietly, by dropping the tail.

## Step 3: Say what each tier does not get

The step that makes it a real design. For each tier, state plainly what it will not receive, and therefore what you will not see.

- **Digital-only accounts produce no relationship signal.** You will not know their champion left, and no dashboard will tell you. Everything you learn about them comes from product telemetry, and if the product is not instrumented you learn nothing at all
- **Pooled accounts have no continuity.** The customer explains themselves each time, which they experience as being unimportant, and no one person notices a slow decline
- **Named-CSM accounts consume more than the model says**, because a named person absorbs everything, and the absorption is invisible until they leave or burn out

Write down what you accept losing at each line. **A model with no stated losses has not been designed, it has been described.**

## Step 4: Make the ratio an output

Cost to serve per tier, times the number of accounts, gives the required capacity. Compare that to the headcount you have. The gap is the finding, and it is a number rather than a feeling.

Where the gap cannot be closed with headcount, it gets closed by one of three things and it is a choice which:

- **Moving accounts to a lower tier**, and accepting the losses from Step 3
- **Reducing what a tier promises**, honestly, rather than quietly missing it
- **Investing in the mechanism that makes a lower tier work** at all, which is product instrumentation, content and triggers rather than more people

**Quietly absorbing the gap is the fourth option and it is the one that happens by default.** It hides the evidence, it burns the team, and it produces churn that arrives without warning because nobody was watching the accounts that were dropped.

## Step 5: Design the transitions, because that is where customers get lost

Every model is tested at its boundaries and almost nobody designs them.

- **A growing account moving up** should gain a person with context, not start again
- **A shrinking account moving down** is the dangerous one. It usually experiences the change as being abandoned at exactly the moment it was already unhappy, and it is a routine cause of avoidable churn
- **Temporary elevation.** An escalation, an onboarding, a renewal cycle. Say who authorises it and when it ends, or every temporary elevation becomes permanent and the model erodes
- **Any move at all needs a handover**, and `handoff` covers it. A tier change is a CSM change from the customer's side

## Step 6: Make digital and pooled actually work, or do not claim them

A digital tier is not an absence of coverage with a nicer name. It requires specific things, and without them it is a euphemism:

- **Product instrumentation** good enough to generate a real signal
- **Content that answers the questions a CSM would have answered**, which someone has to write and maintain
- **Triggers with owners.** A signal nobody acts on is not coverage
- **A route back to a human** when the trigger fires, with someone whose job it is

If those do not exist, say the tier is unserved rather than digital. The honest word changes the conversation with your own leadership, which is usually the point.

## Step 7: Test the model against your actual churn

The step that separates a designed model from a plausible one, and it is cheap.

Take the accounts that churned in the last two years. For each, ask: **under this proposed model, which tier would it have been in, and would anyone have seen it coming?**

If most of your losses would have sat in a tier with no relationship signal, the model does not work, however elegant the tiers are. That is a finding you can act on before implementing rather than after.

Then set a review point, because segmentation drifts as the book grows and a model nobody revisits describes the company you were two years ago.

---

## Output

1. **The segmentation**, on value, complexity and potential, with the accounts that move because of complexity called out
2. **Each tier defined by specifics**: named CSM or not, cadence, entitlements, escalation triggers
3. **What each tier does not get**, and what you therefore will not see
4. **Cost to serve and the capacity gap**, as a number
5. **How the gap is being closed**, named as a choice
6. **The transitions**, especially the downward one
7. **What digital or pooled requires**, and whether it exists
8. **The churn back-test**, and what it showed
9. **What you could not check**

---

## Failure modes

- **Designing backwards from headcount** and calling the resulting ratio a strategy
- **Tiering on revenue alone**, which misplaces small complex accounts in both directions
- **Vague tier definitions.** "High touch" is not an operational commitment
- **A cadence the ratio cannot support**, which the CSMs discover by dropping the tail
- **Not stating what each tier loses**, so the model is described rather than designed
- **Calling an unserved tier "digital"** when the instrumentation, content and triggers do not exist
- **Undesigned transitions**, especially downward, which is a routine cause of avoidable churn
- **Temporary elevations with no end date**, which erode the model back to everything being high touch
- **Absorbing the capacity gap quietly**, which hides the evidence and burns the team
- **Never back-testing against actual churn**, leaving a model that is elegant and would not have caught your losses

---

## What good looks like

- Segmentation uses complexity as well as value, and some accounts moved because of it
- Every tier says what it gets in specifics and what it does not get
- The ratio is an output of cost to serve, not an input
- The capacity gap is a number, and how it is being closed is a stated choice
- The downward transition has a designed experience
- Anything called digital has instrumentation, content, triggers and a route back to a human
- The model was tested against the accounts that actually churned, and the result changed something

---

## Related skills

- `book-triage` for working inside a coverage model that already exists
- `handoff` for the tier transition, which the customer experiences as a CSM change
- `renewal-forecast` for what the model implies about the number
- `churn-postmortem` for the loss history this model should be tested against
- `account-context` for the segment definitions this builds on

---

## Supporting files

None. The output is a tier table, a capacity number and a back-test, all of which are specific to the company and none of which survive a generic template.
