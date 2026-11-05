---
name: price-increase
description: >
  Use when the user says "price increase", "renewal uplift", "raise prices on my book", "which accounts do we protect", "notice period for the increase", "price rise letter". Designs the whole program, not one conversation: a segmentation table, a notice timeline from contract terms, one message draft, a concession ladder set in advance, and how to monitor the cost. Not for just writing the announcement or a broadcast notice (use customer-update) or the live conversation with one customer (use hard-conversation).
---

# Price Increase

Design the uplift as a program: who gets it, who is protected, when notice must go, what you will trade, and how you will know what it cost.

## Start here

If the user gave the uplift, the effective date and a list of accounts with ARR, renewal date and notice terms, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The uplift (percent or dollars), the renewals it applies to, and the reason in customer terms
2. The book: account, ARR, renewal date, price-change notice period, any price cap or lock
3. Per account, what you know about proof of value, the sponsor and any competitor or save plan

If an "Account context" block exists in the conversation, use it. Missing notice terms are written "(assumed, confirm)" and listed at the end.

## Do this

1. **Fix the policy.** Size, scope, effective date, the reason, what is genuinely new for the customer, and one owner. If nothing is new, say so now: the plan then leans on proof and trades.
2. **Write the protect list first.** Then segment every account on value delivered, risk (sponsor, decider, competitor, open save plan) and contract (cap, lock, notice): Apply, Apply with trade, Hold until value is proved, Capped by contract, Exempt. Give each a reason.
3. **Build the timeline from the contract.** Notice-by date = renewal date minus the price-change notice period. Send at least a week ahead, earlier around holidays. Order: sponsor hears first, then formal notice, then a value reminder with proof, then a call. A missed window moves the uplift to the next term.
4. **Set the concession ladder before the first call.** Three rungs and a floor, each with give, get, cost in dollars, and approver. Trade term length, scope, payment terms or a reference. Do not open with discount.
5. **Draft the one message.** Value first, then the change, the date and what happens next. Customer's words for the product. No apology and no jargon. Draft only.
6. **Set monitoring.** A weekly list: sent, acknowledged, call held, accepted, traded, refused. Churn and contraction caused by the program are tracked on their own line against the revenue gained, with a pause trigger.

## Output

Verdict first.

```
PRICE INCREASE PROGRAM: [n] accounts | $[ARR] | [uplift] from [date] | owner [name]
Verdict: expected $[x] ([y] of ARR) against $[blanket] blanket. Biggest risk: [..]
Check with legal or contracts: [notice wording, caps, auto-renew]

Segments: [account | ARR | segment | why | uplift $ low / expected / high]
Timeline: [account | notice by | send by | value reminder | call by]
Message draft: [subject and body]
Concession ladder: [rung | give | get | cost | approver] and floor
Monitoring: [weekly measures, program-attributed churn line, pause trigger]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Notice comes from the contract, not from habit.** A late or non-compliant notice can void the increase for a full term. The user checks windows, caps and auto-renew wording with legal or contracts. Never assume.
- **Notice, value, then a call. Never an email alone.** The customer meets the number before they meet what they got for it, and procurement forwards that number without you. The sponsor hears from the CSM before the letter lands, because they will be asked to defend it.
- **Segment before you send.** A blanket increase lands hardest on fragile sponsors and unproved value, and those accounts leave. Protecting a few accounts costs a few points of uplift and saves the logos.
- **Trade, do not discount.** A discount on call one teaches the book to ask. A trade (term, scope, payment up front, a case study) keeps the price intact and buys something the account was not otherwise giving.
- **One owner, one message.** Three versions from the CSM, the AE and finance read as chaos and give procurement the lowest number to quote.
- **Count the cost on its own line.** Fold program churn into overall retention and the damage is invisible. Compare the uplift to the largest single loss: one lost account often outweighs the whole program.
- **An increase with no new value is a churn event.** If the honest reason is cost, say so in plain words and lean on proof. Dressing it up as innovation costs trust.
- **Hold, do not force, where value is unproved.** Raising price on a customer who cannot say what they get invites the cancellation question. Fix the value first and move the uplift to the next term.

## Related (only if installed)

`hard-conversation` for the live call with one customer. `renewal-negotiation` when procurement pushes back. `customer-update` for a broadcast. `renewal-forecast` to carry the program into the number.
