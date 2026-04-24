# Signal Decay Curves
Status: Draft
Generated: 2026-04-24 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Receipts Guy struggles to see how signal performance degrades or recovers over time, obscuring true reliability beyond raw scores.
- **Goal:** Surface a small, inline chart showing each signal’s performance decay or rebound trajectory over recent weeks, emphasizing failures as much as wins.
- **Metric:** Increase time spent on leaderboard page by 15% among paying users.

## 2. User Stories

- As a Receipts Guy, I want to see how a signal’s edge fades or strengthens over time, so that I’m not fooled by stale top ranks.
- As a Signal Hunter, I want to identify signals with improving momentum despite low overall rank, so I can spot interesting anomalies.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Display a miniature line graph next to each signal on the leaderboard showing rolling 30-day performance trend.
- **Requirement 2:** Include negative dips and flatlining signals with equal visual weight to positive spikes.
- **Requirement 3:** Update curves in real-time with latest trade results; if offline, show last cached data with 'stale' label.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use hand-drawn style lines with rough edges to match the lab’s unpolished vibe; red dips and green rises with no smoothing to preserve rawness.

## 5. Acceptance Criteria (AC)

- Miniature trend lines appear next to every signal name on desktop and mobile.
- Negative performance dips are visually distinct and not hidden or softened.
- Data updates within 5 minutes of new trade results.

## 6. Out of Scope

- No signal ranking changes triggered by decay curves.
- No onboarding or tutorial overlays for interpreting curves.
