# renewal forecast

**A forecast in dollars, with a confidence attached - not a sum of opinions.**

Ninety-four percent of accounts renewing gets reported as a healthy quarter. Then the dollars land eleven percent light, because a third of those renewals came in smaller and nobody had a line in the forecast for contraction - invisible until it's too late to do anything about it.

That gap comes from two structural mistakes: contraction doesn't get counted as its own number, and correlated risks get summed as though independent. This skill forces both apart - gross renewal, contraction and expansion on three separate lines instead of one blended figure, a written entry criterion for every category (commit, likely, at risk, lost, unknown), and at-risk accounts sharing the same mechanism forecast as the single bet they actually are, because thirty accounts citing the same price change aren't thirty independent probabilities.

The failure this exists to prevent: **the logo forecast: ninety-four percent of accounts renewing, reported as a healthy quarter, while the dollars come in eleven percent light because a third of them renewed smaller.**

Part of the **Lead the function** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Forecast dollars, contraction separately | Three numbers - gross renewal, contraction, expansion - each as a range, so a good expansion quarter can't conceal a bad retention one |
| Give every category an evidence-based entry test | Written criteria for commit, likely, at risk, and lost, plus a permitted "unknown" category so unknowns stop getting filed as likely by default |
| Pull the auto-renewals out | The book split into auto-renewing with notice passed, auto-renewing with the window still open, and actively decided - so silent renewals stop inflating apparent accuracy |
| Find the correlated risk and forecast it as one bet | The at-risk book grouped by mechanism - same product gap, same price change, same segment under pressure - and forecast as a group instead of thirty separate probabilities |
| Separate slipping from losing | Accounts at risk of not renewing this period kept apart from accounts genuinely at risk of not renewing at all, because the plays and the owners are different |
| Calibrate the forecasters, not just the forecast | Forecast-versus-actual tracked per person, so sandbagging and happy ears get named and adjusted for explicitly instead of averaged away |
| State what would make this wrong | A confidence range with assumptions named, the single biggest thing that could move the number, and what's needed by when to actually change it |

---

## Who this is for

CS and revenue leaders building a retention or renewal number for finance, a board, or their own leadership - anyone rolling up a team's individual reads into one commitment and needing it to survive contact with what actually lands.

---

## What this needs

**Minimum:** the accounts up for renewal, their values and their dates - enough for a dollar forecast with honest confidence bands.

**Better with:** a current risk read per account, the auto-renewal and notice terms, and last quarter's forecast against what actually landed.

**Best with:** two or more quarters of forecast-versus-actual by forecaster, which is what turns this from arithmetic into calibration.

Missing context never blocks this skill - where an `account-context` document exists, contract shapes and pricing model change how the whole forecast is structured (consumption and hybrid pricing especially); where it's absent, the skill carries on and names the assumption.

---

## Install

**The easy way: one paste**

```
I want to install the renewal-forecast skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/renewal-forecast folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/renewal-forecast` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/forecast-sheet.md` carries the categories, the entry criteria, and the correlation grouping, usable without Claude at all.

---

## What good looks like

- The number is dollars, with contraction on its own line and a range around it
- Every account's category has an evidence test someone else could apply
- Unknowns are counted as unknown
- The at-risk book is grouped by mechanism, and the largest group is named as one bet
- Slip and loss are separate numbers
- Last quarter's forecast was compared against what landed, by person

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
