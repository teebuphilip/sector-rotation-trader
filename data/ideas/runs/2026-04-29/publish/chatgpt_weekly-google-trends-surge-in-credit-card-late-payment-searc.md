# Weekly Google Trends Surge In Credit Card Late Payment Searches Signals Bearish Financials

**Idea ID:** `weekly-google-trends-surge-in-credit-card-late-payment-searc`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in late payment issues signals increasing consumer financial stress, pressuring financial sector credit quality. Higher late payments increase credit losses and risk for financial companies.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short on XLF if weekly Google Trends for 'credit card late payment' rises 20%+ week-over-week

## Entry / Exit
Entry: Enter short on XLF if weekly Google Trends for 'credit card late payment' rises 20%+ week-over-week Exit: Exit after 4 weeks or if search interest declines 10% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Consumer financial stress indicators fluctuate seasonally and with economic conditions.

## Required Keys
- None
