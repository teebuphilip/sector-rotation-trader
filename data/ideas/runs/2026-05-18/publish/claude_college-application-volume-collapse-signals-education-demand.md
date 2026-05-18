# College Application Volume Collapse Signals Education Demand Crisis

**Idea ID:** `college-application-volume-collapse-signals-education-demand`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Dramatic drops in college application volumes during peak application season signal demographic or affordability collapse, reducing future revenue for education services and related consumer spending. Lower application volumes signal weakening middle-class household formation, future discretionary spending, and consumer confidence in education ROI.

## Universe
- XLY

## Data Sources
- Common App weekly application submission totals through html_table adapter from public reports

## Signal Logic
If weekly Common App submissions fall 15% or more below the prior-year same week, short XLY.

## Entry / Exit
Entry: If weekly Common App submissions fall 15% or more below the prior-year same week, short XLY. Exit: Exit after 8 trading days or when submissions recover to prior-year levels.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Common App weekly application submission totals through html_table adapter from public reports via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Common App data is released weekly during application season (Sept–Jan) and 15%+ year-over-year swings happen several times per cycle.

## Required Keys
- None
