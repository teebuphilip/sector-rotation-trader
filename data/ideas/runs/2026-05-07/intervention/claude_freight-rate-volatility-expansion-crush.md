# Freight Rate Volatility Expansion Crush

**Idea ID:** `freight-rate-volatility-expansion-crush`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When freight rate volatility (rolling 4-week standard deviation) expands beyond 2-sigma above 12-month mean, it signals supply chain chaos that pressures industrial inputs but lifts logistics and rail operators. Elevated freight volatility boosts pricing power for transportation and logistics firms while signaling demand uncertainty.

## Universe
- XLI

## Data Sources
- FRED Cass Freight Index (CASS) weekly levels via fred_series adapter

## Signal Logic
When 4-week freight rate volatility exceeds 12-month mean + 2 standard deviations

## Entry / Exit
Entry: When 4-week freight rate volatility exceeds 12-month mean + 2 standard deviations Exit: After 6 trading days or when volatility reverts below mean + 1.5 sigma

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Cass Freight Index (CASS) weekly levels via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight volatility expands 2-3 times per month during seasonal demand swings or supply shocks.

## Required Keys
- None
