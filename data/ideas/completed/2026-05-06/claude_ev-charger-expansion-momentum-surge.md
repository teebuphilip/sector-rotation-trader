# Ev Charger Expansion Momentum Surge

**Idea ID:** `ev-charger-expansion-momentum-surge`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Weekly net additions of EV chargers across North America spike when municipal/utility deployment accelerates, signaling local infrastructure confidence and consumer EV demand confidence. EV charging infrastructure expansion correlates with technology and industrial adoption cycles, benefiting semiconductor and electric vehicle ecosystem players.

## Universe
- XLK

## Data Sources
- OpenChargeMap daily EV charger count aggregation through openchargemap adapter

## Signal Logic
If weekly net EV charger additions exceed 90th percentile of trailing 12-week average, enter long on Monday open

## Entry / Exit
Entry: If weekly net EV charger additions exceed 90th percentile of trailing 12-week average, enter long on Monday open Exit: Exit after 8 trading days or if weekly net additions drop below 60th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily EV charger count aggregation through openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger deployment is volatile week-to-week and crosses the 90th percentile threshold several times per quarter, especially in spring/fall deployment seasons.

## Required Keys
- None
