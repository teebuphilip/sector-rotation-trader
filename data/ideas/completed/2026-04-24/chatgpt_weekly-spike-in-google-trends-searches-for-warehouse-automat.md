# Weekly Spike In Google Trends Searches For Warehouse Automation Failure Signals Bearish Xli

**Idea ID:** `weekly-spike-in-google-trends-searches-for-warehouse-automat`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased interest in warehouse automation failures signals potential operational risks in logistics. Logistics companies face disruptions and cost overruns when automation systems fail.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly search volume for 'warehouse automation failure' rises 30% above 8-week average

## Entry / Exit
Entry: If weekly search volume for 'warehouse automation failure' rises 30% above 8-week average Exit: Exit after 3 weeks or if volume declines below 15% increase

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
- Why It Should Fire Soon: Automation system issues spike occasionally due to new tech rollouts or glitches.

## Required Keys
- None
