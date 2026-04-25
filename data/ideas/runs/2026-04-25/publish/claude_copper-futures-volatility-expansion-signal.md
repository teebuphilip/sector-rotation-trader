# Copper Futures Volatility Expansion Signal

**Idea ID:** `copper-futures-volatility-expansion-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in copper volatility above 40th percentile combined with price strength signal industrial demand uncertainty and infrastructure cycle inflection, driving cyclical materials rotation. Copper volatility expansion reflects uncertainty in industrial demand; resolution often drives materials and mining equity rallies.

## Universe
- XLB

## Data Sources
- Yahoo Finance daily copper futures (HG) prices and implied volatility

## Signal Logic
If 10-day realized volatility of copper futures exceeds 20% AND copper closes above 20-day MA on above-average volume

## Entry / Exit
Entry: If 10-day realized volatility of copper futures exceeds 20% AND copper closes above 20-day MA on above-average volume Exit: After 9 trading days or if copper volatility collapses below 15%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily copper futures (HG) prices and implied volatility via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commodity volatility cycles are continuous; copper volatility surges frequently with geopolitical events and demand data releases.

## Required Keys
- None
