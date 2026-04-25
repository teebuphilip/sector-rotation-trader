# Weekly Surge In Google Trends Searches For Bankruptcy Lawyer Signals Bearish Xlf

**Idea ID:** `weekly-surge-in-google-trends-searches-for-bankruptcy-lawyer`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An uptick in bankruptcy lawyer searches indicates rising consumer financial distress, pressuring financial institutions. Higher consumer stress predicts increased loan defaults hitting financial sector earnings.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'bankruptcy lawyer'

## Signal Logic
Enter short XLF if weekly search interest rises 15% week-over-week

## Entry / Exit
Entry: Enter short XLF if weekly search interest rises 15% week-over-week Exit: Exit after 3 weeks or if searches decline 10% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'bankruptcy lawyer' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Consumer financial distress topics cycle frequently with monthly and quarterly reporting.

## Required Keys
- None
