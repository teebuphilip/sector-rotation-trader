# Commercial Real Estate Vacancy Spike Bearish Signal

**Idea ID:** `commercial-real-estate-vacancy-spike-bearish-signal`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly CRE vacancy announcements and market reports often spike when major tenant departures or defaults occur, signaling real estate distress and reducing property valuations. Rising CRE vacancy directly compresses real estate fundamentals, cap rates, and investor returns in the real estate sector.

## Universe
- XLRE

## Data Sources
- CoStar or CBRE weekly commercial vacancy rate data through html_table adapter

## Signal Logic
If reported CRE vacancy rate rises 0.5% or more week-over-week in any major metro, short XLRE.

## Entry / Exit
Entry: If reported CRE vacancy rate rises 0.5% or more week-over-week in any major metro, short XLRE. Exit: Exit after 12 trading days or when weekly vacancy stabilizes.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use CoStar or CBRE weekly commercial vacancy rate data through html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: CRE vacancies fluctuate weekly and 0.5%+ moves occur multiple times per quarter as tenants relocate or default.

## Required Keys
- None
