# Trade Failure Highlight Reel
Status: Draft
Generated: 2026-05-15 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Failures and losing trades are buried or softened in most products, but users want raw, unfiltered access to all failed trades to understand true signal risk.
- **Goal:** Surface a dedicated, scrollable 'failure reel' showing recent losing trades for each signal in chronological order, fully visible from the leaderboard.
- **Metric:** Increase engagement with failure data by 30% among paying subscribers.

## 2. User Stories

- As the Receipts Guy, I want to see every losing trade laid bare so I can verify the honesty of the lab.
- As the Alt-Data Nerd, I want to analyze the context and timing of losses to hypothesize about signal weaknesses.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a failure reel section beneath each signal's leaderboard entry showing recent losses with timestamp, entry price, and loss percentage.
- **Requirement 2:** Ensure losses are never hidden behind clicks or tabs; they appear inline but collapsible by default to save space.
- **Requirement 3:** Keep failure data updated live and consistent with paper-trading logs.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a compact monospace font and a stark red highlight for losses; collapsible with a minimal 'show failures' toggle to prevent overwhelming the leaderboard.

## 5. Acceptance Criteria (AC)

- Failure reel visible for all signals with losses on desktop and mobile.
- Failure reel updates live as new losing trades occur.
- No loss data is omitted or aggregated into averages; each failure is one line.

## 6. Out of Scope

- Loss softening, aggregation into charts only.
- Push notifications about failures.
