---
name: renewal-negotiation
description: >
  Use when the user says "they want a discount", "procurement is involved", "how much can I give", "they want to cut seats", "competitor quoted us half", "prep the renewal negotiation", or "they are asking for utilization data". Produces a concession ladder (give, get, cost per rung), a written walk-away, the exact sentence for what is not on the table, and who holds the real deadline. Not for deciding if they will renew (use renewal-risk) or delivering a price increase (use hard-conversation).
---

# Renewal Negotiation

A one-page plan to walk into a price conversation knowing what you will trade, what you will not, and where you walk away.

## Start here

If the user gave the account, ARR, term end and what the customer is asking for, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, ARR, term end date, notice period, and whether silence renews or lapses
2. What they asked for (discount, fewer seats, competitor price) and from whom
3. The lowest number the user's company would accept

The contract, usage and a risk read are a bonus. If an "Account context" block exists in the conversation, use it for pricing model and who signs.

## Do this

1. **Gate it.** Is value agreed, meaning can you name a number they would accept as what they got? Is this a negotiation or a decision already taken? A downgrade request often means the scope decision is made. If either fails, say so first and change the plan.
2. **Pull the contract facts.** Opt-out date = renewal date minus notice period, and that is the real deadline. Note auto-renewal, any uplift clause and the term end.
3. **Write both walk-aways.** Yours as a number. Theirs honestly: do nothing, renew smaller, or switch, with the migration cost the person threatening it may not carry. Ask what the competitor demo or pilot actually covered.
4. **Name what each party is measured on.** Procurement usually needs a visible saving, not your margin. List wins that cost you less than a rate cut: term length, payment timing, capped uplift, added scope at near-zero cost, services hours.
5. **Build the ladder.** Three rungs and a floor, each with what you give, what you get, and what it costs in dollars. Lead the output with it.
6. **Write the not-on-the-table sentence** word for word. Say it once, repeat it unchanged.
7. **Map the time.** Whose deadline is real, who escalates on each side, and what you do if they go quiet near the opt-out date.

## Output

Use this skeleton. Concessions and numbers are suggestions for the user to confirm; the user sends anything.

```
RENEWAL NEGOTIATION: [Account] | [ARR] | term ends [date] | opt-out by [date]

Call: NEGOTIATE / VALUE FIRST / BEING INFORMED
Target: $[x]   Walk-away: $[floor]   Their real alternative: [do nothing / smaller / switch]

Concession ladder
| Rung  | I give | I get | It costs us |
| 1     |        |       | $[x]        |
| 2     |        |       |             |
| 3     |        |       |             |
| Floor | below this we do not renew | | $[ARR at risk] |

Not on the table: "[exact sentence]"
Procurement win that is not our margin: [item]
Contract: auto-renew [yes/no] | uplift [clause] | opt-out [date]
Time: [whose deadline is real, and why]
Four asks: discount / low usage / competitor quote / month to month - [one line each]
If it stalls: [who escalates, silence plan, the one thing I will not do]

What I could not check
- [gap, marked (assumed, confirm) inline]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Price needs value on the other side of the scale.** If they have not agreed the thing is worth having, you argue a number against nothing and lose.
- **Nothing is given free.** A free concession tells them the price was never real and invites the next ask.
- **Prefer a one-time credit to a rate cut.** A credit costs once. A cut compounds every year and becomes the starting number next time. If you must move on rate, give it an end date or a cap.
- **Separate rightsizing from rate.** "We use 60% of our seats" is a value conversation in a commercial costume. Granting both double-pays them.
- **Do not match a quote you have not seen.** Half-price quotes are often half the scope, year one only, or without services. A named competitor with no demo behind it is a procurement tactic.
- **Utilization data and contract copies are the negotiation starting.** Treat it as early, not admin.
- **The opt-out date is leverage for whoever knows it.** If silence renews, they are under time pressure, not you. Your quarter end is leverage against you once they know it.
- **Never close a number on the last three days of a quarter.** The calendar set it, and the next owner inherits the price.

## Related (only if installed)

`renewal-risk` first if there is no read yet. `hard-conversation` for delivering a price increase. `expansion-case` if scope and renewal are being discussed together.
