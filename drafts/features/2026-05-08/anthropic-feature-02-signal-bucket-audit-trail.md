# Signal Bucket Audit Trail
Status: Draft
Generated: 2026-05-08 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Alt-Data Nerd follows an algo for weeks and wants to know why it moved from ALPHA to NOISE (or stayed UNRESOLVED). Currently, bucket changes happen silently; the user has to infer the reasoning from the trade log.
- **Goal:** Show the operator's reasoning (one line, timestamp, and the threshold or trade that triggered the move) whenever an algo changes buckets. Make the experiment transparent, not the conclusion arbitrary.
- **Metric:** Paid user dwell time on algo detail pages; % of detail-page visits that include an audit trail scroll; signal followers who stay subscribed 60+ days.

## 2. User Stories

- As an Alt-Data Nerd, I want to see when Signal X moved from UNRESOLVED to NOISE and why (e.g., 'Win rate dropped below 45% over 30 days'), so I know whether I should trust the conclusion or wait longer.
- As the Receipts Guy, I want the operator to explain in one sentence why an algo got downgraded, so I know the decision wasn't hidden or arbitrary.

## 3. Functional Requirements (The "What")

- **Requirement 1:** On the algo detail page, below the bucket label, show a small 'Audit Trail' section (collapsed by default) listing every bucket change: date, old bucket, new bucket, operator note (1-2 sentences, max 140 chars), and the metric threshold or trade count that triggered it.
- **Requirement 2:** Operator notes are visible only to paying users; free users see the bucket and date, not the reasoning.
- **Requirement 3:** If an algo has never changed buckets, the audit trail is empty; no placeholder text.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** The audit trail is a simple list, no timeline UI. Each entry is one line of text with a timestamp. No color coding — just label old→new and the reason. On mobile, the entire section collapses; tapping 'Audit Trail' expands a vertical stack of entries. This keeps the detail page clean and honors the 'no fluff' principle.

## 5. Acceptance Criteria (AC)

- Audit trail appears only on paying user views; free users see the current bucket but no trail.
- Each entry shows date (YYYY-MM-DD), old_bucket, new_bucket, operator_note as plain text.
- If an algo is still in its original bucket, 'Audit Trail' section is not shown.

## 6. Out of Scope

- Alerts when an algo changes buckets.
- Allowing users to filter algos by audit trail events.
