# Receipts Guy Raw Trade Logs
Status: Draft
Generated: 2026-05-01 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Receipts Guys want the full messy truth, including every trade detail for each algo, but current detail views summarize or aggregate.
- **Goal:** Provide a raw chronological trade log per algo accessible from the leaderboard with all trades, wins, losses, and failed signals in full detail.
- **Metric:** Increase Receipts Guy user satisfaction scores by 10% in surveys about transparency.

## 2. User Stories

- As a Receipts Guy, I want to see every trade an algo made, including the losing ones and no-trade days, so I can audit the receipts myself.
- As a Receipts Guy, I want to export or copy the raw trade logs for offline analysis or sharing.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a raw trade log panel accessible from the leaderboard for paid subscribers with timestamp, signal name, trade direction, P&L, and status.
- **Requirement 2:** Support export to CSV and copy-to-clipboard for the displayed trades.
- **Requirement 3:** Ensure trade logs load efficiently even for algos with many trades.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Display logs in a plain text table with no styling frills—just names and numbers. Named algos only. No gloss.

## 5. Acceptance Criteria (AC)

- Trade log loads within 2 seconds on desktop and mobile.
- CSV export produces accurate, complete file of all shown trades.
- Logs include losing trades and no-trade gaps clearly.

## 6. Out of Scope

- No summarization or aggregation of trade logs.
- No AI or commentary on trade quality.
