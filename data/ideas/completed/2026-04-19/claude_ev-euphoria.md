# Ev Euphoria

**Idea ID:** `ev-euphoria`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Growth in the number of public EV charging stations can signal increasing adoption of electric vehicles and related industries. EV adoption is a key driver for the consumer discretionary sector.

## Universe
- XLY

## Data Sources
- OpenChargeMap daily EV charging station counts through openchargemap adapter

## Signal Logic
If the daily count of EV charging stations increases more than 1% from the prior 30-day average

## Entry / Exit
Entry: If the daily count of EV charging stations increases more than 1% from the prior 30-day average Exit: After 5 trading days or once the count falls back to the prior 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily EV charging station counts through openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charging station growth often exhibits regular weekly and monthly patterns, with deviations from typical ranges.

## Required Keys
- None
