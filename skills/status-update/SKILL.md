---
name: status-update
description: >
  Use when the user says "write my standup", "weekly update for my manager", "end of day wrap", "what did I get done this week", "status update", "update for my boss". Turns rough notes or a pasted activity list into a standup (done, next, blocked by account), a weekly update (highlights, lowlights, asks, renewals, commitments) or an end-of-day wrap. Not for a team lead rolling up several CSMs (use team-rollup) or a note to a customer (use customer-update).
---

# Status Update

Paste rough notes. Get the update you owe someone, led by outcomes, with the bad news stated plainly and the asks specific.

## Start here

If the user pasted notes or an activity list and said which update (standup, weekly, wrap), go straight to "Do this". If the kind is not stated, pick by the day (Friday means weekly, late afternoon means wrap) and say which you chose.

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Which update, and who reads it
2. The notes, in any state: bullets, a task list, call summaries
3. Anything that went wrong this period that the reader does not know yet

If an "Account context" block exists in the conversation, use it. If a CRM or mailbox is connected, you may read it. Otherwise use the paste only.

## Do this

1. **Turn activity into outcomes.** "Had calls with Orrin" becomes "Orrin sponsor agreed to bring the VP of Ops to the next review". If there was no outcome, say "no movement" rather than dress it up.
2. **Sort facts from hope.** Mark each claim `said` (a customer told us, name who), `seen` (we observed it) or `inferred` (our read). Hope goes in a line called "My read", never in the outcome.
3. **Put the lowlights in, plainly,** each with a plan and a date. Do not bury them under the wins or soften them into "areas of focus".
4. **Make every ask specific:** a named person or team, the action, and a date. If the user cannot name a person, write "[who]" and list it under What I could not check.
5. **Name the measure on every count** (accounts touched, commitments made, renewals with a date inside 90 days). A bare number is dropped.
6. **Cut to length.** Standup and weekly: about 200 words. Wrap: ten lines. Group standup items by account.
7. **Close with the sources:** what was read, and what was not (CRM, usage, tickets, calendar).

## Output

Pick the one that matches. Verdict line first, always.

```
WEEKLY UPDATE: week of [Mon date] to [Fri date] | [n accounts, ARR] (the user's figure)
Bottom line: [one sentence: the state of the book and the one thing needing help]
Highlights (outcomes): 3 to 5, each [account, $, what changed, said/seen]
Lowlights: 3 to 5, each [account, $, what went wrong, plan, date]
Asks: [who], [action], by [date]
Renewals: [n] with a date inside 90 days, $[x]. [account, $, date, fact | my read]
Commitments to customers: [n] made, [n] on time, [n] late, [n] open, next due [date]
Sources: read [..]. Not checked [..].

STANDUP: Done / Doing next / Blocked (name who unblocks), grouped by account
WRAP: Closed today | Slipped (and why) | Carry over | Tomorrow's first three
```

A filled weekly example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Lead with outcomes, not activity.** A manager cannot act on "had 11 calls", and activity read as effort invites more activity instead of results.
- **Bad news now is cheaper than bad news later.** A lowlight that surfaces in the forecast call costs the reader their own credibility upward, so put it in this update with a plan.
- **Asks are a name, an action and a date.** "Need help with Kestrel" gets sympathy, and "Director, 20 minutes with their practice owner by Fri 13 Nov" gets done.
- **Separate what is true from what is hoped.** A champion's optimism is a `said`, and a renewal "looking good" is a read. Mixing them is how a forecast goes wrong quietly.
- **Every count names its measure.** "6 commitments" is ambiguous, while "6 made, 4 on time, 1 a day late, 1 open" can be checked.
- **Say what was not read.** An update written from memory looks identical to one written from the CRM, so state the sources and let the reader weigh it.
- **Do not pad a quiet week.** Short and true beats long and padded, and the reader learns to trust "no movement".
- **Credit others by name.** A win that depended on support or sales is reported with their name, because the reader checks and the credit is cheap.

## Related (only if installed)

`what-do-i-owe` for the commitments count. `team-rollup` if the user leads a team. `renewal-risk` for the read behind a renewal line. `internal-ask` when an ask needs a fuller case.
