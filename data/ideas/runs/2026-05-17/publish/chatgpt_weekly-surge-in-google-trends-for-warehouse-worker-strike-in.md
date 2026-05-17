# Weekly Surge In Google Trends For Warehouse Worker Strike Indicates Supply Chain Labor Risk

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-worker-strike-in`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing strike interest signals potential labor disruptions in supply chain bottlenecks. Industrial and logistics sectors suffer when labor strikes threaten operational continuity.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'warehouse worker strike'

## Signal Logic
Enter short XLI if weekly Google Trends for 'warehouse worker strike' rises 40%+ WoW

## Entry / Exit
Entry: Enter short XLI if weekly Google Trends for 'warehouse worker strike' rises 40%+ WoW Exit: Exit after 4 weeks or if trend declines 20% WoW

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'warehouse worker strike' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor strike interest and news tend to cluster in short-term bursts.

## Required Keys
- None
