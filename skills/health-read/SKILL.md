---
name: health-read
description: >
  Audits an account health score rather than reporting it, so the number can be trusted or discounted deliberately. Trigger whenever the user says "health score", "account health", "is this account healthy", "the score says green but", "health check", "why is this account red", "our health scores are wrong", "audit the health score", or asks what an account's health actually is. Also trigger when a green account has just churned, or when someone is deciding whether to act on a score. It separates what is measured from what is inferred, finds the inputs that are proxies wearing the clothes of evidence, checks whether the composite is averaging a growing signal against a dying one, and asks the question nobody asks: has this score ever been tested against accounts that actually left. Runs on whatever the user can describe about their scoring, and says plainly which parts of the read are unsupported.
---

# Health Read

A health score is a hypothesis. Almost nowhere is it treated as one.

Most scores were designed once, in a room, with weights set by intuition. They were never back-tested against the accounts that actually churned, and they are never revisited when one of them does. That is not a scoring accident. It is a method nobody validated, producing a number everyone acts on.

The failure this exists to prevent: **"the score was green" offered as an explanation for a churn, when the score being green is the thing that needs explaining.**

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first. What healthy usage looks like in this business is the single most important input here, and without it a low number and a normal number are indistinguishable. Where it is absent, carry on and name the assumption.

**Minimum: the score and what goes into it,** even roughly. If the user does not know the inputs, that is the first finding.

**Better with** the input values for this account, the trend over the last two or three periods, and how the account compares to its own history.

**Best with** the list of accounts that churned in the last year and what their scores were three months before they left. That single list settles most of what follows.

---

## Step 1: Establish what the score actually measures

Before reading the number, get the inputs on the table. For each one:

- **What it is**
- **Its weight**, if anyone knows
- **Who chose that weight, and when**
- **Whether it has ever changed**

A score whose weights nobody can explain, set by someone who has left, and never revised, is not a measurement. Say so plainly and carry on, because it still tells you something about what the company pays attention to.

---

## Step 2: Sort every input into measured, proxy, or absent

This is the step that does the real work.

| Class | What it means | How to treat it |
| :--- | :--- | :--- |
| **Measured** | The thing itself is counted. Logins, tickets, seats provisioned | Evidence |
| **Proxy** | Something else is counted and treated as the thing. Login frequency standing in for value received | A hypothesis, and usually an untested one |
| **Absent** | It matters and nothing captures it. Whether the champion still has budget authority | The gap that decides most churns |

Most health scores are three or four proxies with a confidence interval nobody calculated. **Naming which is which is most of the value of this skill**, because it tells you exactly how much weight the number can carry.

The absent column is the important one. Sponsor change, budget reallocation, a competitor being evaluated, the value metric no longer being true: none of these appear in a usage-derived score, and all of them outrank everything that does.

---

## Step 3: Break the composite apart

A single number is an average, and averages hide the thing you need.

- **Module by module.** On a multi-product account, a growing module and a dying one produce a healthy middle. The average is not just uninformative, it is actively misleading
- **Team by team, or site by site.** Breadth collapsing while one team's depth increases reads as stable
- **Admin against end user.** Heavy configuration, permission audits and bulk export with flat end-user activity is a distinct pattern, and it usually means migration preparation or an audit rather than health
- **One power user.** If a single person generates most of the activity, the aggregate is one resignation away from zero

Ask directly: **what is the most alarming thing this score could be hiding, and would we see it?**

---

## Step 4: Read trajectory, not level

Level is close to worthless on its own. A score of 7 tells you nothing. A 7 that was 8.5 last month tells you a great deal.

- Alert on the **drop**, including drops that stay inside the healthy band
- Compare the account **against its own history** rather than against a portfolio average, because a normal level for one deployment is alarming for another
- Watch for **new-user provisioning stalling** while aggregate usage holds. Flat is not stable when nobody new is arriving

---

## Step 5: Check who the score is about

Usage describes the user. The renewal is decided by the buyer. In enterprise these are barely overlapping populations, and a usage-derived score is silent about the second one entirely.

Ask: **does anything in this score reflect the person who signs?** If the answer is no, the score is measuring adoption and calling it health, and it should be read as adoption from here on.

---

## Step 6: Ask whether the score has ever been right

The question almost nobody asks, and the one that settles how much to trust everything above.

- Of the accounts that churned in the last year, **what did their scores say three months before they left?**
- Of the accounts scored red a year ago, **how many actually churned?**
- Has the score ever been **changed as a result of either answer?**

Three outcomes, and they lead to different places:

**It has been tested and it predicts.** Rare. Trust the number, and say so, because that is worth knowing.

**It has been tested and it does not predict.** Then it is a dashboard, not a signal. Use it to start conversations and never to conclude one.

**It has never been tested.** The most common answer by a wide margin. **This is the finding.** Record it, and make the back-test the recommendation, because it is a day of work that changes every read afterwards.

---

## Step 7: Write the read

Fill `assets/score-audit.md` and give the user the completed audit.

State, in order: what the score says, what it is actually measuring, which inputs are proxies, what it is blind to, what the trajectory shows, and how much confidence the number deserves.

**Give a confidence level and justify it.** "Green, but the score is four usage proxies with no sponsor signal and has never been back-tested, so treat it as evidence the product is being used and nothing more" is a useful sentence. "Green" is not.

---

## Output

1. **What the score says**, and its direction over the last three periods
2. **The input audit**: measured, proxy, absent
3. **What the composite is hiding**, broken out by module, team or role
4. **What it cannot see at all**
5. **The score's track record**, or the plain statement that it has none
6. **How much to trust it**, with the reason
7. **What would make this read better**, and how long each would take

---

## Where this feeds

A score audit is worth more across a team than on one account. `portfolio-review` uses the same distinction to spot reads that match the health score exactly, which usually means the score did the thinking rather than the CSM.

---

## Failure modes

- **Reporting the score instead of auditing it.** The number is the input to this skill, never its output
- **Treating a proxy as a measurement** because it has been in the dashboard for two years
- **Averaging the disagreement.** When the score says green and the person who works the account says red, one of them is wrong. Splitting the difference destroys the information. Find out which
- **Reading quiet as healthy.** Accounts with the fewest logged touches are disproportionately risky and disproportionately rated green. The absence of bad news is not good news
- **Comparing to a portfolio average** rather than to the account's own baseline
- **Auditing the score and then acting on it anyway.** If the audit says the number is untested, the read has to carry that caveat forward

---

## What good looks like

- Someone reading it knows how much the score can be trusted, and why
- Every input is labelled as measured, proxy or absent
- The composite has been broken apart, and what it was hiding is named
- The question "has this ever been right" got an answer, even if the answer is "nobody has checked"
- The recommendation is specific enough to schedule

---

## Reference files

- `assets/score-audit.md` - the audit document to fill
