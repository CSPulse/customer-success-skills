# Invoice Chase

**An overdue invoice or PO turned into a diagnosis, a draft to the right person at the right tone, and the next date. Draft only, you sends.**

**What goes wrong without it:** A chase email sent to the champion, who cannot pay it, while the real cause stays unexamined: a missing PO, a dispute or a delay in accounts payable.

Part of [customer-success-skills](../../#readme).

## What it does

1. State the facts and the age
2. Rank the likely causes
3. If it is a dispute, stop
4. Pick the recipient
5. Pick the ladder step
6. Draft the chase
7. Log the signal and the checks

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "overdue invoice"
- "chase the invoice"
- "they have not paid"
- "the PO is stuck"
- "AP has not paid us"
- "payment reminder"

## Who this is for

Written for CSMs. Included in: `csm-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. Invoice or PO number, amount, due date, terms, and the payment method on the invoice
2. Who has been contacted so far, by whom (a person or an automated reminder), and any reply
3. Anything odd on their side: a new finance system, a changed contact, a complaint, a PO that was never sent

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the invoice-chase skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/invoice-chase folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- Write to whoever moves the money, copy whoever knows the story
- Every chase carries four facts
- Say "our records show it unpaid", never "you have not paid"
- Never threaten suspension or late fees on your own
- Diagnose before choosing tone
- Step out for about three working days after each chase
- A late payment is a signal about the account, not only about cash
- Never invent a detail

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
