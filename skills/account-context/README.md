# Account Context

**You walks away with a block of facts about their business that makes every other answer specific instead of generic.**

**What goes wrong without it:** A renewal read that calls an account at risk for low usage, when quiet usage is what a healthy compliance deployment looks like in that business.

Part of [customer-success-skills](../../#readme).

## What it does

1. Fill the block from whatever came back
2. Write every unknown as `NOT ESTABLISHED`, never a guess and never blank
3. Treat an empty value metric as a finding, not a gap to skip
4. If the user asks for the deeper mode, add up to six lines: segments and how deployments differ, seasonality, integrations that matter and what breaks if one disconnects, who owns renewal and expansion, what CS does not own, and the one fact a new CSM would get wrong in month one
5. Keep the block under 40 lines

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "account context"
- "set up my context"
- "teach you my business"
- "my skills feel generic"
- "what does healthy look like for us"
- "Account context"

## Who this is for

Written for CSMs, team leads and heads of customer success. Included in: `csm-toolkit`, `cs-team-lead-toolkit`, `cs-leader-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. What does a customer say the product does for them, in their words, and what did it replace?
2. Who buys, who uses, and who signs? Are they different people?
3. Contract shape: seat or usage based, term length, notice period, auto-renew yes or no.
4. What number did the customer actually buy (the measure their leadership would check)? "Nobody knows" is a valid answer.
5. What usage pattern would worry you, and what pattern looks alarming on a dashboard but is fine?

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the account-context skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/account-context folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- Five questions, one message
- Ask for the buyer separately from the user
- The value metric is the highest-yield question
- "Looks bad, is fine" is the valuable answer
- Record notice periods exactly
- Facts about price, contract or security come from the user
- Stale context misleads

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
