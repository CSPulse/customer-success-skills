# Sample output

*Invented example. Vendor "Quillstack" and customer "Tidewell Hospitality" are fictional. Input the user gave: "Call with Tidewell tomorrow 10:00, 30 minutes. Hana Brekke (ops director, my champion) and a new finance person, Jonas Aldous, is joining. They renew 31 Jan and I think they are unhappy about the export bug but I want a date for rolling out to the four new hotels."*

---

```
CALL PREP: Tidewell Hospitality | Fri 6 Nov, 10:00, 30 min | Hana Brekke, Jonas Aldous

10-minute version
Outcome: By the end of this call, Hana has agreed a go-live week for the four
  new hotels, and Jonas has said what finance needs to see to approve the seats.
Landmine: the invoice export bug open since 14 Oct (ticket has no owner).
  First line: "Before anything else: the export bug has sat for three weeks with
  no owner. It has one now, Priya on our support engineering team, and I will
  give you her date by Monday."
Ask: Hana to confirm the week of 7 Dec for hotels 15 to 18 by Fri 13 Nov.
  Fallback: a 20 minute scoping session with Jonas before 13 Nov.

Room
- Hana Brekke, ops director | wants the bug fixed and a rollout plan she can
  show her COO | can authorize rollout timing, not spend | met (4 calls)
- Jonas Aldous, finance | wants a reason the spend is justified | can approve
  or block anything over $50k (said, Hana, 2 Nov) | not met
Missing: the COO, who signed the original order. Not needed for this outcome.
Will retell this to: the COO, as "The bug has an owner and a date, and the four
  new hotels go live in December if finance agrees."

What changed on their side
- said     Hana: Jonas started 19 Oct and is reviewing every vendor line
- seen     Hotels 15 to 18 were acquired in Sept; no seats provisioned (admin)
- seen     Weekly active users flat since July (usage dashboard)
- inferred Jonas joining a 30 minute ops call means a spend review is open

Questions
1. Hana: when the month-end export fails, what does your team do by hand?
2. Jonas: how does finance judge whether a tool like this earns its place?
3. Hana: who else has to say yes before hotels 15 to 18 go live?
Avoiding: "Is Quillstack on the list to be cut?" Not yet. Ask Hana privately on
  Mon 9 Nov once the bug has a date.

Time (30 min, about 22 usable)
0-3 intros | 3-8 bug and owner | 8-15 questions 1 and 2 | 15-19 the ask |
19-22 next steps. Cut line: drop question 3 and send it by email.

If it goes sideways
- Complaint first: "That is fair, and here is exactly where it stands." Then
  the owner and date, and ask to keep going.
- Hana absent: run it with Jonas, outcome becomes his approval criteria.

What I could not check
- Whether the original business case had a number finance will recognize
- Contract value and notice date (assumed, confirm: 60 days, so 2 Dec)
```
