# Port Container Velocity Slowdown Liquidation

**Idea ID:** `port-container-velocity-slowdown-liquidation`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly port container volumes drop >15% from the prior week (signaling demand shock or inventory flush), logistics and industrial stocks face sharp repricing. Container volume collapse signals upstream demand destruction, freight rate pressure, and logistics capex cuts.

## Universe
- XLI

## Data Sources
- Port container volume (TEU) via port_container_volume adapter for top 5 US ports, weekly

## Signal Logic
If aggregate 5-port TEU volume drops >15% week-over-week, short XLI

## Entry / Exit
Entry: If aggregate 5-port TEU volume drops >15% week-over-week, short XLI Exit: After 8 trading days or when weekly volume rebounds >5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume (TEU) via port_container_volume adapter for top 5 US ports, weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Post-holiday liquidation, seasonal demand shifts, and supply-chain corrections produce >15% weekly swings 2–4 times annually.

## Required Keys
- None
