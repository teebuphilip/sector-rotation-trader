# Ev Charger Installation Acceleration Play

**Idea ID:** `ev-charger-installation-acceleration-play`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When the weekly rate of new EV charger installations accelerates (week-over-week growth jumps 20%+), it signals municipal/private infrastructure spending surge; this often precedes renewable energy demand and tech equipment procurement. EV charger deployment requires semiconductors, software, and networking gear; acceleration signals tech capex cycle.

## Universe
- XLK

## Data Sources
- OpenChargeMap weekly charger count growth rate via openchargemap adapter

## Signal Logic
If weekly charger installation count growth rate jumps 20%+ above prior week AND cumulative monthly new installations exceed prior 4-week average by 25%

## Entry / Exit
Entry: If weekly charger installation count growth rate jumps 20%+ above prior week AND cumulative monthly new installations exceed prior 4-week average by 25% Exit: After 5 weeks or when growth rate decelerates below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap weekly charger count growth rate via openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger deployment is accelerating nationally; municipal funding tranches and private buildouts create monthly spikes in growth rates.

## Required Keys
- None
