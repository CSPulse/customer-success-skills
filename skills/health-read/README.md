# health read

**Audit the health score. Don't just report it.**

A health score is a hypothesis almost nowhere treated as one. Most are designed once, in a room, with weights set by intuition, and never back-tested against the accounts that actually churned - so when one leaves anyway, "the score was green" gets offered as the explanation, when the score being green is what actually needed explaining.

This skill interrogates the number instead of relaying it. It sorts every input into measured, proxy, or absent - because most health scores are three or four proxies wearing the clothes of evidence, while the genuinely decisive stuff (a sponsor change, a budget reallocation, a competitor being evaluated) sits entirely outside what usage data can see. It breaks the composite apart by module, team, and user, since an average hides a dying signal behind a growing one, and asks what almost nobody asks: of the accounts that churned last year, what did their scores say three months out, and has the score ever been changed as a result? The output is a confidence level with a reason attached - "green" alone doesn't stand.

The failure this exists to prevent: **"the score was green" offered as an explanation for a churn, when the score being green is the thing that needs explaining.**

Part of the **Read the account** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Establish what the score measures | Every input on the table - what it is, its weight, who set that weight and when, whether it's ever changed |
| Sort inputs into measured, proxy, or absent | A labelled list showing exactly how much weight the number can carry, with the absent column - sponsor authority, budget change, a competitor in play - flagged as the gap that decides most churns |
| Break the composite apart | The single number split by module, team or site, admin activity against end-user activity, and a check for one power user propping up the whole aggregate |
| Read trajectory, not level | A comparison against the account's own history rather than a portfolio average, and an alert on drops that stay inside the "healthy" band |
| Check who the score is about | A direct answer to whether anything in the score reflects the actual buyer, as opposed to just the user population |
| Test whether the score has ever been right | The churned-accounts-three-months-out check, and the plain finding when - as is most common - that check has never been run |
| The written read | A completed audit stating what the score says, what it actually measures, what it's blind to, and a justified confidence level |

---

## Who this is for

CSMs, team leads, and anyone in RevOps who owns a health scoring model and has never had it questioned - especially useful right after a green account churns, or when someone is about to act on a score (an escalation, a save play, a portfolio triage) and needs to know how much weight it can bear.

---

## What this needs

**Minimum:** the score, and roughly what goes into it. If the user doesn't know the inputs, that itself is the first finding.

**Better with:** the input values for this account, the trend over the last two or three periods, and how the account compares to its own history.

**Best with:** the list of accounts that churned in the last year and what their scores were three months before they left - that single list settles most of what follows.

Missing context never blocks this skill - where an `account-context` document (what healthy usage looks like in this business) doesn't exist, it carries on and names the assumption.

---

## Install

**The easy way: one paste**

```
I want to install the health-read skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/health-read folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/health-read` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/score-audit.md` is the fill-in audit document itself.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
