# Weekly Spike In Freightlogistics Railcar Loadings Portending Industrial Sector Pressure

**Idea ID:** `weekly-spike-in-freightlogistics-railcar-loadings-portending`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden increase in railcar loadings signals rising industrial production and logistics demand. Industrial ETFs benefit from increased freight activity.

## Universe
- XLI

## Data Sources
- Railcar loadings dataset from freight_logistics adapter

## Signal Logic
Entry when weekly railcar loadings rise more than 8% over prior 3 weeks average

## Entry / Exit
Entry: Entry when weekly railcar loadings rise more than 8% over prior 3 weeks average Exit: Exit when loadings drop 5% below 3-week average or after 5 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Railcar loadings dataset from freight_logistics adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly freight logistics data fluctuates regularly with economic cycles.

## Required Keys
- None
