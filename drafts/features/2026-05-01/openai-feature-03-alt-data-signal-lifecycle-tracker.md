# Alt-Data Signal Lifecycle Tracker
Status: Draft
Generated: 2026-05-01 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds want to follow the evolving status of weird signals (real, dead, unresolved) but this info is fragmented and hidden.
- **Goal:** Build a lifecycle status indicator per algo on the leaderboard, showing if it's actively running, dead (no trades in 30+ days), or unresolved (mixed results).
- **Metric:** Increase time Alt-Data Nerds spend reviewing signal details by 25%.

## 2. User Stories

- As an Alt-Data Nerd, I want to know at a glance which signals are still 'live experiments' versus dead or conclusively noise.
- As an Alt-Data Nerd, I want to filter or sort algos by lifecycle status so I can prioritize my attention.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Display a lifecycle badge or colored dot next to each algo name: green for active, gray for dead, yellow for unresolved.
- **Requirement 2:** Allow filtering leaderboard by lifecycle status with toggles.
- **Requirement 3:** Automatically update status daily based on trade activity and performance criteria.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use raw colored dots or simple text labels—no jargon or icons that could feel corporate. Keep named algos front and center.

## 5. Acceptance Criteria (AC)

- Lifecycle badges update correctly and visibly on all devices.
- Filters apply instantly without page reload.
- Clear distinction and no overlap between lifecycle statuses.

## 6. Out of Scope

- No detailed explanation or reasoning behind lifecycle status.
- No auto-archiving or removal of dead algos.
