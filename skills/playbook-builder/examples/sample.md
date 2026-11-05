# Sample output

*Invented example. "Wrenfield Software" and every customer named are fictional. Input the user gave: "New customers go quiet after kickoff and nobody notices until the day-90 review. I want a repeatable play for low adoption at day 45. 8 CSMs, 90-day onboarding, accounts from $30k to $120k. Last month Pinewood Dental was the example."*

---

```
PLAY READY: Low adoption at day 45. Trigger: under 40% of licensed users active, owner
Onboarding CSM, decision by day 14, escalation by day 21. v1, 5 Nov 2026.

Use when: an account is 38 to 45 days past contract start and, in the Monday usage
report, fewer than 40% of licensed users logged in over the last 14 days, OR the
first-value milestone from the kickoff plan has no date. Detected by CS ops, checked
weekly. (40% is a common default, set your own.)
Do not use when: under 10 licensed users (digital onboarding), a signed delayed
go-live, the champion has left (champion play), or the customer is already escalated.
Owner: Onboarding CSM | Backup: pod lead | Escalates to: CS manager, then exec sponsor

Steps
1. Day 0 (Monday) | Post the risk status in the account record with the usage numbers
   | Leaves: dated note, within 2 business days
2. Day 0 to 2 | Diagnose from data before calling: invited vs logged in, and which
   kickoff goal has no activity. Four causes: no active owner, wrong users invited,
   technical blocker, goal changed | Leaves: one-line cause (inferred)
3. Day 2 | Send message A to the sponsor | Leaves: sent note, working session requested
4. Day 5 to 7 | 45-minute working session with sponsor and team lead: pick one user
   group and one use case, set a 14-day target | Leaves: written plan, three dated
   actions, sent the same day
5. Day 10 | Check usage. If flat, message the team lead directly | Leaves: updated note
6. Day 14 | Decide: resolved or escalate | Leaves: decision in the record
Mistake to avoid: a generic "just checking in" email. It names no number and asks
for nothing, so it is not answered.

Resolved when: two consecutive weekly reports at or above 40% AND the first-value
milestone is done or dated in writing by the sponsor.
Escalate when: not resolved at day 14. By day 21: CS manager and exec sponsor call,
success plan rescoped in writing, renewal record set to "at risk, mechanism: adoption".

Messages (drafts, owner edits and sends)
A. Subject: [Account] rollout, where we are. "Hi [Sponsor], [x] of [y] licensed
   people have logged in over the last two weeks, and [goal from kickoff] has no
   activity yet. I think it is [cause]. Could we take 45 minutes this week with
   [team lead] to pick one group and one use case to get live by [date]?"
B. Invite: "Goal: [use case] live for [group] by [date]. Bring: who should be
   invited, and what is blocking them."
C. To manager: "[Account], day [n], [x]% active, plan sent [date], not moving
   because [cause]. I need [exec call / scope change] by [date]."

Measures: ran on time (risk note within 2 business days) | worked (resolved by
day 21) | cost (owner hours, and one line of customer reaction). Review after
10 plays or 31 Mar 2027.

Test case: Pinewood Dental, 80 licensed, 12 active at day 45. The old process sent a
check-in at day 60. The play would have fired at day 45 and found that the invite
went to front-desk staff, not the hygienists named at kickoff. Change made: step 2
now compares the invite list with the roles named in the kickoff plan.

What I could not check
- Whether CS ops can produce the Monday report with the 14-day window
- Whether the 40% line suits every product tier
- Whether a first-value milestone is recorded for every account at kickoff
```
