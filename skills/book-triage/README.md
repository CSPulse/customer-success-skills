# book triage

**Decide where your attention goes this week, and write down where it deliberately doesn't.**

Even coverage feels like diligence. It's actually the failure: forty accounts touched equally every week is forty accounts touched too lightly to change anything, and the CSM doing it feels busy while moving nothing. What usually decides where the attention goes is who emailed loudest - which correlates with neither risk nor value, and quietly starves the quiet accounts where the real danger lives.

This skill sorts by what changed in the last two to four weeks rather than by health colour or size, asks honestly whether four hours here would actually move anything, and forces the part everyone skips: a not-this-week list, named explicitly, each entry carrying the trigger that would pull it back on.

The failure this exists to prevent: **the week spent on the accounts that asked. Attention allocated by who emailed loudest, which correlates with neither risk nor value, and which systematically starves the quiet accounts where the actual danger is.**

Part of the **Run the book** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Step 1: Sort by movement, not by state | Accounts ranked by what changed in the last two to four weeks - usage, a person, a commercial event - not by static health colour |
| Step 2: Add the dates that cannot move | Notice date and budget lock surfaced ahead of the renewal date itself, since those are what's actually binding |
| Step 3: Ask where you can change the outcome | Every candidate tested against "if I spend four hours here, does anything move" - including the honest no |
| Step 4: Find the silent accounts | At least one account deliberately chosen for having the fewest logged touches, sorted by last real contact rather than last automated email |
| Step 5: Weight by value, last | Contract size used to break ties and set depth, never to decide who makes the list in the first place |
| Step 6: Write the not-this-week list | Every consciously-skipped account named, with the trigger that would change the decision |
| Step 7: Set the cadence | A short weekly list of five to eight accounts, each carrying one line on what changed and what you'll do |

---

## Who this is for

Any CSM or account manager carrying a book too large to cover evenly - the person who has said, or thought, "I have too many accounts" or "I can't cover them all." It's a weekly ritual, not a quarterly planning exercise, built for someone who needs a Monday-morning list they can act on without re-deriving it from scratch.

---

## What this needs

**Minimum:** your account list, with renewal dates and rough values. It will lean more on what you already know than on data, but it still produces a real triage.

**Better with:** usage trend, support activity, and last-contact dates. That last field is the single most valuable one, and the one most often missing.

**Best with:** health scores you know the composition of, and a stakeholder picture, so movement can be read rather than guessed at.

Missing context never blocks this skill - without an `account-context` document, "usage dropped" can't be told apart from a normal seasonal pattern, so it names that assumption rather than reading every dip as risk.

---

## Install

**The easy way: one paste**

```
I want to install the book-triage skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/book-triage folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/book-triage` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/triage-sheet.md` is the same structure as a one-page weekly sheet you can fill in by hand.

---

## What this does not do

- It does not produce a list of twenty. Five to eight accounts, or it's the book again with extra steps.
- It does not absorb an uncoverable book quietly. Where the tail is permanently unservable at any allocation, that's named as a `coverage-model` problem and said upward, not compensated for weekly.
- It does not treat "no change" as requiring a touch. No movement is a legitimate answer and earns a lower rank, not automatic attention.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
