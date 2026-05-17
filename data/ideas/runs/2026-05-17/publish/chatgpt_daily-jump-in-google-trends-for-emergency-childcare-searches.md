# Daily Jump In Google Trends For Emergency Childcare Searches Signals Labor Market Stress

**Idea ID:** `daily-jump-in-google-trends-for-emergency-childcare-searches`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising urgent childcare searches indicate acute labor supply constraints due to family care disruptions. Consumer discretionary spending suffers when labor availability and consumer confidence weaken.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'emergency childcare'

## Signal Logic
Enter short XLY if daily Google Trends for 'emergency childcare' rises 30%+ over 3-day moving average

## Entry / Exit
Entry: Enter short XLY if daily Google Trends for 'emergency childcare' rises 30%+ over 3-day moving average Exit: Exit after 7 trading days or if trend normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'emergency childcare' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Childcare issues spike frequently due to seasonal illness and school closures.

## Required Keys
- None
