# Receipts Export
Status: Draft
Generated: 2026-04-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Receipts Guy wants to take the leaderboard data and all trade history offline to audit it himself, build his own models, or prove to others that the lab is real. Right now, that data is view-only on the site—there's no way to extract it in bulk.
- **Goal:** Let paid users export the complete record—leaderboard, trades, equity curves, bucket history—in a format they can trust and analyze.
- **Metric:** Paid users initiating exports; export frequency; retention correlation with export usage.

## 2. User Stories

- As the Receipts Guy, I want to download the entire trade history for all algos (or just the ones I tag) as a CSV, so I can audit the math, check for survivorship bias, and build my own models.
- As an Alt-Data Nerd, I want to export an algo's full equity curve and bucket history to compare it against my own experiments and see if the signal is real.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Offer two export types: (1) Leaderboard snapshot (current force rank, all-time record, 30D record, bucket, operator); (2) Full trade history (one CSV per algo: date, entry, exit, P&L, signal reason if logged).
- **Requirement 2:** Exports include explicit headers noting data freshness, the export date, and a note: 'This is the unfiltered record. No survivorship bias removal applied. All trades shown as recorded.'
- **Requirement 3:** Implement a rate limit: one export per user per hour, max file size 50MB. If a user requests all 200+ algos, offer a query builder to filter by bucket, force rank range, or tag.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Export button lives on the leaderboard page (for snapshot) and on each algo detail page (for full history). A modal lets users choose format (CSV recommended, JSON optional). File is generated on-demand and downloaded directly—no email, no queuing. Name the file with the export date and type (e.g., 'CSA-leaderboard-2025-01-15.csv'). Include a README in the ZIP if exporting multiple files.

## 5. Acceptance Criteria (AC)

- Paid user can export current leaderboard as CSV; file includes force rank, all-time W-L, 30D W-L, bucket, and trade count for all algos.
- Paid user can export full trade history (entries, exits, P&L, dates) for a single algo as CSV; file includes a header row and a data-freshness note.
- If a user requests a bulk export (multiple algos), the system either generates a ZIP with one CSV per algo or offers a filtered query to reduce file size; all exports are timestamped and note that no survivorship bias correction has been applied.

## 6. Out of Scope

- Scheduled or recurring exports.
- Email delivery of exports.
- Custom SQL queries or interactive data warehouse access.
- Survivorship bias adjustment in the export itself—the lab provides raw receipts only.
