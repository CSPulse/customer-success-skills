# csql motion

**The first badly handled handoff ends the flow of signals within a month.**

A CSM flags a real expansion signal, it lands in a sales queue, and someone who's never read the account calls the customer cold. It reads as exactly what it is - a sales pitch dressed as a check-in. The CSM never flags another one, and the programme keeps existing on a slide long after it's stopped producing anything.

This skill designs how CS generates and hands off qualified expansion leads without spending the trust that produced them. It forces the decision nobody wants to make explicitly - spot and hand off, own expansion end to end, or do neither - because the unstated default, CSMs expected to sell without training or pay for it, is the worst of the three. It defines what actually qualifies as a signal instead of a hunch, designs the handoff as a warm introduction where the CSM stays in the room, and settles attribution and what the CSM gets before the first lead moves.

The failure this exists to prevent: **the lead dropped into a queue.** A CSM passes a real signal, it is worked by someone with no context, the customer experiences a cold sales approach from a company that is supposed to know them, and the CSM never passes another one.

Part of the **Lead the function** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Decide whether CS should be selling at all | One of three explicit positions - spot and hand off, own it end to end, or deliberately neither |
| Define what actually qualifies | Two or three written, behavioural criteria, with the CSM naming which one fired |
| Design the handoff as an introduction | The CSM stays in the room, context travels and gets read before contact, and a response window is agreed |
| Protect what the customer experiences | Rules that keep the value conversation and the sales conversation from merging, and make a no genuinely free |
| Settle attribution up front | What counts as CS-sourced versus CS-influenced, and what the CSM actually gets - stated even when it's nothing |
| Measure the two things that matter | Conversion against sales' other sources, and relationship cost tracked afterward, not just volume |
| Write the kill criteria | The named conditions and review date that let the programme actually stop instead of being quietly ignored |

---

## Who this is for

CS and revenue leaders designing or fixing how expansion signals move from customer success to a sales team - whether the motion doesn't exist yet, is producing volume with no conversion, or has already had the handoff go wrong once and needs to be rebuilt with the trust question answered honestly this time.

---

## What this needs

**Minimum:** what you want CS to spot, and who would work it. Enough for a qualification definition, a handoff shape, and an attribution rule.

**Better with:** historical expansion data, so qualification gets built from what actually converted rather than from what feels promising.

**Best with:** the compensation plans of both teams, because those decide behaviour far more than any process document.

Missing context never blocks this skill - where an `account-context` document is absent, it carries on and names the assumption.

---

## Install

**The easy way: one paste**

```
I want to install the csql-motion skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/csql-motion folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/csql-motion` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the whole method. There are no reference files or templates - the output is a position, a qualification definition, an attribution rule, and a kill condition, all company-specific decisions rather than documents.

---

## What this does not do

- Does not accept "they seem happy" or a high health score as a qualifying signal - satisfaction and buying intent correlate weakly
- Does not let the CSM disappear at handoff, or allow cold outreach into a warm account
- Does not let the value conversation and the sales conversation merge into the same meeting
- Does not defer the attribution conversation until after the first big deal, which is when these programmes usually start arguing
- Does not report volume as the success measure - relationship cost has to be tracked too, or the programme's main risk is invisible by design

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
