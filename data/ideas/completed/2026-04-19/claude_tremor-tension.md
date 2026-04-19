# Tremor Tension

**Idea ID:** `tremor-tension`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Spikes in earthquake activity can signal increased volatility and risk aversion in financial markets. Earthquakes and natural disasters often drive increased healthcare and disaster relief spending.

## Universe
- XLV

## Data Sources
- USGS daily earthquake activity data through earthquake_activity adapter

## Signal Logic
If the daily number of earthquakes worldwide increases more than 10% above the prior 7-day average

## Entry / Exit
Entry: If the daily number of earthquakes worldwide increases more than 10% above the prior 7-day average Exit: After 3 trading days or once earthquake activity falls back to the prior 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS daily earthquake activity data through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity exhibits regular daily and weekly patterns, and deviations from typical ranges often occur.

## Required Keys
- None
