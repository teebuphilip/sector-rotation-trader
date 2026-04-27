# Weekly Surge In Google Trends For Warehouse Fire Signals Bearish Xli

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-fire-signals-bea`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in warehouse fires signals supply chain disruptions and inventory losses impacting industrial stocks. Warehouse fires cause immediate logistics disruption and inventory write-offs.

## Universe
- XLI

## Data Sources
- Google Trends weekly data for 'warehouse fire'

## Signal Logic
Enter short if weekly trend rises 40%+ week-over-week

## Entry / Exit
Entry: Enter short if weekly trend rises 40%+ week-over-week Exit: Exit after 3 weeks or when trend normalizes below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'warehouse fire' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Warehouse fire incidents and related media coverage occur several times yearly.

## Required Keys
- None
