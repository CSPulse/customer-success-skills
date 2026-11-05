# CS Scorecard

**Paste an account list or a few numbers. Get a scorecard with exact definitions, the values computed from your paste with the arithmetic shown, the red flags and what to change.**

**What goes wrong without it:** A dashboard full of metrics with no definitions. Two people read the same number differently, and a strong net figure hides a leaking base.

Part of [customer-success-skills](../../#readme).

## What it does

1. Fix the level and cadence
2. Fix the cohort
3. Compute the lagging set, showing the arithmetic
4. Fill the leading set from what is pasted
5. Pair each metric with a counter-metric
6. Judge against the book's own trailing baseline
7. Name up to three red flags and one change

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "CS scorecard"
- "CS metrics"
- "what should we measure"
- "KPIs for my book"
- "how do I report on my team"
- "define our retention metrics"

## Who this is for

Written for team leads and heads of customer success. Included in: `cs-team-lead-toolkit`, `cs-leader-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. The level and the reader: one CSM's book, a team, or the whole function
2. The list: account, ARR at the start of the period, ARR now, renewal date, health if you has one
3. The period, and which metrics are already reported

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the cs-scorecard skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/cs-scorecard folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- Report gross next to net, every time
- Every metric has a numerator, denominator, period and owner
- Every count names its measure
- Pair each activity metric with an outcome
- Weight health by ARR, not by count
- Use the book's own trailing baseline
- Leading metrics weekly, lagging monthly or quarterly
- A metric nobody can move is a report, not a scorecard
- State coverage

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
