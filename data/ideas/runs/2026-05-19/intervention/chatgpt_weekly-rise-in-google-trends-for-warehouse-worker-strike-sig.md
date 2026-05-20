# Weekly Rise In Google Trends For Warehouse Worker Strike Signals Labor Unrest Risk

**Idea ID:** `weekly-rise-in-google-trends-for-warehouse-worker-strike-sig`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing search interest in warehouse worker strikes often precedes labor disruptions impacting industrial and consumer goods sectors. Labor strikes can reduce output and increase costs in industrial supply chains.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI when 2-week Google Trends for 'warehouse worker strike' rises by more than 20% week-over-week

## Entry / Exit
Entry: Enter short XLI when 2-week Google Trends for 'warehouse worker strike' rises by more than 20% week-over-week Exit: Exit after 3 weeks or when trend drops below 10% weekly increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor unrest is a recurrent theme with measurable weekly search interest surges.

## Required Keys
- None
