# Health Score

**Either an honest verdict on how far an existing score can be trusted, or a small explainable score the team can validate.**

**What goes wrong without it:** A score that was green the quarter before a churn, offered as the explanation when the green score is the thing that needs explaining.

Part of [customer-success-skills](../../#readme).

## What it does

1. List each input, its weight, who chose it and when
2. Label every input `measured` (the thing itself is counted), `inferred` (derived from something else) or `proxy` (a stand-in for value, like logins)
3. Break the composite apart: by module, team and role
4. Backtest: for each churned account, what did the score say 90 days before?
5. Give a trust level and what to fix first
6. Pick 6 to 12 signals the team can explain in one sentence each, with at least one from the buyer side (sponsor contact, executive meeting), not usage only
7. Score each as change against the account's own baseline, not a portfolio average
8. Add a qualitative CSM override with a required reason and an expiry date
9. Specify what to validate: backtest on past outcomes (several dozen before trusting weights), check against expansion as well as churn, and recalibrate on a schedule

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "audit our health score"
- "the score said green but they churned"
- "build a health score"
- "is our health score any good"
- "why is this account red"
- "backtest the score"

## Who this is for

Written for team leads and heads of customer success. Included in: `cs-team-lead-toolkit`, `cs-leader-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

- Whatever you know about the situation

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the health-score skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/health-score folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- Most scores were never backtested
- Trust needs outcomes
- Score the change, not the level
- Averaging hides the disagreement
- Usage describes the user; the renewal is decided by the buyer
- Keep it explainable
- Validate against expansion too

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
