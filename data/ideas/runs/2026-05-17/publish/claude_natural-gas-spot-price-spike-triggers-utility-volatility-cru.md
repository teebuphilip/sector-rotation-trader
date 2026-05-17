# Natural Gas Spot Price Spike Triggers Utility Volatility Crush

**Idea ID:** `natural-gas-spot-price-spike-triggers-utility-volatility-cru`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When natural gas spot prices jump >8% in a single day, utilities face immediate margin compression and hedging repricing. This creates a short-term tactical opportunity as the market reprices utility equity risk. Utilities are direct consumers of natural gas input costs; sudden price spikes compress earnings guidance and trigger sell-offs in dividend stocks.

## Universe
- XLU

## Data Sources
- FRED series DHHNGSP (Henry Hub Natural Gas Spot Price) daily

## Signal Logic
XLU closes down >1.5% on a day when DHHNGSP rises >8% from prior close

## Entry / Exit
Entry: XLU closes down >1.5% on a day when DHHNGSP rises >8% from prior close Exit: XLU closes up >1% from entry or 7 calendar days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DHHNGSP (Henry Hub Natural Gas Spot Price) daily via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Natural gas prices are volatile; 8%+ daily moves occur 3–5 times per quarter, making this a realistic monthly signal.

## Required Keys
- None
