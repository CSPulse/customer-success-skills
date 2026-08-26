# Getting the Transcript

This skill is recorder-agnostic. It does not care which tool captured the call, only that you end up holding **the complete verbatim transcript**. Everything below is about how to get there from whatever the user gave you.

The AI summary, where one exists, is a cross-check. It is never the source.

---

## The order to try

**1. A connected recorder.** If the session has a meeting-recorder connector, use it. Nearly all of them follow the same three-call shape:

- a resolver that turns a pasted link or a call ID into an internal recording ID
- a transcript call that returns the verbatim text
- a summary or notes call, and often an action-items call, for cross-checking

Find the resolver first. Do not run a search or list call when the user has already pasted a specific link, because that is discovery and you already know which call you want.

**2. An unrecognised link.** Share links rarely look like the platform that issued them, so do not rule a connector out on the URL alone. Try, in order:

- the resolver on each connected recorder
- `WebFetch` on the URL, since some platforms serve a readable transcript page

**3. Ask.** If nothing resolves, or no recorder is connected at all, stop and ask. Say which routes you tried and what you need. Be specific about what a usable handoff contains:

- the full verbatim transcript, not the summary or the highlights
- the auto-generated summary or notes as well, if the tool produced them
- the attendee list with full names, and their email addresses if the user has them
- the call date and, ideally, its length

Accept it as a paste, a file upload, or an export in any format. A transcript is a transcript.

**4. Never invent.** Do not build a recap from a URL slug, a meeting title, a calendar invite, or a summary alone. An invented recap is worse than no recap, because it is confidently wrong about what a customer said, and it reaches that customer in an email.

---

## A pasted transcript

The normal case, not the fallback. Skip resolution and go straight to reading it. Note in the output document that the source was a paste, so anyone reading later knows there is no recording to check a disputed line against.

If the paste is clearly a summary rather than a transcript, say so before working from it. The read on the call will be shallower and the user should know why.

---

## Notes on specific recorders

Only relevant when that connector is present. Treat these as shortcuts, not requirements.

| Recorder | Getting there |
| :--- | :--- |
| Fathom | Resolve a pasted URL or call ID to a `recording_id`. A bare number may be either a call ID or a recording ID, so if the first lookup misses, retry the same number as the other kind. Pass the canonical URL to the transcript call so segments come back with timestamped deep links, which let the user jump to the moment behind any claim you make. |
| Grain | Resolve the URL, then pull the transcript, notes and action items. Its action items catch explicit commitments and miss the ones phrased as questions. "Should we get 30 minutes on your calendar?" is an action item. |
| Granola | Locate the meeting, then pull the transcript. Granola leans note-heavy, so check whether what came back is a real transcript or a summary wearing one's clothes. |
| Wispr Flow | Resolve the share link or search for the meeting. Its attendee-email lookup is useful even when the transcript came from somewhere else, because it resolves attendees to real addresses. |

Recorders not listed here are not unsupported. Look for the same three-call shape and it will usually be there.

---

## Timezones

Recording platforms commonly return timestamps in UTC. Convert to the user's local timezone before showing them anything, and say which timezone you used when a time appears in a draft email.

---

## Reading any transcript

Auto-transcription mangles names, and it mangles names outside the transcriber's dominant language especially badly - expect plausible-looking near-misses rather than obvious garbage, which is what makes them easy to miss. Reconcile every name against the account's stakeholder list before it reaches a draft. Misspelling a senior stakeholder's name in an email to them is a small error with an outsized cost.

Also expect the transcript to attribute lines to the wrong speaker during crosstalk. If a quote is load-bearing for your read on the call, check the surrounding turns make sense before attributing it.

Cross-check the transcript against the summary on anything you plan to assert. Where they disagree, the transcript wins.
