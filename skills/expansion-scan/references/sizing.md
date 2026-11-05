# Sizing and confidence defaults

Every number here is a common default. Replace it with your own history of what expansions actually closed at.

## Confidence

| Level | Weight | When |
| :--- | :--- | :--- |
| High | 0.6 | The customer stated a need in their words, and the payer and rough scope are known |
| Medium | 0.3 | The customer stated a need, but payer or scope is unknown |
| Low | 0.1 | Usage or capacity signals only, nobody on their side has said anything |

Weighted value = expected size times weight. It ranks the list. It is not a forecast.

## Sizing, strongest basis first

1. **Customer-stated scope times today's unit price.** "Three more clinics, about ten people each" gives 30 units. Mark the headcount `inferred` until they confirm.
2. **Capacity signal (units 90 percent or more in use).** Add about a quarter of current units at today's unit price. Unit price is ARR divided by units bought, which ignores discounts, so confirm it.
3. **Proof signal (customer-stated result).** About a fifth of ARR as the size of the conversation.
4. **Momentum signal only (usage up by about a third).** About 15 percent of ARR.

Low = the smaller of the methods that apply, or half of expected when only one applies. Expected = the customer-side figure when they gave one, else the default.

## Hold list tests

Hold the account if any is true: open severity-one issue, adoption stalled or falling, sponsor gone or unmet decider, renewal notice date inside 60 days, last reply from the champion was cool. Write the fix and a rescan date for each.

## Timing

Now (ask within two weeks), Next quarter (wait for their budget cycle or a milestone), Wait (a blocker or the notice window).
