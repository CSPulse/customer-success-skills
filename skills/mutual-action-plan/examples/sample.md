# Sample output

*Invented example. Vendor "Routewise" and customer "Hollis Brothers Building Supply" are fictional. Input the user gave: "Hollis Brothers signed Monday, 11 branches, Routewise delivery scheduling. Gwen Pruitt is the sponsor, Dev Anand is their IT lead, Marisol Reyes runs dispatch at Branch 1. Kickoff is Mon 9 Nov. They want everyone off the whiteboard by 8 Jan and freeze all changes 24 Dec to 3 Jan. Make me a plan I can send them."*

---

```
MUTUAL ACTION PLAN: Hollis Brothers and Routewise | onboarding | goal date Fri 8 Jan 2027

Goal (their words): "Dispatch stops using the whiteboard. All 11 branches book
and route deliveries in Routewise by Fri 8 Jan."
Sponsors: Gwen Pruitt (Hollis) | Lena Okafor (Routewise)

| # | Milestone or DECISION | Owner (side) | Date | Needs | Status |
| 1 | Kickoff: confirm goal, dates, owners | Gwen Pruitt (Hollis) | Mon 9 Nov | none | Agreed |
| 2 | Send branch list, delivery zones, driver roster | Dev Anand (Hollis) | Fri 13 Nov | 1 | Proposed |
| 3 | Send single sign-on settings sheet | Ravi Shah (Routewise) | Fri 13 Nov | 1 | Proposed |
| 4 | DECISION: choose the 2 pilot branches | Gwen Pruitt (Hollis) | Wed 18 Nov | 2, our branch comparison Mon 16 Nov | Proposed |
| 5 | Load zones and drivers into the test environment | Ravi Shah (Routewise) | Fri 20 Nov | 2 | Proposed |
| 6 | Turn on single sign-on for pilot users | Dev Anand (Hollis) | Wed 25 Nov | 3, 5 | Proposed |
| 7 | Release 6 pilot dispatchers for training day | Marisol Reyes (Hollis) | Mon 30 Nov | 4, 6 | Proposed |
| 8 | Pilot go-live: whiteboard off at 2 branches | Marisol Reyes (Hollis) | Mon 7 Dec | 7 | Proposed |
| 9 | Pilot read: bookings, late deliveries, feedback | Lena Okafor (Routewise) | Tue 15 Dec | 8 | Proposed |
| 10 | DECISION: roll out to the other 9, or hold | Gwen Pruitt (Hollis) | Wed 16 Dec | 9 | Proposed |
| 11 | Train the other 9 branches (4 remote sessions) | Lena Okafor (Routewise) | Thu 17 to Fri 18 Dec | 10, dispatchers released | Proposed |
| 12 | All 11 branches booking in Routewise, sign-off | Gwen Pruitt (Hollis) | Fri 8 Jan | 11 | Agreed |

If a decision is late
- Row 4 (pilot branches): rows 5 to 8 slip day for day, and the pilot cannot start
  before the freeze without squeezing rows 10 and 11.
- Row 10 (roll out or hold): the 9 branches cannot be trained before 24 Dec, so
  8 Jan moves to after the freeze and we agree a new date together.

Shared risks
- Training on 17 to 18 Dec, go-live after the 24 Dec to 3 Jan freeze. Trigger:
  pilot dispatchers still using the whiteboard on more than 3 deliveries a day.
  Mitigation: 20 minute refreshers on Tue 5 Jan.
- One IT contact for rows 2 and 6. Trigger: either slips 3 working days.
  Mitigation: a named backup in IT, agreed at kickoff.

Review: Tuesdays 10:00, 20 minutes. Gwen, Dev, Marisol, Lena, Ravi. If a row
slips more than 3 working days we raise it with Gwen that week, so the dates
get reset together instead of drifting.

Cover note
Gwen, here is the plan from kickoff to the 8 Jan finish. Every date marked
Proposed is yours to change, so please fix anything that clashes with your
calendar. Two decisions sit with you, on 18 Nov and 16 Dec, and each row says
what it needs.

--- below this line is for the user, not the customer ---
Proposed, not yet agreed: every date except rows 1 and 12. Dev's and Marisol's
hours have not been confirmed with them (assumed, confirm at kickoff).
What I could not check
- Gwen's goal wording comes from the sales call notes (confirm at kickoff)
- Whether Routewise can import a driver roster file (ask Ravi before sending)
- Whether single sign-on needs a security review at Hollis (could add weeks)
- Whether branches differ in weekend dispatch hours
```
