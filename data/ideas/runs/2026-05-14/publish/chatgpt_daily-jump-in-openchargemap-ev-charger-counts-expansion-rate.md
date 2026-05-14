# Daily Jump In Openchargemap Ev Charger Counts Expansion Rate Signals Bullish Consumer Discretionary

**Idea ID:** `daily-jump-in-openchargemap-ev-charger-counts-expansion-rate`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden acceleration in the number of new EV chargers installed signals increased EV adoption and consumer spending on EV-related products. Faster EV infrastructure growth supports higher EV sales and discretionary spending on related goods.

## Universe
- XLY

## Data Sources
- OpenChargeMap daily EV charger counts

## Signal Logic
If daily % increase in EV charger counts exceeds 0.5% over a 3-day rolling window

## Entry / Exit
Entry: If daily % increase in EV charger counts exceeds 0.5% over a 3-day rolling window Exit: After 10 trading days or when growth rate slows below 0.2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily EV charger counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily EV charger additions fluctuate regularly due to project completions and announcements.

## Required Keys
- None
