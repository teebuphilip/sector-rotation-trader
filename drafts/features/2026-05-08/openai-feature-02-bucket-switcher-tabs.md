# Bucket Switcher Tabs
Status: Draft
Generated: 2026-05-08 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Signal Hunters want a fast way to filter the leaderboard by the core buckets (ALPHA / noise / unresolved) without losing sight of losses.
- **Goal:** Enable toggling between buckets with persistent visibility of losses and failures in each view.
- **Metric:** Boost paid user engagement with bucket-filtered leaderboards by 25%.

## 2. User Stories

- As a Signal Hunter, I want to instantly flip through signal buckets to see which weird ideas are holding up in each category.
- As the Alt-Data Nerd, I want to track unresolved signals separately without losing the honest failure data.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Implement three tabs on the leaderboard labeled ALPHA, noise, and unresolved.
- **Requirement 2:** Ensure losses and failure metrics remain fully visible and unsoftened in each bucket view.
- **Requirement 3:** Remember last bucket selected per user session without requiring onboarding or explanations.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Tabs must look like crude lab notebook tabs, hand-drawn style or scratched lines, not polished buttons; no animations other than simple highlight.

## 5. Acceptance Criteria (AC)

- Tabs filter signals correctly by their assigned buckets.
- Failures and losses appear identically in each filtered view as on the full leaderboard.
- Selected bucket persists if user navigates away and returns within session.

## 6. Out of Scope

- Auto-assigning signals to buckets or reclassifying on the fly.
- Adding sorting beyond force rank and days running in tab views.
