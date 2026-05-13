# Port Container Volume Surge Signals Import Demand Recovery And Consumer Spending Rebound

**Idea ID:** `port-container-volume-surge-signals-import-demand-recovery-a`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Container imports spike 8-12 weeks ahead of retail sales beats when retailers frontload inventory in advance of holiday or promotional seasons. Sustained volume surge is bullish for discretionary. Rising port container volumes signal retailers are confident enough to increase inventory, a leading indicator for sales growth and profit.

## Universe
- XLY

## Data Sources
- Port of Los Angeles, Port of Long Beach, and Port of Newark container throughput via port_container_volume adapter, weekly data

## Signal Logic
When weekly aggregate container volume (LA + LB + Newark TEU) exceeds 8-week moving average by 10% or more

## Entry / Exit
Entry: When weekly aggregate container volume (LA + LB + Newark TEU) exceeds 8-week moving average by 10% or more Exit: After 12 trading days or when volume falls back to within 5% of 8-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port of Los Angeles, Port of Long Beach, and Port of Newark container throughput via port_container_volume adapter, weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port cycles turn seasonally and with retail calendars. Back-to-school (Aug), holiday season (Sep-Oct), and seasonal demand shifts produce regular 10-15% volume swings multiple times per year.

## Required Keys
- None
