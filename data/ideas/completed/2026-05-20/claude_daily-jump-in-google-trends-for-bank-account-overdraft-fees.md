# Daily Jump In Google Trends For Bank Account Overdraft Fees

**Idea ID:** `daily-jump-in-google-trends-for-bank-account-overdraft-fees`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in overdraft fee searches signal liquidity crises and account shortfalls among consumers; precedes weakness in consumer discretionary spending and loan demand. Rising overdraft searches indicate household cash flow stress and declining purchasing power; pressures discretionary sector earnings.

## Universe
- XLY

## Data Sources
- Google Trends daily search volume for 'overdraft fees', 'bank fees complaint' via google_trends adapter

## Signal Logic
When daily Google Trends search volume for overdraft-related queries spikes 50% above the 10-day rolling average

## Entry / Exit
Entry: When daily Google Trends search volume for overdraft-related queries spikes 50% above the 10-day rolling average Exit: After 6 trading days or once volume returns to within 15% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search volume for 'overdraft fees', 'bank fees complaint' via google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Bill payment cycles and paycheck timing create regular search spikes; threshold fires 2–3 times per month.

## Required Keys
- None
