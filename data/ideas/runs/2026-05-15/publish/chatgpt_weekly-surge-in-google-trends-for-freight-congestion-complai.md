# Weekly Surge In Google Trends For Freight Congestion Complaints Correlating With Industrial Sector Risk

**Idea ID:** `weekly-surge-in-google-trends-for-freight-congestion-complai`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising complaints about freight congestion signal worsening supply chain delays impacting industrial output. Industrial sector profitability is pressured by logistics bottlenecks and delays.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for freight congestion

## Signal Logic
If weekly search volume rises 30% above 5-week average

## Entry / Exit
Entry: If weekly search volume rises 30% above 5-week average Exit: When volume returns below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for freight congestion via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly freight issues and complaints vary with port activity and transport disruptions.

## Required Keys
- None
