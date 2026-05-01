# Weekly Jump In Google Trends Searches For Warehouse Automation Failure Triggers Bearish Industrials Sector

**Idea ID:** `weekly-jump-in-google-trends-searches-for-warehouse-automati`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches on warehouse automation failures highlight operational bottlenecks and risks in supply chains. Logistics and industrial firms face margin pressure due to automation disruptions.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI when weekly search volume for 'warehouse automation failure' rises 40% above 12-week average

## Entry / Exit
Entry: Enter short XLI when weekly search volume for 'warehouse automation failure' rises 40% above 12-week average Exit: Exit after 5 weeks or if volume drops below 12-week average

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
- Why It Should Fire Soon: Warehouse automation issues are regularly reported, causing weekly interest spikes.

## Required Keys
- None
