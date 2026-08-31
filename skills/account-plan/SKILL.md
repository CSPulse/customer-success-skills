---
name: account-plan
description: >
  Writes the durable per-account plan you get measured against later, aimed at someone picking the account up in month four who needs to know what was promised and by whom. Trigger whenever the user says "account plan", "success plan", "strategic account plan", "plan for this account", "what is our plan for", "write up the account strategy", "twelve month plan", "growth plan for the account", or is asked to produce a plan for a named account. It writes the objective in the customer's words with a measure attached, names owners on both sides, attaches triggers to the risks, and refuses to plan more activity than anyone will do. Use onboarding-plan for the first ninety days, account-context for the business-wide substrate every skill reads, and book-triage for which accounts earn a plan at all.
---

# Account Plan

Most account plans are written once, for a review, and never opened again. They are a document produced to prove planning happened rather than an instrument anyone uses.

The test that fixes this: **could someone inheriting this account in month four read it and know what was promised, by whom, and what is supposed to be true by when.** If not, it is a status report with an ambitious heading.

The failure this exists to prevent: **the plan full of activity.** Twelve initiatives, no measure, no owners on the customer side, and no way to be wrong. It cannot be failed, so it is never achieved.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first for the value metric and the segment norms. This plan expresses one account's version of what that document defines generally. Where it is absent, carry on and name the assumption.

**Minimum: the account, its contract, and what you know about their goals.** Enough for a plan with honest gaps marked.

**Better with** the original business case, the current outcome data and a stakeholder picture, which between them give the objective, the measure and the owners.

**Best with** the customer's own stated goals, agreed with them rather than inferred. A plan written about a customer is weaker than one written with them, and the difference shows at the renewal.

---

## Which plan is this

Three objects in this library carry the word plan and they are not interchangeable.

- **`account-context`** is business-wide. What the product does, how segments differ, what healthy looks like here. Written once, read by everything
- **`onboarding-plan`** is the first ninety days of one account, aimed at a first result
- **`account-plan`**, this one, is the durable twelve-month picture of one account: what they are trying to achieve, how you will know, who owns what, and what would derail it

Not every account earns one. `book-triage` decides which do, and writing plans for a whole book of forty is how the format loses credibility.

---

## Step 1: Write the objective in their words, with a measure

One or two objectives. Not five.

- **The objective in the customer's own language.** Not "drive adoption" or "increase usage", which are your goals about their behaviour. Theirs sound like reducing time to close the books, cutting escalations to the field team, passing an audit without findings
- **The measure**, with a baseline and a target. A measure without a baseline cannot show movement, which means at the renewal you will be arguing about whether anything improved
- **Who on their side owns it.** A named person who would recognise this objective as theirs. If nobody would, it is your objective and it will not survive contact

**Where you cannot state the measure, write that as the first gap and make agreeing it the first action.** An account with no agreed measure is the single most common shape of a healthy-looking renewal that fails.

## Step 2: Say where the account actually is

Short and honest, in four lines: what is working, what is not, what has changed since the last version of this plan, and what you do not know.

The last one matters most and appears least. A plan that presents complete knowledge is either wrong or written by someone who did not look.

## Step 3: Name the people, and what each one needs

Not an org chart. For each person who can affect the outcome: what they want, what they can authorise, and whether they have actually been met.

`stakeholder-map` does this properly and this plan should point at it rather than duplicating it badly. What belongs here is the summary: the decider, the champion, the sceptic, and the biggest relationship gap with a route to closing it.

**Include your own side.** Who from your company is on this account, and what they have committed.

## Step 4: Plan less than you think

The discipline that separates a plan people use from one they file.

- **Three to five actions for the period.** More than that and nothing is prioritised
- **Each with a named owner and a date.** An action owned by "the team" is owned by nobody
- **Each with a stated so-what.** Which objective it serves. An action that serves none of the objectives is either the objectives being wrong or the action being habit
- **Actions on their side too**, agreed with them. A plan where every action is yours is a plan the customer has not committed to

Where an activity happens whatever the plan says, a QBR cadence or a monthly report, list it as a rhythm rather than as an action. Rhythms in the action list are what make plans look full and feel empty.

## Step 5: Give every risk a trigger

A risk register that lists worries is decoration. What makes it useful is a trigger and a response attached to each one.

For each risk: **what would tell you it is happening, what you would do, and by when you need to know.**

"Champion may leave" is a worry. "Champion is interviewing, which we would see as a slowed reply pattern and a drop in meeting acceptance; if that happens we accelerate the introduction to their VP, which is already an action" is a risk with a plan.

Two that belong on almost every plan and are usually absent: **single-threading**, and **no agreed measure** where Step 1 could not produce one.

## Step 6: Write it so a successor can use it

The whole point, and it costs almost nothing at writing time.

- **Date everything.** Every claim, every number, every commitment, with when it was true
- **Attribute commitments.** Who said it, on which side, and when. A commitment with no name is unenforceable in either direction
- **Mark inference as inference.** What someone told you and what you concluded are different objects, and month-four you cannot tell them apart afterwards
- **Say what you do not know**, rather than leaving a confident gap

## Step 7: Set the review trigger, not just the cadence

Plans die of quarterly review. Set a cadence, and also set the events that force an update regardless: a change of sponsor, a contraction, an escalation, a missed measure, a reorg on their side.

Each review answers three questions and nothing else: what moved, what did not and why, and what changes in the plan. A review that only reports is what turns the plan into a document again.

---

## Output

1. **One or two objectives**, in their words, with baseline, target and a named customer owner
2. **Where the account is**, including what you do not know
3. **The people summary**: decider, champion, sceptic, biggest gap and the route to it
4. **Three to five actions**, each with an owner, a date and a so-what, some of them theirs
5. **The rhythms**, listed separately from the actions
6. **Risks with triggers and responses**, including single-threading and no-agreed-measure if they apply
7. **The review cadence and the events that force an update**
8. **What you could not check**

`assets/account-plan.md` is the plan itself, written to be filled in and inherited.

---

## Failure modes

- **Activity as strategy.** Twelve initiatives, no measure, nothing that can be failed
- **Your objective in their sentence.** "Drive adoption" is what you want them to do, not what they are trying to achieve
- **No baseline**, so at renewal you argue about whether anything improved
- **No customer-side owner**, so the objective is yours and it does not survive contact
- **No customer-side actions**, which means they never agreed to any of it
- **Rhythms listed as actions**, making the plan look full and feel empty
- **A risk register of worries** with no triggers and no responses
- **Undated claims and unattributed commitments**, which are useless to whoever inherits it
- **Written once for a review** and never opened again
- **A plan for every account in the book**, which is how the format stops being taken seriously
- **Duplicating the stakeholder map badly** instead of pointing at it

---

## What good looks like

- Someone picking this up in month four knows what was promised, by whom, and what is meant to be true by when
- The objective is in the customer's words and a named person on their side would agree it is theirs
- Every measure has a baseline
- There are five or fewer actions and some of them belong to the customer
- Every risk has a trigger, so it can be noticed rather than merely feared
- Everything is dated, commitments are attributed, and inference is marked
- The last review changed the plan rather than reporting on it

---

## Related skills

- `account-context` for the business-wide substrate this expresses one account's version of
- `onboarding-plan` for the first ninety days, which this succeeds
- `book-triage` for which accounts earn a plan at all
- `stakeholder-map` for the people picture this summarises rather than duplicates
- `renewal-risk` for the read on whether the plan is working
- `business-review` for the meeting where the plan gets agreed with the customer

---

## Supporting files

- `assets/account-plan.md` - the plan, written to be inherited, usable without an assistant
