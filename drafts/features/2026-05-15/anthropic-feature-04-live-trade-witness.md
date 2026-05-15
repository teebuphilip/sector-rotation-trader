# Live Trade Witness
Status: Draft
Generated: 2026-05-15 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Signal Hunter trusts the leaderboard but feels disconnected from the actual moment an algo fires. A trade happened 2 hours ago. Was it fast? Did it catch the move? Was the execution realistic? The lab is a black box between updates.
- **Goal:** Show live trade execution in a public feed so users can watch signals work in real time and build confidence in the live-running claim.
- **Metric:** Measure visitor-to-subscriber conversion by cohort (users who view live trades). Track daily active viewers of trade witness. Measure time-on-site for free vs paid users during market hours.

## 2. User Stories

- As a Signal Hunter, I want to see every trade fire in real-time (algo name, symbol, side, quantity, timestamp, execution price), so I can build confidence that the lab is actually running live and not backtested theater.
- As a Receipts Guy, I want to see when a trade fails or misses the intended price, so I know the lab is showing real execution friction, not fantasy fills.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Create a time-ordered feed of all trades from the last 24 hours, updated in real-time during market hours. Include: algo name (full, e.g., 'Baileymol'), symbol, side (BUY/SELL), qty, executed price, intended price (if available), slippage, timestamp (precise to second).
- **Requirement 2:** Display as a scrollable timeline on a new 'Live Witness' page (free user sees last 2 hours, last 20 trades; paid user sees last 24 hours, all trades). Sort by timestamp descending. Allow filter by algo name or symbol.
- **Requirement 3:** Show slippage in stark terms: 'Biscotti AAPL BUY 100 @ $187.32 (intended $187.25, +$7 slippage).' No euphemism. If execution was poor, show it.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Minimal page. Single column. Each trade is a row: '[HH:MM] Baileymol TSLA BUY 50 @ $245.10 (slippage +0.15%)' Light background, monospace font for prices. No animations, no notifications. Free users see a 'Subscribe for full 24h history' banner at the top. Paid users see nothing but trades.

## 5. Acceptance Criteria (AC)

- Trade feed updates within 2 seconds of execution during market hours. Mobile view is readable; desktop shows full data without truncation.
- Slippage calculation is accurate to ±$0.01. If no intended price is available, slippage is not shown.
- Free user feed shows last 2 hours of trades; paid user feed shows last 24 hours. Both update in real-time. Archive beyond 24 hours is not shown on this page (cold storage only).

## 6. Out of Scope

- Execution alerts or notifications — no push, no email, no activity center. The feed is passive, not active.
- Trade-level commentary or 'why did this trade happen' explanations — that is editorial. The feed is a witness, not a narrator.
