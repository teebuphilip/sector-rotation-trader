# Electricity Demand Spike During Extreme Cold Snap Triggers Utility Sector Rally

**Idea ID:** `electricity-demand-spike-during-extreme-cold-snap-triggers-u`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Winter temperature drops below -10°F in major grid regions cause residential heating demand surge, pushing electricity consumption to seasonal highs. Utilities benefit from higher utilization and pricing. Utilities are the direct beneficiary of sustained high electricity demand driven by heating needs.

## Universe
- XLU

## Data Sources
- EIA electricity demand weekly series through eia_electricity adapter

## Signal Logic
When weekly EIA total electricity demand increases 8% or more week-over-week AND temperature data shows 3+ consecutive days below -5°F in Northeast or Midwest

## Entry / Exit
Entry: When weekly EIA total electricity demand increases 8% or more week-over-week AND temperature data shows 3+ consecutive days below -5°F in Northeast or Midwest Exit: After 10 trading days or when weekly demand falls back below 2% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA electricity demand weekly series through eia_electricity adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Winter months (Dec-Feb) reliably produce multiple cold snaps with multi-week demand surges. EIA data updates weekly and extreme weather is seasonal and predictable.

## Required Keys
- None
