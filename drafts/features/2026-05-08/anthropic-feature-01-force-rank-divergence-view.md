# Force Rank Divergence View
Status: Draft
Generated: 2026-05-08 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** A Signal Hunter scanning the leaderboard sees overall rank but can't quickly spot which algos are doing something different — crushing it in the last 30 days while ranked #40 all-time, or vice versa. That honest divergence is buried.
- **Goal:** Surface algos where rolling rank (30D, 7D) meaningfully differs from force rank. Show the Signal Hunter which signals are still unresolved or staging a comeback.
- **Metric:** Paid user engagement: % who click into an algo from the divergence view per session; CTR on divergence-flagged rows vs. non-flagged rows.

## 2. User Stories

- As a Signal Hunter, I want to see algos where 30D rank is top 10 but force rank is bottom 20, so I can spot which signals might be turning real.
- As the Receipts Guy, I want to see an algo's rank history (force, 30D, 7D, today) in one row, so I can spot both the honest failures and the honest comebacks.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Leaderboard rows include a small divergence indicator (e.g., ↗ or ↘) when 30D rank differs from force rank by >15 positions; clicking it expands a mini history: force rank, 30D rank, 7D rank, 1D rank.
- **Requirement 2:** Sorting by 'divergence' ranks algos by the largest gap between force and rolling rank; ties break to force rank.
- **Requirement 3:** Divergence view is read-only; no filters or toggles — it is a column, not a mode.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Keep the indicator minimal (one character, no color). The history should be text only, not a chart. No animation. On mobile, the divergence column compresses to icon-only; tap to see the 4-rank breakdown in a small overlay. This answers the question 'is this algo actually changing?' without leaving the leaderboard.

## 5. Acceptance Criteria (AC)

- Divergence indicator appears on any algo where |force_rank - 30d_rank| > 15.
- Clicking or tapping the indicator shows a 2x2 grid: force rank, 30D rank, 7D rank, 1D rank; each cell shows the rank number and the date it was calculated.
- Sorting by 'divergence' produces a consistent order (largest gap first) and is repeatable across page loads.

## 6. Out of Scope

- Alerts or notifications when divergence changes.
- Predictive claims about which direction the algo is headed.
