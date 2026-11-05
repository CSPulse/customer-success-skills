---
name: team-rollup
description: >
  Use when the user says "team rollup", "weekly roll-up for my VP", "what do I send upward", "summarize my CSMs' updates", "leadership summary for the week", "my director wants the team status". Turns CSM updates and account reads into one page for leadership: asks first, the week in three lines, portfolio figures, risks that need help, renewals at 30, 60 and 90 days, wins and commitments. Not for one CSM's own update to a manager (use status-update).
---

# Team Rollup

Paste the CSMs' updates and your own notes. Get the one page your leadership reads, with the asks at the top and nothing in it they will first hear about somewhere else.

## Start here

If the user pasted updates from two or more CSMs, or the lead's own notes with account names, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Each CSM's update, rough is fine, plus the lead's own notes
2. Book ARR, account count, and last week's roll-up if there is one (so change shows)
3. Renewals in the next 90 days with ARR and date, and which are flagged

If an "Account context" block exists in the conversation, use it for segment and definitions. If the user has a scorecard, use its definitions so the numbers match.

## Do this

1. **Inventory the inputs.** List every CSM and whether their update arrived. A missing update is reported as missing, never as "no news".
2. **Find what needs leadership.** Per risk: a decision, executive time, an exception, or a resource. Write each as a specific ask: a name, an action, a date, and why now. If there are no asks, write that plainly.
3. **Write the week in three lines.** Lead with the bad news if there is any, then the asks, then the wins. State a bad week as a bad week with its cause.
4. **Build the figures** with the measure named: book ARR and accounts, ARR flagged at risk, renewals in the next 30, 60 and 90 days (count and ARR), and one or two scorecard metrics. Show the change since last week.
5. **List risks that need help.** Account, ARR, renewal date, mechanism in one line, owner, next date, status (new, worse, same, better). Where the lead disagrees with a CSM's rating, say so and tag it inferred.
6. **List wins and commitments.** Name the person for each win, including hard saves. List what leadership was promised last time, with a status against each.
7. **Finish with what is unverified,** and trim to one page.

## Output

Use this skeleton. Keep it to one page.

```
TEAM ROLL-UP: week ending [Friday date] | [n] CSMs | book $[ARR], [n] accounts

Asks of leadership
1. [Ask: decision / exec time / exception], [who], by [date]. Why: [one line]

The week in three lines
[bad news plain, then asks, then wins]

Figures ([measure named], change since last week)
| Book ARR | Flagged at risk | Renewals 30 / 60 / 90 days | [scorecard metric] |

Risks that need help
| Account | ARR | Renews | Mechanism | Owner | Next date | Status |

Wins: [person] - [outcome, number]
Commitments to leadership: [what] | [due] | [on track / late / done]

What I could not check
- [missing updates, carried-forward numbers, unverified ratings]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Asks first.** Leaders skim the top, and this page exists to change their week, so what you need from them goes before what happened.
- **No surprises.** A risk first seen at the board is a failure of this page, so list every flagged account the week it is known, with an owner and a date, even when unresolved. A line now costs less than credibility later.
- **Do not hide a bad week.** Explain it with the cause and what changes, because leadership learns it from finance anyway and then doubts the good weeks.
- **Use the scorecard's definitions.** A number that changed its definition mid-quarter reads as a trend, so flag any redefinition.
- **Every count names its measure.** "7 of 78 reported accounts outside cadence" can be checked, and "coverage is fine" cannot.
- **Separate what the CSM said from what the lead reads.** Averaging CSM optimism into the roll-up passes it upward, so mark disagreements inferred.
- **Credit people by name and fairly.** Include saves and hard calls, not only closes, because unrecognized work stops being reported.
- **A missing update is a finding.** Carry forward last week's figures only with a label, because stale numbers presented as current are the quietest surprise.

## Related (only if installed)

`cs-scorecard` for the definitions behind the figures. `renewal-forecast` for the dollar forecast under the renewals row. `internal-ask` to write any single ask at full length. `portfolio-review` to test the CSMs' ratings before they go in.
