# Freight Logistics Weekly Surge In Railroad Carload Volume Signals Industrial Demand Pickup

**Idea ID:** `freight-logistics-weekly-surge-in-railroad-carload-volume-si`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising carload volumes indicate greater industrial throughput and economic activity. Railroad volumes correlate strongly with industrial production.

## Universe
- XLI

## Data Sources
- Public weekly railroad carload volume data

## Signal Logic
Enter long XLI if weekly carload volume rises >10% above 4-week average

## Entry / Exit
Entry: Enter long XLI if weekly carload volume rises >10% above 4-week average Exit: Exit after 5 weeks or if volume declines below 5% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public weekly railroad carload volume data via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Railroad carload data regularly fluctuates with industrial cycles.

## Required Keys
- None
