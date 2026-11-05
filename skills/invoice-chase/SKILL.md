---
name: invoice-chase
description: >
  Use when the user says "overdue invoice", "chase the invoice", "they have not paid", "the PO is stuck", "AP has not paid us", "payment reminder". Produces a likely-cause read, who to write (finance for the money, the champion for context), the chase draft with invoice number, amount, due date and how to pay, a dated tone ladder, and the account signal to log. Not for a customer asking for a discount (use renewal-negotiation) or a billing dispute that has become an escalation (use escalation).
---

# Invoice Chase

An overdue invoice or PO turned into a diagnosis, a draft to the right person at the right tone, and the next date. Draft only, the user sends.

## Start here

If the user gave the invoice number or PO, amount, due date and who it went to, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Invoice or PO number, amount, due date, terms, and the payment method on the invoice
2. Who has been contacted so far, by whom (a person or an automated reminder), and any reply
3. Anything odd on their side: a new finance system, a changed contact, a complaint, a PO that was never sent

If an "Account context" block exists in the conversation, use it. Payment details always come from the user, never from memory.

## Do this

1. **State the facts and the age.** Invoice, amount, due date, days overdue measured from the due date. Say whether any human has chased yet. Automated reminders are not a chase.
2. **Rank the likely causes** with the evidence for each: forgot, stuck in AP (no PO match, wrong bill-to, missing vendor form), PO expired or never issued, dispute, budget problem. Name the one question that tells them apart.
3. **If it is a dispute, stop.** Do not chase the amount. Find the real issue first, and ask for payment of any undisputed part.
4. **Pick the recipient.** AP or finance for the payment, the champion copied for context and routing. If no finance contact is known, the first ask to the champion is "who processes this".
5. **Pick the ladder step:** friendly nudge, then firm (amount and due date, a payment date requested), then escalate to the finance lead or economic buyer. Put a date on each step, with about three working days between them (a common default, set your own).
6. **Draft the chase.** It must carry invoice number, amount, due date, how to pay, and a question that is easy to answer ("what do you need from us to get this into the next payment run?").
7. **Log the signal and the checks.** Late payment goes in the account notes as a risk signal. List what to confirm with the user's finance team before sending.

## Output

```
INVOICE CHASE: [Account] | [number] | [amount] | due [date] | [n] days overdue
Likely cause: [cause] (confidence) | Next most likely: [cause]
Tells them apart: [one question]
Ladder step: 1 / 2 / 3 - [why this step]

To: [role or name] | Copy: [champion] | Not: [who not to chase alone]

Subject: [subject]
[draft]

Ladder
- [date] step 1 | [date] check, no reply means step 2 | [date] step 3 to [who]

Account signal to log: [one line, with date]
Check before sending
- [contract terms, finance team, payment details]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **Write to whoever moves the money, copy whoever knows the story.** AP processes tickets and rarely reads the CSM's emails, and a champion chased alone becomes the collector, which costs the relationship the renewal runs on.
- **Every chase carries four facts:** number, amount, due date, how to pay. AP replies to an email missing one by asking for it, and that costs a payment cycle.
- **Say "our records show it unpaid", never "you have not paid".** The money may be in flight, and a wrong accusation turns a process delay into a grievance. Ask for the remittance advice if it was sent.
- **Never threaten suspension or late fees on your own.** Only the contract and the user's finance team can say what is allowed, and an unauthorized threat can breach terms and sour the renewal. Flag "contract check" instead.
- **Diagnose before choosing tone.** A forgotten invoice needs a smile, a stuck PO needs a fix, and a firm note sent into a dispute makes it worse.
- **Step out for about three working days after each chase.** Faster reads as nagging, and AP often pays in scheduled runs, so ask for the date of the next one.
- **A late payment is a signal about the account, not only about cash.** One slip is usually process. Late plus a new executive, falling usage or a slow champion belongs in the renewal read. A customer that stops paying on time may have moved priorities.
- **Never invent a detail.** Bank details, a PO number or a payment date come from the user or the customer, and a wrong remittance detail is worse than a late chase.

## Related (only if installed)

`renewal-risk` when the late payment sits beside other signals. `escalation` if it turns into a dispute with a senior name on it. `email-critic` to check the tone before it goes.
