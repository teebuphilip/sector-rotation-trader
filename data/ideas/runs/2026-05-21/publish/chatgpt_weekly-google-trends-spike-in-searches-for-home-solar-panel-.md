# Weekly Google Trends Spike In Searches For Home Solar Panel Repair Signals Green Energy Sector Repair Demand

**Idea ID:** `weekly-google-trends-spike-in-searches-for-home-solar-panel-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing search interest for solar panel repair reflects aging infrastructure and consumer stress in green energy adoption. Repair demand supports energy services and green energy equipment sectors.

## Universe
- XLE

## Data Sources
- Google Trends weekly home solar panel repair searches

## Signal Logic
Enter long when weekly search interest rises 30% above 5-week average

## Entry / Exit
Entry: Enter long when weekly search interest rises 30% above 5-week average Exit: Exit when interest falls below 15% above 5-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly home solar panel repair searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Solar panel maintenance needs frequently increase during seasonal weather transitions.

## Required Keys
- None
