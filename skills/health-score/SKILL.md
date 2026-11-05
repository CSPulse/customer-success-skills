---
name: health-score
description: >
  Use when the user says "audit our health score", "the score said green but they churned", "build a health score", "is our health score any good", "why is this account red", "backtest the score". AUDIT mode sorts inputs into measured, inferred and proxy and backtests against churned accounts 90 days before they left. BUILD mode designs 6 to 12 explainable signals scored against each account's own baseline, with a CSM override. Not for one account's renewal call (use renewal-risk) or book-level coverage (use coverage-model).
---

# Health Score

Either an honest verdict on how far an existing score can be trusted, or a small explainable score the team can validate.

## Start here

Pick the mode from the request. If unclear, ask one question: "Audit a score you have, or build one?" If an "Account context" block exists in the conversation, use its idea of healthy usage.

AUDIT needs: the inputs and weights (rough is fine), and, if possible, accounts that churned in the last year with their scores 90 days before. BUILD needs: the signals available, the product's usage rhythm, and what counts as retained.

Ask for at most 3 things in ONE message, then proceed. Missing data becomes a line under What I could not check.

## Do this

**AUDIT**
1. List each input, its weight, who chose it and when. Weights nobody can explain are a finding.
2. Label every input `measured` (the thing itself is counted), `inferred` (derived from something else) or `proxy` (a stand-in for value, like logins). Name what is absent: sponsor change, budget, competitor, a stale value metric.
3. Break the composite apart: by module, team and role. Averaging a growing signal with a dying one hides both.
4. Backtest: for each churned account, what did the score say 90 days before? For red accounts a year ago, how many left? Report hits, misses and false alarms with counts.
5. Give a trust level and what to fix first.

**BUILD**
1. Pick 6 to 12 signals the team can explain in one sentence each, with at least one from the buyer side (sponsor contact, executive meeting), not usage only.
2. Score each as change against the account's own baseline, not a portfolio average.
3. Add a qualitative CSM override with a required reason and an expiry date.
4. Specify what to validate: backtest on past outcomes (several dozen before trusting weights), check against expansion as well as churn, and recalibrate on a schedule.

## Output

```
HEALTH SCORE: [AUDIT / BUILD] | [Company or score name]

Verdict: [Trust fully / trust as adoption only / do not act on it] because [one sentence]. Confidence: low / medium / high

AUDIT: Inputs
| Input | Weight | Class (measured/inferred/proxy) | Note |
Backtest: [n] churned, [n] scored green 90 days before, [n] red. False alarms: [n]
Hidden by averaging: [what]. Blind to: [what]

BUILD: Signals
| Signal | Measure | Baseline | Alert when | Why it matters |
Override: [rule]. Validate: [steps]

Fix first: [action] | Owner | By

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length.

## Rules

- **Most scores were never backtested.** A number built in a meeting and never checked against churners is a hypothesis; the 90 day lookback is the cheapest test there is.
- **Trust needs outcomes.** With a handful of churns, weights are noise; collect a few dozen outcomes (a common default, set your own) before tuning.
- **Score the change, not the level.** A 7 that was 8.5 last month says more than a 7, and a normal level for one deployment alarms another.
- **Averaging hides the disagreement.** If the score says green and the CSM says red, one is wrong; splitting the difference destroys the information. Find out which.
- **Usage describes the user; the renewal is decided by the buyer.** A usage-only score is an adoption score, so say so.
- **Keep it explainable.** Past roughly a dozen signals nobody can say why an account is red, and an unexplained red gets ignored.
- **Validate against expansion too.** A score that predicts churn but misses growth steers the team away from the accounts that matter most.

## Related (only if installed)


`renewal-risk` for a single account call. `coverage-model` to set touch levels from the score. `portfolio-review` to spot reads that only echo the score.
