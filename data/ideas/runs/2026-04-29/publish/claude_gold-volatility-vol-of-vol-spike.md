# Gold Volatility Vol-of-vol Spike

**Idea ID:** `gold-volatility-vol-of-vol-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When the intraday volatility of gold prices begins spiking (vol-of-vol), it signals macro uncertainty; this often precedes a reallocation into defensive commodities. Tech and growth equities underperform when gold volatility rises, signaling flight-to-safety behavior.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily prices for GLD and USO via price_only adapter

## Signal Logic
If 5-day rolling standard deviation of GLD daily returns exceeds 2x the 60-day rolling mean, AND GLD closes above its 20-day MA

## Entry / Exit
Entry: If 5-day rolling standard deviation of GLD daily returns exceeds 2x the 60-day rolling mean, AND GLD closes above its 20-day MA Exit: After 7 trading days or when vol-of-vol reverts to mean (5-day std dev falls below 1.5x 60-day mean)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for GLD and USO via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Volatility spikes in commodities occur multiple times per month; gold vol-of-vol thresholds trigger 2-4 times quarterly.

## Required Keys
- None
