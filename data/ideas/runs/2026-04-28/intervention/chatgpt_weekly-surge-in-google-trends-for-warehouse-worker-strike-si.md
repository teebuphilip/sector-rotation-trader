# Weekly Surge In Google Trends For Warehouse Worker Strike Signals Freight Logistics Disruption

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-worker-strike-si`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest in warehouse strikes signals imminent labor disruptions affecting freight flow. Industrial sector faces headwinds from labor disruptions in key logistics hubs.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI if weekly Google Trends searches for 'warehouse worker strike' rise 25% week-over-week

## Entry / Exit
Entry: Enter short XLI if weekly Google Trends searches for 'warehouse worker strike' rise 25% week-over-week Exit: Exit after 3 weeks or if search interest drops below prior week

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
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor unrest topics spike repeatedly during contract talks and economic stress periods.

## Required Keys
- None
