# Electric Vehicle Charger Count Surge Impacts Tech Sector

**Idea ID:** `electric-vehicle-charger-count-surge-impacts-tech-sector`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid daily increases in EV charging infrastructure correlate with tech sector bullishness due to EV tech exposure. Growth in EV infrastructure signals expanding tech adoption in automotive and energy.

## Universe
- XLK

## Data Sources
- OpenChargeMap daily EV charger counts combined with XLK prices

## Signal Logic
If daily EV charger count increases >2% vs prior day for 3 consecutive days

## Entry / Exit
Entry: If daily EV charger count increases >2% vs prior day for 3 consecutive days Exit: After 7 trading days or 4% XLK gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily EV charger counts combined with XLK prices via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger buildouts have ongoing daily growth with occasional surges.

## Required Keys
- None
