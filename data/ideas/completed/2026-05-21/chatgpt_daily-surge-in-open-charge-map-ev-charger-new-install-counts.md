# Daily Surge In Open Charge Map Ev Charger New Install Counts Signals Auto Tech Growth

**Idea ID:** `daily-surge-in-open-charge-map-ev-charger-new-install-counts`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Accelerated EV charger installations indicate growing EV adoption and infrastructure expansion. EV infrastructure growth supports consumer discretionary auto tech and green vehicle sectors.

## Universe
- XLY

## Data Sources
- OpenChargeMap daily new EV charger counts

## Signal Logic
Enter long when daily new charger installs increase 30% above 7-day average

## Entry / Exit
Entry: Enter long when daily new charger installs increase 30% above 7-day average Exit: Exit when installs fall below 10% above 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily new EV charger counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger installation rates fluctuate with government incentives and market expansion.

## Required Keys
- None
