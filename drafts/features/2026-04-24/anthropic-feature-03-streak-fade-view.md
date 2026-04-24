# Streak & Fade View
Status: Draft
Generated: 2026-04-24 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Receipts Guy wants to see honest divergence (e.g., an algo that is #45 force rank but #1 rolling 30-day) but the current leaderboard flattens that tension into a single number; users can't quickly spot which signals are on a hot streak or losing steam.
- **Goal:** Surface rolling performance windows (7D, 30D, 90D) on the leaderboard as a lightweight sparkline or mini-chart, so users can see if an algo is heating up, cooling off, or flat.
- **Metric:** % of users who interact with sparkline (hover, click) per session; bounce rate on algo detail pages after sparkline engagement.

## 2. User Stories

- As a Receipts Guy, I want to see a mini-chart showing how an algo's rank has moved over the last 30 days, so I can spot if a top-ranked signal is fading or if a low-ranked one is suddenly hot.
- As a Signal Hunter, I want to filter for algos where 30-day performance is better than force rank, so I can find signals that are currently holding up despite a rougher all-time history.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a 'Spark' column to leaderboard (right of Force Rank): small line chart (7D, 30D, 90D rolling rank) visible on hover or always-on (configurable per user); chart shows rank position over time (lower = better), not returns.
- **Requirement 2:** Clicking the sparkline expands to a larger view showing the three windows side-by-side with win rate, Sharpe, and max drawdown for each window; operator's notes (if any) appear below.
- **Requirement 3:** Mobile: replace sparkline with a '↑↓' indicator (red/green) showing if 30-day rank is better or worse than force rank; tap to expand.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Sparkline uses simple black line on transparent bg, no fill. If an algo has < 7 days of history, show only available window(s). Algo names remain visible and unchanged. Interaction is read-only; no drag, no zoom.

## 5. Acceptance Criteria (AC)

- Sparkline data matches force rank calculation; a rank 5 algo on day X shows position 5 on the chart for that day.
- Expanded view loads in < 200ms and shows all three windows with correct date ranges even if algo has < 90 days of history.
- User preference (always-on or hover-only sparkline) persists across sessions.

## 6. Out of Scope

- Predictive trend forecasting or slope-based ranking; sparkline is historical only.
- Customizable time windows beyond 7D/30D/90D.
