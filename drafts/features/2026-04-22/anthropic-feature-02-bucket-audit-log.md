# Bucket Audit Log
Status: Draft
Generated: 2026-04-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Alt-Data Nerd and Signal Hunter want to see the running record of which bucket an algo sits in (ALPHA / noise / unresolved) and *when* that changed. Right now, buckets are a current state only—there's no visible experiment log.
- **Goal:** Make the bucket assignment process visible and auditable. Show the raw reasoning behind why an algo moved buckets, with dates and thresholds crossed.
- **Metric:** Paid user engagement with bucket audit logs; number of algos audited per session; paid user retention correlated with audit log visits.

## 2. User Stories

- As an Alt-Data Nerd, I want to see the full history of an algo's bucket assignments—when it moved from ALPHA to noise, what threshold it crossed, and what the lab learned.
- As a Signal Hunter, I want to audit the lab's own grading criteria—to know if an algo was moved to noise because it hit a real statistical edge or because it failed a specific test I should understand.

## 3. Functional Requirements (The "What")

- **Requirement 1:** For every algo with a bucket assignment, maintain a timestamped log of every bucket change, including the threshold or rule that triggered it (e.g., 'moved to noise: <50% win rate over 60+ trades').
- **Requirement 2:** Display the audit log as a reverse-chronological table: date, old bucket, new bucket, rule triggered, trade count and win rate at time of change.
- **Requirement 3:** Log must include *why* an algo entered its current bucket on day 1—not just transitions. If an algo was born into ALPHA, log that decision and its initial criteria.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** The audit log is a paid-only detail page, accessible from the algo detail view. No explanation required beyond the table itself—the operator's own logic is the narrative. Show losses and bad trades in context (e.g., 'moved to noise: 3 losses in last 5 trades, 40% win rate'). Names of the buckets stay consistent across all surfaces.

## 5. Acceptance Criteria (AC)

- Audit log shows all bucket transitions with date, old bucket, new bucket, and the specific rule or threshold that triggered the change; initial bucket assignment is logged with its reasoning.
- Win rate and trade count at time of change are shown alongside the rule, so context is never missing.
- If a bucket was assigned manually (by the operator, not auto-triggered), it is logged as 'manual' with a note—no hiding discretionary calls.

## 6. Out of Scope

- User-defined bucket rules or custom thresholds.
- Predictive bucket changes or 'at risk of moving to noise' warnings.
