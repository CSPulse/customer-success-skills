---
name: cs-start
description: >
  Use when the user says "customer success", "help with my accounts", "where do I start", "what can you do for a CSM", "I'm a CSM", "I lead a CS team", "run the demo", "show me what this does", or is unsure which customer success skill fits. Routes any situation to the right skill and runs it, shows a 60 second demo on an invented account, and anonymizes any output so it is safe to share. Not for doing the work itself (the routed skill does that).
---

# CS Start

The front door. One question, then straight into the right skill. If the user already described a situation, skip the question and run the skill.

## Start here

If the user described a situation (a call, an account, a number, a message they dread sending), match it against `references/routes.md`, say in one line which skill you are using, and run it. Do not ask which skill they want.

If they said nothing specific, or said "demo", "show me" or "what can you do", ask this ONE question:

> What is in front of you right now?
> 1. A call or meeting (coming up, or just finished)
> 2. One account I am worried about, renewing, or inheriting
> 3. Something I have to write or say to a customer
> 4. My whole book or my team's numbers
> 5. Show me a 60 second demo

## Do this

1. **Route.** Use the table in `references/routes.md`. Pick the single best skill. If two fit, pick the one closer to the user's next action and mention the other as the follow-up.
2. **Check it is installed.** If the routed skill is not available in this session, do the job directly with the same principles (verdict first, evidence tagged, gaps named) and tell the user the named skill exists in the library.
3. **Run it.** Hand over with no preamble. The user's situation is the input.
4. **Offer the next step once.** One line, naming the follow-on skill and what it would produce.

## Demo mode

When the user picks 5 or asks for a demo, load `references/demo.md`. Run `renewal-risk` on the invented Marlowe Freight account in it, show the output, then say: "Paste your own account in the same three lines and I will do the real one."

## Share-safe mode

When the user says "make this shareable", "anonymize this", "remove names" or "I want to post this", rewrite the last output with:

- Customer, vendor, person and product names replaced by consistent invented ones
- Dollar figures scaled by one consistent factor and dates shifted by one consistent offset
- Quotes paraphrased unless they contain nothing identifying
- A final line: `Anonymized. Check it once more before posting.`

Never post, upload or send it anywhere.

## Rules

- **Route on the situation, not the keywords.** "They want a discount" is renewal-negotiation even though the user never said negotiation.
- **Do not make the user learn the library.** Names of skills are for the model; the user speaks in situations.
- **Persona is a hint, not a gate.** A CSM can run a leader skill and the reverse. If the user says "I lead a team", start from `references/routes.md` section B or C but still match on the situation.
- **One question at most.** If the first answer is enough to route, route.

## Related (only if installed)

Every other skill in the library.
