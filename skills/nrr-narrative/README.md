# nrr narrative

**Decompose the number before you narrate it - a board that's seen this before will ask exactly one question, and the headline alone doesn't survive it.**

Net revenue retention is a ratio, and every ratio hides its composition: 110% built on a price increase, 110% built on seat growth in existing teams, and 110% built on two enormous expansions covering broad contraction are three different companies with the same slide. Present the headline alone and you survive exactly one follow-up question before the room stops trusting every number you show for the rest of the meeting.

This skill forces the decomposition first - expansion, price, contraction, and churn, kept strictly separate, since price and expansion get merged constantly despite meaning different things: one is evidence customers want more, the other that you charged more, and a board that finds the difference after the fact treats every later number as suspect. It puts gross retention next to net, since gross can't be rescued by a few large expansions, forces a call on cohort versus blended (blended flatters fast growth for reasons unrelated to whether the product holds anyone), and makes you say out loud, before anyone asks, exactly what the number is concealing - the difference between a narrative and a defense.

The failure this exists to prevent: **presenting the number without its composition**, which survives exactly one question from anyone who has seen this before, and which loses you the room for the rest of the meeting.

Part of the **Lead the function** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Decompose before narrating | Expansion, price, contraction and churn separated out, with price and expansion kept strictly apart because only one of them is a demand signal |
| Gross next to net, always | The honest number placed beside the flattering one, so a deteriorating base can't hide behind a handful of large expansions for years |
| Cohort or blended, stated | An explicit call on which you're showing, and what blended retention might be concealing if that's all you have |
| Find the concentration | How much of the expansion came from how few accounts, and where the churn actually clusters - by segment, cohort, product, or channel |
| Answer what the board is actually asking | Whether the number is repeatable, what recurs on its own versus what needed a one-time push, and the leading indicator that predicts it two quarters out |
| Name what the number hides | The common concealments checked before anyone else finds them - one big expansion covering contraction, deferred churn on multi-year terms, a mid-period definitional change |
| The three sentences | What happened, why, and what you're doing about it - written before a single slide, because a deck built on unfinished analysis turns into forty minutes of questions about axis labels |

---

## Who this is for

CS and RevOps leaders preparing a retention narrative for a board, an investor update, or an executive team - anyone about to present NRR or GRR who has been caught flat by a follow-up question before, or who wants to disclose the composition themselves rather than have someone else find it first.

---

## What this needs

**Minimum:** the retention numbers and the period. Enough for a decomposition attempt and an honest list of what can't yet be separated.

**Better with:** the movement already broken into expansion, price, contraction and churn, plus the same numbers for prior periods.

**Best with:** cohort data and segment-level retention, which is where the actual story almost always lives.

Missing context never blocks this skill - where an `account-context` document (pricing model, contract shapes, segments) doesn't exist, it carries on and names the assumption, and it says plainly what it couldn't check or separate.

---

## Install

**The easy way: one paste**

```
I want to install the nrr-narrative skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/nrr-narrative folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/nrr-narrative` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method - no supporting files. The output is a decomposition and three sentences, both specific to the business, and a template would invite filling in boxes rather than doing the actual decomposition.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
