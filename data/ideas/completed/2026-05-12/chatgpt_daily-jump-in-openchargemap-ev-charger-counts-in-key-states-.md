# Daily Jump In Openchargemap Ev Charger Counts In Key States Signals Tech Sector Acceleration

**Idea ID:** `daily-jump-in-openchargemap-ev-charger-counts-in-key-states-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A daily surge in EV charger deployments reflects accelerating EV adoption and infrastructure investment, boosting tech and clean energy segments. Technology sector benefits from increased EV infrastructure and related technology deployments.

## Universe
- XLK

## Data Sources
- OpenChargeMap daily new EV charger installations by state

## Signal Logic
Enter long XLK when daily new EV charger installations rise 40%+ above 7-day average in key states

## Entry / Exit
Entry: Enter long XLK when daily new EV charger installations rise 40%+ above 7-day average in key states Exit: Exit after 7 trading days or when installations fall below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily new EV charger installations by state via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Infrastructure rollouts have bursts related to funding cycles and state initiatives.

## Required Keys
- None
