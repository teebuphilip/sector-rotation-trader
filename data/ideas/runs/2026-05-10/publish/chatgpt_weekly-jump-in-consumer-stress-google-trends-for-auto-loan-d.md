# Weekly Jump In Consumer Stress Google Trends For Auto Loan Default Signals Discretionary Sector Caution

**Idea ID:** `weekly-jump-in-consumer-stress-google-trends-for-auto-loan-d`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for auto loan defaults reflect growing consumer financial strain, pressuring discretionary spending. Consumer discretionary spending weakens as auto loan stress rises.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'auto loan default' via google_trends adapter

## Signal Logic
If weekly search interest rises more than 15% week-over-week

## Entry / Exit
Entry: If weekly search interest rises more than 15% week-over-week Exit: Once search interest declines below 5% week-over-week change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'auto loan default' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Consumer credit stress indicators fluctuate regularly with economic cycles.

## Required Keys
- None
