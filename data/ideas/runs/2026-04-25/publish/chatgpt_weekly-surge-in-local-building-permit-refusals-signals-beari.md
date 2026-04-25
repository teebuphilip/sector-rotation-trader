# Weekly Surge In Local Building Permit Refusals Signals Bearish Xlre

**Idea ID:** `weekly-surge-in-local-building-permit-refusals-signals-beari`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising building permit refusals constrain real estate development and signal future supply shortages. Real estate sector growth slows when permits are denied, reducing new inventory and sales.

## Universe
- XLRE

## Data Sources
- Public scrape of weekly local government building permit refusals

## Signal Logic
Enter short XLRE if weekly refusals increase by 20% vs prior 4-week average

## Entry / Exit
Entry: Enter short XLRE if weekly refusals increase by 20% vs prior 4-week average Exit: Exit after 6 weeks or if refusals revert below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public scrape of weekly local government building permit refusals via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Building permit decisions are reported weekly and fluctuate with local politics and economic cycles.

## Required Keys
- None
