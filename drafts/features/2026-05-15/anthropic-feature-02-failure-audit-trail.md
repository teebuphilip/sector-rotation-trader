# Failure Audit Trail
Status: Draft
Generated: 2026-05-15 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Receipts Guy sees a signal go from rank #12 to #89 in two weeks and has no idea why. Was it bad luck, broken code, or changed market conditions? The leaderboard shows the present, not the cause.
- **Goal:** Create a public audit log for every algo showing when it stopped firing, lost its edge, or entered unresolved territory, so failures are documented as honestly as wins.
- **Metric:** Measure paid subscriber retention by cohort. Track paid users who view failure audits at least monthly. Measure content engagement (do Signal Hunters share notable failure audits on Twitter?).

## 2. User Stories

- As a Receipts Guy, I want to see a timestamped log of when Biscotti's trade frequency dropped from 5/week to 0/week and what the equity curve looked like at each inflection, so I know the failure is real and documented.
- As an Alt-Data Nerd, I want to export a failure audit (CSV: date, rank, win rate, trade count, last trade, notes) for algos I'm tracking, so I can cross-reference with market regime shifts or data anomalies.

## 3. Functional Requirements (The "What")

- **Requirement 1:** For every algo, track state transitions: Active → Degrading (rolling win rate <50% for 10 trades), Degrading → Unresolved (no trades in 30 days), Unresolved → Cold (no trades in 90 days). Log the date, rank before/after, trigger metric.
- **Requirement 2:** Display a 'Failure Timeline' on detail pages: horizontal bar chart showing algo rank over time with color-coded state zones (green=active, yellow=degrading, gray=unresolved, black=cold). Overlay trade frequency as a sparkline.
- **Requirement 3:** Provide CSV export: algo name, date, force rank, 30-day rank, trade count (period), win rate, last trade timestamp, state transition reason.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** No modal, no wizard. Add a small 'Audit' tab on detail pages next to 'Equity Curve' and 'Trade History'. Timeline is read-only, stark, no animation. Export button is a link. State transitions are labeled with the metric that triggered them: '[Date] Entered Unresolved: 0 trades in 30 days.'

## 5. Acceptance Criteria (AC)

- Failure Audit Trail renders for all algos with >10 days running time. Cold algos (no trades in 90+ days) show full timeline from Active to Cold.
- CSV export includes all rows back to algo launch date. File is downloadable and opens correctly in Excel and Google Sheets.
- Timeline updates once per trading day. A user viewing at market close sees the current day's state transitions reflected by next morning.

## 6. Out of Scope

- Automated hypothesis generation or 'why this signal failed' AI suggestions — that is narrative, not data.
- Comparison tool showing which market regimes correlate with failures across multiple algos (editorial analysis, not feature).
