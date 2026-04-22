# Divergence View
Status: Draft
Generated: 2026-04-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** A user can't quickly spot algos that are behaving differently across time horizons—an algo might be force-rank #45 all-time but rolling 30D #1, signaling a real shift. This divergence is buried in the detail pages and feels like noise instead of signal.
- **Goal:** Surface honest divergence as a feature, not a bug. Let users spot algos that are waking up or dying in real time.
- **Metric:** Clicks to divergence-flagged algos; time spent on algos with >10-rank delta between all-time and 30D force rank.

## 2. User Stories

- As a Signal Hunter, I want to see which algos have shifted rank dramatically in the last 30 days, so I can spot signals that are either hot right now or falling apart.
- As the Receipts Guy, I want to know if an algo's recent rank is misleading compared to its lifetime record, so I don't get fooled by a lucky streak.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Calculate force-rank delta between all-time and 30D rolling window for every algo on the leaderboard.
- **Requirement 2:** Flag algos with >10-rank delta (either direction) with a visual indicator (arrow up/down, no emoji, no language like 'momentum').
- **Requirement 3:** Clicking the flag opens a mini card showing both ranks side-by-side with trade counts and win rates for each period—no smoothing, no narrative.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** The indicator lives right next to the algo name on the leaderboard. No hover state required. A user who knows what they're looking at understands instantly: this algo is moving. The card is text-only, numbers-heavy, no charts. Losses in the 30D period shown as clearly as wins.

## 5. Acceptance Criteria (AC)

- Divergence flag appears on leaderboard for algos with >10-rank delta; clicking it shows all-time vs 30D force rank, trade count, and win rate for each period.
- If an algo has <10 trades in the 30D window, the flag still appears but the card notes 'low sample size' plainly—no hiding the data.
- Mobile: flag and rank delta remain visible in a single-column layout; clicking opens a full-width card below the leaderboard entry.

## 6. Out of Scope

- Predictive modeling of which divergences will persist or reverse.
- Notifications or alerts when an algo's divergence threshold is crossed.
