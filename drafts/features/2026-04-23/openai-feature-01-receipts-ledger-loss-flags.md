# Receipts Ledger: Loss Flags
Status: Draft
Generated: 2026-04-23 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Receipts Guys struggle to quickly identify and verify signal failures and losses amidst winning algos on the leaderboard.
- **Goal:** Make losses and failed trades visually and contextually explicit on the leaderboard so Receipts Guys can instantly see the full truth.
- **Metric:** Increase the time spent by Receipts Guys on loss-related signal data by 30%.

## 2. User Stories

- As a Receipts Guy, I want losses and failed signals flagged prominently on the leaderboard, so that I can verify the honesty of the lab’s results.
- As a Receipts Guy, I want to compare failure patterns across signals, so that I can spot systemic survivorship bias or buried losses.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a distinct 'Loss Flag' icon or color code next to algos with negative returns or recent failures.
- **Requirement 2:** Display raw loss counts and failure streaks directly on the leaderboard row without hiding details.
- **Requirement 3:** Ensure the feature works offline by caching last known loss flags for offline leaderboard viewing.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a worn paper receipt motif for loss flags, maybe a red stamp style icon labeled 'LOSS' to fit the honest lab notebook vibe.

## 5. Acceptance Criteria (AC)

- Loss flags appear next to all signals with negative recent returns on both desktop and mobile.
- Clicking the loss flag reveals a mini breakdown of loss trades inline.
- No loss data is hidden or aggregated away; raw counts and streaks always visible.

## 6. Out of Scope

- Loss smoothing or aggregation into a single score.
- Onboarding tooltips explaining loss flags.
