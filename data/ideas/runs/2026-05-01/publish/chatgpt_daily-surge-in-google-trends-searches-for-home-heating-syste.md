# Daily Surge In Google Trends Searches For Home Heating System Failure Signals Consumer Stress Impacting Utilities

**Idea ID:** `daily-surge-in-google-trends-searches-for-home-heating-syste`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased searches for heating failures reflect consumer stress and urgent repair demand impacting utilities. Higher utility usage and repair spending lift utilities sector demand.

## Universe
- XLU

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long XLU when daily search volume for 'home heating system failure' rises 50% above 7-day average

## Entry / Exit
Entry: Enter long XLU when daily search volume for 'home heating system failure' rises 50% above 7-day average Exit: Exit after 6 trading days or when volume reverts below 7-day average

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
- Why It Should Fire Soon: Heating failures spike daily during colder weather, prompting frequent signals.

## Required Keys
- None
