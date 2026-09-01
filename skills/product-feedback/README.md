# product feedback

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Turns a customer's feature request into something a product team can actually act on - the job to be done rather than the feature they named, how many accounts share the job, and what happens if nothing changes, said honestly. Product teams rarely ignore customer success on purpose; they ignore feedback that arrives as a feature name with an account attached and no way to weigh it against the forty other asks competing for the same quarter.

It starts by sorting the request into what it actually is: a bug (support fixes it today, no roadmap involved), a discoverability problem (the product already does this and the customer couldn't find it - submitting this as a feature request quietly tells product their product is worse than it is), a misunderstanding of the job, a genuine gap, or a gap with a workaround. Only the last two belong in a product submission, and they're different submissions. It then translates the customer's already-designed solution back into the underlying job, what they do today to work around it, and what that costs them in their own units - without proposing a fix of its own, since a submission that leads with a design gets argued about on the design instead of considered on the problem. Sizing is where credibility gets spent or earned: it counts accounts that share the job, not accounts that asked for the same feature name, states a churn claim only when the CSM would defend it at the renewal, and writes "they'll be annoyed and renew anyway" when that's the honest answer. It finishes by writing the submission in the product team's own intake format and closing the loop back to the customer - including when the answer is no, because two rounds of silence is what teaches a customer to stop reporting anything.

The failure this exists to prevent: **forwarding a customer email into a channel.** It transfers the request and none of the information that would let anyone act on it, and it puts the translation work on the person least equipped to do it.

Part of the **Work it internally** group in this library.

## Who this is for

For CSMs who need their own company to act, not just the customer.

## What this needs

Works with nothing but what the customer asked for and who they are. Gets better with other accounts raising it, usage data, your product team's intake format.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the product-feedback skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/product-feedback,
zip the product-feedback folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/product-feedback`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
