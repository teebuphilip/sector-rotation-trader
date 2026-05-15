# Signal Decay Tracker
Status: Draft
Generated: 2026-05-15 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Signals can perform well initially but then fade or fail, and users need a clear way to see when a signal's edge is deteriorating without spin or hiding losses.
- **Goal:** Provide a transparent metric showing the 'decay rate' of each signal's effectiveness over recent periods, highlighting when a formerly strong signal is losing its edge.
- **Metric:** Increase time spent on leaderboard page by 10% and reduce user queries about signal reliability by 15%.

## 2. User Stories

- As a Signal Hunter, I want to see a clear indicator of how a signal's performance has changed recently, so that I can decide if it's still worth tracking.
- As a Receipts Guy, I want to spot signals that have sharply declined without any sugarcoating, so I can call out survivorship bias.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Show a 'decay rate' percentage or trend line for each signal comparing recent returns to historical returns over multiple time frames.
- **Requirement 2:** If a signal has not fired trades in 30+ days, visually flag it as 'stale' but keep it visible at the bottom of the leaderboard.
- **Requirement 3:** Integrate decay info into the existing leaderboard without cluttering or requiring extra clicks.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use subtle but unmistakable color shifts (e.g., desaturated red for decay) next to signal names; no tooltips or modals, info must be glanceable.

## 5. Acceptance Criteria (AC)

- Decay metric visible for every signal on desktop and mobile leaderboards.
- Signals with no trades in last 30 days are flagged 'stale' and positioned at bottom.
- No changes to existing signal naming or rankings except added decay info.

## 6. Out of Scope

- Detailed decay explanation pages or onboarding.
- Automatic hiding or filtering of decayed signals.
