# Daily Jump In Google Trends Searches For Job Quitting Signals Labor Market Tightness Benefiting Consumer Discretionary

**Idea ID:** `daily-jump-in-google-trends-searches-for-job-quitting-signal`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising job quitting searches suggest increased worker confidence and wage pressure, which can boost consumer spending and discretionary sector demand. Tight labor markets tend to increase consumer spending power.

## Universe
- XLY

## Data Sources
- Google Trends daily queries

## Signal Logic
If daily Google Trends search volume for 'job quitting' rises by 10% compared to prior day

## Entry / Exit
Entry: If daily Google Trends search volume for 'job quitting' rises by 10% compared to prior day Exit: After 7 trading days or once search volume declines 10% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily queries via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor market chatter fluctuates daily with new reports and seasonal hiring cycles.

## Required Keys
- None
