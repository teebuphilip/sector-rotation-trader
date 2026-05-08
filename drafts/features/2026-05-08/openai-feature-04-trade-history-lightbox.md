# Trade History Lightbox
Status: Draft
Generated: 2026-05-08 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds want quick access to raw trade logs for signals from the leaderboard without leaving the page or losing context.
- **Goal:** Provide an on-demand overlay showing a signal’s full recent trade history including losses and failures in raw form.
- **Metric:** Increase trade history views per user session by 40%.

## 2. User Stories

- As the Alt-Data Nerd, I want to open a signal’s trade log right from the leaderboard to verify every loss and win personally.
- As the Receipts Guy, I want to see the unvarnished trade receipts without wading through pages or dashboards.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Clicking a signal name on the leaderboard opens a modal lightbox with a chronological list of trades.
- **Requirement 2:** Trade entries must show date, size, result (win or loss), and any notes without hiding losses.
- **Requirement 3:** Lightbox must be mobile-friendly and dismissible by clicking outside or pressing escape.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use a typewriter-style monospace font and black-on-white text for raw data feel; no charts or graphs, purely tabular raw logs.

## 5. Acceptance Criteria (AC)

- Lightbox opens for any signal clicked on the leaderboard for paying users.
- Trade data matches backend logs exactly with no filtering or smoothing.
- Lightbox closes cleanly and returns user to same leaderboard scroll position.

## 6. Out of Scope

- Editing or annotating trade history inside the lightbox.
- Exporting trade histories to external files.
