# Renewal Runway

**A dated table, pasteable into a calendar or CRM tasks, that works back from the real deadline.**

**What goes wrong without it:** Starting the renewal plan from your own renewal date. The customer's notice date and budget cycle come first, and the decision may be made before you begin.

Part of [customer-success-skills](../../#readme).

## What it does

1. Compute the opt-out date
2. Set checkpoints
3. Give each checkpoint
4. Mark the status of each date
5. If the user is late, compress
6. End with a table
7. Sanity check the spacing

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "renewal runway"
- "renewal timeline"
- "when do I start the renewal"
- "plan backward from the renewal date"
- "I am late on this renewal"
- "opt-out date"

## Who this is for

Written for CSMs. Included in: `csm-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. Renewal date and notice or opt-out period (days)
2. ARR and whether it auto-renews
3. Who signs, and whether you has met them

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the renewal-runway skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/renewal-runway folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- The opt-out date is the deadline
- Checkpoints are defaults, not law
- Every checkpoint needs a test that can fail
- Late means compress, not repeat
- Confirm the notice clause from the contract text
- Count from the customer's calendar too
- Drafts and tasks only

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
