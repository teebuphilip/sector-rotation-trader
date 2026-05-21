# Ev Charger Rollout Acceleration Green Energy Sector Tailwind

**Idea ID:** `ev-charger-rollout-acceleration-green-energy-sector-tailwind`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly new EV charger installations exceed 500 units nationally or 50+ in major metro, signaling accelerated EV infrastructure buildout. Charger buildout accelerates EV adoption, reducing oil demand and signaling shift to renewable power demand; bullish for alternative energy ETFs.

## Universe
- XLE

## Data Sources
- OpenChargeMap EV charger count by US region weekly via openchargemap adapter

## Signal Logic
If weekly new charger count exceeds 500 nationally and is >20% above 12-week MA

## Entry / Exit
Entry: If weekly new charger count exceeds 500 nationally and is >20% above 12-week MA Exit: After 3 weeks or on sharp pullback in installation pace

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap EV charger count by US region weekly via openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV charger rollout accelerates in Q1 and Q3 due to federal incentive cycles; 500+ weekly installs occur monthly in expansion phases.

## Required Keys
- None
