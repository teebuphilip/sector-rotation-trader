# Daily Surge In Ev Charger Installations Signals Bullish Communication Services

**Idea ID:** `daily-surge-in-ev-charger-installations-signals-bullish-comm`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid increase in new EV charger installations indicates accelerating electric vehicle adoption and related telecom infrastructure demand. EV growth drives demand for telecom and connected vehicle technologies in communication services.

## Universe
- XLC

## Data Sources
- Open-Charge-Map daily EV charger counts

## Signal Logic
Enter long on XLC if daily new EV charger installations increase by 25%+ compared to 7-day average

## Entry / Exit
Entry: Enter long on XLC if daily new EV charger installations increase by 25%+ compared to 7-day average Exit: Exit after 10 trading days or if installations fall below 7-day average

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
- Why It Should Fire Soon: EV infrastructure growth is accelerating with periodic surges.

## Required Keys
- None
