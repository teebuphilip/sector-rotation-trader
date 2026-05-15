# Ev Charger Buildout Acceleration Play

**Idea ID:** `ev-charger-buildout-acceleration-play`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rapid week-over-week growth in public EV charger deployment signals infrastructure capex cycles and local clean energy investment momentum. EV charging buildout drives industrial capex, construction jobs, and equipment orders for utilities and industrial suppliers.

## Universe
- XLI

## Data Sources
- OpenChargeMap EV charger count by state/region weekly snapshot

## Signal Logic
If weekly EV charger additions exceed 52-week median by 50% or more in any 3-state cluster

## Entry / Exit
Entry: If weekly EV charger additions exceed 52-week median by 50% or more in any 3-state cluster Exit: After 4 weeks or if weekly additions fall back to median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap EV charger count by state/region weekly snapshot via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regional infrastructure grants and utility capex cycles create recurring deployment bursts; statistically fires 2–3 times per quarter.

## Required Keys
- None
