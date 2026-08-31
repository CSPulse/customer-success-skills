---
name: renewal-risk
description: >
  Produces a defensible read on whether an account will renew - the decision, the decider, the mechanism, the evidence, the dollars at stake and the play - rather than a colour on a dashboard. Trigger whenever the user asks "will they renew", "is this account at risk", "renewal risk", "churn risk", "should I be worried about this account", "what's the read on", "health check on", or names an account and a renewal date in the same breath. Also trigger when preparing for a forecast call, a risk review, or a QBR on an account whose renewal is inside two quarters. Use business-review when the job is running the meeting; use this when the job is deciding what is true. The skill works from whatever evidence exists and states plainly what it could not check.
---

# Renewal Risk

Usage tells you about the user. The renewal is decided by the buyer. In enterprise those two populations barely overlap, and almost every bad risk read is a variant of confusing them.

The failure this exists to prevent: "at risk, low usage." That sentence states a category, names no mechanism, and implies no action. It is the most common thing in a risk review and the least useful.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: it carries the product, the segments, the contract shapes, the value metric and what healthy usage looks like in this business. Where it is absent, carry on and name the assumption you are making instead. It is context, never a prerequisite.

**Minimum: what you know.** Tell it about the account and it will produce the read, marking every gap as a gap. On an account you have just inherited, run `account-research` first: a risk read without the original promise is a read against a standard nobody has established. A read with three unknowns that names them is more useful than a confident one that hides them.

**Better with** access to usage data, the mailbox or CRM for relationship history, and support ticket history. Each one converts a "cannot verify" into evidence.

**Best with** the account plan, the original business case, and the contract - which together let it check whether the value the customer bought is the value they are getting.

Nothing here is required. Missing evidence changes what the read can honestly claim, never whether it runs.

---

## Step 1: Set the clock to their calendar, not yours

Your renewal date is the least important date on the account. Establish these first:

- **Their budget planning cycle.** Once budget is reallocated in planning, you are arguing against a decision that has already been made. For enterprise this is often 9-12 months before your renewal date.
- **Their notice or opt-out date.** After it passes, they have decided. Auto-renewal clauses commonly carry 30-90 day notice windows.
- **Their fiscal year end**, which governs when money can move.
- **Any operational blackout** - retail peak, financial year-end close, a manufacturing shutdown, an audit period - when no decision will be made and no meeting will land.

Then state how much time is actually left, in their terms. "Ninety days to renewal" and "three weeks until their budget lock" are different situations wearing the same number.

Enterprise buyers routinely begin renewal preparation 6-18 months out for strategic vendors. If your risk motion starts at T-90, you are arriving after their evaluation started.

---

## Step 2: Name the decision and the decider

Before any signal analysis, answer three questions in one line each:

1. **What decision** is being made - renew as-is, renew smaller, renew with different terms, or replace.
2. **Who makes it.** A named human with budget authority.
3. **Have you spoken to them, ever.**

**If you cannot name the decider, that is the risk, and it outranks everything else on the account.** Say so first and do not bury it under usage analysis. The same applies if the person you talk to is not the person who signs - those are two different failures, and the second one hides behind good relationships.

Check single-threading here too. One relationship means no recovery path when that person leaves.

Where the relationship picture is unclear or stale, `stakeholder-map` does this properly: it sorts people by what they can do to the outcome, carries a column for whether you have actually met them, and gives single-threading a number rather than an impression.

---

## Step 3: Read the signals in order of decision-weight

Work down these tiers. A Tier 1 signal outranks any amount of Tier 2 comfort.

### Tier 1 - decision mechanism

- Economic buyer or executive sponsor changed, or is about to
- You cannot name who signs, or have never met them
- Single-threaded relationship
- **No agreed, currently-true value metric.** Nobody can state the number the customer bought. This is the mechanism behind most "healthy usage, still churned"
- Sponsor-specific silence - the working team still engaged while the sponsor has gone quiet, which usually means the decision has moved above your line of sight

### Tier 2 - usage shape, never usage level

Before leaning on a health score here, be clear how much it can carry. `health-read` audits the score rather than reporting it, and separates the inputs that are measured from the ones that are proxies.

Level is close to worthless. Shape, direction and composition carry the signal:

- **Trajectory over snapshot.** A score of 7 is not reassuring if it was 8.5 last month. Alert on the drop, including drops inside the healthy band
- **Breadth against depth.** Concentration in one or two features means a point solution can displace you. One power user carrying the account inflates the aggregate and is one resignation from zero
- **Admin against end-user composition.** Heavy admin activity - config changes, permission audits, bulk export, reporting - with flat end-user activity often means migration prep or an audit, not health
- **Failure rate, not just usage rate.** "The product does not work for them" is a different diagnosis from "they do not use it", and the plays are opposite. Most health scores cannot tell them apart
- **Integration count and health.** Disconnecting integrations is disentangling
- **New-user provisioning.** Zero new users in 90 days is a stall even at flat aggregate usage

### Tier 3 - commercial and procurement

The buyer starts before you do, and the highest-value signals here are routinely misread as helpfulness:

- **They ask for utilisation data, seat counts, contract copies, invoice history, or the notice date.** This is negotiation preparation, not admin
- A mid-term security, legal or vendor-risk re-review of an existing vendor - a re-buy in disguise
- A request to shorten the term, move to monthly, or remove auto-renew - they are buying optionality
- A new procurement, vendor-management or FinOps party appearing in the thread
- Competitor or benchmark pricing mentioned in conversation
- A downgrade request is **lagging**. The scope decision is already made; the leading version of that signal was the utilisation audit two months earlier

### Tier 4 - support and sentiment

Ticket volume alone signals nothing in either direction. Rising volume means friction; falling volume from a previously active account means resignation. What is predictive:

- **Type.** Bulk export or API extraction requests, deprovisioning questions, permission audits, and above all questions about cancellation terms or notice periods
- **Who is filing.** The champion stopped and only junior admins remain, at steady total volume
- **Language shift** from "still" and "confusing" toward "unacceptable" and "disappointed"
- **Non-response.** B2B survey response rates are low enough that silence is the default state and cannot be read as consent. Who used to respond and stopped is the signal, not the score

### Tier 5 - organisational

Low frequency, high impact: their acquisition or merger, layoffs, a new functional leader, a reorg, a cost-out programme, a vendor consolidation initiative, a funding problem. A new executive reviews everything their predecessor bought.

Note the direction on M&A. Them being acquired is usually a standardisation risk on the acquirer's timeline, not yours. Them acquiring is an expansion opportunity plus a bake-off.

---

## Step 4: Normalise before you conclude

The same signal means different things in different contexts. Adjust for:

**Segment.** Enterprise risk is political and procedural, decided by committee on their calendar - weight stakeholder changes, procurement activity and budget cycles. Mid-market risk is relational and champion departure dominates, because there is no bench. SMB risk is mechanical and fast - usage direction, payment failure, business closure - and relationship signals largely do not exist to read.

**Pricing model.** Seat-based risk is legible but lagging, and shows up as a rightsizing demand. Consumption risk is continuous and quiet, with no renewal event to detect it - track burn-down against commitment pace instead, and hold two inversions in mind: falling consumption with stable outcomes can mean the customer got efficient, and rising consumption can mean bill shock and a smaller next cycle. Platform and multi-product accounts must be read module by module, because an account-level average of one growing and one dying module tells you nothing.

**Motion.** In product-led accounts, behavioural signals are all you have and they move fast. Watch for the conversion moment where procurement or IT notices the account - SSO and SCIM requests, security questionnaires, a move from card to invoice. Those are simultaneously expansion and risk signals, and most scoring models read only the first.

**Industry.** Ask what normal looks like here before calling a deviation. Retail usage collapses after peak season and that is not risk. Compliance and disaster-recovery tooling is bought to sit unused. Project-based professional services usage ends when the engagement ends. Regulated industries treat a periodic security re-review as routine governance in some cases and as a re-buy in others, and you need to know which. See `references/context-adjustments.md`.

---

## Step 5: State the mechanism, not the category

This is the step that separates a read from a status update. Write the causal chain from what you observed to non-renewal.

Not this: *usage is down 40%.*

This: *the ops team driving 70% of usage was cut in January. The remaining team uses only the reporting module, which the BI tool they bought in March already covers. The incoming VP Operations has a stated consolidation mandate and has not met us.*

The first is an observation. The second tells you who to call and what to say.

If you cannot construct the chain, say that the mechanism is unknown and that finding it is the next action. An unknown mechanism is a legitimate finding; a fabricated one is not.

---

## Step 6: Argue against yourself

Name what would make this read wrong. Experienced leaders ask this first and its absence is conspicuous.

- What is the strongest evidence **against** your conclusion?
- Which of your evidence is a statement by someone, and which is your inference? Mark them differently
- Whose statement is it - the champion's, or the economic buyer's? A champion's optimism is evidence about the champion, not about the account
- Is this a risk, or an outcome that has already happened? A downgrade request is a negotiation you are already in, and calling it a risk conceals how late you were

---

## Step 7: Forecast dollars, not logos

Most accounts labelled "at risk" are not at risk of leaving. They are at risk of renewing 30% smaller. A binary flag hides that entirely.

Give a range with a number attached: full renewal, likely contraction and its size, and the downside. If you are guessing, say which parts are guesses.

Also ask whether this risk is correlated. Thirty accounts with the same risk reason is one product or pricing decision, not thirty individual saves.

---

## Step 8: Name the play, the owner, the ask, and the checkpoint

A risk with no ask is a status update.

- **The play**, matched to the mechanism. A low-adoption playbook fired at a budget-cut risk is pure motion
- **The owner and the date**
- **What you need from your own side** - executive time, discount authority, a roadmap commitment, services hours - and what that is worth against the dollars at stake
- **The conversation the play depends on.** Most plays here come down to one call. `call-prep` builds it around an outcome that can be failed, and `hard-conversation` handles it where the play is a commercial change or a roadmap no. Where the read lands on contraction rather than churn, `renewal-negotiation` prepares the conversation where the number gets agreed
- **A falsifiable checkpoint**: "if we have not met the new VP by the 14th, escalate." A checkpoint you cannot fail is not a checkpoint

Be honest about the window. Before an alternative is named, fixing value realisation and re-multithreading still work. After a replacement has been procured, or budget has been reallocated in planning, or the notice date has passed, they generally do not - and saying so is more useful than a save plan nobody believes.

---

## Output

A short written read, not a dashboard:

1. **The call** - renew, contract, or churn - with the dollars and a confidence level
2. **The decision and the decider**, and whether you have met them
3. **The mechanism**, in three or four sentences
4. **Evidence**, dated and attributed, with inference marked as inference
5. **What would make this wrong**
6. **The play**, with owner, date and ask
7. **What you could not check**, named plainly

Keep it under a page. If it is longer than the account is worth, it will not be read.

---

## Failure modes

- **Sandbagging.** Risk flagged with no play attached, flagged late, never changing state. The tell is an at-risk book that renews at 95%
- **Happy ears.** The only evidence is verbal, from one person, who does not control budget
- **Reading quiet as healthy.** The accounts with the fewest logged touches are disproportionately risky and disproportionately rated green. A CSM's avoidance is itself a signal and no health score captures it
- **Anchoring on your renewal date** rather than their budget cycle and notice date
- **Single-signal reads** - declaring risk on usage alone, or safety on a score that has never been tested against actual churn
- **Risk theatre.** Risk logged, playbook fired, training offered, nothing touching the actual mechanism
- **Averaging disagreement.** When the model says green and the CSM says red, one of them is wrong. Splitting the difference destroys the information
- **Laundering.** "It was an acquisition" concealing nine months of neglect

---

## What good looks like

- Someone who has never seen the account can read it and know who to call and what to say
- The mechanism is specific enough to be wrong
- The dollar range is stated, not just a colour
- Inference is visibly separated from what someone actually said
- The gaps are named rather than smoothed over
- It was written early enough that the play still has room to work

---

## Reference files

- `references/context-adjustments.md` - how segment, pricing model, motion and industry change what a signal means
