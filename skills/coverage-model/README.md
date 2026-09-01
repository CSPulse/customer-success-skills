# coverage model

**The ratio is an output, not an input.**

Most coverage models get built the same way: divide CSMs by accounts, call the result a ratio, and present whatever falls out as a strategy. The tiers get names - high touch, pooled, digital - and the part where the bottom forty per cent of the book gets nothing stays unsaid until it shows up as churn nobody predicted.

This skill designs coverage as a set of decisions about who you're choosing not to serve properly, said out loud. It segments by value, complexity, and potential rather than revenue alone - a small account with three business units and heavy regulatory exposure often costs more than a large simple one, and gets tiered as if it costs nothing. It makes the ratio an output of cost to serve, names what each tier doesn't get, designs the boundary transitions, refuses to call a tier "digital" without real instrumentation and triggers behind it, and tests the finished model against the accounts that actually churned.

The failure this exists to prevent: **the model designed backwards from headcount.** Take the number of CSMs, divide by the number of accounts, call the result a ratio, and describe whatever that produces as a strategy.

Part of the **Lead the function** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Segment by need, not only revenue | Tiers built on value, complexity, and potential, with the accounts that move because of complexity called out |
| Define each tier in specifics | Named CSM or not, cadence, entitlements, and the escalation trigger - not a vague label like "high touch" |
| State what each tier does not get | What signal you lose at each line, said plainly instead of discovered later |
| Make the ratio an output | Cost to serve times account count, compared to real headcount - the capacity gap as a number, and how it's being closed |
| Design the transitions | What happens when an account moves up, moves down, or gets a temporary elevation with a stated end date |
| Make digital and pooled real | The instrumentation, content, and owned triggers a tier needs to be coverage rather than a euphemism for none |
| Test against actual churn | Where your real losses would have sat under this model, and whether anyone would have seen them coming |

---

## Who this is for

CS leaders and managers designing or defending how a team is deployed across a book - building a coverage model from scratch, defending an existing ratio to leadership, or answering "do we need more headcount" with a number instead of a feeling.

---

## What this needs

**Minimum:** the account list with values, and your headcount. Enough for a first model with the trade-offs stated.

**Better with:** churn history by segment, product usage data, and support load per account - the cost side nobody counts.

**Best with:** the last two years of churn, including the reason and the segment, so the model can be tested against losses it should have caught rather than just described in the abstract.

Missing context never blocks this skill - it names the assumption where an `account-context` document or churn history is absent, rather than guessing around the gap.

---

## Install

**The easy way: one paste**

```
I want to install the coverage-model skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/coverage-model folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/coverage-model` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the whole method. There are no reference files or templates - the output is a tier table, a capacity number, and a back-test, all specific to your company, none of which survive a generic template.

---

## What this does not do

- Does not tier on revenue alone - that misplaces small, complex accounts in both directions
- Does not accept a vague tier definition. "High touch" is not an operational commitment
- Does not call a tier "digital" or "pooled" without the instrumentation, content, triggers, and route back to a human that make it real
- Does not let a capacity gap get absorbed quietly - it forces the choice between moving accounts down, reducing what a tier promises, or investing in the mechanism, named as a choice
- Does not skip the back-test. A model that would not have caught your actual losses is plausible, not working

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
