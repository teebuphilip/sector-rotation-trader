# Alt-Data Nerd’s Divergence Spotlight
Status: Draft
Generated: 2026-04-23 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds find it hard to spot and interpret honest divergences where rolling short-term ranks contradict longer-term force ranks.
- **Goal:** Surface and highlight interesting honest divergences on the leaderboard to fuel ongoing alt-data experiments.
- **Metric:** Increase Alt-Data Nerds’ interaction with divergence data by 40%.

## 2. User Stories

- As an Alt-Data Nerd, I want to see signals with top rolling 30D rank but poor overall force rank highlighted, so I can investigate unresolved patterns.
- As an Alt-Data Nerd, I want to toggle a divergence view that groups signals by divergence type, so I can track weird signals more easily.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Display a divergence icon next to signals where 30D rank and force rank differ by a configurable threshold.
- **Requirement 2:** Provide a toggle to filter leaderboard to only show divergent signals.
- **Requirement 3:** On divergence highlight hover or tap, show the raw rank numbers and a short annotation about the discrepancy.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a subtle but distinct 'split arrow' icon representing divergence, styled like a hand-drawn lab note scribble.

## 5. Acceptance Criteria (AC)

- Divergence highlights appear correctly for all qualifying signals on desktop and mobile.
- The divergence filter toggle updates leaderboard results instantly.
- Annotations appear on interaction without obscuring leaderboard readability.

## 6. Out of Scope

- Automatically interpreting divergence causes.
- Machine-generated divergence explanations.
