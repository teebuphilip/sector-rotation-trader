# Ev Charging Station Stampede

**Idea ID:** `ev-charging-station-stampede`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Rapid growth in the number of public EV charging stations can signal increasing consumer adoption of electric vehicles and related infrastructure investment. EV adoption and charging infrastructure growth are closely tied to consumer discretionary spending and the future of transportation.

## Universe
- XLY

## Data Sources
- Openchargemap public EV charging station data through openchargemap adapter

## Signal Logic
If the weekly growth rate in public EV charging stations exceeds 2%

## Entry / Exit
Entry: If the weekly growth rate in public EV charging stations exceeds 2% Exit: After 2 weeks or once the growth rate falls below 1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Openchargemap public EV charging station data through openchargemap adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Adoption of electric vehicles and expansion of charging infrastructure is a long-term trend, but can exhibit periods of accelerated growth that may occur within a 30-day timeframe.

## Required Keys
- None
