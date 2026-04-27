# Weekly Surge In Google Trends For Office Reopening Delay Signals Bearish Xlre

**Idea ID:** `weekly-surge-in-google-trends-for-office-reopening-delay-sig`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest in office reopening delays suggests commercial real estate usage is lagging, pressuring REITs. Delayed office reopening reduces commercial real estate demand and rental income.

## Universe
- XLRE

## Data Sources
- Google Trends weekly data for 'office reopening delay'

## Signal Logic
Enter short if weekly trend rises 30%+ week-over-week

## Entry / Exit
Entry: Enter short if weekly trend rises 30%+ week-over-week Exit: Exit after 4 weeks or when trend falls below prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'office reopening delay' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Office reopening news and delays frequently shift with corporate and pandemic updates.

## Required Keys
- None
