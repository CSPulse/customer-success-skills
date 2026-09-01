# offboarding

**Lose well. The decision is made - the only thing left to protect is what happens next.**

The account is marked closed lost, and the damage that follows is usually what happens by default: the last two weeks get no attention, the data export drags, the exit conversation never gets asked for, and a customer who left for a solvable reason tells people you were fine until you stopped caring - a story that travels further than the product problem that caused the churn.

This skill assumes the decision is final and treats trying to reverse it as actively harmful, since every further save attempt converts the goodwill you have left into irritation. It runs three jobs in order: get the data out cleanly and fast, ask for the honest exit conversation separately from the commercial wind-down so it doesn't read as one more sales attempt, and leave the door open deliberately, since champions move and carry a memory of how this ended. The exit conversation uses sharp, specific questions - not "what went wrong" but "when did you first start thinking about this," almost always far earlier than your systems show.

The failure this exists to prevent: **the account that goes cold the moment it is marked closed lost** - the last two weeks get no attention, the data export is slow, the final conversation never happens, and a customer who left for a solvable reason becomes a customer who tells people you were fine until you stopped caring.

Part of the **Run the set-piece** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Step 0: confirm it's actually over | A check on whether the decision was really made by the decider (versus one person in one meeting), and whether the mechanism can still be changed - because running this on a live account costs you the save |
| Step 1: the contractual work, fast | Notice and dates, data handover, deletion obligations confirmed in writing, access wind-down with warning, and a final invoice with no surprises in it |
| Step 2: the exit conversation, asked for separately | A held-apart, no-selling fifteen minutes with pointed questions - when they first started thinking about it, what they didn't get, whether there was a moment it could have changed |
| Step 3: reason versus mechanism | The stated reason and the apparent cause kept clearly separate in the record, captured verbatim and handed to `churn-postmortem` rather than smoothed over |
| Step 4: leave the door open | What would have to change for them to reconsider, said honestly with no pitch attached, and a plan to stay in touch as a person rather than a lapsed CRM record |
| Step 5: hand over internally, once | Who needs to know before they hear it elsewhere, the honest version of the record rather than the sanitized one, and the correlated-loss question - how many other accounts share this mechanism |
| Step 6: the last message | Short, specific thanks, what's done and what's left, a door left open in one line, and nothing that reads as a win-back attempt |

---

## Who this is for

CSMs and account managers running the wind-down on a lost account - a non-renewal, a cancellation, a churn that's already decided. It's built specifically for the period after the decision is final, and it deliberately does not help with a save attempt; `renewal-risk` is the skill for while the outcome is still open.

---

## What this needs

**Minimum:** the account and the end date. Enough for the wind-down plan, the exit questions, and the internal handover.

**Better with:** the contract, for notice, data retention and deletion obligations, the final invoice position, and any wind-down period already owed.

**Best with:** the account history and the original business case, because the exit conversation is much sharper when you can ask about the specific thing they bought the product to do.

Missing context never blocks this skill - where an `account-context` document doesn't exist, it carries on and names the assumption instead.

---

## Install

**The easy way: one paste**

```
I want to install the offboarding skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/offboarding folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/offboarding` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/offboarding-checklist.md` carries the wind-down, the exit questions, and the handover on one page.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
