# Call Recap

**An honest read of the call, every email it created (not just the recap), and a CRM note, all in chat from a pasted transcript.**

**What goes wrong without it:** A tidy recap sent to the main contact while the emails that actually move the account stay unwritten.

Part of [customer-success-skills](../../#readme).

## What it does

1. Read the transcript, not the summary
2. Write the honest read in 150 words or fewer
3. List every email the call generated, from commitments not topics
4. Ground every claim
5. Draft each email in chat
6. Write the CRM note

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "recap this call"
- "here is the transcript"
- "what do I owe after that call"
- "write the follow-ups"
- "emails from this call"
- "what did you make of that call"

## Who this is for

Written for CSMs and team leads. Included in: `csm-toolkit`, `cs-team-lead-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

- Whatever you know about the situation

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the call-recap skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/call-recap folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- One email per recipient
- The transcript hedge belongs in the email
- Never write "as discussed, we sent X" unless the user confirms it was sent
- Never guess an address or a spelling
- Context goes in the flag, the ask goes in the email
- Someone else's topic is someone else's email
- Order the sends
- A newer written record beats the call
- Hold flagged drafts back
- Name the weak call

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
