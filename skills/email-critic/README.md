# Email Critic

**You walks away knowing whether to send the draft, what is wrong with it, and a version that fixes only that.**

**What goes wrong without it:** A customer email checked for tone while its facts go unchecked, so a wrong date or an upgraded maybe reaches the customer.

Part of [customer-success-skills](../../#readme).

## What it does

1. Name what the email is for
2. Check facts against the source first
3. Check what the customer will notice missing
4. Check the ask
5. Read it as the recipient
6. Give the verdict
7. Verify the fix is executable

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "would you send this"
- "review this email"
- "tighten this"
- "does this sound right"
- "how will the customer take this"

## Who this is for

Written for CSMs. Included in: `csm-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. The source: transcript, notes or the customer email being answered
2. Who it goes to and what you needs back
3. Anything you already owes this person

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the email-critic skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/email-critic folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- Truth before tone
- No score, ever
- Do not manufacture criticism
- Every criticism names its fix
- Rewrite only what you named
- Pull out what you cannot verify
- No house style the user has not stated
- A chase must change shape
- Bad news is a call first

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
