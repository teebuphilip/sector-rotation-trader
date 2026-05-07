# Weekly Surge In Consumer Stress Google Trends For Credit Card Maxed Out Boosts Financial Sector Caution

**Idea ID:** `weekly-surge-in-consumer-stress-google-trends-for-credit-car`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches indicate increasing consumer credit stress which can pressure banks. Worsening consumer credit conditions often reduce banking sector profitability.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'credit card maxed out'

## Signal Logic
Enter short XLF if weekly search interest exceeds 20% above 8-week moving average

## Entry / Exit
Entry: Enter short XLF if weekly search interest exceeds 20% above 8-week moving average Exit: Exit after 4 weeks or when search interest drops below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'credit card maxed out' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Consumer credit stress fluctuates frequently with macroeconomic news and policy shifts.

## Required Keys
- None
