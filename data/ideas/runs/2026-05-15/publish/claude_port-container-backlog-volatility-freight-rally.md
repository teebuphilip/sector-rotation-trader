# Port Container Backlog Volatility Freight Rally

**Idea ID:** `port-container-backlog-volatility-freight-rally`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Week-over-week swings in port container throughput >15% signal volatility in global trade flows and logistics demand. Port volatility creates urgency for shippers to use alternative routes/carriers; freight rates rise.

## Universe
- XLI

## Data Sources
- Port of LA/Long Beach container volume weekly data via port_container_volume adapter

## Signal Logic
If weekly port container volume swings >15% above or below 13-week moving average

## Entry / Exit
Entry: If weekly port container volume swings >15% above or below 13-week moving average Exit: Exit after 4 weeks or when volatility normalizes to <8% of MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port of LA/Long Beach container volume weekly data via port_container_volume adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Container volume swings are seasonal and event-driven; fires 2–4 times per quarter.

## Required Keys
- None
