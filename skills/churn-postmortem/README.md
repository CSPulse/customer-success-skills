# churn postmortem

**Find the mechanism, not the category.**

Somebody asks why the account left, and the answer is "budget cuts" or "they got acquired" or "low adoption." The deal gets marked closed-lost, and nine months of nobody calling the sponsor never makes it into the record - the stated reason is polite, often partly true, and almost never the actual mechanism.

This skill runs the postmortem properly instead of filing a label: the stated reason kept separate from the causal chain, the date the account was actually lost marked apart from the date anyone noticed, and what was genuinely detectable at the time kept apart from what's only obvious in hindsight. Then it checks what most postmortems skip - whether this loss was one of a correlated set a single fix would prevent, or a true one-off.

The failure this exists to prevent: **"it was an acquisition" filed as a cause, concealing nine months of nobody calling.** A postmortem that produces a category rather than a mechanism produces no change.

Part of the **Read the account** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Record the stated reason | What the customer said, in their words, dated, and set aside rather than accepted as the finding |
| Reconstruct the timeline | Two separate dates - when the account was actually lost, and when anyone noticed - with the gap between them named as the finding |
| Find the earliest detectable signal | A signal that was visible at the time to someone looking, kept apart from what is only obvious in hindsight |
| Write the mechanism | A three- or four-sentence causal chain from what happened to non-renewal, or an honest "unknown" if it can't be built |
| Test the stated reason against the mechanism | Whether they match, the stated reason is downstream, or it was a courtesy answer |
| Find when it stopped being winnable | Not whether it could have been saved - when the outcome became fixed, and what would have had to be true three months earlier |
| Check for correlation | How many other accounts were lost to the same mechanism, and what they share |
| Write the two lists | What changes, owned and dated - and what is correctly left alone |

---

## Who this is for

CSMs and account managers who need an honest read on why an account left - whether it's one they ran for years or one they inherited three months before it walked. It's also the right tool before a churn review, or the moment several accounts have been lost for what sounds like the same reason and somebody needs to find out if that's actually true.

It assumes you're willing to write down that the loss was winnable and nobody acted, or that nothing could have changed it. Both are legitimate findings; a postmortem that always finds a fix is performing, not analysing.

---

## What this needs

**Minimum:** what you remember. Memory is biased, but a postmortem written from memory that says so beats one that never gets written.

**Better with:** the account's email and meeting history, the support record, and whatever the renewal conversation produced in writing.

**Best with:** the original business case and the health-score history - together they show whether the account was ever delivering what it was bought for - plus an `account-context` document, particularly its value metric and what healthy usage looks like in your business, so usage numbers don't get misread.

Missing context never blocks this skill - it runs on whatever record survives and names what could not be reconstructed rather than guessing around the gap.

---

## Install

**The easy way: one paste**

```
I want to install the churn-postmortem skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/churn-postmortem folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/churn-postmortem` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/postmortem-template.md` is the fill-in postmortem itself - usable without Claude involved at all.

---

## What this does not do

- Does not accept a category as an answer. "Low adoption" is where the analysis starts, not where it ends
- Does not treat hindsight as detection. If a signal was only visible knowing how it ended, it does not count
- Does not assign blame to the person who held the account - that reliably ends honest postmortems for everyone else
- Does not skip the correlation check. Thirty accounts lost to the same mechanism are one decision, not thirty individual failures

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
