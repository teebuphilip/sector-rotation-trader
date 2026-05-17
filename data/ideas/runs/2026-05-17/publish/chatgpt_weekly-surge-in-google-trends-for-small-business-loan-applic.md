# Weekly Surge In Google Trends For Small Business Loan Applications Signals Financial Strain

**Idea ID:** `weekly-surge-in-google-trends-for-small-business-loan-applic`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An uptick in searches for small business loans indicates rising financial stress among small businesses, often preceding increased credit market activity. Financial sector ETFs often weaken with increased credit risk signals among small business borrowers.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'small business loan application'

## Signal Logic
Enter short XLF if weekly Google Trends for 'small business loan application' rises by 15%+ WoW

## Entry / Exit
Entry: Enter short XLF if weekly Google Trends for 'small business loan application' rises by 15%+ WoW Exit: Exit after 3 weeks or if the trend falls below a 10% WoW increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'small business loan application' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends for financial search terms routinely move 10-20% week-to-week.

## Required Keys
- None
