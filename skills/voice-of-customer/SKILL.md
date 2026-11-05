---
name: voice-of-customer
description: >
  Use when the user says "voice of the customer", "VoC report", "what are customers asking for", "themes across my accounts", "product feedback report", "what are customers saying about the product". Produces a ranked theme report from pasted call notes, emails and tickets: accounts and ARR per theme, bug versus gap versus misunderstanding, the need behind each ask, quotes with source, and who to tell back. Not for escalating one customer's urgent issue (use internal-ask).
---

# Voice of the Customer

Paste what customers said across accounts. Get the monthly product report: themes ranked by accounts and ARR, the need under each request, the customers' own words, and the loop to close.

## Start here

If the user pasted notes, emails or tickets from two or more accounts, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The raw material, with the account name on each piece (call notes, thread excerpts, tickets)
2. ARR per account (rough is fine) and which accounts are strategic, a reference, or renewing soon
3. The period, and who reads the report (product, leadership)

If an "Account context" block exists in the conversation, use it to learn what the product does and which words the business uses.

## Do this

1. **Extract items.** One line per thing a customer asked for, reported broken, complained about or praised: account, who said it (role), date, source. Skip pleasantries, resolved issues and anything the vendor said. Quote only words that are in the paste.
2. **Classify each item.** Bug (should work, does not), gap (never did this), misunderstanding (it exists, they could not find or use it), praise. Each routes to a different owner: engineering, product, enablement or docs, the team.
3. **Group into themes** of two to five words. Merge items that share a need even when the requested feature differs.
4. **Count accounts, then ARR.** Per theme: distinct accounts, summed ARR of those accounts, share of the ARR read. Show mentions but never rank on them.
5. **Write the need.** Per top theme: the request as stated, then the job underneath ("so that ..."). If the paste does not show the job, write "need unknown" and the one question to ask which account.
6. **Flag who matters beyond ARR:** strategic or reference accounts, and anyone renewing inside 90 days (a common default, set your own).
7. **Close the loop.** Per theme: who to tell, what to say (yes, no, not yet, or it already exists) and by when. A no is sent too.

## Output

Use this skeleton. Keep it to one page plus quotes.

```
VOICE OF THE CUSTOMER: [period] | [n] accounts, $[ARR] read | [n] sources, [n] items
Headline: [top theme and the one thing to ask product, one sentence]

| # | Theme | Type | Accounts | ARR | Share of ARR read | Mentions |

Per theme (top 3 to 5)
[Theme] - [bug / gap / misunderstanding] - owner: [who]
Asked: [as stated]   Need: [job underneath, said / inferred]
"[verbatim quote]" - [account], [role], [source, date]
Ask: [what the user wants from the owner]

Flags: [strategic, reference or renewing accounts inside a theme]
Loop to close: [theme] - tell [accounts] - [yes / no / not yet / exists] - by [date]
Praise worth passing on: [quote, source]

What I could not check
- [sources not read, accounts silent, causes inferred]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Count accounts, not mentions.** One loud account repeating itself inflates a theme, while a quiet account saying it once is the better signal.
- **Show ARR next to the count, never instead of it.** ARR alone turns the biggest customer's wish list into the roadmap, and count alone hides where the money sits.
- **Separate bug, gap and misunderstanding.** They route to different owners: a misunderstanding sent to product burns a sprint, and a bug filed as a request waits in the backlog.
- **The request is rarely the need.** Three accounts asking for three features may share one job, and building the feature to the letter can miss it. Record the job, and label it inferred if the customer did not say it.
- **Keep the customer's own words.** A quote is verbatim with account, role and date, because product trusts a sentence they can trace and discounts a paraphrase.
- **Say which sources were read and which were not.** An account with no notes is silent, not satisfied, so name the gaps before anyone reads a ranking as the whole book.
- **Close the loop, including on a no.** Customers who hear a reasoned no keep telling you things, and customers who hear nothing stop.
- **A fix that serves one account is a favor, not a theme.** Say so, and route it through the normal exception path.

## Related (only if installed)

`internal-ask` to turn the top theme into a request your own company acts on. `customer-update` for the note back to every account behind a theme. `expansion-case` when a theme is also a paid need.
