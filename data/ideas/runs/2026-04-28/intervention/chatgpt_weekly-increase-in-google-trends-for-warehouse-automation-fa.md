# Weekly Increase In Google Trends For Warehouse Automation Failure Signals Industrial Disruption

**Idea ID:** `weekly-increase-in-google-trends-for-warehouse-automation-fa`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches on warehouse automation failure signal operational risks and potential delays. Industrial sector faces headwinds from increased automation issues and supply chain delays.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI if weekly Google Trends for 'warehouse automation failure' rises 20% week-over-week

## Entry / Exit
Entry: Enter short XLI if weekly Google Trends for 'warehouse automation failure' rises 20% week-over-week Exit: Exit after 3 weeks or if search interest falls 10% week-over-week

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
- Why It Should Fire Soon: Automation failures in warehouses occur sporadically and generate notable search interest spikes.

## Required Keys
- None
