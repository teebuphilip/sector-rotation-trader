# Weekly Rise In Google Trends For Freight Train Delays Signals Logistics Bottlenecks

**Idea ID:** `weekly-rise-in-google-trends-for-freight-train-delays-signal`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased freight train delay searches indicate supply chain slowdowns impacting industrial logistics. Industrial and logistics sectors see margin pressure from freight delays and bottlenecks.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends for 'freight train delays' rises 40% WoW

## Entry / Exit
Entry: If weekly Google Trends for 'freight train delays' rises 40% WoW Exit: After 3 weeks or if trend falls below 15% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Freight delays fluctuate regularly with weather and rail network congestion.

## Required Keys
- None
