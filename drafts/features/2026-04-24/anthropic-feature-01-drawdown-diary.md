# Drawdown Diary
Status: Draft
Generated: 2026-04-24 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Signal Hunters and Receipts Guys can't quickly see which algos are currently underwater and by how much — the equity curve tells part of the story, but a live drawdown column on the leaderboard gets missed in a crowded view.
- **Goal:** Make current drawdown (peak-to-trough) visible at a glance on the leaderboard, sorted and filterable, so users can spot which signals are taking real heat right now.
- **Metric:** % of paid users who filter or sort by drawdown column within first 3 sessions; correlation between drawdown transparency and subscription retention.

## 2. User Stories

- As a Receipts Guy, I want to see which algos are currently down from peak in a dedicated column, so I can trust the lab is showing me the bad days, not just the winners.
- As a Signal Hunter, I want to filter the leaderboard to show only algos with drawdown > 10%, so I can evaluate which underwater signals are still worth watching.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add 'Current Drawdown %' column to leaderboard (calculated as: (current equity - peak equity) / peak equity * 100); update in real-time after each trading session.
- **Requirement 2:** Allow column sort (ascending/descending) and range filter (e.g., show only algos with drawdown between 5–20%); persist user's sort/filter preference in session.
- **Requirement 3:** If an algo has never been in drawdown (all-time high equals current), display '0%' with neutral styling; if algo has no equity data, display '—' (not a zero).

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Red text for negative drawdown (no softening), placed right of 'Force Rank' column. Tooltip on hover shows date of peak and current equity. Mobile: make column left-swipeable to reveal if screen is tight.

## 5. Acceptance Criteria (AC)

- Drawdown calculates correctly for algos with 1-day history, 30-day history, and multi-year history.
- Sorting by drawdown (worst first) matches leaderboard force rank behavior: ties are broken by oldest-algo-first.
- Filter persists across page reload and works in combination with other filters (e.g., 'Days Running > 60' + 'Drawdown > 5%').

## 6. Out of Scope

- Historical drawdown tracking (e.g., 'worst drawdown ever'); this feature shows current state only.
- Drawdown alerts or notifications; the leaderboard is the only place to look.
