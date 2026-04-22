# Ev Charger Density Saturation Play

**Idea ID:** `ev-charger-density-saturation-play`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Rapid week-over-week growth in EV charger deployments (>5% WoW) signals infrastructure buildout completion and maturation—near-term EV demand plateau. EV charger saturation signals slowing capex spending on charging; tech companies and EV suppliers face slower order flow.

## Universe
- XLK

## Data Sources
- OpenChargeMap daily EV charger counts by state/region through openchargemap adapter

## Signal Logic
When weekly EV charger net additions exceed prior 4-week average by ≥25%

## Entry / Exit
Entry: When weekly EV charger net additions exceed prior 4-week average by ≥25% Exit: After 8 trading days or when weekly charger additions fall below 2-week moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily EV charger counts by state/region through openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal infrastructure spending (spring/summer buildout) creates recurring charger installation spikes; 2–4 high-growth weeks per quarter.

## Required Keys
- None
