# Weekly Unusual Jump In Ev Charger New Installations

**Idea ID:** `weekly-unusual-jump-in-ev-charger-new-installations`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sudden rapid increases in EV charger installations reflect accelerated local EV adoption trends impacting energy and tech sectors. Communication and tech sectors benefit from increased EV infrastructure adoption and related innovation.

## Universe
- XLC

## Data Sources
- OpenChargeMap daily EV charger installation counts aggregated weekly

## Signal Logic
Enter long XLC when weekly new charger installations increase >30% WoW

## Entry / Exit
Entry: Enter long XLC when weekly new charger installations increase >30% WoW Exit: Exit after 4 weeks or when growth slows below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily EV charger installation counts aggregated weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger install rates have multiple bursts aligned with policy announcements or incentives.

## Required Keys
- None
