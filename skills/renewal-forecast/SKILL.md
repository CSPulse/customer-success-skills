---
name: renewal-forecast
description: >
  Produces a renewal and expansion forecast in dollars with a stated confidence, with contraction sized separately and correlated risks named as one bet rather than thirty. Trigger whenever the user says "renewal forecast", "forecast the quarter", "what will we renew", "gross retention forecast", "commit number", "roll up my team's renewals", "forecast call", "what is the risk to the number", or is preparing a retention number for finance or a board. It sets evidence-based entry criteria for each category, separates timing slip from loss, pulls auto-renewals out of the judgement pool, and tracks per-forecaster accuracy so the number stops being a personality test. Use renewal-risk for the read on any single account, and portfolio-review for the meeting where the reads get challenged.
---

# Renewal Forecast

A forecast is not a sum of opinions. It is a commitment with a confidence attached, and the two most common ways it goes wrong are structural rather than analytical: **contraction is not counted, and correlated risks are added up as though they were independent.**

The failure this exists to prevent: **the logo forecast.** Ninety-four per cent of accounts renewing, reported as a healthy quarter, while the dollars come in eleven per cent light because a third of them renewed smaller.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: contract shapes, pricing model and segments. On consumption or hybrid pricing the whole shape of this changes. Where it is absent, carry on and name the assumption.

**Minimum: the accounts up for renewal, their values and their dates.** Enough for a dollar forecast with honest confidence bands.

**Better with** a current risk read per account, the auto-renewal and notice terms, and last quarter's forecast against what actually landed.

**Best with** two or more quarters of forecast-versus-actual by forecaster, which is what turns this from arithmetic into calibration.

---

## Step 1: Forecast dollars, and size contraction separately

Three numbers, not one:

- **Gross renewal dollars**, the value at risk that renews at all
- **Contraction**, the dollars lost from accounts that renew smaller
- **Expansion**, kept apart from renewal so a good expansion quarter cannot conceal a bad retention one

**Contraction is where most misses live.** An account labelled at risk of churn is usually at risk of renewing thirty per cent smaller, and a binary renew-or-not model cannot represent that at all. Every account in the forecast needs a value range, not a flag.

Report gross retention and net retention separately, always. A single blended number lets an expansion quarter hide a retention problem for two quarters, which is exactly long enough for it to become structural.

## Step 2: Give every category an entry criterion made of evidence

Categories without written entry criteria become a mood ring. Each one needs a test somebody else could apply.

- **Commit.** The decision is made by the person who makes it, or the term auto-renews and the notice window has passed. Evidence: written confirmation, an executed order, or an expired notice date
- **Likely.** The decider is known and engaged, no Tier 1 risk signal is live, and the value is agreed. Evidence: a named decider you have spoken to this quarter
- **At risk.** A named mechanism, not a feeling. If nobody can state the mechanism it is not at risk, it is unknown, which is its own category and usually a bigger problem
- **Lost.** A decision communicated, or a notice served

**"Unknown" must be a permitted category.** Without it, unknowns get filed as likely, because likely is the comfortable default, and that single behaviour accounts for a large share of forecast misses.

## Step 3: Pull the auto-renewals out

Accounts that renew on silence are in the number whether anyone touched them or not. Mixing them with accounts requiring an active decision inflates apparent accuracy and hides where the judgement actually is.

Split the book into: auto-renewing with the notice window passed, auto-renewing with the window still open, and actively decided. The middle group is the one people forget, and it is the group where a customer's inaction is doing your forecasting for you until the day it does not.

## Step 4: Find the correlated risk and forecast it as one bet

**The most important step and the one almost universally skipped.**

Thirty accounts flagged at risk for the same reason are not thirty independent events. They are one event that has not happened yet, and treating them as independent understates the variance enormously. A portfolio that looks like a manageable spread of small risks can be a single unhedged bet on one pricing decision, one deprecation, or one segment's budget cycle.

Group the at-risk book by mechanism, not by account:

- The same product gap
- The same price change
- The same segment or industry under pressure
- The same acquiring parent standardising vendors
- The same integration partner going away

Then forecast the group. **If the mechanism resolves, most of them renew; if it does not, most of them do not.** That is a different number and a different conversation from thirty separate probabilities, and it is the conversation a board actually needs.

## Step 5: Separate slipping from losing

A renewal that moves a quarter is not a loss, but it destroys the quarter it left, and it is frequently reported as at-risk when the real issue is timing.

Track them apart: at risk of not renewing, and at risk of not renewing *this period*. The plays are different. Slip is usually procurement, a signature chain or a budget cycle, and it is often fixable with attention to their process rather than to their satisfaction.

## Step 6: Calibrate the forecasters, not just the forecast

Without this, a roll-up is an average of personalities. The two failure shapes are well known and they cancel out only by accident:

- **Sandbagging.** An at-risk book that renews at ninety-five per cent. The tell is risk flagged without a play attached and never changing state
- **Happy ears.** Everything likely, evidence verbal and single-sourced, usually from a champion who does not control budget

Track forecast against actual per person over time. Two quarters is enough to see it. Then adjust the roll-up explicitly and say that you are doing it, rather than silently discounting one person's numbers, which is how a forecast process loses the trust it needs.

**Where a model and a human disagree, do not average them.** One of them is wrong, and splitting the difference destroys the information that the disagreement contained. Find out which.

## Step 7: State what would make this wrong

Three lines that make a forecast a forecast rather than a report:

- **The confidence**, as a range with the assumptions named
- **The single biggest thing that would move it**, which after Step 4 is usually one correlated mechanism
- **What you need**, and by when, to change the number rather than merely observe it

Then record the number, so Step 6 has something to calibrate against next quarter.

---

## Output

1. **Three numbers**: gross renewal dollars, contraction, expansion, each as a range
2. **Category breakdown** with the entry criterion each account met
3. **The auto-renewal split**, including the window-still-open group
4. **The correlated risks**, grouped by mechanism and forecast as single bets
5. **Slip against loss**, separated
6. **Forecaster calibration**, and any explicit adjustment made to the roll-up
7. **What would make this wrong**, and what you need to change it
8. **What you could not check**

`assets/forecast-sheet.md` carries the categories, the criteria and the correlation grouping.

---

## Failure modes

- **Forecasting logos.** Ninety-four per cent renewing and the dollars eleven per cent light
- **No contraction line.** The place most misses actually live
- **A blended retention number** that lets expansion hide a retention problem for two quarters
- **Categories with no written entry criteria**, which makes them a mood ring
- **No "unknown" category**, so unknowns get filed as likely
- **Auto-renewals mixed into the judgement pool**, inflating apparent accuracy
- **Correlated risks added up as independent**, understating variance badly and hiding a single unhedged bet
- **Slip reported as risk**, so the play is satisfaction when the problem is a signature chain
- **Never calibrating the forecasters**, leaving a roll-up that is an average of personalities
- **Averaging a model and a human who disagree**, which destroys the information in the disagreement

---

## What good looks like

- The number is dollars, with contraction on its own line and a range around it
- Every account's category has an evidence test someone else could apply
- Unknowns are counted as unknown
- The at-risk book is grouped by mechanism, and the largest group is named as one bet
- Slip and loss are separate numbers
- The roll-up carries a stated adjustment where a forecaster's calibration warrants it
- Last quarter's forecast was compared against what landed, by person

---

## Related skills

- `renewal-risk` for the read on any single account this forecast is built from
- `portfolio-review` for the meeting where those reads get challenged before they enter the number
- `renewal-negotiation` for the accounts where contraction is being decided
- `nrr-narrative` for turning the resulting numbers into something a board follows
- `churn-postmortem` for whether last quarter's misses shared a mechanism

---

## Supporting files

- `assets/forecast-sheet.md` - categories, criteria and correlation grouping, usable without an assistant
