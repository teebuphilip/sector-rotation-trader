# Daily Change In Open Charge Map Ev Charger Counts Indicates Ev Sector Momentum

**Idea ID:** `daily-change-in-open-charge-map-ev-charger-counts-indicates-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid daily increases in EV charger installations signal accelerating EV adoption momentum. EV infrastructure growth supports technology and clean energy sectors.

## Universe
- XLC

## Data Sources
- Open Charge Map daily EV charger count updates

## Signal Logic
Enter long XLC when daily EV charger count increases by 1% or more versus previous day

## Entry / Exit
Entry: Enter long XLC when daily EV charger count increases by 1% or more versus previous day Exit: Exit after 7 trading days or when daily growth falls below 0.5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open Charge Map daily EV charger count updates via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger installations grow steadily with occasional bursts from clean energy subsidies.

## Required Keys
- None
