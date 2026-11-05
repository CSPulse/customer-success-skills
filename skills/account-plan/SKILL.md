---
name: account-plan
description: >
  Use when the user says "account plan", "strategic account plan", "twelve month plan", "what is our plan for [account]", "plan for this account", "write up the account strategy". Produces a one to two page plan a successor could run in month four: the objective in the customer's words with a baseline and target, owners on both sides, 3 to 5 dated actions and risks with triggers. Not for the first 90 days of a new customer (use onboarding-plan), a renewal call (use renewal-risk) or choosing which accounts earn a plan (use book-triage).
---

# Account Plan

A durable plan for one account that someone inheriting it in month four could read and know what was promised, by whom, and what should be true by when.

## Start here

If the user gave the account, the contract (ARR, renewal, notice period) and what the customer is trying to achieve, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, ARR, renewal date, notice period
2. What the customer says they are trying to achieve, in their words, and who said it
3. Who decides, who champions, and who has not been met

Anything else (usage, the original business case, emails) is a bonus. If an "Account context" block exists in the conversation, use it for the value metric and what healthy looks like here.

## Do this

1. **Write one or two objectives in the customer's words.** "Cut dispute resolution from 14 days to 5" is theirs. "Drive adoption" is yours. Give each a baseline with the date it was taken, a target with a date, and a named owner on their side.
2. **If no measure exists, say so first.** Agreeing the measure becomes action one. An account with no agreed measure is the common shape of a healthy-looking renewal that fails.
3. **State where it stands in four lines:** what works, what does not, what changed since the last version, what is not known. Tag facts `said`, `seen` or `inferred`.
4. **Summarize the people:** decider, champion, sceptic, the biggest gap and the route to close it, and who is on the account from our side. Point to a stakeholder map if installed rather than rebuilding it.
5. **Write 3 to 5 actions.** Each has an owner, a date, the objective it serves, and at least two belong to the customer. Recurring items (QBR cadence, monthly report) go under Rhythms, not here.
6. **Give every risk a trigger.** What would tell you it is happening, what you will do, by when you need to know. Include single-threading and no agreed measure if they apply.
7. **Set review triggers, not just a cadence:** sponsor change, contraction, escalation, missed measure, their reorg. Each review answers what moved, what did not and why, and what changes in the plan.

## Output

Use this skeleton. Keep it to two pages. A fill-in version is `assets/account-plan.md`.

```
ACCOUNT PLAN: [Account] | [ARR] | renews [date] | opt-out by [date] | written [date]

Plan in one line: [objective, measure, biggest risk]

Objective: [in their words] | Measure: [baseline, date] to [target, date]
Their owner: [name, role]. Agrees it is theirs: yes / no / not asked

Where it stands
- Working / Not working / Changed / Not known (each tagged said, seen, inferred)

People: Decider [name, met?] | Champion [..] | Sceptic [..] | Gap and route [..]

Actions: [action | owner | side | date | objective served]
Rhythms: [recurring items]

Risks: [risk | trigger | response | know by]

Review: [cadence] and forced updates on [events]

Commitments on record: [what | by whom | side | date said]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **A plan with no measure cannot be failed, so it is never achieved.** Activity lists feel full and prove nothing at renewal.
- **A measure without a baseline cannot show movement.** At the renewal you would argue about whether anything improved.
- **An objective nobody on their side owns is yours.** It will not survive a change of sponsor.
- **Five actions or fewer.** More than that and nothing is prioritized, and the plan stops being opened.
- **Actions that are all ours mean the customer never agreed.** Some must be theirs, agreed with them.
- **A risk without a trigger is a worry.** Triggers are what let you notice it early enough to act.
- **Date everything and attribute commitments.** A commitment with no name is unenforceable both ways, and month-four you cannot tell what was told from what was concluded.
- **Not every account earns a plan.** A plan for all forty accounts is how the format loses credibility.

## Related (only if installed)

`book-triage` to decide which accounts earn a plan. `stakeholder-map` for the people picture. `renewal-risk` for whether the plan is working. `business-review` for the meeting where it is agreed with the customer.
