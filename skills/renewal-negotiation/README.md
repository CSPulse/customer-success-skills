# renewal negotiation

**Prepares the renewal conversation itself, before either side is in the room.**

The discount you give in the last week of a quarter doesn't end when the quarter does - it becomes the number the account expects next year, because every concession is permanent unless you deliberately make it temporary. Most renewal conversations go wrong before anyone says a number out loud: value was never agreed, so what's actually happening is an argument about price with nothing on the other side of the scale, and that argument is lost by default.

This skill checks first whether value is agreed - if not, the meeting to run is a value conversation, not this one. It makes you write your own walk-away as an actual figure, then honestly assess theirs, which is almost never "switch next month" and almost always "do nothing" or "renew smaller while we evaluate." It reads the contract's notice date, auto-renewal clause and uplift terms before it reads the room, since those set the conversation's shape more than anything said in it, and it builds a concession ladder with a price on every rung, because a free concession reads as proof the original price was never real.

The failure this exists to prevent: **negotiating price before value is established. If the customer has not agreed that the thing is worth having, you are not negotiating a price. You are arguing about a number with nothing on the other side of the scale, and you will lose that argument every time.**

Part of the **Run the set-piece** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Check whether you've earned the right to negotiate | An honest answer on whether value is agreed and whether this is actually a negotiation or a decision already made - run `renewal-risk` first if that read doesn't exist yet |
| Work out both walk-aways | Your number, written down so it can't move under pressure, and an honest read of their real alternative (usually "do nothing," rarely "switch") rather than the one they're describing |
| Read the contract before the room | The notice date, the auto-renewal clause, and any uplift or index term - the three facts that set who actually holds the time pressure |
| Know what the other side is measured on | The business owner's real fear (disruption, not price) separated from procurement's actual scorecard (a percentage win, not necessarily your money) |
| Build the concession ladder | Three rungs and a floor, each with what you give, what you get in return, and what it costs - plus the exact sentence for what's not on the table |
| Take time seriously | A clear-eyed read of whose deadline is actually real, so a number doesn't get set by your quarter-end and mistaken for a negotiated outcome |
| Handle the four asks you'll get | Scripted responses to the discount ask, the underutilization argument, the competitor quote, and the month-to-month request - each one a different problem wearing a commercial costume |
| Decide what happens if it stalls | Who escalates on each side, what silence near the notice date means, and the one thing you will not do, written down in advance |

---

## Who this is for

CSMs, account managers and renewal owners heading into a conversation where both sides already know a number is going to get agreed - especially once procurement has entered the thread, a discount has been asked for, or a competitor has been named.

---

## What this needs

**Minimum:** the account, the date, and roughly what they pay - enough for a concession ladder, a walk-away, and the likely asks.

**Better with:** the contract itself, particularly the notice date, the auto-renewal clause and any uplift or index clause - these three decide the shape of the conversation more than anything you'll say in it.

**Best with:** a current risk read and the original business case, because the first tells you how much leverage you actually have and the second tells you what value you're entitled to point at.

Missing context never blocks this skill - where an `account-context` document exists, it uses contract shapes, pricing model and who signs to decide what you can move without asking; where it's absent, the skill carries on and names the assumption.

---

## Install

**The easy way: one paste**

```
I want to install the renewal-negotiation skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/renewal-negotiation folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/renewal-negotiation` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/negotiation-plan.md` is the same structure as a one-page plan you can fill in by hand.

---

## Where this comes from

The walk-away analysis in Step 1 - your number written down in advance, and an honest assessment of the customer's real alternative rather than the one they describe - is the BATNA concept (Best Alternative To a Negotiated Agreement) from principled negotiation, most widely known through Fisher and Ury's *Getting to Yes*. The skill applies it specifically to the renewal moment: the customer's stated alternative ("we'll switch") is treated as a claim to verify against their actual BATNA ("do nothing" or "renew smaller"), not accepted at face value.

---

## What good looks like

- The walk-away was written down before the first call and did not move
- Every concession bought something, and you can say what
- Anything given on rate has an end date or a cap attached
- Procurement got a win that was not your margin
- You know what their real alternative is, not the one they described
- The number was agreed on value and timing, not on your quarter

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
