# Daily Spike In Google Trends Searches For Home Heating System Failure Signals Winter Utility Stress

**Idea ID:** `daily-spike-in-google-trends-searches-for-home-heating-syste`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased searches for heating failures indicate household energy demand surges and potential utility sector stress. Utilities benefit from emergency heating repairs and higher winter energy consumption.

## Universe
- XLU

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily searches exceed 30% over prior 7-day average

## Entry / Exit
Entry: If daily searches exceed 30% over prior 7-day average Exit: When searches drop below 10% above 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heating system issues spike seasonally with cold weather extremes.

## Required Keys
- None
