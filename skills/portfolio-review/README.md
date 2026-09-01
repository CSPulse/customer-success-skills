# portfolio review

**Reviews your team's reads, not their accounts.**

You know this meeting. Someone raises the first account, the room starts solving it, and four accounts get discussed out of the thirty on the agenda. Everyone leaves feeling it was useful. Twenty-six reads went unexamined, and the wrong ones stay wrong until they show up in next quarter's forecast as a miss nobody saw coming.

That happens because reviewing accounts and reviewing reads look identical for the first ten minutes, then diverge. This skill is built for the second meeting: it samples rather than covers the whole book, always pulls a genuinely random handful nobody chose in advance, asks the same four questions of every account so a thin read has nowhere to hide, and watches for sandbagging and happy ears by their actual tells. It also does what no individual CSM can do alone - find the same mechanism showing up on five accounts, which is one problem wearing five faces, not five separate saves.

The failure this exists to prevent: **the review that becomes a working session on the first account raised - everyone leaves feeling it was useful, and twenty-six reads went unexamined.**

Part of the **Lead the function** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Say which meeting this is | A named purpose - calibration, coaching, or problem-solving - decided before it starts, because coaching in front of peers isn't coaching, it's a performance |
| Sample rather than cover | Three groups worth reviewing: exceptions, a genuinely random five or six, and the accounts with the lowest last-contact dates - announced as random, which changes how reads get written before the meeting even runs |
| Ask the four questions that expose a thin read | The same four questions on every account, in the same order: what's the mechanism, who decides and when did you last speak to them, what's said versus what's inferred, and what would make you wrong |
| Know the tells | The actual signatures of sandbagging (risk flagged late, with no play, that never changes state) and happy ears (all-verbal, single-sourced, single-threaded evidence with no bad news anywhere) |
| Protect the person who brings bad news | A rule against criticizing a downgraded read in front of peers, and at least one action taken off someone's plate in the meeting, so the next red flag actually gets surfaced |
| Look across the book, not just down it | The cross-account pattern - five accounts citing the same product gap or price change - routed to `internal-escalation` or `product-feedback` instead of five separate save plays |
| End with changes, not notes | Which reads changed and to what, what the manager took on, and whether last review's changes actually happened |

---

## Who this is for

CS leaders and managers running a recurring review of a team's book - the person whose forecast is only as good as the reads feeding into it, and who needs a way to find the wrong ones before they reach a QBR or a board number rather than after.

---

## What this needs

**Minimum:** the team's current reads on their accounts - enough to sample, question, and find the thin ones.

**Better with:** last-contact dates, health scores you know the composition of, and the previous review's notes, so movement in the reads is visible.

**Best with:** forecast-versus-actual history per person, which turns "I don't believe this read" into a calibrated statement rather than an opinion.

Missing context never blocks this skill - where an `account-context` document exists, it uses what healthy looks like per segment to tell a wrong read from a merely unusual account.

---

## Install

**The easy way: one paste**

```
I want to install the portfolio-review skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/portfolio-review folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/portfolio-review` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/review-agenda.md` is the meeting laid out on one page, usable without an assistant at all.

---

## What good looks like

- The random sample was reviewed, and it was genuinely random
- Every account got the same four questions
- At least one read changed in the meeting
- Somebody surfaced something bad and was visibly better off for it
- A pattern across accounts was found and given an owner
- Last review's changes were checked, and some of them had not happened, and that was said

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
