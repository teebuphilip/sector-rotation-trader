# Trade Log Receipts
Status: Draft
Generated: 2026-04-24 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Subscribers can see equity curves and daily P&L, but when they want to audit a specific trade or understand why a signal entered/exited, they hit a wall — the lab doesn't expose individual trade records in a scannable format.
- **Goal:** Publish a per-algo trade log (entry, exit, rationale, slippage) as a downloadable CSV or viewable table, so Receipts Guys and Signal Hunters can see the actual receipts, not just the aggregate scorecard.
- **Metric:** % of paid users who download or view trade log per month; support tickets asking 'why did this algo buy/sell X' after trade log exists.

## 2. User Stories

- As a Receipts Guy, I want to download a CSV of every trade an algo has ever made (entry date, exit date, symbol, entry price, exit price, P&L), so I can spot-check it against my own broker data and verify the lab isn't gaming the numbers.
- As a Signal Hunter, I want to see the operator's reason for entry/exit (e.g., 'signal fired on high volume', 'stop loss hit'), so I can understand if the algo is trading the signal or if it's over-engineered with extra logic.

## 3. Functional Requirements (The "What")

- **Requirement 1:** For each algo, generate a trade log table (viewable in UI and downloadable as CSV) with columns: entry date/time, exit date/time, symbol, entry price, exit price, shares, gross P&L, % return, slippage estimate, operator note (if any).
- **Requirement 2:** Operator can add a one-line rationale per trade (e.g., 'signal threshold crossed', 'volatility rule triggered', 'manual exit') before the trade is published; this note is visible in the log.
- **Requirement 3:** CSV includes metadata row at top (algo name, date range, total trades, win rate) so context travels with the file; CSV is re-generated daily after market close.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Trade log is a sub-page under each algo detail, not on the main leaderboard. Table is sortable by any column; search by symbol. Mobile: table scrolls horizontally. Operator's note is visible as a small icon/badge on the row; hover reveals text.

## 5. Acceptance Criteria (AC)

- Trade log shows every trade for the algo since inception; a newly-published algo has an empty log (zero rows) until its first trade fires.
- CSV download works for algos with 1 trade and algos with 10,000+ trades (file size tested; no timeout).
- Slippage is calculated consistently (entry price vs order fill price); if slippage data is unavailable, field shows 'N/A' (not zero or estimated).

## 6. Out of Scope

- Intraday or partial-fill detail; log shows entry and exit only, not intermediate order adjustments.
- Benchmarking trades against SPY (that is leaderboard work); trade log is algorithm-centric only.
