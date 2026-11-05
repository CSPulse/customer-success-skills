# Sample output

*Invented example. Customer "Cobalt Ridge Foods" and every person named are fictional. Input the user gave: "Cobalt Ridge Foods owes us $24,000, invoice INV-20418, the annual platform fee, due Mon 19 Oct, Net 30. Today is Fri 6 Nov. Only our finance system's two automated reminders have gone out, nothing back. Champion is Elena Brandt in ops. The invoice went to ap@cobaltridge.example and has a payment link. Renewal is in March."*

---

```
INVOICE CHASE: Cobalt Ridge Foods | INV-20418 | $24,000 | due Mon 19 Oct | 18 days overdue
Likely cause: stuck in AP, no PO or vendor match (low to medium confidence)
Next most likely: forgotten, the champion is not the payer
Tells them apart: "Does your AP system show this invoice as received, and
against which PO?" A dispute looks unlikely: no complaint has been raised
(inferred, from the user's notes).
Ladder step: 1. No human has chased yet, and two automated reminders are not
a chase (seen, finance system log).

To: ap@cobaltridge.example | Copy: Elena Brandt (ops champion)
Not: Elena alone. She runs the tool, she does not release payments.

Subject: Invoice INV-20418, $24,000, due 19 October

Hello,

Our records show invoice INV-20418 for $24,000 (annual platform fee) as
unpaid. It was due on 19 October, so it is now 18 days past due. If it has
already been sent, a remittance advice would let us match it.

You can pay through the link on the invoice, copy attached.

What do you need from us to get this into your next payment run? A PO
number, a vendor form or a different bill-to contact are the usual
blockers, and I can sort any of them quickly. Could you tell me the expected
payment date by Thursday 12 November?

Thank you,
Jordan Hale, Customer Success

Separate note to Elena (2 lines)
"Elena, I have copied you on a note to your AP team about INV-20418. It is
probably a process snag. Is there a PO or an approver I should know about,
and who owns vendor payments on your side?"

Ladder
- Fri 6 Nov: step 1 to AP, Elena copied
- Thu 12 Nov: check (Wed 11 is a US bank holiday). No payment date means
  step 2: firm, same four facts, asks for a committed payment date
- Tue 17 Nov: step 3 to the finance lead or economic buyer, after the
  user's own finance team agrees the wording

Account signal to log: Fri 6 Nov, $24k annual fee 18 days overdue, no human
reply to two automated reminders, cause unknown. Bring into the March
renewal read if still unpaid on 17 Nov.

Check before sending
- The payment link and remittance details attached are current (user)
- The order form says whether a PO number is required, and what it says on
  late fees or suspension. The draft mentions neither. Do not add either in
  step 3 without finance and the contract
- No payment landed today in your finance system

What I could not check
- Whether INV-20418 reached ap@cobaltridge.example or bounced
- Who the finance lead is (name needed for step 3)
- Whether last year's invoice was paid on time
```
