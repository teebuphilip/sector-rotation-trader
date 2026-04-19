# Xlre Daily New Ev Charger Installations Spike

**Idea ID:** `xlre-daily-new-ev-charger-installations-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Surges in new EV charger installations signal rising real estate demand for commercial charging infrastructure. Real estate related to EV infrastructure benefits from installation growth.

## Universe
- XLRE

## Data Sources
- Openchargemap daily EV charger counts aggregated nationally

## Signal Logic
Enter long if daily new charger installs increase by more than 30% versus 7-day average

## Entry / Exit
Entry: Enter long if daily new charger installs increase by more than 30% versus 7-day average Exit: Exit after 10 trading days or if installs revert

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Openchargemap daily EV charger counts aggregated nationally via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger rollout is accelerating and often shows short bursts of installation surges.

## Required Keys
- None
