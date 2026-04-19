# Xlf Weekly Fed Funds Rate Surprise Reaction

**Idea ID:** `xlf-weekly-fed-funds-rate-surprise-reaction`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Unexpected Fed funds rate moves often trigger rapid financial sector ETF reactions. Financial stocks react negatively to surprise rate hikes.

## Universe
- XLF

## Data Sources
- FRED weekly effective Fed funds rate data

## Signal Logic
Enter short if weekly Fed funds rate increases by more than 10 basis points unexpectedly

## Entry / Exit
Entry: Enter short if weekly Fed funds rate increases by more than 10 basis points unexpectedly Exit: Exit after 3 weeks or if XLF outperforms SPY over 5 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly effective Fed funds rate data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Fed funds data updates weekly and rate hikes can occur within 30 days.

## Required Keys
- None
