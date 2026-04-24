# Biscotti’s Blunder Board
Status: Draft
Generated: 2026-04-24 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds want a spotlight for the most spectacular signal failures, not just the winners, to study what went sideways.
- **Goal:** Create a dedicated section highlighting the worst-performing signals over various time windows, preserving brutal transparency.
- **Metric:** Increase engagement with failure-related content by 20% among Alt-Data Nerds.

## 2. User Stories

- As an Alt-Data Nerd, I want to track the signals that tanked the hardest recently, so I can learn what kind of alt-data flops.
- As a Receipts Guy, I want brutal honesty showcased, so I’m reassured the lab doesn’t hide losses.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a persistent failure leaderboard showing bottom 10 signals by return over 7, 30, and 90 days.
- **Requirement 2:** Failure leaderboard must name signals exactly, with no euphemisms or hiding of data.
- **Requirement 3:** Allow paid users to filter failure board by signal category (ALPHA / noise / unresolved).

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Design the failure board as a gritty, hand-sketched blackboard style panel with red chalk text and no shiny UI gloss.

## 5. Acceptance Criteria (AC)

- Failure board updates live alongside main leaderboard.
- Signal names and exact loss percentages are always visible and never redacted.
- Filters for time window and bucket category function without errors.

## 6. Out of Scope

- No automatic suggestions to drop or kill failed signals.
- No gamification or 'failure badges' to soften the blow.
