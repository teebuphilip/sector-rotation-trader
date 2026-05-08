# Failure Footprint Overlay
Status: Draft
Generated: 2026-05-08 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Users struggle to visually parse how losses and failures distribute across signals alongside wins on the leaderboard.
- **Goal:** Provide an at-a-glance overlay that maps failure events and drawdowns directly onto each signal’s leaderboard entry.
- **Metric:** Increase time spent on leaderboard page by 20% and reduce user complaints about lack of loss clarity by 50%.

## 2. User Stories

- As the Receipts Guy, I want to see exactly when and how badly a signal lost money, so I can trust the honesty of the lab.
- As the Signal Hunter, I want to identify signals with volatile failure patterns quickly, so I can weigh risk versus reward efficiently.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a small failure timeline bar integrated into each leaderboard row showing drawdown spikes and loss events.
- **Requirement 2:** Gracefully handle signals with no recent trades by showing a faded or empty failure footprint.
- **Requirement 3:** Ensure overlay does not obscure signal naming or key metrics and updates in real-time with live trades.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a stark red-on-gray minimalist overlay with no animations to maintain lab notebook feel; failure events must stand out without glamorizing.

## 5. Acceptance Criteria (AC)

- Failure footprint appears on every leaderboard entry for paying subscribers.
- Overlay updates within 5 seconds of new trade data.
- Failure events are visually distinct and labeled on hover with date and size.

## 6. Out of Scope

- Interactive failure event deep dives or expanded charts outside leaderboard context.
- Any smoothing or hiding of negative outcomes.
