# Signal Divergence Report
Status: Draft
Generated: 2026-05-15 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** A Signal Hunter sees an algo ranked #45 overall but #1 in the last 30 days and has no way to know if it's a real trend or noise. Divergence between force rank and rolling windows is invisible.
- **Goal:** Surface honest contradictions in algo performance so users can spot signals that are either recovering, degrading, or unresolved.
- **Metric:** Increase time-on-leaderboard by 15%. Track clicks on divergence-flagged algos. Measure paid subscriber engagement with detail pages for algos showing >10-rank divergence.

## 2. User Stories

- As a Signal Hunter, I want to see when an algo's 30-day rank differs from its all-time rank by >10 positions, so I can catch real momentum shifts or spot algos that are dying in slow motion.
- As an Alt-Data Nerd, I want to filter the leaderboard by divergence buckets (recovering, degrading, stable), so I can focus on the unresolved experiments worth monitoring.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Compute and cache divergence score (abs(force_rank - rolling_30d_rank)) for every algo on every update cycle.
- **Requirement 2:** Add optional 'Divergence View' toggle to leaderboard that highlights algos with >10-point gaps; sort by divergence magnitude descending.
- **Requirement 3:** Include divergence context on detail pages: 'Baileymol was rank 67 all-time but rank 8 last 30 days. Last trade 3 days ago.' Show the equity curve overlay with the divergence window shaded.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** No new page. Toggle on leaderboard. Divergence flagging uses a small directional arrow (↑ recovering, ↓ degrading) beside the rank. Clicking the arrow jumps to the detail page with the divergence window highlighted. Stark, no gradient. Names stay full — Baileymol is Baileymol.

## 5. Acceptance Criteria (AC)

- Leaderboard divergence toggle computes and displays in <500ms on a list of 200 algos.
- Divergence score is recalculated every trading session and persisted. A user visiting 3 days later sees the same divergence state.
- Detail page shows force rank, 30-day rank, and 90-day rank side-by-side with trade count and last trade date for each window.

## 6. Out of Scope

- Predictive divergence modeling or 'which divergences matter most' scoring — that is editorial, not algorithmic.
- Custom rolling window selection (divergence is always 30-day vs all-time; no user configuration).
