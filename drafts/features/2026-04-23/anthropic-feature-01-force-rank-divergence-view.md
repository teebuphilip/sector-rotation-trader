# Force Rank Divergence View
Status: Draft
Generated: 2026-04-23 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** A Signal Hunter can't easily spot algos that are tanking overall but crushing the last 30 days — the honest contradictions that reveal which signals are actually waking up or dead on arrival.
- **Goal:** Surface algos where all-time rank and rolling 30D rank differ by >20 positions, letting users spot reversals and decay patterns without smoothing over the noise.
- **Metric:** % of paid users who click into at least one divergence card per week; time spent on divergence view.

## 2. User Stories

- As a Signal Hunter, I want to see which algos have flipped from bottom-quartile to top-quartile in the last 30 days, so I can identify signals that might have found their footing.
- As a Receipts Guy, I want to see the full rank history (all-time, 90D, 30D, 7D) on one card, so I can track how bad an algo really got and whether it's actually recovering or just got lucky.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Compute divergence delta (all-time rank minus 30D rank) for every algo; flag if delta >= 20 or <= -20.
- **Requirement 2:** Render mini sparkline showing 30-day rank trajectory (not equity curve, just force rank movement) on divergence cards.
- **Requirement 3:** Divergence view must be sortable by delta size, recency of divergence start, and current 30D rank; filter by bucket (ALPHA / noise / unresolved).

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** No explanation needed — the cards are self-contained: algo name, all-time rank, 30D rank, delta, sparkline, bucket tag. One click goes to full algo detail. Divergence view lives as a toggle or tab on the main leaderboard, not a separate page. Desktop-first; mobile shows abbreviated version (name, ranks, sparkline only).

## 5. Acceptance Criteria (AC)

- Divergence delta calculation is correct for all algos with >7 days of history; algos with <7 days are excluded.
- Sparkline reflects actual daily force rank changes; if an algo hasn't traded in 3+ days, that shows as a flat line segment.
- View loads in <2s on desktop, handles 100+ algos without lag; mobile view renders correctly on iPhone SE and up.

## 6. Out of Scope

- Predictive modeling of which divergences will continue or reverse; we show the pattern, not the forecast.
- Notification or alert when divergence threshold is crossed; this is a pull feature only.
