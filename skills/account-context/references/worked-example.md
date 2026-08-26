# Worked Example

*A completed context document for **Ledgerline**, an entirely fictional records-retention and audit-trail platform. Invented to show the level of specificity that makes this useful. Any resemblance to a real company is accidental.*

Read this for the texture, not the content. The useful version of every answer below is concrete enough to be wrong.

---

## The product

**What a customer says it does for them:**
> "It means when the regulator asks for seven years of approvals, we can produce them in an afternoon instead of three weeks."

**What they were doing before:**
> Shared drives plus a spreadsheet index, maintained by one person in compliance. That person is usually still there, and is usually the champion.

**What it is genuinely bad at:**
> Bulk migration of badly-organised legacy archives. The first ninety days are painful whenever the customer's existing filing was inconsistent, and we consistently underestimate this in the sales cycle.

---

## Segments

| Segment | Who buys | Who uses | Normal deployment | Onboarding when it goes well | What usually goes wrong |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Regulated enterprise | General Counsel or Chief Risk Officer | Compliance analysts, 4 to 12 seats, plus read-only access for auditors | 3 to 6 business units, phased | 10 to 14 weeks | Security review discovered late, adding 6 weeks |
| Mid-market financial services | Head of Compliance, with real budget scrutiny | 2 to 5 analysts | Single business unit | 4 to 6 weeks | Champion is the only user, so departure is fatal |
| Professional services firms | Managing Partner | Practice managers, 1 to 3 seats | Firm-wide from day one | 2 to 3 weeks | Seat count tracks their own headcount, so contraction is often not about us |

---

## Contract shape

| | |
| :--- | :--- |
| **Pricing model** | Seat-based, with a storage tier above 5TB |
| **Typical term** | 24 months for enterprise, 12 for everyone else |
| **Multi-year common?** | Yes in enterprise, and risk accumulates silently across it |
| **Notice or opt-out window** | 60 days for enterprise, 30 for mid-market |
| **Auto-renewal** | Yes, unless notice is served |
| **Who signs, by role** | General Counsel or CFO. Procurement runs the process |
| **Does CS ever meet them?** | Rarely. This is the single biggest structural risk on the book |

---

## The value metric

**The number the customer bought:**
> Hours to produce a complete audit response. Baselined at intake, typically 60 to 120 hours before, target under 8.

**Can anyone state it?**
> Yes for enterprise, where it is captured in the implementation kickoff and reviewed at each business review. **No for mid-market**, where it was never baselined, and that is why mid-market renewals are argued rather than confirmed.

---

## What healthy looks like here

| | |
| :--- | :--- |
| **Natural rhythm** | Event-driven, not daily. Spikes at audit windows and quarter close |
| **Is low usage ever the intended state?** | **Yes, and this is the most misread signal on the platform.** A well-run deployment ingests documents automatically and is barely opened between audits. Flat login counts on an enterprise account are usually correct behaviour |
| **Breadth of a full deployment** | 3 to 6 business units. Breadth matters far more than depth per user |
| **Integrations that matter** | The document source system and single sign-on |
| **What breaks if one disconnects** | If document ingestion disconnects, the archive silently stops updating and nobody notices until an audit fails. This is an account event, not a support ticket |
| **Seasonality** | Decisions freeze during audit periods and financial close. No meeting will land in those windows |

**Patterns that would worry us:**
> A stalled business-unit rollout. Bulk export activity. Ingestion integrations disconnecting. Any question about data portability or contract notice dates.

**Patterns that look alarming on a dashboard but are fine:**
> Near-zero logins between audit cycles. A drop in document views after a migration finishes. Both trip our health score and neither means anything.

---

## Motion and ownership

| | |
| :--- | :--- |
| **Motion** | Sales-led throughout. There is no self-serve tier |
| **What happens when a self-serve account gets big** | Not applicable |
| **Who owns the renewal** | Customer success for mid-market and professional services. A renewals desk for enterprise, with CS advising |
| **Who owns expansion** | The account executive. CS surfaces the signal and hands it over |
| **What CS does not own** | Technical escalation, which runs through support, and anything contractual, which runs through the renewals desk. Drafting an engineering escalation directly is not a path that exists here |

---

## What could not be established

| Gap | Where the answer probably lives |
| :--- | :--- |
| Whether mid-market accounts ever had a baseline captured at sale | The original opportunity notes in the CRM, or the implementation lead |
| The real churn reason for the three professional-services losses last year | Exit conversations, if any were recorded |
