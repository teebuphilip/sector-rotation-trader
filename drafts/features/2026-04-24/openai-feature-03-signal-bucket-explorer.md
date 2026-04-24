# Signal Bucket Explorer
Status: Draft
Generated: 2026-04-24 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Signal Hunters need a quick way to understand which bucket a signal belongs to and why, without guessing or digging through jargon.
- **Goal:** Add a compact, on-hover or tap overlay on each signal that shows its bucket (ALPHA / noise / unresolved) plus the core lab takeaway in plain language.
- **Metric:** Reduce support questions about signal classification by 30%.

## 2. User Stories

- As a Signal Hunter, I want to instantly know what bucket a signal is sorted into and the lab’s reasoning, so I save time vetting ideas.
- As a Receipts Guy, I want bucket info that includes failures and uncertainty, so I get the full picture.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Overlay triggered by hover on desktop and tap on mobile over signal name in leaderboard.
- **Requirement 2:** Overlay text must include bucket name, a sentence on current lab findings (including failures), and days running context.
- **Requirement 3:** Overlay must not hide losses or soften failure language.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Overlay uses a torn paper effect with raw typewriter font to emphasize lab notebook feel, no corporate polish.

## 5. Acceptance Criteria (AC)

- Overlay appears reliably on hover/tap with no lag.
- Bucket names and lab notes reflect most recent lab conclusions.
- Losses and unresolved signals language is direct and unfiltered.

## 6. Out of Scope

- No onboarding or tooltip-style explanations beyond the overlay text.
- No edits or euphemisms of bucket descriptions.
