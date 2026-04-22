# Cross-Algo Pattern Spotter
Status: Draft
Generated: 2026-04-22 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Signal Hunter and Alt-Data Nerd can't quickly see which types of signals or data sources are working across multiple algos. A user has to manually compare leaderboard entries to notice 'all the weather-based algos are in the top 10' or 'volume-based signals are failing everywhere.' That pattern is the insight.
- **Goal:** Let users tag algos with signal type or data source, then see which buckets those tags cluster into. Show real correlation without claiming causation.
- **Metric:** Paid users creating and viewing tags; number of tagged algos per signal type; time spent exploring cross-algo patterns.

## 2. User Stories

- As a Signal Hunter, I want to tag algos by their signal type (e.g., 'weather-based', 'options-flow', 'social-sentiment') and see which types are ALPHA vs noise, so I know where to focus my own research.
- As the Receipts Guy, I want to see that social-sentiment algos are 3-for-12 in the top 50, so I know what the actual win rate is for that bucket—not a story someone told me.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Allow paid users to add free-form tags to any algo (max 3 tags per algo). Tags are user-created and visible only to that user—no shared tagging.
- **Requirement 2:** Build a 'Pattern View' (linked from the leaderboard) that shows: tag name → count of algos with that tag → force rank distribution of those algos → win rate and trade count for algos in each bucket with that tag.
- **Requirement 3:** The Pattern View displays as a simple table: tag | total algos | ALPHA count | noise count | unresolved count | avg win rate in ALPHA | avg trades in ALPHA. No chart. No inference.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Tags are added via a '+Tag' button on the algo detail page. Pattern View is a paid-only page accessible from the main nav. The table is sortable by count and win rate. No suggestion engine for tags—users must type them. Losses are shown in context: if 'weather-based' algos have a 30% win rate in ALPHA, that number is visible and unsoftened.

## 5. Acceptance Criteria (AC)

- Paid user can add up to 3 tags to any algo; tags are stored per-user and visible only to that user on the algo detail page.
- Pattern View shows all tags created by the user, sorted by count; clicking a tag shows all algos with that tag, their bucket, win rate, and trade count.
- Failing tags (e.g., 'social-sentiment' with 0 ALPHA algos, 8 noise algos) are shown clearly with no narrative softening; user can see the full picture.

## 6. Out of Scope

- Shared or public tagging systems.
- Tag suggestions or autocomplete based on past tags.
- Any inference about why certain signal types cluster in certain buckets.
