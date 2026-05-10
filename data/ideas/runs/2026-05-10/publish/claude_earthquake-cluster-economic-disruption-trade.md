# Earthquake Cluster Economic Disruption Trade

**Idea ID:** `earthquake-cluster-economic-disruption-trade`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of moderate seismic activity in economically active regions trigger insurance and property damage expectations, boosting financials and industrials short-term positioning. Earthquake clusters drive insurance payouts, reinsurance demand, and property damage claims that benefit financial services and adjust valuations.

## Universe
- XLF

## Data Sources
- USGS earthquake activity API, magnitude 4.5+ events within major US metros, daily updates

## Signal Logic
If 3+ magnitude 4.5+ earthquakes occur within 500km radius in 7 days, enter long financial sector

## Entry / Exit
Entry: If 3+ magnitude 4.5+ earthquakes occur within 500km radius in 7 days, enter long financial sector Exit: Exit after 12 trading days or once seismic activity returns to baseline (no events in 5 days)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity API, magnitude 4.5+ events within major US metros, daily updates via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: US experiences 1–2 magnitude 4.5+ earthquake clusters per month; regional clustering within 7 days happens monthly on average.

## Required Keys
- None
