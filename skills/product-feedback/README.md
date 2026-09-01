# product feedback

**Turns customer noise into something product will actually act on.**

You forward the email - "big customer wants this, can we prioritize?" - into a channel with forty other messages that look exactly like it, none comparable, none sized, all competing for the same quarter on whoever asked loudest. Six months later the customer asks what happened, and the honest answer is it went nowhere because nobody could act on it in the form it arrived.

Product teams don't ignore customer success - they ignore feedback that arrives as a feature name with an account attached and no way to weigh it against everything else asking for the same slot. This skill sorts whether the thing is a bug, a discoverability problem, a misunderstanding of the job, or a genuine gap (only the last two belong in a submission), converts the customer's proposed solution back into the underlying job, sizes it by counting accounts with that job rather than accounts that used that feature name, and refuses to inflate the churn risk past what you'd defend at the renewal.

The failure this exists to prevent: **forwarding a customer email into a channel. It transfers the request and none of the information anyone needs to act on it, and puts the translation work on the person least equipped to do it.**

Part of the **Work it internally** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Work out what kind of thing this is | A classification - bug, discoverability problem, misunderstanding of the job, genuine gap, or gap with a workaround - before anything gets written, since only the last two belong in a product submission |
| Translate the request back into the job | The underlying job in the customer's own words, what they do today to work around it, what that costs them, and their proposed solution recorded as a proposal rather than a requirement |
| Size it honestly | A count of accounts with the same job (not the same feature name), the contract value attached, the segment shape, and what actually happens if nothing changes - said honestly, not inflated |
| Bring evidence, not adjectives | Dated, attributed quotes, usage or support data, frequency across accounts, and anything the customer already built or paid for to work around it |
| Write it in their format | The submission built to the product team's actual intake fields and prioritization cycle, so it gets read instead of triaged |
| Close the loop, especially on a no | What the customer is told and when - including "we're not building this" - instead of the silence that's the single most common reason customers stop reporting anything |
| Keep a register | One list per account and per theme, so "what happened to my request" has an answer without archaeology, and the fifth report of the same job is recognized as the fifth, not the first |

---

## Who this is for

CSMs and account managers who field customer requests and need them to survive contact with a product team's prioritization process - and anyone who has been told, or suspects, that product ignores what they send over.

---

## What this needs

**Minimum:** what the customer asked for and who they are - enough to do the translation, size it honestly, and write the submission.

**Better with:** other accounts that have raised something similar, the usage data behind the claim, and the contract value of each - these turn an anecdote into a case.

**Best with:** your product team's own intake format and prioritization criteria, because a submission written in their frame gets read, and one written in yours gets triaged.

Missing context never blocks this skill - where an `account-context` document exists, it uses the product and segment picture to say whether a gap is isolated or systemic; where it's absent, the skill carries on and names the assumption it's making instead.

---

## Install

**The easy way: one paste**

```
I want to install the product-feedback skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/product-feedback folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/product-feedback` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/feedback-submission.md` is the same structure as a fill-in submission and register entry, usable without Claude at all.

---

## Where this comes from

The core move - treating a customer's requested feature as evidence about an underlying job rather than as the requirement itself - is the "jobs to be done" framing associated with Clayton Christensen and popularized in product circles by Tony Ulwick and others. This skill applies it specifically to inbound customer requests: the proposed solution is data about the job, not a specification to pass along.

---

## What good looks like

- The submission names a job, not a feature
- The number of accounts is a count of the job, and someone else could verify it
- The churn claim is either absent or one you would defend at the renewal
- Evidence is dated and attributed, and no adjective is doing the work of a number
- The customer was told what happened, including when the answer was no
- A year later, the register answers what happened without anyone digging

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
