# Weekly Jump In Google Trends For Truck Driver Shortage Signals Labor Stress In Transportation

**Idea ID:** `weekly-jump-in-google-trends-for-truck-driver-shortage-signa`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for truck driver shortage indicate labor tightness impacting freight logistics and supply chain. Labor shortages increase costs and reduce efficiency in transportation and industrial sectors.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends for 'truck driver shortage' rises 35% WoW

## Entry / Exit
Entry: If weekly Google Trends for 'truck driver shortage' rises 35% WoW Exit: After 4 weeks or if trend falls below 15% above baseline

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
- Why It Should Fire Soon: Driver shortage news and concern cycles regularly with regulatory changes and market shifts.

## Required Keys
- None
