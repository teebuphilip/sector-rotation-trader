# Weekly Surge In Google Trends Searches For Warehouse Worker Shortage Signals Labor Tightness

**Idea ID:** `weekly-surge-in-google-trends-searches-for-warehouse-worker-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in searches for warehouse worker shortage suggests rising labor scarcity in logistics-heavy sectors. Labor shortages in industrial sectors likely increase costs and disrupt supply chains.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches for 'warehouse worker shortage' rise more than 15% over prior 4 weeks

## Entry / Exit
Entry: If weekly searches for 'warehouse worker shortage' rise more than 15% over prior 4 weeks Exit: When searches decline below 10% above 4-week prior average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor tightness topics often fluctuate weekly and can spike due to seasonal demand or economic shifts.

## Required Keys
- None
