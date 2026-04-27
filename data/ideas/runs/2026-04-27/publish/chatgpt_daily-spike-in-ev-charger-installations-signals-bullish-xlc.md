# Daily Spike In Ev Charger Installations Signals Bullish Xlc

**Idea ID:** `daily-spike-in-ev-charger-installations-signals-bullish-xlc`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid increases in EV charger installations indicate accelerating EV adoption and infrastructure build-out, benefiting communication and tech sectors. EV infrastructure growth supports tech and communication sectors through increased demand for related services.

## Universe
- XLC

## Data Sources
- OpenChargeMap daily EV charger counts

## Signal Logic
Enter long if daily EV charger counts increase by more than 10% day-over-day

## Entry / Exit
Entry: Enter long if daily EV charger counts increase by more than 10% day-over-day Exit: Exit after 10 trading days or when daily increases fall below 3%

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
- Why It Should Fire Soon: EV infrastructure expansions occur frequently as new projects come online.

## Required Keys
- None
