# Sample output

*Invented example. Vendor "Tallyfield" and customer "Orchard Row Foods" are fictional. Input the user gave: "Here is the excerpt from Tuesday's call with Orchard Row (I'm Dana, CSM). Build the commitments ledger as of today, Thu 5 Nov. Marcus is their ops director, Beth is IT, Ravi is our SE."*

```
Dana: Marcus, on 15 Oct you said the warehouse list would come the week after. It is 3 Nov and I do not have it.
Marcus: Still on me, sorry. You will have it by end of this week.
Beth: We need SSO on before the second site goes live on 1 Dec. Can you do that?
Dana: I think so. I will find out what SSO needs and come back to you by Thursday.
Beth: I can send the IdP metadata Monday.
Ravi: Good. Once I have it I will turn it on in staging first.
Marcus: Finance needs the order form for the extra 40 seats before the 20th or the PO slips to January.
Dana: Understood, I will get the order form to you by next Wednesday.
Marcus: I will try to get our CFO to join the January review.
Dana: Great. Let us look at a custom report for your cold-chain audit.
Beth: And the night shift needs training.
Dana: We will set something up in December.
```

---

```
COMMITMENTS: Orchard Row Foods | call Tue 3 Nov 2026 | as of Thu 5 Nov
6 firm open (4 ours, 2 theirs) | 2 soft | 1 due today, 1 due tomorrow

| # | Side | Owner | What | Due | Date basis | Quote | Status |
| 1 | Theirs | Marcus | Warehouse list for location mapping | Fri 6 Nov | stated; first promised ~Fri 23 Oct (implied), 13 days ago | "by end of this week" | Open, slipped once |
| 2 | Ours | Dana | SSO requirements back to Beth | Thu 5 Nov | stated | "come back to you by Thursday" | DUE TODAY |
| 3 | Theirs | Beth | IdP metadata to Ravi | Mon 9 Nov | stated, "I can send" read as firm | "send the IdP metadata Monday" | Open |
| 4 | Ours | Ravi | Enable SSO in staging | none | implied: after #3, confirm | "turn it on in staging first" | Blocked on #3 |
| 5 | Ours | Dana | Revised order form, +40 seats | Wed 11 Nov or Wed 4 Nov | implied, two readings, confirm | "by next Wednesday" | Open, or 1 day late |
| 6 | Ours | Dana | Night shift training session | "December" | implied month only, propose a date | "set something up in December" | Open |

Soft (not counted, watch)
- Marcus: "I will try to get our CFO to join the January review" - a try, and the unmet decider is the point; ask again in writing.
- Dana: "Let us look at a custom report for your cold-chain audit" - no owner, no date. Beth may already count it as agreed.

Not promises
- "SSO on before 1 Dec" is Beth's ask. Dana said "I think so". Nobody promised it, so do not confirm it until Ravi checks.
- Finance needs the order form before Fri 20 Nov: their constraint. It sets the real deadline for #5.

Close first
1. #2 SSO requirements to Beth, due today. Ask Ravi for the list first and send requirements only, with no go-live date.
2. #5 Confirm the date with Marcus. If he heard Wed 4 Nov we are already late. Verify pricing for the +40 seats before anything goes out.
3. #1 Warehouse list, due tomorrow. It gates the location mapping and so the 1 Dec second site. A second slip is theirs, and it is the early warning.

Our tasks: #2 today | #4 agree a date with Ravi by Mon 9 Nov | #5 order form to Marcus, confirm date today | #6 offer two December dates to Beth by Fri 13 Nov.

Nudge to Marcus (re: #1), send Thu afternoon
Subject: Warehouse list for the Dec 1 plan
Marcus, ahead of tomorrow: the warehouse list is the last input for the second site's location mapping. Is Friday still realistic? If it is easier, send what you have and we can start with it. And if something has moved on your side, tell me and we will re-plan 1 Dec together. Dana
Flag: confirm with Ravi that a partial list lets mapping start before offering it.

What I could not check
- Whether the order form went out earlier in the week (no sign of it in the excerpt)
- Whether "next Wednesday" was 4 or 11 Nov, and the +40 seat price
- Whether the 15 Oct promise was "the week of 19 Oct" or "by 23 Oct"
```
