# Signal Divergence Flags
Status: Draft
Generated: 2026-05-08 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Users find it hard to notice when a signal’s short-term rank greatly diverges from its long-term force rank, which is a key insight.
- **Goal:** Surface clear, honest flags for signal rank divergence right on the leaderboard without editorializing.
- **Metric:** Increase user interactions with signals flagged for divergence by 30%.

## 2. User Stories

- As the Signal Hunter, I want to spot signals with conflicting short vs long-term performance instantly, so I can dig deeper.
- As the Alt-Data Nerd, I want to understand honest contradictions in ranking without losing context or getting marketing spin.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Calculate divergence as absolute difference between 30-day rolling rank and overall force rank for each signal.
- **Requirement 2:** Display a simple textual or icon flag (e.g., "DIVERGENT") next to signal names where divergence exceeds a threshold.
- **Requirement 3:** Allow paying users to click the flag to see a minimal tooltip explaining the divergence numbers without hype.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Flags should look like hand-stamped lab notes, rough edges, no polished iconography; tooltips plain monospace text.

## 5. Acceptance Criteria (AC)

- Flags appear accurately for all signals meeting divergence criteria.
- Tooltip opens on click and closes on clicking outside or pressing escape.
- No flags appear for signals with divergence below threshold.

## 6. Out of Scope

- Automatic recommendations based on divergence flags.
- Hiding or downplaying signals with divergence.
