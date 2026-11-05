---
name: coaching
description: >
  Use when the user says "coach my CSM", "feedback on this call", "call review", "my CSM keeps making the same mistake", "how do I give feedback on", or pastes a call transcript or a few sentences on what they saw. Produces a one page prep sheet for the conversation: diagnosis (skill, knowledge, will, environment), the single behavior, the opening self-assessment question, the quoted moment, two rehearsal prompts and the next-observation date. Not for calibrating account reads across a team (use portfolio-review) or writing the customer recap (use call-recap).
---

# Coaching

A one page prep sheet for the manager, so the conversation changes one behavior instead of describing a call.

## Start here

If the user pasted a transcript, or gave about three sentences on what they saw (who, what happened, what the customer did), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. What you saw: the call or artifact, and the moment that bothered you
2. Whether the person has done this well before, here or elsewhere
3. Their book size and what they are measured on

Never coach on rumor: if the user only has a secondhand report, say so under "What I could not check" and build the sheet from what exists. If an "Account context" block exists in the conversation, use it.

## Do this

1. **Diagnose before choosing an approach.** Skill (does not know how): coach it. Knowledge (does not know the product or segment): teach it, faster. Will (knows how, not doing it): that is an expectations or fit conversation, not coaching. Environment (book too big, wrong incentive, missing tooling): that is the manager's problem. Give the evidence for the call and the one question that tests it: "have you done this before, somewhere it worked?"
2. **Pick one behavior.** Observable and repeatable, such as "ask what outcome they need before showing anything". Choose the highest leverage one, which is often upstream of the visible miss. Cut the rest on purpose.
3. **Write the opening self-assessment question** in the manager's voice: "How do you think that went, and what would you do differently?" Say what each likely answer tells you.
4. **Quote the moment.** A timestamp or line, what was said, the neutral description and the consequence in outcome terms. Never a trait.
5. **Write two rehearsal prompts** to run in the room, aloud, such as a customer line to answer cold. Tell the manager to let it be awkward.
6. **Set the next observation:** the named call or document, a date, and the follow-up conversation date. Flag anything that is an environment problem and therefore the manager's to fix.

## Output

Use this skeleton. It must fit one page.

```
COACHING PREP: [Name], [role] | observed [call or artifact, date]

Call: COACH / TEACH / PERFORMANCE CONVERSATION / FIX THE ENVIRONMENT
Diagnosis: skill / knowledge / will / environment - [evidence, said / seen / inferred]

The one behavior: [observable, one sentence]. Why this one: [leverage]

Open with: "[self-assessment question]"
If they name it: [what to do]. If they do not: [the gap is the finding]

The moment: [timestamp] "[quote]" 
What happened: [neutral]. Consequence: [outcome]

Rehearse
1. "[prompt]"
2. "[prompt]"

Next observation: [call or document] on [date]. Follow-up conversation: [date]
Mine to fix: [environment items, or none]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length.

## Rules

- **One behavior, never six.** A list of six improvements is accurate, fair and impossible to act on, so nothing changes.
- **Diagnose first.** Coaching a knowledge gap wastes weeks, coaching a will problem insults the person, and coaching an environment problem tells someone a structural failure is their fault.
- **Self-assessment before feedback.** A thing they name themselves is one they act on, and where they do not, the gap between their read and yours is the real finding.
- **Describe the moment, never the person.** "You did not ask what outcome they wanted" can be acted on tomorrow. "You are not curious enough" cannot be argued with or acted on.
- **Rehearse, do not advise.** Advice is understood and forgotten, and two minutes of practice out loud also shows whether it is really a skill problem.
- **Coach the cause upstream.** A weak recap email is usually a listening problem in the call, so fixing the email fixes nothing.
- **No next observation means it did not happen.** If nobody looks again, the team learns these conversations are ceremony.
- **Keep it out of forecast and portfolio meetings and away from pay talk.** Mixing "is this number right" with "are you good" corrupts both, and nothing said after money is heard as development.

## Related (only if installed)

`portfolio-review` for calibrating reads across a team. `call-recap` for the artifact most call coaching is about. `coverage-model` when the performance problem is a book that cannot be covered.
