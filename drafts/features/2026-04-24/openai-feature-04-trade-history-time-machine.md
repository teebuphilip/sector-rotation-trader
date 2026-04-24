# Trade History Time Machine
Status: Draft
Generated: 2026-04-24 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds want to deep-dive into a signal’s full trade history to see its live experiment unfold, including every failure and delay.
- **Goal:** Provide an accessible timeline view of every trade a signal has made, with clear markers for wins, losses, and no-fires.
- **Metric:** Increase time spent on individual signal detail pages by 25%.

## 2. User Stories

- As an Alt-Data Nerd, I want to scroll through a signal’s full trade history timeline, so I can study patterns of failure and success firsthand.
- As a Receipts Guy, I want every dud trade logged clearly, so the lab’s honesty shines through.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Build a horizontal or vertical scroll timeline showing every trade event, labeled with date, outcome (win/loss/no fire), and return %.
- **Requirement 2:** Trades with no activity for 30+ days should be marked as 'dormant' explicitly.
- **Requirement 3:** Timeline data must sync with live trade logs and be accessible on desktop and mobile.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Timeline uses rough sketch style icons for wins (green check), losses (red X), and no-fires (gray dash), with no smoothing or aggregation.

## 5. Acceptance Criteria (AC)

- Trade timeline loads fully within 3 seconds on desktop and mobile.
- All trade events appear with accurate labels and outcomes.
- Dormant periods visually distinct and labeled.

## 6. Out of Scope

- No predictive or forecast data added to timeline.
- No interactive trade editing or annotations by users.
