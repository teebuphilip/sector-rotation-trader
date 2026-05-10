# Freight Diesel Volatility Spike Contraction Signal

**Idea ID:** `freight-diesel-volatility-spike-contraction-signal`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When diesel prices spike >5% week-over-week while container volumes contract >3% weekly, supply chain tightening creates logistics margin pressure and industrial demand signals. Diesel spikes + volume contractions signal demand shock and rising cost pressures on transport and manufacturing.

## Universe
- XLI

## Data Sources
- FRED series GASDESW (diesel prices) and port_container_volume adapter (weekly TEU data), daily/weekly updates

## Signal Logic
If GASDESW spike >5% WoW and port TEU volumes fall >3% WoW simultaneously, enter short industrials

## Entry / Exit
Entry: If GASDESW spike >5% WoW and port TEU volumes fall >3% WoW simultaneously, enter short industrials Exit: Exit after 8 trading days or if either metric normalizes (diesel falls back <2% or TEU growth turns positive)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series GASDESW (diesel prices) and port_container_volume adapter (weekly TEU data), daily/weekly updates via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Diesel and port volume volatility cross thresholds 2–3 times per quarter; simultaneous moves occur monthly or near-monthly.

## Required Keys
- None
