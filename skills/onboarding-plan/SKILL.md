---
name: onboarding-plan
description: >
  Builds a customer onboarding plan aimed at a result the customer can point to, not a checklist your team can close - with success criteria carrying a baseline, named owners on both sides, and the early signals that predict a bad year. Trigger whenever the user says "onboarding plan", "kickoff", "new customer", "just closed", "first 90 days", "implementation plan", "handover from sales", "success plan", or names an account that has recently signed. Also trigger when they ask why an onboarding is stalling or whether a customer is really live. The plan it produces becomes the evaluation frame for the renewal, so it is written to be measured against later.
---

# Onboarding Plan

Completion is internal. Value is external. The test of whether onboarding is done is not whether your tasks are closed, it is whether the customer can walk you through a specific result. If they cannot, they are not onboarded - they are trained.

Go-live is a vendor event. Adoption is a customer state. Confusing the two is how accounts arrive at renewal with a green implementation record and no argument for renewing.

The failure this exists to prevent: a fully completed onboarding checklist attached to a customer who cannot say what changed.

---

## What this needs

**Minimum: what was sold and to whom.** It will build the plan, the questions and the risk list from that, and mark what it could not confirm.

**Better with** the sales handover notes, the contract scope, and the stakeholder map - which together let it catch the gap between what was sold and what was bought.

**Best with** the original business case and access to product data, so success criteria can be instrumented rather than aspirational.

---

## Step 1: Read the handover for what is missing, not what is there

Six things must transfer from sales. Check each and name the gaps:

1. **The business objective** that motivated the purchase, and its measurable success metric
2. **Deal context** - what else they evaluated, the pricing terms, how long the cycle ran. A competitive displacement onboards differently from a greenfield purchase, and a heavily discounted deal has different renewal physics
3. **The relationship map** - economic buyer, champion, users, **and the sceptics**. The sceptics are the element most often omitted and most often fatal
4. **Open risks** - technical dependencies, data migration needs, approvals still pending
5. **Every commitment made during the sale**, including custom demos, integrations, workflow assumptions and roadmap hints. Undocumented promises become scope disputes in month three
6. **First-30-day priorities and the customer's own responsibilities**

If you are asking sales a lot of follow-up questions, that itself is a signal: incomplete handovers predict rediscovery friction and expectation mismatch later.

Where there is no handover at all, or the account arrived without one because it was transferred rather than sold to you, `account-research` reconstructs what was promised from the deal record instead.

**Move fast.** The gap between signature and kickoff is idle time at the moment of peak customer enthusiasm. Five business days is a reasonable ceiling.

---

## Step 2: Validate, do not re-interrogate

The customer has already explained their problem, to someone who has now disappeared. Asking them to do it again is the most common early own goal.

Say instead: *"Here is what we understand from your conversations with [AE]. Is that accurate, and what would you change?"* Then ask only targeted clarifications.

What **is** legitimate new ground, because sales rarely captures it, is operational rather than problem discovery:

- How change actually gets rolled out here, and who has to approve it
- How this team prefers to learn
- What integrations exist in the real environment, as opposed to the diagram
- Whether the champion has changed since the deal closed

If you can, run the handover as a three-way call including the champion. It turns re-asking from an embarrassment into a visible continuity ritual, and lets the champion correct the account of their own goals in front of you.

---

## Step 3: Get success criteria with a baseline

A target without a baseline is unfalsifiable, and unfalsifiable criteria are worthless at renewal.

**Ask, in this order:**

- What business problem are you trying to solve?
- Why now? - this surfaces the real forcing function
- What would success look like six months from today?
- **How will your leadership decide whether this investment was worthwhile?** - the highest-yield question, because it forces them to name the person whose judgement actually decides the renewal

**Convert to something measurable.** Weak: "complete the integration by week four" - that measures your work. Strong: "cut manual reporting effort by half within 90 days of launch, from the current 12 hours a week."

**When they will not or cannot commit**, diagnose which of three situations you are in, because they need different responses:

- **They cannot articulate it** - no baseline exists because they do not measure this today. Make establishing the baseline the first success criterion. This is real work and it converts a stall into a deliverable
- **They lack the authority** - the person in the room cannot sign up to a business metric. This is a sponsor problem, not a criteria problem. Get 20 minutes with the economic buyer, or accept a proxy the project owner can own while logging explicitly that the business metric is unowned
- **They are hedging** - they suspect the criteria will be used against them, or they doubt it will work. Reframe from measurement to protecting their own investment. And treat continued refusal as the signal it is: a sponsor who will not say what good looks like will not defend the spend later either

**Fallback ladder**, in descending order of usefulness: business outcome with a baseline, then a leading operational metric with a baseline, then a named workflow that must be running in production by a date, then a named person who will publicly say it worked. Never close the plan with none of these.

**Then confirm in writing the same day.** Absence of explicit confirmation means they have not agreed.

---

## Step 4: Build the plan around first value, then everything else

**Separate first value from full value.** First value is the first tangible result the customer cares about - a live workflow, a synced integration, a delivered report. Not a completed configuration. Full value is the original business case delivered at intended scale, and it is reached through a sequence of milestones rather than on a single date.

Protect the path to first value from everything else. Configuration that does not sit on that path gets sequenced later, however easy it would be to do now.

**Time-to-first-value expectations vary by segment** - days for self-serve, days to a couple of weeks for smaller assisted accounts, weeks for mid-market, and a month to a quarter or more for enterprise where legal, security and IT are all in scope. Data migration complexity overrides segment: dirty data and nested transformations turn a two-week plan into a two-month one.

**Five things must be true before the kickoff call ends:**

1. Success criteria with baseline, target and timeline
2. A specific go-live date - explicitly not "as fast as possible"
3. Named people on the customer side, with hours per week
4. An agreed communication cadence
5. One early win achievable in the first week or two

**Shape of the first 90 days:** foundation and first value in the first 30, expansion of usage and the first real workflows by 60, and by 90 a measured result plus the review that confirms it. Adjust the dates, keep the sequence.

**Warn them about the dip.** Right after go-live, people are slower than they were before - they are thinking consciously about tasks that used to be automatic, and re-checking outputs against the old process. Customers who are not warned interpret this as product failure. The goal is not to avoid the dip; it is to keep it shallow and short.

---

## Step 5: Watch the signals that predict a bad year

**Process signals, visible without any product data:**

- Kickoff not held within a week of signature
- No named admin or project owner with allocated hours. "The exec will handle it" is a red flag
- Champion or executive sponsor absent from the kickoff
- Security or IT review discovered after kickoff rather than planned into it - planned, these run days; discovered late, they are unbounded
- Success criteria never agreed, or shaped around your deliverables rather than their outcome
- Environment provisioned and never used
- The customer resists a regular check-in cadence, which designs radio silence into the plan
- Vague success language never converted into a number
- Attendees disagreeing with each other about the timeline - the sold-versus-bought gap surfacing in the first hour, which is the best possible time
- Blockers aging. Blockers existing is normal; blockers sitting is not

**Relationship signals:** meeting durations quietly shrinking, seniority of attendees dropping, the sponsor no longer joining, hesitation when outcomes are discussed, approval delays on small decisions.

**Usage signals:** flat active-user growth, a widening gap between purchased and active seats, usage that does not match the stated use case, integrations connected and then disconnected.

**The one most often missed:** a customer can have green metrics and still be at risk if they do not feel progress is happening. Health scores are historical. Perceived momentum is current, and it is what they carry into the renewal conversation.

---

## Step 6: Hand over properly, and keep measuring

If implementation and ongoing ownership sit with different people, the handover between them needs the same rigour as the one from sales: documentation, the risk log, the stakeholder map, the success metrics, and a health baseline at the point of transfer.

Then keep going. Onboarding does not end at go-live, and the account should not go quiet the moment the project plan closes - that transition is where a well-run implementation turns into a silent first year.

---

## Output

A plan document containing:

1. **The business objective and success criteria** - baseline, target, timeline, and who owns each
2. **First value** - what it is, and the date
3. **Milestones** with owners on both sides and dependencies named
4. **The customer's commitments**, explicitly, with names and hours
5. **Risks and open questions** from the handover, including what sales promised that is not in scope
6. **The signal watchlist** for the first 90 days
7. **What could not be confirmed**, stated plainly

Write it as a shared document rather than an internal one. The plan is the thing you will be measured against at renewal, and a plan the customer never saw cannot hold them to anything.

---

## Failure modes

- **Onboarding as a checklist.** Tasks closed, no result the customer can name
- **Training the wrong people** - the people who attend are not the people who will use it
- **Declaring go-live as success**, which measures your work rather than their outcome
- **No executive sponsor**, so nothing survives the first competing priority
- **Scope creep from the sales promise**, unmanaged because the promise was never written down
- **Going dark after go-live**, exactly when the productivity dip is at its worst
- **Reading customer silence as success.** It usually means stalled progress
- **Measuring too late** to correct anything

---

## What good looks like

- The customer can describe a specific result, in their own words, without prompting
- The success criteria have a baseline, and someone senior owns the number
- The plan is a shared document both sides have edited
- The commitments the customer made are written down and being met
- Someone picking up the account in month four can tell what was promised and what was delivered
- The renewal conversation eleven months later is evidence, not persuasion
