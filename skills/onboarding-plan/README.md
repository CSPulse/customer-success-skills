# onboarding plan

**Build the plan the customer can point to, not the plan your team can close.**

Go-live is a vendor event. Adoption is a customer state. Most onboardings confuse them: the implementation record turns green, everyone moves on, and eleven months later the renewal conversation has nothing to point to, because nobody ever checked whether anything actually changed for the customer.

This skill forces success criteria to carry an actual baseline instead of an aspiration, names an owner on both sides for every milestone, and watches for the signals - a shrinking meeting, a sponsor who stops joining, a widening gap between seats bought and seats used - that predict a bad year long before the health score notices. It also treats the sales handover as evidence to check, not a briefing to trust, since the six things that have to transfer from sales are exactly the six most often lost.

The failure this exists to prevent: **a fully completed onboarding checklist attached to a customer who cannot say what changed.**

Part of the **Run the set-piece** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Read the handover | The six things that should have transferred from sales - objective, deal context, the relationship map including sceptics, open risks, every commitment made, and 30-day priorities - checked one by one, with the gaps named rather than assumed away |
| Validate, don't re-interrogate | A "here's what we understand, what would you change" opener instead of re-asking discovery, plus the operational questions sales never captures (how change actually gets approved, how the champion has changed) |
| Success criteria with a baseline | A target that can be falsified, converted from vague language ("complete the integration") into a number with a baseline ("cut manual reporting from 12 hours a week by half"), plus a diagnosis of *why* a sponsor won't commit - can't articulate it, lacks authority, or is hedging - because each needs a different response |
| The plan itself | First value separated from full value, a specific go-live date, named people with hours per week on the customer side, an agreed cadence, and one early win achievable in week one or two |
| The 90-day shape | Foundation and first value by day 30, expanded usage by 60, a measured result and review by 90 |
| The signal watchlist | Process signals (no named admin, security review discovered late), relationship signals (seniority quietly dropping, sponsor going quiet), and usage signals (flat growth, disconnected integrations) tracked from kickoff, not from the first QBR |
| The handover onward | A properly documented transfer to whoever owns the account after go-live - risk log, stakeholder map, success metrics, health baseline - so the account doesn't go quiet the moment the project plan closes |

---

## Who this is for

CSMs and implementation leads running a kickoff, especially in the window right after a deal closes when a handover from sales is supposed to happen and often doesn't. It's also for anyone inheriting a stalled onboarding and trying to work out whether the account is actually live or just has a closed task list, and for anyone about to walk into a renewal wondering whether the original success criteria were ever written down anywhere.

You don't need the full sales record to start. The skill is built to work from what was sold and flag, explicitly, everything it couldn't confirm.

---

## What this needs

**Minimum:** what was sold, and to whom. The skill builds the plan, the validation questions, and the risk list from that alone, and marks what it couldn't confirm.

**Better with:** the sales handover notes, the contract scope, and a stakeholder map - together these catch the gap between what was sold and what was actually bought.

**Best with:** the original business case and access to product usage data, so success criteria can be instrumented rather than left aspirational.

Missing context never blocks this skill - it builds the plan from whatever transferred and states plainly, in the output, what it could not confirm, which itself becomes one of the risks to close.

---

## Install

**The easy way: one paste**

```
I want to install the onboarding-plan skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/onboarding-plan folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/onboarding-plan` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method - plain markdown, no dependencies.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
