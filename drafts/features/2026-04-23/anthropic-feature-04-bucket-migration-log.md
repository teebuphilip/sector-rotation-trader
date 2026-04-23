# Bucket Migration Log
Status: Draft
Generated: 2026-04-23 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** A Signal Hunter sees an algo in the ALPHA bucket and wants to know: has it been there since launch or did it just get upgraded from noise? How volatile is its classification? Is this real or did one good month push it up?
- **Goal:** Show when and why each algo moved between buckets (ALPHA ↔ noise ↔ unresolved), with the metrics that triggered the move, so users can assess classification stability.
- **Metric:** # of paid users who check migration history per week; avg algos with >2 migrations (indicating volatility).

## 2. User Stories

- As a Signal Hunter, I want to see that Biscotti was reclassified from 'noise' to ALPHA on [date] because its 90-day Sharpe crossed 0.8, so I know the upgrade was earned and not arbitrary.
- As a Receipts Guy, I want to see that an algo bounced between 'unresolved' and 'noise' four times in the last 60 days, so I can tell it is unstable and not worth paying attention to yet.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Bucket Migration Log is a timeline/table on each algo's detail page showing: date, prior bucket, new bucket, trigger metric (e.g., 'Sharpe(90D) = 0.82'), and a link to the trade history on that date.
- **Requirement 2:** Migrations are auto-computed based on operator-defined thresholds (e.g., ALPHA if Sharpe > 0.8 for 30 days) and manual reclassifications (operator can move it anytime with a reason).
- **Requirement 3:** Log includes the full history from algo launch; if algo is <7 days old, show 'Not yet classified; awaiting baseline trades.'

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Timeline view (not a table) works best: vertical line with dots for each migration, label shows old/new bucket and metric trigger, click expands to show trade context. Desktop: sidebar timeline on detail page. Mobile: full-screen scrollable timeline. No animations; clarity over motion.

## 5. Acceptance Criteria (AC)

- Migration date is accurate to the day; trigger metric is correct and current as of that date.
- Manual reclassifications show operator reason (e.g., 'Data issue during this period; reclassified by operator') in the log entry.
- Algos with 0 migrations show as 'Classified since [launch date] as [bucket]; no changes.' Stability is visible without motion.

## 6. Out of Scope

- Predictive alerts when an algo is close to a bucket threshold; this is historical only.
- Allowing users to customize bucket thresholds for their own view; thresholds are operator-set and global.
