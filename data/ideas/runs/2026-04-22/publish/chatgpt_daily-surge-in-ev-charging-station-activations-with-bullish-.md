# Daily Surge In Ev Charging Station Activations With Bullish Xlc Momentum

**Idea ID:** `daily-surge-in-ev-charging-station-activations-with-bullish-`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid expansion of EV charging infrastructure signals accelerating EV adoption benefiting communications and infrastructure-related stocks. EV infrastructure growth supports communications and technology sector growth.

## Universe
- XLC

## Data Sources
- OpenChargeMap daily new EV charger activations and Yahoo Finance daily XLC prices

## Signal Logic
Enter long XLC if daily new charger activations increase >10% day-over-day and XLC outperforms SPY

## Entry / Exit
Entry: Enter long XLC if daily new charger activations increase >10% day-over-day and XLC outperforms SPY Exit: Exit after 7 trading days or if activations decline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily new EV charger activations and Yahoo Finance daily XLC prices via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charger activations are daily and often show bursts.

## Required Keys
- None
