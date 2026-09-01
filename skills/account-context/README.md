# account context

**Answer the same handful of questions once, so every other skill in this library stops asking.**

Install a dozen of these skills and each one starts by interviewing you from scratch: what the product does, how segments differ, what healthy usage looks like. This skill answers that once, so the other 31 skills read the answer instead of asking again.

The one question worth slowing down for is the value metric - the number the customer's own leadership uses to judge the purchase. Asked directly it usually comes back as a guess, so this skill asks it three different ways and marks it `NOT ESTABLISHED` when no one actually knows, rather than guessing.

The failure this exists to prevent: **a renewal risk read that flags an account for low usage, with no idea that quiet usage is what a healthy compliance deployment looks like.**

This is the one skill in [customer-success-skills](../../#readme) that sits underneath all the others rather than inside one of the seven categories - every other skill reads it where it exists, and names the assumption where it doesn't.

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Step 0: Check for an existing document | A read-back and an update, instead of a full re-interview |
| Step 1: The product, in the customer's words | One sentence in their vocabulary, what it replaced, and what it's genuinely bad at |
| Step 2: Segments, and how they differ | Buyer vs. user, a normal deployment, onboarding time, and what usually goes wrong - per segment, only where the answer actually changes |
| Step 3: Contract shape | Pricing model, term length, notice and auto-renewal windows, and who signs |
| Step 4: The value metric | The number the customer's own leadership uses to judge the purchase - or the honest statement that none is agreed |
| Step 5: What healthy looks like | The natural usage rhythm, whether low usage is ever the intended state, and what looks alarming but isn't |
| Step 6: Motion and ownership | Product-led vs. sales-led, who owns renewal and expansion, and what CS explicitly does not own |
| Step 7: Write it down | A completed two-page context document, or the same content as a paste-able block if no file can be saved |

---

## Who this is for

Whoever is setting up this library for their team - usually the first person on a CS team to install more than one or two of these skills and notice they're each asking the same onboarding questions. It also fits naturally into a "let me tell you about our product" moment with a new hire, or any point where a skill's output has started to feel generic.

You run this once per business (or once per meaningfully different product line), not once per account. Every other skill in the library is written to check for its output and use it when present.

---

## What this needs

**Minimum:** five minutes and what you already know. Nothing here is looked up - it's what someone who has worked the book for a month can answer from memory, with the gaps recorded as gaps.

**Better with:** the pricing page, a sample contract, and a health-score definition if one exists.

**Best with:** the original business case for two or three accounts, because that's where the value metric is actually written down.

Missing context never blocks this skill - every unanswerable question gets marked `NOT ESTABLISHED` rather than guessed at, and the finished document closes with the two or three gaps most worth closing and where the answer probably lives.

---

## Install

**The easy way: one paste**

```
I want to install the account-context skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/account-context folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/account-context` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method. `references/worked-example.md` is a completed context document for a fictional company, showing the level of specificity that makes this useful, and `assets/context-template.md` is the blank document you can fill in by hand, with or without Claude involved at all.

---

## What this does not do

- It does not look anything up. Everything it captures comes from what the user already knows, plus whatever documents they choose to hand it.
- It does not block any other skill. The pattern across this library is: use the context document where it exists, name the assumption where it doesn't, never fail for lack of one.
- It does not stay valid forever. Pricing changes, segments get renamed, the renewal owner moves - a context document more than two quarters old should be re-checked before it's trusted.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
