# Signal Divorce Papers
Status: Draft
Generated: 2026-05-01 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** A Signal Hunter or Alt-Data Nerd has no clear record of *why* an algo stopped running or was killed. Was it noise? Did it break? Did the operator give up? The silence is worse than the failure.
- **Goal:** Give every dead or retired signal an explicit exit memo—operator-written, timestamped, honest. Make failure a readable event, not a ghost.
- **Metric:** Subscriber engagement with retired algos increases 40%. Conversion from free to paid increases 15% (users see the lab is willing to kill its darlings).

## 2. User Stories

- As a Signal Hunter, I want to read why Biscotti was retired so I can decide if the same weakness applies to the signal I'm watching now.
- As an Alt-Data Nerd, I want to see a pattern in *how* signals die (momentum decay vs data degradation vs operator burnout) so I can spot warning signs in live algos.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Operator can attach a timestamped, plain-text memo to any algo on retirement. Memo is public and lives on the algo's detail page forever.
- **Requirement 2:** Retired algos remain on leaderboard but grouped separately (e.g., 'Graveyard'). Last equity curve and win rate stay visible. No hiding, no archiving.
- **Requirement 3:** Memo field supports Markdown. No WYSIWYG editor. Plain text only. Max 500 words. The operator writes it like a lab notebook entry, not a press release.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Retired algos sit at the bottom of the leaderboard in a distinct section. Each entry shows: algo name, final rank, total days running, final equity, and a small 'Exit Note' link that expands inline. The memo appears in a monospace font, unformatted. No design flourishes. It looks like a handwritten note scanned and pasted.

## 5. Acceptance Criteria (AC)

- An operator can retire an algo and attach a memo. The memo appears on the algo detail page within 1 minute of submission.
- Free users see that a memo exists but cannot read it (paid feature). Paid users see the full memo inline.
- Retired algos appear in search and sort results. They do not disappear from the leaderboard.

## 6. Out of Scope

- Auto-detection of when an algo should be retired (no machine decision-making).
- Email notifications when an algo is retired.
