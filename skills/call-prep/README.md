# call prep

**Prepare for the one thing the call has to produce, not for what you plan to say.**

Most call prep is reading: open the account, scan the last few notes, feel prepared, and walk in with no outcome attached. The call goes fine, a recap gets sent, and the account is exactly where it was, with the next call carrying the same agenda.

This skill forces four things into existence first: a one-sentence outcome specific enough to be failed, a real picture of who's in the room and who can actually authorise anything, the thing the customer is quietly annoyed about - addressed before they raise it - and an ask with a fallback, so the call doesn't end on "let me know if that would be useful." With no time to spare, it collapses to a ten-minute version: outcome, landmine, ask.

The failure this exists to prevent: **the call that goes fine, generates a recap, and moves nothing. Everyone leaves satisfied, the account is exactly where it was, and the next call has the same agenda.**

Part of the **Handle the conversation** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Step 1: Name the outcome | One verifiable sentence - "by the end of this call, [named person] has [done or committed to a specific thing]" |
| Step 2: Work out who's really in the room | Each attendee's actual wants and authority, who's missing, who they report to afterward, and who's new |
| Step 3: Find what changed on their side | Their organisation, their business, their usage, their commercial picture - fact and inference marked separately |
| Step 4: Find the landmine | The thing they're quietly annoyed about, named before the call, with a decision on whether you raise it first |
| Step 5: Write the questions | Three real questions plus the one you're avoiding, and a decision on whether to ask it |
| Step 6: Set the ask and the fallback | A specific request of a named person with a date, and what you'll take if they say no |
| Step 7: Budget the time | Minutes allocated in order, the ask placed before anything droppable, and a cut line decided in advance |
| Step 8: Prepare for it going sideways | Two lines: what you say if they open with a complaint, and what happens if the decider doesn't show |

---

## Who this is for

Anyone with a customer call on the calendar that isn't already covered by a more specific skill - a check-in, a first meeting on an inherited account, a technical working session, a risk conversation. It's built to work whether you have an hour to prepare or ten minutes before the call starts.

It is explicitly not for a QBR or EBR (`business-review` owns that, including whether it should happen), a meeting whose whole point is a senior person on the customer side (`exec-conversation`), or a call whose job is delivering bad news (`hard-conversation`).

---

## What this needs

**Minimum:** who you're meeting and why. Even a single line produces an outcome, a set of questions, and an ask - with everything unverified marked as such.

**Better with:** the last call's notes or recap, recent email history, and the invite with its attendee list. Those three convert most of the guesses into facts.

**Best with:** a stakeholder map and the account plan, so the prep knows who's missing from the room, not just who's in it.

Missing context never blocks this skill - if the call is imminent, it collapses straight to the ten-minute version (outcome, landmine, ask) rather than stalling for a full prep pass.

---

## Install

**The easy way: one paste**

```
I want to install the call-prep skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/call-prep folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/call-prep` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/prep-sheet.md` is the same structure as a blank one-page template - written to be filled in by hand and pasted back in afterward so `call-recap` inherits what the call was supposed to produce.

---

## What this does not do

- It does not treat an unfalsifiable outcome as a real one. "Align on the rollout" or "touch base" can't be failed, so they don't count - the outcome has to be stated in a form that could turn out wrong.
- It does not let a deck become the agenda. Material prepared before the outcome tends to dictate its own running order and crowd out the questions; this skill prepares questions first and treats slides as backup.
- It does not skip the landmine hoping it won't come up. It always comes up - the only choice this skill leaves you is whether it's raised on your terms or theirs.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
