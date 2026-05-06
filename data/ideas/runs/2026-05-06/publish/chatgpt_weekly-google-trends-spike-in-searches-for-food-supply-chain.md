# Weekly Google Trends Spike In Searches For Food Supply Chain Disruptions

**Idea ID:** `weekly-google-trends-spike-in-searches-for-food-supply-chain`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing consumer interest in food supply disruptions signals potential shortages or inflation in staples. Staples sector may face margin pressure and stock volatility during supply chain issues.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches for 'food supply chain disruption' rise more than 20% week-over-week

## Entry / Exit
Entry: If weekly searches for 'food supply chain disruption' rise more than 20% week-over-week Exit: After 3 weeks or when growth drops below 7%

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
- Why It Should Fire Soon: Food supply chain concerns frequently arise due to weather, logistics, or geopolitical events.

## Required Keys
- None
