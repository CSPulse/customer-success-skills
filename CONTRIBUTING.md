# Contributing

This library is meant to be a hub, not a monologue. The most valuable contribution is not a new skill. It is telling us that an existing one is wrong.

These skills are written by practitioners, but no one person has run accounts in every industry, at every segment, on every pricing model. Where a skill states something that does not match how it works in your world, that is a defect and we want to hear about it.

---

## The three things worth contributing

**1. A skill is wrong or thin.** Open an issue saying what happens in reality and what the skill assumed instead. Be specific. "The renewal timing is off for us" is hard to act on. "In healthcare, procurement starts eleven months out, not six, because the budget cycle is set at the clinical committee in Q1" is a fix.

**2. A skill is missing.** Open an issue describing the job, how often it recurs, and what a good output looks like. The bar is that it has to be a job with a right and a wrong way to do it. If the only answer is "it depends entirely", it is a conversation rather than a skill.

**3. You have written one.** Open a pull request. Read the rest of this file first.

---

## The two rules

Everything published here holds both.

**Nothing may be a prerequisite.** A skill that errors because you lack a file, a connector or a workspace gets uninstalled. Every skill states the least you can give it and still get value, then says what each additional input would add. Missing context changes what a skill can honestly claim, never whether it runs.

**Every skill names the failure it exists to prevent.** In one sentence, near the top. If it cannot say what goes wrong without it, it is a template rather than a skill.

---

## Writing a skill

### Structure

```
skills/<skill-name>/
  SKILL.md              the method
  references/           detail the method points at, one level deep only
  assets/               templates the skill fills in and hands over
```

### SKILL.md

- **Under 500 lines.** Detail moves into `references/`
- **Frontmatter carries `name` and `description`.** The `name` matches the folder exactly
- **The description goes under 1,024 characters and leads with literal trigger phrases.** Assistants truncate the tail of a description when the listing gets long, so the phrases someone would actually type go first, not the explanation
- **References are one level deep.** A reference that points at another reference gets partially read
- **Third person throughout.** "The user", not "you" and never a named person

### Ship an asset, not just advice

The single biggest difference between a skill people install and one they do not is whether it hands over something. A template, a rubric, a checklist, a worked example, a filled document. A skill that returns advice competes with the assistant's own general knowledge. A skill that returns a filled agenda does not.

### Name the mechanism

Say why something is true, not that it is. "Ticket volume alone signals nothing in either direction; rising volume means friction, falling volume from a previously active account means resignation" is useful. "Monitor ticket trends" is not.

---

## House style

- **No em dashes.** Use a comma, a colon, a spaced hyphen or a full stop
- **No statistics you cannot source.** A great deal of circulated customer success data traces back to vendor marketing with no study behind it. Build on mechanisms rather than numbers, and where a number is genuinely load-bearing, name where it came from
- **No customer names, employer names or anything identifying.** This applies to worked examples too. Invent a company, and make it obviously invented
- **Say what you could not check.** In the skill's own output format, there is a place for this. Use it

---

## Before you open a pull request

- [ ] SKILL.md is under 500 lines and references are one level deep
- [ ] The description leads with trigger phrases and is under 1,024 characters
- [ ] The skill states the least it needs to run
- [ ] The failure it prevents is named
- [ ] It ships at least one asset, or there is a reason it does not
- [ ] There is a worked example, using an invented company
- [ ] No em dashes
- [ ] No real customer, employer or personal names anywhere
- [ ] The folder name, the frontmatter `name`, and the entry in `.claude-plugin/marketplace.json` all match
- [ ] The README is updated in **all five places**: the skills table, the category table, the "works with nothing but" table, **the diagram**, and **the opening paragraph**

That last pair is the one that gets missed. The three tables have a row per skill, so a missing one is visible. The diagram and the opening prose have no per-skill structure, so nothing about them looks incomplete when they are.

---

## What happens next

Pull requests get read as a diff before merging, which is where a stray name or a broken claim actually shows up. Expect questions on anything that states a fact about how customer success works without saying where that came from. That is the standard the library is trying to hold, and it applies to the maintainers as much as to anyone else.
