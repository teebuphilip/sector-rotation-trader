# Freight Rate Volatility Spike

**Idea ID:** `freight-rate-volatility-spike`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden spikes in spot freight rates indicate supply-demand imbalance in trucking/shipping, signaling upstream input cost inflation and logistics stress. Rising freight costs compress margins for manufacturers, retailers, and logistics firms; signals inflation pressure on supply chains.

## Universe
- XLI

## Data Sources
- Cass Freight Index or FreightWaves spot rate index (weekly via HTML scrape or RSS feed)

## Signal Logic
If weekly spot freight rate rises >12% above 6-week moving average

## Entry / Exit
Entry: If weekly spot freight rate rises >12% above 6-week moving average Exit: After 14 trading days or when rate retreats 8% below entry spike peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Cass Freight Index or FreightWaves spot rate index (weekly via HTML scrape or RSS feed) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight rates are volatile and driven by seasonal demand, weather, and capacity; multiple spikes per quarter are normal.

## Required Keys
- None
