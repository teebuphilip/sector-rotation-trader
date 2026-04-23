# Trade-Level Signal Audit Trail
Status: Draft
Generated: 2026-04-23 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** An Alt-Data Nerd wants to reverse-engineer what a signal actually fired on, but today only sees the entry/exit prices and dates — not the raw signal condition or data source that triggered each trade.
- **Goal:** Let users inspect the 'why' behind each trade: what condition fired, what data fed it, and how that compares to SPY at the same moment.
- **Metric:** # of paid users who expand trade audit details; avg trades audited per session; correlation between audit view time and 30-day renewal rate.

## 2. User Stories

- As an Alt-Data Nerd, I want to see what alternative data or condition triggered a specific trade (e.g., 'Twitter sentiment score > 0.7, VIX < 18'), so I can judge if the signal is real or curve-fit.
- As a Signal Hunter, I want to compare that signal condition to SPY's price and sector moves on the same date, so I can tell if the algo found alpha or just rode the market.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Each trade in the trade history table must have an 'Inspect' action that opens a modal showing: signal name, trigger condition (e.g., 'RSI > 70 AND Volume Spike'), data sources used, entry price, SPY price at entry, days held.
- **Requirement 2:** Condition text must be human-readable (not code); if a signal uses proprietary data (e.g., 'whale wallet movements'), show data source name and publication lag without revealing the raw data.
- **Requirement 3:** For trades older than 90 days, gray out the 'Inspect' button with tooltip: 'Signal definition changed; audit not available for this trade.'

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Audit modal is narrow (350px max width on desktop) and reads like a lab notebook entry: signal name at top, condition in a monospace block, data sources as tags, entry/exit comparison as a small 2-line chart. Mobile: full-screen bottom sheet. No animations; stark, readable layout. Close button or swipe to dismiss.

## 5. Acceptance Criteria (AC)

- Audit modal renders in <500ms; all text is selectable and copyable (researchers like to paste conditions into notes).
- Data source tags are consistent across all algos (e.g., 'alt-data:sentiment' always renders the same way); missing or redacted data shows as '—' not empty.
- SPY comparison shows price delta and % change from entry; if SPY moved 5% up and algo gained 3%, that is transparent in the modal.

## 6. Out of Scope

- Allowing users to modify or test 'what if' versions of the signal condition; this is read-only audit only.
- Exporting or sharing individual trade audits; that would require permission workflows outside the scope.
