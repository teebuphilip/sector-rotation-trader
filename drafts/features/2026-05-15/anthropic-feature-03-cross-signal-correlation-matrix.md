# Cross-Signal Correlation Matrix
Status: Draft
Generated: 2026-05-15 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Alt-Data Nerd has 8 algos running on correlated data sources (all receipt-based, for example) but cannot see whether they are all failing for the same reason or for different ones. No way to spot redundancy or hidden dependencies.
- **Goal:** Show which signals move together and which move independently, so users can build more resilient signal portfolios and spot when a data source is the real winner, not the signal.
- **Metric:** Measure adoption among paying subscribers with 5+ algos in their watchlist. Track time spent in correlation view. Measure signal diversity in user-created watchlists (are users adding less correlated algos after seeing the matrix?).

## 2. User Stories

- As an Alt-Data Nerd, I want to see a correlation matrix of the last 60 days' equity curves for all algos I'm following, so I can tell if Baileymol and Biscotti are really different signals or just copies with noise.
- As a Signal Hunter, I want to flag a subset of algos (e.g., all receipt-based signals) and see their pairwise correlation, so I can decide if I should ignore one or double-weight the other.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Compute 60-day rolling returns for every algo. Calculate Pearson correlation for all pairs. Store in a matrix indexed by algo name.
- **Requirement 2:** On leaderboard, add optional 'Correlation' mode that shows a heatmap: algos on x and y axes, cells colored by correlation strength (red=high, white=low, blue=negative). Hovering a cell shows the exact r-value and period.
- **Requirement 3:** Allow users to select a subset of algos and recalculate the matrix for just that subset. Persist the last-selected subset in session storage.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** No new page. Add a second toggle on leaderboard: 'Correlation View'. Clicking it swaps the leaderboard for a matrix view. Matrix is sortable by average correlation (so most-redundant algos cluster). Cell hover shows 'Baileymol ↔ Biscotti: r=0.73'. Names stay full. Color scheme is stark: red, white, blue. No gradients.

## 5. Acceptance Criteria (AC)

- Correlation matrix renders for up to 50 algos in <1 second. Matrix is responsive on mobile (table scrolls horizontally).
- A user can select/deselect algos by clicking checkbox row labels. Matrix recalculates in <200ms for subset size ≤20.
- Correlation values update once per trading day. A user viewing Friday afternoon sees correlation through Friday close; Saturday/Sunday show Friday's values.

## 6. Out of Scope

- Weighted portfolio optimization based on correlation ('which algos should I blend') — that is advisory, not data.
- Causality analysis or factor decomposition — we show correlation, not drivers.
