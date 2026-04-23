# Weekly Increase In Local Economy Weirdness Sudden Rise In Building Permit Denials Bearish Xlre

**Idea ID:** `weekly-increase-in-local-economy-weirdness-sudden-rise-in-bu`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising permit denials imply local regulatory or economic headwinds, pressuring real estate development and XLRE. Permit denials restrict new real estate supply and signal economic weakness.

## Universe
- XLRE

## Data Sources
- Municipal building permit denial counts weekly scrape

## Signal Logic
Enter short XLRE when weekly permit denials rise 30%+ over prior 4 weeks

## Entry / Exit
Entry: Enter short XLRE when weekly permit denials rise 30%+ over prior 4 weeks Exit: Exit after 6 weeks or when denials fall below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Municipal building permit denial counts weekly scrape via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Local government data releases regularly produce weekly permit fluctuations.

## Required Keys
- None
