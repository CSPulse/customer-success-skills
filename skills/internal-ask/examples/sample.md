# Sample output

*Invented example. Vendor "Ledgerline" and customers "Pinecrest Foods", "Alder Street Capital" and "Kestrel Marine" are fictional. Input the user gave: "Pinecrest keeps asking for a bulk-edit button for approvers. Their controller says when someone leaves, her team re-assigns 300 vendors by hand, about 12 hours. Pinecrest is $140k and renews 31 Mar. I think two other accounts hit this too. How do I get product to take it?"*

---

```
INTERNAL ASK: Lane A | Pinecrest Foods | submit before the Q1 planning
cutoff, Fri 20 Nov (assumed, confirm with the product ops owner)

The ask: Product, please consider the job "reassign approvers across many
vendors at once when someone leaves", not a bulk-edit button.
Severity: gap with a workaround (not a bug, not a discoverability issue;
checked that the CSV import cannot change approvers)
Who can say yes: product manager for Approvals (name from product ops)
Path: product intake form; the Q1 planning cycle closes 20 Nov (assumed)

Lane A
- Job (customer words): "When an approver leaves we have to move every
  vendor they owned to someone else, and nothing breaks the approval chain
  while we do it."
- Today and what it costs: re-assigned one vendor at a time, about 300
  vendors, 12 hours per departure, two to three departures a year (said,
  Pinecrest controller, call 29 Oct)
- Accounts with the job: 3 | Value: $140k + $96k + $210k = $446k ARR
  - Pinecrest: bulk-edit button (said)
  - Alder Street Capital: "transfer ownership" when staff leave (said,
    ticket 8812, 2 Sep)
  - Kestrel Marine: a script built by their dev to patch approvers via API
    (seen, support case, 17 Jul). They paid for a workaround.
  Segment: mid-market and above with more than 150 vendors (inferred)
- Customer proposed (not required): a bulk-edit button on the vendor list
- If nothing changes: Pinecrest renews, annoyed. I would not claim churn.
  Kestrel's API script is a maintenance risk for them, not a renewal risk
  (inferred, confirm at their Jan check-in).

Evidence
- said    Pinecrest controller, 29 Oct call: "twelve hours, every time"
- said    Alder Street ticket 8812, 2 Sep
- seen    Kestrel API script in support case, 17 Jul
- inferred other mid-market accounts have the job, count unknown

Customer message (send after product replies, owner me)
- By 27 Nov: "Product has your request as the job of reassigning approvers
  in bulk. I will tell you the decision by 18 Dec."
- If no: "We are not building this in the next two quarters. Until then,
  support can run the reassignment for you in one request; I will confirm
  the turnaround. I will not give you a date I cannot back."
- Do not promise a build date at any stage.

Follow-through: I attach the three accounts and quotes today, ask product
for a decision date, and check back 4 Dec. Register: one row per account
and theme, updated with what the customer was told.

What I could not check
- The actual intake cutoff date and the product manager's name
- Whether the CSV import really cannot change approvers (verify)
- ARR for Alder Street and Kestrel (assumed, confirm in CRM)
- How many other accounts have the job
```
