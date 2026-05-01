# Rolling Rank Divergence View
Status: Draft
Generated: 2026-05-01 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** An algo that ranks #2 overall but #47 in the last 30 days is interesting—it means something changed. But the current leaderboard hides that tension under a single number. Receipts Guy and Signal Hunter both need to spot these divergences.
- **Goal:** Surface the gap between force rank (all-time) and rolling rank (30D, 90D, YTD) so anomalies and reversals become visible without clicking.
- **Metric:** Paid subscribers spend 25% more time on leaderboard. Requests to add algos to 'watch list' increase 30%.

## 2. User Stories

- As a Signal Hunter, I want to see that TradingDogMem just dropped from #8 to #34 in the last month so I can investigate whether the signal is decaying or the market has shifted.
- As a Receipts Guy, I want proof that an algo that looks good overall is actually struggling right now, so I can trust that the lab isn't burying recent losses under old wins.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Leaderboard adds three new columns: 30D Rank, 90D Rank, YTD Rank. Each shows the algo's rank for that rolling window. If an algo hasn't run long enough for a window, show '—'.
- **Requirement 2:** Add a 'Divergence' badge next to force rank. Badge lights up if any rolling rank differs from force rank by >10 positions. Clicking badge sorts leaderboard by largest divergence first.
- **Requirement 3:** All rolling windows use the same force-rank methodology (win rate, days-running context, no curve-fitting). No separate scoring systems.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Columns are small and left-aligned. Numbers only, no icons. Badge is a small red dot with a label 'Diverging' that appears next to force rank if any window differs by >10 spots. Clicking the badge re-sorts the entire leaderboard by divergence magnitude (largest gap first). No animations. No hover states. Clean, plain.

## 5. Acceptance Criteria (AC)

- Rolling rank columns appear on the leaderboard for all paid users. Free users do not see these columns.
- Divergence badge appears only if an algo has run for at least 30 days and has a 30D rank available.
- Leaderboard remains sortable by all columns, including rolling ranks. Default sort is force rank, but user can sort by divergence.

## 6. Out of Scope

- Custom time window selection (e.g., user-defined rolling periods).
- Alerts or notifications when an algo enters/exits divergence state.
