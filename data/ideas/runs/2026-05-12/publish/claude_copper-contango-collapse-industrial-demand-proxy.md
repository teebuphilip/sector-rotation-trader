# Copper Contango Collapse Industrial Demand Proxy

**Idea ID:** `copper-contango-collapse-industrial-demand-proxy`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When copper spot rallies but forward curve flattens (contango narrows), market is signaling near-term demand strength but supply confidence; bullish for materials. Copper demand elasticity is high for construction, manufacturing, and power; curve shape is a sensitive real-economy gauge.

## Universe
- XLB

## Data Sources
- FRED series MMNRNJ (Copper prices, spot) daily for spot; pair with CME futures curve slope via price_only adapter (HG nearest vs 6-month forward prices)

## Signal Logic
If copper spot rises >2% in 3 days AND 6-month forward premium (contango) shrinks to <1.5% annualized

## Entry / Exit
Entry: If copper spot rises >2% in 3 days AND 6-month forward premium (contango) shrinks to <1.5% annualized Exit: After 7 trading days or if contango widens beyond 2.5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (Copper prices, spot) daily for spot; pair with CME futures curve slope via price_only adapter (HG nearest vs 6-month forward prices) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commodity curve dynamics shift weekly with supply/demand news; this signal fires 2–3 times per month.

## Required Keys
- None
