# Customer Success Skills

**Paste three lines about an account. Get the read you would defend in a forecast call.**

Thirty-three skills for the work customer success actually does: renewals, escalations, hard conversations, QBRs, handoffs, forecasts and the weekly scramble. Free, MIT, and built to be argued with.

Works in Claude (app, Cowork, Code) and anything that reads `SKILL.md`. No setup, no connectors, no API keys. Nothing here sends an email or touches your CRM. You press send.

---

## See it work

You type this:

> Marlowe Freight, $180k ARR, renews 14 March, 60 day notice. My champion is Priya in compliance. Usage looks fine but she mentioned there's a new CFO. I haven't met them.

Plain AI gives you a paragraph that could be about any account: *"Usage is stable, which is a positive sign, but the new CFO may introduce risk. Consider scheduling a meeting..."*

The `renewal-risk` skill gives you this:

```
RENEWAL READ: Marlowe Freight | $180k | renews 14 Mar | opt-out by 13 Jan

Call: CONTRACT
Dollars: $110k to $180k, expected $135k   Confidence: medium

Decider: new CFO (name unknown), approves anything over $100k. Met: no.
Mechanism: The new CFO inherited a cost-out target and is reviewing every
vendor over $100k. Priya runs the tool but does not control the budget. If
the CFO sees us as compliance overhead rather than a revenue protector, the
likely outcome is a smaller tier, not a replacement.

Evidence
- said     Priya: "the new CFO started in October" (call, 4 Nov)
- seen     Priya asked for a seat utilization export on 28 Oct
- inferred The export is the CFO's team preparing a negotiation, not admin

What would make me wrong
- The export may be for an internal audit. Ask her what it is for.

Play: Get 30 minutes with the CFO before 12 Dec, sponsored by Priya, framed
      around audit cost avoided. Owner: me. Need: exec sponsor for one call.
Checkpoint: "If I have not met the CFO by 12 Dec, my director asks for the
             meeting at their level and I prepare the contraction case."

What I could not check
- Who else sits on the CFO's review panel
```

A call, a dollar range, a named decider, evidence separated from guesses, a falsifiable checkpoint, and an honest list of what it could not check. Every skill ends the same way.

---

## Try it in a minute

1. Install (pick your role below).
2. Say **"run the demo"**, or just describe what is in front of you: *"I have a QBR Thursday"*, *"they want a discount"*, *"my champion just left"*. The `cs-start` skill routes you to the right skill and runs it.
3. Run it on your messiest real account.
4. Want to post the result? Say **"make this shareable"** and it anonymizes names, dollars and dates first.

---

## Pick your role

| You are | Install | You get |
| :--- | :--- | :--- |
| **A CSM** | `csm-toolkit` | Calls, renewals, escalations, hard conversations, customer writing, your own book |
| **A team lead** | `cs-team-lead-toolkit` | Review your team's reads, coach from a call, forecast, audit health scores, team plays |
| **A head of CS** | `cs-leader-toolkit` | Forecast, coverage model, board retention narrative, health score design, expansion handoff |
| **All of it** | `customer-success-skills` | Everything below |

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install csm-toolkit@cspulse
```

No terminal? In the Claude app: download this repo, zip one folder from `skills/`, then **Customize, Skills, Create skill, Upload a skill**. The folder name must match the skill name.

Or paste this to an assistant that can read and write files:

```
Install skills from https://github.com/CSPulse/customer-success-skills.
Clone it and copy the skill folders I want into ~/.claude/skills/. Start with
cs-start. Tell me where each one landed.
```

---

## What is in it

You do not call skills by name. You describe the situation and the right one fires.

### Before and after a call
| Skill | The job |
| :--- | :--- |
| [`call-prep`](skills/call-prep) | Ten-minute prep around the one outcome the call has to produce, with the landmine and the fallback ask |
| [`call-recap`](skills/call-recap) | An honest read of the call plus every follow-up email it generated, grouped by recipient |
| [`exec-conversation`](skills/exec-conversation) | Fifteen minutes with someone three levels up: one ask, one number they recognize |

### Read the account
| Skill | The job |
| :--- | :--- |
| [`renewal-risk`](skills/renewal-risk) | Will they renew: the call, the decider, the mechanism, the dollars, the play |
| [`renewal-runway`](skills/renewal-runway) | A dated backward plan from the opt-out date, with a pass or fail test at each checkpoint |
| [`champion-loss`](skills/champion-loss) | The first ten days after your sponsor leaves, with the three messages to send |
| [`stakeholder-map`](skills/stakeholder-map) | Who decides, by what they can do rather than their title; who you have never met |
| [`churn-postmortem`](skills/churn-postmortem) | Why they actually left, and what was detectable at the time |

### Run the moments that matter
| Skill | The job |
| :--- | :--- |
| [`escalation`](skills/escalation) | The first four hours of an account on fire: holding statement, the forwardable answer, the internal ask |
| [`hard-conversation`](skills/hard-conversation) | The two opening sentences first, then what you can offer and on whose authority |
| [`renewal-negotiation`](skills/renewal-negotiation) | The concession ladder, the walk-away and the exact sentence for "not on the table" |
| [`business-review`](skills/business-review) | A QBR that drives a decision, slide by slide, and when to send an async report instead |
| [`expansion-case`](skills/expansion-case) | The one-page business case your champion carries without you in the room |
| [`onboarding-plan`](skills/onboarding-plan) | A first-90-days plan aimed at a result the customer can name |
| [`offboarding`](skills/offboarding) | Losing well: the data handed over fast, the honest exit conversation, the door left open |

### Write to customers
| Skill | The job |
| :--- | :--- |
| [`email-critic`](skills/email-critic) | Checks a draft against the transcript and thread, facts before prose |
| [`customer-update`](skills/customer-update) | The proactive message nobody wants to send, segmented by impact |
| [`one-pager`](skills/one-pager) | The page a sponsor forwards to their boss without editing |

### Run your book
| Skill | The job |
| :--- | :--- |
| [`book-triage`](skills/book-triage) | This week's five to eight accounts, the silent one, and the not-this-week list with triggers |
| [`account-plan`](skills/account-plan) | The plan the next owner can pick up in month four |
| [`handoff`](skills/handoff) | Leaving an account or inheriting one: what never reaches a system, and the 30 day check |
| [`advocacy-ask`](skills/advocacy-ask) | References and case studies, timed to realized value rather than renewal |
| [`internal-ask`](skills/internal-ask) | Getting your own company to act: product requests and urgent leadership asks |

### Lead a team or the function
| Skill | The job |
| :--- | :--- |
| [`renewal-forecast`](skills/renewal-forecast) | A forecast in dollars with contraction on its own line and correlated risks grouped as one bet |
| [`portfolio-review`](skills/portfolio-review) | Reviews your team's reads, not their accounts, with a random sample |
| [`coaching`](skills/coaching) | A one-page coaching plan from a call or an observation |
| [`playbook-builder`](skills/playbook-builder) | Turns a recurring situation into a repeatable team play |
| [`health-score`](skills/health-score) | Audit the score you have against accounts that actually left, or build a small explainable one |
| [`coverage-model`](skills/coverage-model) | Who gets a named CSM, who is pooled, who is digital, tested against real churn |
| [`nrr-narrative`](skills/nrr-narrative) | Retention decomposed before it is narrated, with gross next to net |
| [`csql-motion`](skills/csql-motion) | Expansion signals from CS to sales without burning the relationship |

### Shared
| Skill | The job |
| :--- | :--- |
| [`cs-start`](skills/cs-start) | The front door: routes any situation, runs a demo, anonymizes output for sharing |
| [`account-context`](skills/account-context) | Optional. A 60-second profile of your product and segments so every other skill stops guessing |

---

## Why these are different

- **Short and executable.** Each skill is a page of instructions, not an essay. They load fast and they behave the same way twice.
- **Every skill ships a filled example.** Open any `skills/<name>/examples/sample.md` and see exactly what you will get before you install.
- **Verdict first.** The call, the draft or the answer leads. The reasoning follows.
- **Evidence is tagged.** Facts are `said`, `seen` or `inferred`, so a guess never passes as a finding.
- **Honest about gaps.** Every output ends with what it could not check. Missing input never blocks a skill; it changes what the skill claims.
- **Dollars and dates, not colors.** Ranges and deadlines, not green-yellow-red.
- **No invented statistics.** Mechanisms over numbers. Where a number is a default, it says so.
- **Nothing is a prerequisite.** No setup, no connectors, no other skill required. Connected tools make it faster; they are never needed.

The thinking is built on published customer success practice. See [SOURCES.md](SOURCES.md) for what each skill draws on and how strong the evidence is.

---

## Contributing

The most useful thing you can do is tell us a skill is wrong. Open an issue saying what happens in your world and what the skill assumed. Missing a skill? Describe the job and what good output looks like.

Writing one? Read [template/SPEC.md](template/SPEC.md), copy [template/SKILL.md](template/SKILL.md), ship a filled `examples/sample.md`, and run `python3 tools/check.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).

Maintained by [CS Pulse](https://cspulse.com?ref=github), a community for customer success practitioners.

## License

MIT. See [LICENSE](LICENSE).
