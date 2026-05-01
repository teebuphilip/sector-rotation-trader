# Failure Waterfall View
Status: Draft
Generated: 2026-05-01 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Receipts Guys want to see losses and failures as clearly as wins but the current leaderboard mixes all outcomes in a linear list.
- **Goal:** Create a visual waterfall chart that shows each algo's cumulative wins and losses over time, emphasizing the drawdowns and failure streaks.
- **Metric:** Increase engagement time on leaderboard page by 15% among Receipts Guy users.

## 2. User Stories

- As a Receipts Guy, I want to see the sequence of wins and losses for each algo, so that I can verify the honest, unvarnished track record.
- As a Receipts Guy, I want to identify which algos have brutal drawdowns despite occasional wins, so I can call out survivorship bias.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Display a waterfall chart per algo, showing daily P&L contributions stacked cumulatively.
- **Requirement 2:** If the user is offline, show cached last-loaded waterfall charts with a stale data warning.
- **Requirement 3:** Integrate with the existing leaderboard so clicking an algo toggles its waterfall view in place.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use stark red and black color coding for losses and gains, no gloss or gradient. Label each bar with date and P&L. Named algos only, no generic IDs.

## 5. Acceptance Criteria (AC)

- Waterfall toggles open and close smoothly on desktop and mobile.
- Losses and drawdowns are visually distinct and cannot be hidden.
- Chart updates live with new trading data every day without user refresh.

## 6. Out of Scope

- No smoothing or aggregation of P&L data beyond daily granularity.
- No AI-generated commentary or signal quality scores.
