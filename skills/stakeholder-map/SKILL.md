---
name: stakeholder-map
description: >
  Maps the people who decide an account's outcome by what they can do to it, not by their job titles. Trigger whenever the user says "stakeholder map", "who are the stakeholders", "relationship map", "who do I need to know", "who actually decides", "who signs", "map the account", "we are single-threaded", "my champion left", or asks who to call about a renewal. Also trigger when an account has gone quiet, when a new executive has arrived on the customer side, or before any first meeting with an inherited account. It sorts people by influence on the outcome rather than seniority, flags who has never actually been met, tests for single-threading, and tracks who is new, who has gone, and who used to respond and stopped. Runs on whatever the user knows and marks every gap as a gap.
---

# Stakeholder Map

An org chart tells you what people are called. A stakeholder map tells you what they can do to this renewal. They are not the same document and the first one is easy to mistake for the second.

The useful question is never "what is their title". It is **"what happens to this account if this person says no, and what happens if they leave".**

The failure this exists to prevent: **a beautifully complete contact list on an account nobody can name a decider for.**

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first. It says who signs in this business, by role, and whether customer success ever meets them. That answer sets the bar for everything below. Where it is absent, carry on and name the assumption.

**Minimum: the names you know and roughly what they do.** Gaps are the output here, not a blocker.

**Better with** the last few months of email and meeting history, so "who used to respond and stopped" can be answered rather than guessed.

**Best with** the original deal notes, which usually name the economic buyer and almost always name the sceptic that nobody has thought about since.

---

## Step 1: Sort by what they can do, not what they are called

Six positions. A person can hold more than one, and the same title maps differently in different companies.

| Position | What defines them | Why they matter |
| :--- | :--- | :--- |
| **Economic buyer** | Controls the budget line. Can say yes alone | The renewal is theirs. Everything else is influence |
| **Champion** | Wants this to succeed and will spend their own credibility on it | Carries you internally in rooms you are not in |
| **Sceptic** | Argued against it, or would if asked | The most frequently omitted and most often fatal |
| **User** | Uses the product. Usually has no budget authority | Generates the evidence, decides nothing |
| **Coach** | Tells you how the organisation actually works | Not the same as a champion. A coach may not even like the product |
| **Gatekeeper** | Procurement, security, legal, IT. Can block without deciding | Cannot say yes. Can absolutely say no |

**Getting the sceptic on the list is the point of the exercise.** Every account has one. If the map has no sceptic, it is incomplete rather than exceptional.

---

## Step 2: Add the column everybody skips

For each person: **have you actually spoken to them?**

Three honest values, and the difference between them matters:

- **Met.** A real conversation, not a group call they attended
- **Aware of.** You know they exist and what they do. You have never spoken
- **Assumed.** You believe this role exists and someone fills it, but you cannot name them

**If the economic buyer is Aware-of or Assumed, that is the account's largest risk and it outranks every usage signal on the page.** Say it first, before anything else in the read, and do not bury it under relationship detail.

---

## Step 3: Test for single-threading

Count the people who would have to be replaced if one person left tomorrow.

- **One relationship** means no recovery path. Champion departure ends the account's institutional memory of why it was bought
- **Two, both in the same team,** is single-threading wearing a disguise
- **Three or more, across functions,** is genuine coverage

Then ask the harder version: **if your champion left this month, who inside the customer could explain why they bought this?** If the answer is nobody, the value story lives in one person's head and leaves with them.

---

## Step 4: Track movement, not just position

A map is a snapshot, and the changes carry more signal than the state.

- **Who is new.** A new executive reviews everything their predecessor bought. This is not personal and it is not negotiable
- **Who has left**, and whether anyone inherited what they were doing
- **Who has gone quiet.** Someone who used to reply within a day and now takes a week has told you something. Non-response from a previously responsive person is the signal; a low survey score is not
- **Whose remit changed.** Same person, same title, different budget, is a change nobody logs

Sponsor-specific silence deserves its own flag. The working team still engaged while the sponsor has gone quiet usually means the decision has moved above your line of sight.

---

## Step 5: Name the gaps and what closes them

For each gap, one line on how it gets closed and by when. A map that identifies a missing economic-buyer relationship and stops there has described the problem.

Realistic routes: an introduction from the champion, a business review with the sponsor invited, an executive-to-executive introduction from your own side, or a specific piece of value worth their fifteen minutes.

**Be honest about the ones that will not close.** Some economic buyers will not meet a vendor. That is a real constraint and it changes the play rather than the effort.

---

## Step 6: Write it down

Fill `assets/map-template.md` and hand over the completed map.

Lead with the answer to "who decides and have we met them". Everything else is supporting detail.

---

## Output

1. **The decider**, named, and whether you have met them
2. **The map**, by position rather than title, with the met column filled
3. **Single-threading verdict**, with the count
4. **What has changed** since the last look: arrivals, departures, silences
5. **The gaps**, each with a route to close it and a date
6. **What you could not establish**

---

## Failure modes

- **Reproducing the org chart.** Seniority is not influence, and the person who signs is often not the most senior person on the list
- **No sceptic.** Every account has one. An absent sceptic means the map is incomplete
- **Counting group calls as relationships.** Someone who has been on a call with you is not someone you have met
- **Mistaking the champion's enthusiasm for the buyer's decision.** A champion's optimism is evidence about the champion
- **Treating the map as static.** The version that is a quarter old is describing an organisation that has moved
- **Listing a gap without a route.** The gap was already obvious. The route is the work

---

## What good looks like

- The first line names the decider and says whether you have met them
- The sceptic is on the map
- Single-threading has a number, not an impression
- Every gap has a named route and a date
- Someone picking up this account could tell who to call first, and why

---

## Reference files

- `assets/map-template.md` - the map to fill
