# Daily Surge In Ev Charger Installations Signals Accelerating Ev Adoption

**Idea ID:** `daily-surge-in-ev-charger-installations-signals-accelerating`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid daily growth in EV charger installations signals increasing EV infrastructure buildout and demand. Communication and tech sectors benefit from EV ecosystem growth and associated infrastructure.

## Universe
- XLC

## Data Sources
- Open-Charge-Map daily EV charger counts

## Signal Logic
Enter long XLC if daily EV charger count rises 1.5% above 7-day moving average

## Entry / Exit
Entry: Enter long XLC if daily EV charger count rises 1.5% above 7-day moving average Exit: Exit after 10 trading days or if daily installs fall below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Charge-Map daily EV charger counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger installation rates often see bursts with government incentives and private rollout phases.

## Required Keys
- None
