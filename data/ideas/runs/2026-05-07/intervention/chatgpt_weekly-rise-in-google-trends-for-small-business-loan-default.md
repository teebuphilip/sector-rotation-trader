# Weekly Rise In Google Trends For Small Business Loan Default Signals Financial Sector Risk

**Idea ID:** `weekly-rise-in-google-trends-for-small-business-loan-default`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing default-related search interest indicates rising credit risk in small business lending. Small business credit stress can reduce bank loan performance and profitability.

## Universe
- XLF

## Data Sources
- Google Trends weekly searches for 'small business loan default'

## Signal Logic
Enter short XLF if weekly search interest rises 25% above 12-week average

## Entry / Exit
Entry: Enter short XLF if weekly search interest rises 25% above 12-week average Exit: Exit after 6 weeks or if search interest falls below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'small business loan default' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Credit stress indicators fluctuate regularly with economic news and policy changes.

## Required Keys
- None
