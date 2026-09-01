# renewal risk

**A defensible read on whether an account will renew - not a colour on a dashboard.**

You've sat through the risk review where someone says "at risk, low usage," the room nods, and the account shows up amber again next month with nothing new attached to it. That happens because usage describes the user, and the renewal is decided by the buyer - in enterprise, often two different people who barely overlap.

This skill works the account in a fixed order instead: whose calendar the renewal actually runs on, who the decider is and whether you've ever spoken to them, signals ranked by how much decision-weight they carry (normalized for segment, pricing model and industry), resolved into a causal mechanism rather than a category, argued against, and priced in dollars rather than flagged as a logo.

The failure this exists to prevent: **"at risk, low usage." That sentence names a category, states no mechanism, and implies no action - the most common thing said in a risk review and the least useful.**

Part of the **Read the account** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Set the clock to their calendar | Their budget lock date, notice date, fiscal year end and any blackout window - because "ninety days to renewal" and "three weeks to their budget lock" are different situations wearing the same number |
| Name the decision and the decider | A one-line answer to what's being decided, who decides it, and whether you've ever actually spoken to them - if you can't name the decider, that's the top risk on the account |
| Read the signals in tiers | Signals ranked from decision-mechanism (an unmet economic buyer, single-threading, no agreed value metric) down through usage shape, procurement tells, support sentiment and organisational change - so a Tier 1 signal beats any amount of Tier 2 comfort |
| Normalise for context | The same signal re-weighted for segment, pricing model, motion and industry, so an enterprise committee delay and a PLG usage dip aren't read by the same rule |
| State the mechanism | A causal chain from what you observed to non-renewal, specific enough to be wrong - not "usage is down 40%" but who was cut, what replaced you, and who hasn't met you yet |
| Argue against yourself | What would make this read wrong, which evidence is a statement versus your own inference, and whose statement it is |
| Forecast dollars, not logos | A range - full renewal, likely contraction and its size, downside - instead of a binary at-risk flag, plus whether the risk is correlated across other accounts |
| Name the play | The play matched to the mechanism, an owner and a date, what you need from your own side, and a falsifiable checkpoint you can actually miss |

---

## Who this is for

CSMs and account managers who need an honest answer on an account - one they've run for years or one they inherited last month and have to read cold. It's built for the moment before a forecast call, a risk review, or a QBR on an account whose renewal sits inside the next two quarters, when "I think they're fine" isn't going to hold up in the room.

If you've just inherited the account, the skill points you to `account-research` first - a risk read without knowing the original promise is a read against a standard nobody has established.

---

## What this needs

**Minimum:** what you already know about the account. Tell it what you've got and it produces the read, marking every gap as a gap rather than filling it in.

**Better with:** usage data, mailbox or CRM history for the relationship picture, and support ticket history - each one turns a "cannot verify" into actual evidence.

**Best with:** the account plan, the original business case, and the contract, which together let it check whether the value the customer bought is the value they're actually getting.

Missing context never blocks this skill - it changes what the read can honestly claim, not whether it runs. It names what it could not check instead of guessing around the gap.

---

## Install

**The easy way: one paste**

```
I want to install the renewal-risk skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/renewal-risk folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/renewal-risk` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `references/context-adjustments.md` holds the full breakdown of how segment, pricing model, motion and industry change what a given signal means - worth reading on its own before your next risk review even without Claude involved.

---

## What good looks like

- Someone who has never seen the account can read it and know who to call and what to say
- The mechanism is specific enough to be wrong
- The dollar range is stated, not just a colour
- Inference is visibly separated from what someone actually said
- The gaps are named rather than smoothed over

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
