# Metric definitions

Loaded when building a scorecard. Targets shown are common defaults, set your own. Each metric: numerator / denominator, period, owner, what it hides, counter-metric.

## Lagging (what already happened)

| Metric | Numerator / denominator | Period | Owner | What it hides | Counter |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Gross retention | (start ARR - churn - contraction) / start ARR | trailing 12 months | CS lead | Expansion is excluded, so it ignores growth; a few big accounts dominate | Net retention |
| Net retention | (start ARR - churn - contraction + expansion) / start ARR | trailing 12 months | CS lead | One large expansion can mask several lost logos | Gross retention, logo churn |
| Logo churn | logos lost / logos at start | trailing 12 months | CS lead | Treats a $5k and a $500k logo alike | ARR churn |
| ARR at risk | ARR of accounts flagged at risk / current ARR | today | CSM | Depends on who flags and when; a flag-shy team shows zero | Back-test: flagged then lost |
| Renewal rate on time | renewals signed by opt-out date / renewals due | quarter | CSM | Early discounted renewals count as wins | Average price change at renewal |
| Contraction | ARR reduced on accounts that stayed / start ARR | trailing 12 months | CSM | Often precedes churn; small each, large together | Seats unused at renewal |

## Leading (what is about to happen)

| Metric | Numerator / denominator | Period | Owner | What it hides | Counter |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Health, ARR-weighted | ARR in green, yellow, red / total ARR | weekly | CSM | A score nobody back-tested; averaging hides one red dimension | Churned accounts' score 90 days before |
| Adoption, breadth | active seats or teams / licensed | trailing 30 days | CSM | Active is a login, not value | Depth: key feature use |
| Adoption, depth | accounts using the key feature weekly / accounts | trailing 30 days | CSM | Chosen feature may not be the value driver | Customer-stated outcome |
| Sentiment | share of responding contacts positive; name the survey | quarter | CSM | Low response means silence; a score is a person, not an account | Response rate, who is missing |
| Time to first value | days from signature to the agreed first outcome | per cohort | onboarding owner | Averages hide a long tail | Share live by day 60 |
| Champion coverage | accounts with an engaged champion (contact in 60 days) / accounts | monthly | CSM | One champion is single-threaded | Accounts with a second contact |
| Executive coverage | accounts where the economic buyer was spoken to in 90 days / accounts | quarterly | CSM | A meeting is not support | Renewals decided by an unmet buyer |
| Contact cadence | accounts touched within their tier's cadence / accounts | monthly | CSM | Touch type is ignored | Renewals kept per touch |
| Reply time | median hours from customer message to first reply | weekly | CSM | Fast replies, wrong answers | Customer-stated satisfaction |
| Recap rate | calls with a recap sent in 24 hours / customer calls | monthly | CSM | Quality of the recap | Commitments closed on time |
| Tasks on time | tasks done by due date / tasks due | monthly | CSM | Easy tasks inflate it | Overdue promises to customers |
| Success plans in place | accounts with a dated plan reviewed in 90 days / accounts above the plan threshold | quarterly | CSM | A plan on file is not a plan in use | Plan goals hit |

## By level

- **Book (CSM, weekly):** health ARR-weighted, ARR at risk, renewals in 30, 60, 90 days, contact cadence, reply time, recap rate, tasks on time.
- **Team (lead, weekly or monthly):** the book set rolled up by CSM, plus gross and net retention, contraction, champion coverage, success plans, time to first value, and the spread between CSMs.
- **Function (leader, quarterly):** gross and net retention with the bridge, logo churn, ARR at risk with back-test, concentration (top accounts' share of ARR, largest renewal month's share), cost to serve, expansion sourced.

## Common starting targets

Set your own; these exist only to start a conversation. Gross retention 90%. Net retention 100 to 110%, higher with a strong expansion motion. Logo churn under 10%. Champion coverage 90%. Cadence coverage 90%. Recap within 24 hours for most calls. Replace each with the book's trailing baseline after two quarters of data.
