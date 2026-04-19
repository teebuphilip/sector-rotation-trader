# Port Congestion Squeeze

**Idea ID:** `port-congestion-squeeze`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Surges in port activity can signal supply chain bottlenecks and inventory shortages that impact multiple sectors. Industrials and transportation sectors will benefit from higher shipping volumes and infrastructure investment.

## Universe
- XLI

## Data Sources
- Port container volume data through port_container_volume adapter

## Signal Logic
If the week-over-week change in port container volume exceeds 10%

## Entry / Exit
Entry: If the week-over-week change in port container volume exceeds 10% Exit: After 4 weeks or when the weekly volume change falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume data through port_container_volume adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Port activity frequently experiences volatile swings due to supply chain disruptions and seasonal factors.

## Required Keys
- None
