---
name: sales-handoff
description: >
  Use when the user says "closed-won handoff", "the AE just closed", "sales handoff", "what did sales promise", "intake from the AE", "questions for the AE". Produces the intake for a newly signed customer (why they bought, goals with baselines, a ledger of promises checked against the contract, people and politics, competitor, terms), the exact questions to put to the AE, and a first-week kickoff plan. Not for CSM to CSM or leaving an account (use handoff) or the full onboarding schedule (use onboarding-plan).
---

# Sales Handoff

Turn a signed deal and whatever the AE wrote into an intake the CSM can run from, plus the questions that close the gaps before the customer finds them.

## Start here

If the user pasted the AE's notes or the opportunity record and the order form (or its key terms), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The AE's handoff notes, deal summary or opportunity notes
2. The order form or contract terms: units, price, term, start, renewal and notice, special clauses
3. Anything the customer wrote during the sale (RFP answers, emails, call notes)

If an "Account context" block exists in the conversation, use it. If goals, promises or an onboarding plan for this customer are already in the conversation, merge into them. Do not restart or duplicate.

## Do this

1. **Check what already exists.** Goals, promises or a plan already captured, or a kickoff already booked, means extend them. Say what you merged and what is new.
2. **Why they bought, in their words.** The trigger event, the problem, one quote. Then each goal with measure, baseline, target and date. A missing baseline is written "baseline missing, capture at kickoff", never guessed.
3. **Build the promise ledger.** Every promise made in the sale (features, integrations, dates, pricing, services, support levels, security answers): who made it, to whom, the quote, and a check against the paper: in contract, not in contract, or contradicts it. Mark what the customer was told apart from what the product does. Product, price and security facts are for the user to verify, never asserted.
4. **Map the people.** Economic buyer (named even if never met), sponsor, daily users, technical, procurement, anyone cool or hostile. Mark who the AE actually met and what each person wants to be seen to have won.
5. **Record the rest.** Competitor and why they lost, what they offered, commercial terms with the renewal and opt-out dates, known risks.
6. **Write the questions for the AE.** One per gap, in the order of the damage it could do, specific enough to answer in a line or a forwarded email.
7. **Plan the first week and set the sign-off.** Internal sync within about two business days, customer meeting within about a week, a 30 day check asking the customer what they were promised that they have not seen (common defaults, set your own). The handoff is complete when the receiving CSM says so.

## Output

Verdict first. Keep it to about a page and a half.

```
SALES HANDOFF: [Customer] | $[ARR] | [term] | signed [date] | AE [name]
Readiness: READY / KICK OFF WITH GAPS / NOT READY
Top risks to the first 90 days: 1. .. 2. .. 3. ..

Why they bought: [trigger, problem, quote with source]
Goals: [goal | measure | baseline | target and date | source]
Promises: [# | promise | made by, to whom | in contract? | owner | due | status]
People: [name | role | AE met? | what they want]
Competitor: [who, why they lost, what they offered]
Terms: [units, price, term, start, renewal, opt-out, payment]

Questions for the AE (send today)
1. ..

First week: [dated actions]
Complete when I can answer without the AE: [list]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Trust the paper over the person.** Sales promises that never reached a contract or a system are the main source of first-90-day surprise. The customer remembers the promise, not the clause, so find the gap before they do.
- **Separate told from true.** "The AE said we integrate with X" is not "the product integrates with X". A buyer who bought on a told claim tests it in week three, so route every such claim to someone who can verify it.
- **Name the economic buyer even if nobody has met them.** The renewal is signed by the buyer, and a deal won through one champion is single-threaded from day one.
- **Meet the customer within a week.** Enthusiasm and the AE's warm introduction fade together. Ask the AE to join the first call so the transfer is visible to the customer.
- **Capture the baseline now.** After go-live the before number is gone and the value can never be proved.
- **Record why the competitor lost and what they offered.** That is the comparison the customer will make again at renewal.
- **Never restart or duplicate.** Resetting a running onboarding wipes the steps already done, and two copies of a goal become two versions the customer hears.
- **Done means the CSM says done.** An AE finishing the notes transfers paperwork, not understanding. Keep the AE reachable for the first 30 days (a common default).

## Related (only if installed)

`onboarding-plan` for the full schedule once the gaps close. `commitments` to keep the ledger live. `stakeholder-map` to deepen the people list. `internal-ask` when a promise needs product to confirm.
