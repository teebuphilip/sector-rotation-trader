# Bucket Thesis Statement
Status: Draft
Generated: 2026-04-23 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** A Receipts Guy wants to understand why an algo ended up in the 'noise' bucket instead of ALPHA, but today there is no explanation — just a label. The operator's reasoning is invisible.
- **Goal:** Let the operator attach a 1-2 sentence thesis to each algo explaining what it is testing, what would make it real, and why it is currently classified as ALPHA / noise / unresolved.
- **Metric:** % of algos with theses filled in; avg time Receipts Guys spend reading theses; correlation between thesis clarity and subscription renewals.

## 2. User Stories

- As a Receipts Guy, I want to read the operator's actual thesis for why Baileymol is in the 'unresolved' bucket, so I can understand if it is still running because it's promising or because he is just stubborn.
- As an Alt-Data Nerd, I want to see what the operator thinks would prove the signal is real (e.g., 'Needs 50+ trades with >55% win rate in rising markets'), so I can track whether the signal is trending toward proof or away from it.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Each algo on the leaderboard detail page gets a 'Thesis' section: operator-authored text (250 chars max), edit-only by operator, visible to all users (free and paid).
- **Requirement 2:** Thesis must include: (1) what the signal tests, (2) current bucket classification and why, (3) what would move it to the next bucket (if applicable).
- **Requirement 3:** Theses are timestamped and versioned; clicking 'History' shows prior theses (e.g., when it was reclassified from ALPHA to noise, the thesis changed).

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Thesis block sits right below the algo name and bucket tag on detail view; reads like a lab note, not marketing. Mono font, light gray box, no decoration. On leaderboard card view, show first 80 chars of thesis as a tooltip. Mobile: full text visible on tap. Operator can edit inline (pencil icon, hit Enter to save).

## 5. Acceptance Criteria (AC)

- Thesis text is plaintext (no rich formatting, no links); special characters render correctly (%, &, >, <).
- Timestamp shows when thesis was last updated; if never updated, shows 'No thesis provided yet.'
- Thesis history is accurate; prior versions are retrievable and compared side-by-side if user clicks 'Compare to [Date].'

## 6. Out of Scope

- Allowing other users to comment on or vote on theses; this is operator voice only.
- Auto-generating theses from trade data or ML summaries; the operator must write it by hand or not at all.
