# Sample output

*Invented example. Vendor "Ledgerline" and customer "Harbor and Pike Insurance" are fictional. Input the user gave: "Harbor and Pike, $240k, renews 30 April, 60 day notice. I talk to Dana in compliance every week, and I have met her analyst Raul. Procurement sent a vendor review form in October. I think the CFO signs but I have never spoken to anyone above Dana."*

---

```
WHO DECIDES: CFO (name not confirmed, assumed) | Met: no
Threads: 2 relationships (Dana, Raul), both in compliance: disguised single thread
Sceptic: not identified, map incomplete. Procurement is the likeliest source.

Map
| Person            | Position        | Met     | Last contact | Stance                                   |
| Dana, Compliance  | Champion, coach | Met     | 31 Oct       | said: "we need this for the exam"        |
| Raul, Analyst     | User            | Met     | 22 Oct       | seen: 90% of document uploads            |
| CFO               | Economic buyer  | Assumed | never        | inferred: signs over $100k               |
| Procurement lead  | Gatekeeper      | Aware   | never        | seen: vendor review form sent 9 Oct      |
| Head of IT        | Gatekeeper      | Aware   | never        | seen: approved SSO setup in March        |

Changed since last look
- 9 Oct: procurement vendor review form arrived (new step, none last year)
- 14 Oct: Dana moved from reporting to the COO to reporting to the CRO
  (remit change nobody logged; she may no longer hold budget)

Gaps and routes
- CFO unmet and unnamed | Route: ask Dana who signs and whether she will
  introduce the user at the March exam readout | Owner: me | By: 20 Nov
- No sceptic named | Route: ask Dana "who would push back on renewing?"
  on the next weekly | Owner: me | By: 12 Nov
- Procurement unmet | Route: answer the review form myself and ask for a
  15 minute call on their timeline | Owner: me | By: 18 Nov
- Single thread | Route: invite the CRO to the Q4 review as Dana's new boss
  | Owner: me | By: 5 Dec
- May not close: the CFO may refuse any vendor meeting. If so, Dana carries
  a one-page value summary and we price for contraction.

Opt-out date is 1 March (renewal minus 60 days). Gaps above must close by
mid-January to leave room.

What I could not check
- Whether the CFO actually signs (assumed, confirm with Dana)
- Whether Dana's reporting change moved her budget
- Who else sat in the October procurement review
