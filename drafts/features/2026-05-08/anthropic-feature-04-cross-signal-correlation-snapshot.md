# Cross-Signal Correlation Snapshot
Status: Draft
Generated: 2026-05-08 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Alt-Data Nerd suspects two algos are reading the same signal and wants proof — are they correlated, or is it just luck? There's no built-in way to check whether two algos are actually different or if they're just regurgitating the same idea.
- **Goal:** Show a simple correlation matrix (or pairwise scatter) for any subset of algos a user selects. Honest, no-spin: if two algos move together 0.92, that's shown. Unresolved correlations stay unresolved.
- **Metric:** Paid user engagement with algo comparison; # of users who view correlation data per week; time spent on correlation view.

## 2. User Stories

- As an Alt-Data Nerd, I want to select 3–5 algos and see their daily return correlation, so I know if they're all chasing the same signal or if they're genuinely different ideas.
- As the Receipts Guy, I want to see which algos moved together during wins and which diverged during losses, so I can spot if the lab is accidentally double-betting on the same thing.

## 3. Functional Requirements (The "What")

- **Requirement 1:** On the leaderboard or from algo detail pages, a paid user can click a 'Compare' button; a modal appears with a list of all algos; user checkboxes 3–5; clicking 'Calculate' shows a Pearson correlation matrix (rows and columns are algo names, cells are correlation coefficients from 0 to 1, rounded to 2 decimals).
- **Requirement 2:** The correlation is calculated on daily returns over the past 90 days; if an algo has fewer than 30 days of history, it is grayed out and marked 'Too Young'.
- **Requirement 3:** No interpretation, no color coding, no 'strong / weak' labels — just the number. A footnote says 'Correlation does not imply the same signal; see trade logs for details.'

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** The modal is simple: checkbox list, 'Calculate' button, result is a text-based table (or a small matrix grid if the designer prefers). No heat map, no 3D, no D3. On mobile, the matrix stacks vertically (one algo per row, correlation values in columns). The user can 'Export as CSV' if they want to dig deeper in Excel. This is a tool for nerds, not a dashboard.

## 5. Acceptance Criteria (AC)

- User can select 3–5 algos; clicking 'Calculate' produces a symmetric matrix of Pearson correlation coefficients (to 2 decimals).
- Algos with <30 days history are shown but grayed out and labeled 'Too Young'.
- Correlation is based on daily returns over the past 90 days; the footer notes 'Last 90D' and the date range.

## 6. Out of Scope

- Real-time correlation updates or alerts.
- Predictive correlation forecasts.
- Causal analysis or trade-log alignment (e.g., 'both algos bought AAPL on the same day').
