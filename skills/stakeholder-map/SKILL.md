---
name: stakeholder-map
description: >
  Use when the user says "stakeholder map", "who actually decides", "who signs this", "map the account", "we are single-threaded", "who do I need to know". Produces a map sorted by what each person can do to the outcome, not title, with a met / not met column, a single-threading count and a dated route to close each gap. Not for a champion who just left (use champion-loss) or for the renewal call itself (use renewal-risk).
---

# Stakeholder Map

An org chart says what people are called. This says what each person can do to the account, who the user has really met, and what to do about the gaps.

## Start here

If the user gave names and roughly what they do, go straight to "Do this". If an "Account context" block exists in the conversation, use it for who signs in this business.

Otherwise ask for these in ONE message, then proceed with whatever comes back (do not wait for all three):

1. The people the user knows on the account, with role and last contact date
2. Who the user thinks signs, and whether they have ever spoken to them
3. Anything that changed lately: new executive, someone gone quiet, someone left

Gaps are the output here, not a blocker.

## Do this


1. **Sort by position, not title.** Economic buyer (controls the budget), champion (spends their own credibility for you), sceptic (argued against it or would), user, coach (explains how the org works, may not like the product), gatekeeper (procurement, security, legal; can block, cannot approve). One person can hold two.
2. **Add the met column.** Met means a real conversation, not a group call they attended. Aware of means known, never spoken to. Assumed means the role exists but cannot be named.
3. **Say who decides first.** If the economic buyer is aware-of or assumed, that is the account's largest risk and goes at the top of the output.
4. **Count the threads.** One relationship is no recovery path. Two in the same team is single-threading in disguise. Three or more across functions is coverage. Then ask: if the champion left this month, who inside the customer could explain why they bought?
5. **Track movement.** New arrivals, departures, remit changes, and anyone who used to reply in a day and now takes a week.
6. **Give each gap a route and a date:** an introduction from the champion, a review with the sponsor invited, an exec-to-exec ask, or a piece of value worth their fifteen minutes. Say honestly which gaps may not close.

## Output


```
WHO DECIDES: [Name, role] | Met: yes / no / only through [person]
Threads: [n] relationships, [single / disguised single / multi] threaded
Sceptic: [name or "not identified, map incomplete"]

Map
| Person | Position | Met | Last contact | Stance (said/seen/inferred) |

Changed since last look
- [arrival / departure / quiet / remit change, with date]

Gaps and routes
- [gap] | Route: [how] | Owner: [who] | By: [date]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.
Match its length and specificity: real dates, real counts, no placeholders in the final output.

## Rules

- **Every account has a sceptic.** A map without one is incomplete, not lucky, because the person nobody thought about is the one who surfaces at signature.
- **Seniority is not influence.** The signer is often not the most senior name, so ask what happens to the renewal if this person says no.
- **A group call is not a relationship.** Someone who sat on a webinar-style call has not been met, and counting them hides the real gap.
- **A champion's optimism is evidence about the champion.** Tag it `said` and name whose mouth it came from.
- **Sponsor silence while the working team stays engaged** usually means the decision moved above the user's line of sight.
- **A gap without a route is only a description.** The gap was already obvious; the route and date are the work.
- **The map goes stale.** An organization that reorganized last quarter is not the one on the page, so date the map and re-check it at every renewal checkpoint.

## Related (only if installed)


`champion-loss` when the sponsor left. `exec-conversation` to prepare the meeting once it is granted. `renewal-risk` to turn the map into a call.
