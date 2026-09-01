# customer update

**Say whether it affects them and whether they have to do anything, in the first two lines.**

A customer update rarely goes to a person - it goes to a list, gets forwarded to people who were never on it, and gets read in about eleven seconds by someone who wants one thing answered: does this affect me, and do I have to act. Most fail that test because they're written from the sender's side of the glass, with the thing that actually touches the customer buried in the middle, unmarked.

This skill writes the message nobody wants to send - an incident, a delay, a deprecation, a price change, maintenance, or a CSM change. It segments recipients by impact, not mailing list, so the five percent badly affected don't get buried in reassurance meant for the other ninety-five. It puts the news in the subject line, treats "no action needed" as a load-bearing sentence rather than filler, separates confirmed from expected, and writes every draft assuming it gets forwarded to an executive, a security team, and occasionally a lawyer.

The failure this exists to prevent: **the update written from your side of the glass.** A paragraph about your infrastructure, your roadmap process or your team change, with the thing that actually affects them somewhere in the middle, unmarked.

Part of the **Write to the customer** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Decide one message or several | Recipients sorted into materially affected, affected but no action needed, and not affected - each with its own channel |
| Write the subject line first | A subject that carries the actual news, with no borrowed urgency the content doesn't back up |
| Lead with what changes for them | Three lines, in order: what's changing, what it means for them, what they need to do (or that they don't) |
| Separate confirmed from expected | A plain split of what's known now, and a next-update date you will actually keep |
| Write it to survive a forward | No internal shorthand, no blame, no liability language where money or data is involved, one topic per message |
| Handle a CSM change as a relationship event | Named accounts hear it from a person first, a human being gets introduced, and what carries over is stated concretely |
| Decide who answers the replies | A named owner, a response window, and the two or three answers you already know are coming |

---

## Who this is for

Anyone who has to tell a list of customers something rather than one person by voice - a CSM handing over their book, someone drafting an incident notice, a team announcing a deprecation, price change, or maintenance window. For news going to a single account by voice, `hard-conversation` is the better fit; for something already on fire, `escalation`.

---

## What this needs

**Minimum:** what is changing, when, and who it touches. Enough for segmentation, the subject line, and a first draft.

**Better with:** the account list with contract and usage detail, so impact gets assessed rather than assumed, plus any legal or security obligation attached to the notice.

**Best with:** a prior update of the same type that went well or badly - the format matters more than the wording, and yours may already be set.

Missing context never blocks this skill - where an `account-context` document is absent, it carries on and names the assumption.

---

## Install

**The easy way: one paste**

```
I want to install the customer-update skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/customer-update folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/customer-update` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `references/by-update-type.md` breaks down how incident, delay, deprecation, pricing, maintenance and CSM-change updates each differ from the general method - useful on its own even without Claude involved.

---

## What this does not do

- Does not send one message to a whole list when impact varies - that buries the badly affected and alarms the unaffected
- Does not omit "no action is needed" when it's true - its absence reads as an ask and generates support tickets
- Does not publish a cause before it's established, or promise a next-update date it won't keep
- Does not send a CSM change as a mass email or let a customer discover it from an auto-reply

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
