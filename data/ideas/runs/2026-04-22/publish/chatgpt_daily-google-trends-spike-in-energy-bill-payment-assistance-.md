# Daily Google Trends Spike In Energy Bill Payment Assistance Predicts Consumer Stress In Utilities

**Idea ID:** `daily-google-trends-spike-in-energy-bill-payment-assistance-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising searches for energy bill help indicate consumer stress, potentially pressuring utilities consumption sentiment. Consumer stress may reduce discretionary utility usage and increase payment risk.

## Universe
- XLU

## Data Sources
- Google Trends daily search interest for 'energy bill payment assistance'

## Signal Logic
Entry when daily search interest spikes more than 25% over 3-day average

## Entry / Exit
Entry: Entry when daily search interest spikes more than 25% over 3-day average Exit: Exit after 7 trading days or once interest drops below 10% spike

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'energy bill payment assistance' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Utility bill assistance searches spike frequently during seasonal stress periods.

## Required Keys
- None
