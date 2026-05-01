# Raw Trade Log Export
Status: Draft
Generated: 2026-05-01 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** An Alt-Data Nerd or Signal Hunter who wants to replicate or stress-test a signal can see equity curves and win rates, but cannot see the actual trade list. They have to trust the summary. The lab has the trades; it just doesn't share the raw feed.
- **Goal:** Let paid subscribers download the complete trade history (entry date, exit date, symbol, P&L, reason) for any algo as CSV. No UI wrapper. No 'analysis.' Just the receipts.
- **Metric:** 5% of paid subscribers download a trade log in their first month. 40% of downloader retention after 3 months (they're serious users building on it).

## 2. User Stories

- As an Alt-Data Nerd, I want to download Biscotti's full trade log so I can correlate the entry/exit dates with my own event data and see if the signal is real.
- As a Signal Hunter, I want the raw CSV so I can feed it into my own backtester and stress-test it against different market regimes without rebuilding the signal.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Each algo's detail page has a 'Download Trades' button. Clicking it generates and serves a CSV with columns: Date Entered, Date Exited, Symbol, Entry Price, Exit Price, P&L ($), P&L (%), Days Held, Trade Reason (if available).
- **Requirement 2:** CSV includes all trades for the algo's entire run, not just recent trades. No pagination or sampling.
- **Requirement 3:** If a trade is still open, 'Date Exited' and 'Exit Price' are empty. Current unrealized P&L is shown as blank or 'OPEN'.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Button is plain text, styled like a link. 'Download Trades (CSV)'. Click triggers a file download. No modal, no confirmation, no email. The file is named like 'biscotti_trades_20250101.csv'. Plain, quiet, instant.

## 5. Acceptance Criteria (AC)

- Paid users can download a CSV from any algo detail page. Free users do not see the download button.
- CSV is valid and opens correctly in Excel, Google Sheets, and any standard CSV reader.
- Downloaded CSV includes all trades for the algo's full history. No data is truncated or sampled.

## 6. Out of Scope

- Automated periodic email delivery of trade logs.
- Interactive pivot tables or visualizations of trade data in the UI.
- Filtering or custom time window selection for the export (users filter the CSV themselves).
