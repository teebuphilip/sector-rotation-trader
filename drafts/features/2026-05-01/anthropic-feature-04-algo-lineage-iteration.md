# Algo Lineage & Iteration
Status: Draft
Generated: 2026-05-01 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** When an operator forks or tweaks a signal, there's no visible record of which algos are related or descended from the same original idea. A Signal Hunter can't tell if TradingDogMem v2 is a refinement or a completely new bet. The lab loses the narrative of iteration.
- **Goal:** Let operators link an algo to a 'parent' or 'ancestor' algo. Display these relationships on the leaderboard and detail page so users see the genealogy of signal ideas.
- **Metric:** Paid subscribers discover 20% more algos per session (by following lineage chains). Operator storytelling increases (they tag algos and explain the fork in algo notes).

## 2. User Stories

- As a Signal Hunter, I want to see that TradingDogMemV2 descends from the original TradingDogMem, and compare their metrics side by side, so I can understand if the tweak helped or hurt.
- As an Alt-Data Nerd, I want to follow the entire lineage of a signal idea from v1 to v3, including all dead ends, so I can see what the operator learned and whether the current version is a real improvement.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Operator can optionally set a 'parent algo' when creating or editing an algo. Parent must be an existing (or retired) algo in the lab. This creates a directed link, not a group.
- **Requirement 2:** Algo detail page shows lineage as a simple tree: grandparent → parent → current. Each node is a clickable link to that algo's page. Show all siblings too (other children of the same parent).
- **Requirement 3:** Leaderboard shows a small lineage badge next to algo name if it has a parent or children. Badge is a small icon (e.g., '⎇') that expands on hover to show parent name or child count.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Lineage is displayed as a text tree, not a graphic. E.g., 'TradingDogMem (original) → TradingDogMemV2 → TradingDogMemV3 (current)'. Each name is a link. Siblings are listed below as 'Also descended from TradingDogMem: TradingDogMemAlt, TradingDogMemLite'. Clean, scannable, no flowchart.

## 5. Acceptance Criteria (AC)

- Operator can set a parent algo when creating a new algo. Parent algo link is stored and displayed.
- Algo detail page shows the full lineage (ancestors) and all siblings. All names are clickable.
- If an operator removes the parent link, the lineage disappears. Lineage history is not logged or shown to users.

## 6. Out of Scope

- Auto-suggestion of parent algos based on name or performance similarity.
- Forced lineage tagging (operator must opt-in to link algos).
- Comparison views that surface metrics only from lineage trees (users must click individually).
