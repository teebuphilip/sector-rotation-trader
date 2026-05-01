# Signal Divergence Flags
Status: Draft
Generated: 2026-05-01 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Signal Hunters need to quickly spot honest interesting divergence between force rank and rolling 30-day rank but it's buried in raw numbers.
- **Goal:** Add visual flags on leaderboard entries that highlight honest rank divergences and provide quick access to context.
- **Metric:** Increase clicks on algo details by 20% from users tagged as Signal Hunters.

## 2. User Stories

- As a Signal Hunter, I want to see which algos have high rolling rank but low overall force rank, so I can investigate intriguing recent momentum.
- As a Signal Hunter, I want to quickly filter the leaderboard to only show algos with significant divergence, so I can focus my research.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Add a colored badge icon next to algo names when their rolling 30-day rank and force rank differ beyond a threshold.
- **Requirement 2:** Allow users to filter the leaderboard by divergence status with a simple toggle.
- **Requirement 3:** Ensure badges update daily with fresh rank data.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Badges are minimal, maybe a split red/green circle to show divergence direction. No tooltips that explain fancy math—just raw numbers side by side.

## 5. Acceptance Criteria (AC)

- Badge appears only when divergence threshold is met and updates daily.
- Filter toggle shows/hides only divergent algos instantly.
- Works seamlessly on mobile and desktop leaderboard views.

## 6. Out of Scope

- No AI or predictive modeling on divergence.
- No onboarding or explanations for what divergence means.
