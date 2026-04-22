# Shipping Container Squeeze Play

**Idea ID:** `shipping-container-squeeze-play`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Elevated container backlogs in major Asian ports signal supply chain tightness and rising freight costs, inflating input prices for manufacturing and retail. Manufacturing sector faces margin compression from elevated logistics costs; industrials are most exposed to freight cost pass-through friction.

## Universe
- XLI

## Data Sources
- Port of Shanghai weekly container export volumes and backlog through port_container_volume adapter (public shipping indices)

## Signal Logic
When Shanghai port weekly export backlog exceeds 90th percentile of 52-week rolling history

## Entry / Exit
Entry: When Shanghai port weekly export backlog exceeds 90th percentile of 52-week rolling history Exit: After 10 trading days or when backlog normalizes below 70th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port of Shanghai weekly container export volumes and backlog through port_container_volume adapter (public shipping indices) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal shipping surges (Chinese New Year, holiday inventory builds) and port congestion recur predictably; 2–3 backlog spikes per quarter.

## Required Keys
- None
