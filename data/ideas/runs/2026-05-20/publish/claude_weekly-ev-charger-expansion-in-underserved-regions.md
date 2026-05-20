# Weekly Ev Charger Expansion In Underserved Regions

**Idea ID:** `weekly-ev-charger-expansion-in-underserved-regions`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Acceleration in charger deployment outside major metro areas signals government subsidy stimulation and broadening EV adoption; correlates with XLE weakness and XLK strength. Rural EV charger expansion cannibilizes traditional fuel demand and signals structural energy transition; pressures legacy energy sector valuations.

## Universe
- XLE

## Data Sources
- OpenChargeMap API weekly EV charger counts in rural and secondary markets via openchargemap adapter

## Signal Logic
When weekly EV charger count growth in non-metro regions exceeds 12% annualized rate (>0.2% per week) for 2 consecutive weeks

## Entry / Exit
Entry: When weekly EV charger count growth in non-metro regions exceeds 12% annualized rate (>0.2% per week) for 2 consecutive weeks Exit: After 20 trading days or once growth rate falls below 6% annualized

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API weekly EV charger counts in rural and secondary markets via openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Government subsidy cycles and corporate EV deployment initiatives drive regular acceleration pulses; fires 1–2 times per quarter.

## Required Keys
- None
