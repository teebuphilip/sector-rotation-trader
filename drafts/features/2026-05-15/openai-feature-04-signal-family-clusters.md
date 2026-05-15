# Signal Family Clusters
Status: Draft
Generated: 2026-05-15 | Provider: openai

## 1. The "Why" (Context)

- **Problem:** Signal Hunters struggle to grasp which signals share similar data sources or logic, making it harder to diversify or identify correlated failures.
- **Goal:** Group signals into 'families' based on shared alt-data tags or trading logic and show these clusters on the leaderboard with clear nameplates, losses included distinctly per signal.
- **Metric:** Increase user exploration of related signals by 20%, measured by clicks within clustered groups.

## 2. User Stories

- As a Signal Hunter, I want to see which signals are siblings or cousins so I can judge if my exposure is really diversified.
- As the Receipts Guy, I want to compare losses within a cluster to spot systemic failure points.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Assign each signal to zero or one family cluster with a short family name displayed above grouped signals.
- **Requirement 2:** Clusters must be collapsible on the leaderboard but show all signals’ wins and losses when expanded.
- **Requirement 3:** Cluster definitions editable only by the operator, reflecting real shared alt-data or algo kinship.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Use subtle boxed outlines and family name banners with a rough, hand-drawn style; no corporate grouping visuals.

## 5. Acceptance Criteria (AC)

- Clusters load correctly on leaderboard with expand/collapse toggles.
- Losses for each signal remain fully visible and unaggregated within clusters.
- Operator can create and edit clusters via admin tools.

## 6. Out of Scope

- Automatically inferred clusters without operator input.
- Merging signals or hiding individual signal data within clusters.
