# Earthquake Aftershock Amplifier

**Idea ID:** `earthquake-aftershock-amplifier`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Significant earthquake events can trigger increased aftershock activity, which may signal volatility and uncertainty in energy and industrial sectors. Earthquakes can disrupt energy infrastructure, supply chains, and construction activity.

## Universe
- XLE

## Data Sources
- USGS earthquake activity through earthquake_activity adapter

## Signal Logic
If the daily earthquake activity index increases by more than 50% compared to the prior 7-day average

## Entry / Exit
Entry: If the daily earthquake activity index increases by more than 50% compared to the prior 7-day average Exit: After 5 trading days or once the index retreats by 30%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake clusters and aftershock sequences are common, and can often be observed within a 30-day timeframe, especially in seismically active regions.

## Required Keys
- None
