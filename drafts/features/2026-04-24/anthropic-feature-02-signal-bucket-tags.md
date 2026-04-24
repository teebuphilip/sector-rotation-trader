# Signal Bucket Tags
Status: Draft
Generated: 2026-04-24 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Alt-Data Nerds and Signal Hunters land on the leaderboard but can't easily categorize which algos are exploratory noise, proven-ish (repeatable signal), or genuinely unresolved — the operator knows, but the taxonomy is invisible.
- **Goal:** Expose the operator's working classification of each algo (ALPHA / NOISE / UNRESOLVED / DEAD) as a user-facing tag, so subscribers understand which bucket the lab thinks each signal lives in.
- **Metric:** % of paying users who click into 'Bucket' tag page within first week; time-to-insight (seconds from landing to understanding signal quality tier).

## 2. User Stories

- As an Alt-Data Nerd, I want to see which signals the lab classifies as UNRESOLVED so I can follow along with active experiments, not just finished ones.
- As a Signal Hunter, I want to filter the leaderboard to show only ALPHA-bucket algos, so I can focus on signals the operator thinks have real edge.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add 'Bucket' column to leaderboard with four tags: ALPHA (rolling 30D Sharpe > 0.5 + days running > 90), NOISE (force rank > 75th percentile), UNRESOLVED (< 90 days running, not yet classified), DEAD (no trades in 180 days).
- **Requirement 2:** Each tag is clickable and links to a micro-page explaining the operator's definition and rules for that bucket; rules are human-readable, not algorithmic jargon.
- **Requirement 3:** Re-evaluate bucket assignment daily after market close; if an algo moves buckets, show a small timestamp on the tag ('reclassified 3 days ago').

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Tags use muted colors: ALPHA = green, NOISE = gray, UNRESOLVED = yellow, DEAD = dark gray. No animations. Tag text is uppercase, operator's voice in the explainer (e.g., 'UNRESOLVED: too early to call, still running'). Mobile: tags wrap but remain sortable.

## 5. Acceptance Criteria (AC)

- Bucket assignment logic is deterministic and auditable; operator can override a tag manually for a specific algo with a note (visible to all users).
- Filtering by bucket (e.g., 'show only ALPHA') correctly returns algos and persists; combining filters (e.g., 'ALPHA + days running > 120') works.
- Bucket explainer page is under 300 words and uses plain language (no 'proprietary methodology').

## 6. Out of Scope

- User-created or custom bucket categories; taxonomy is operator-defined only.
- Predictive reclassification (e.g., 'this NOISE signal will become ALPHA'); tags reflect current state only.
