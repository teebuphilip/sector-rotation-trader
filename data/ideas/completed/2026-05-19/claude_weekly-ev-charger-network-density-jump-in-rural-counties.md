# Weekly Ev Charger Network Density Jump In Rural Counties

**Idea ID:** `weekly-ev-charger-network-density-jump-in-rural-counties`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rural county EV charger deployments cluster in specific weeks as infrastructure grants roll out; rapid county-level density changes signal local economic stimulus and tech adoption momentum. Infrastructure build-out and manufacturing for EV charging hardware drives industrial production and materials demand.

## Universe
- XLI

## Data Sources
- OpenChargeMap charger counts by county through openchargemap adapter

## Signal Logic
When a county's week-over-week charger count increases by >5 net new units and density is >20% above county 52-week average

## Entry / Exit
Entry: When a county's week-over-week charger count increases by >5 net new units and density is >20% above county 52-week average Exit: After 10 trading days or when density falls below 15% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap charger counts by county through openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Federal and state EV infrastructure programs release deployment tranches in predictable waves; clusters occur 2-3 times per quarter.

## Required Keys
- None
