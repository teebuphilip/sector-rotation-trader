# Weekly Google Trends Surge For Small Business Loan Default Signals Financial Sector Stress

**Idea ID:** `weekly-google-trends-surge-for-small-business-loan-default-s`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing default-related searches indicate rising credit stress in small businesses, often foreshadowing pressure on financial sector banks. Financial sector vulnerability rises with increased loan defaults and credit concerns.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short if 'small business loan default' search interest increases 25% week-over-week

## Entry / Exit
Entry: Enter short if 'small business loan default' search interest increases 25% week-over-week Exit: Exit after 5 weeks or when search interest returns near baseline

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
- Why It Should Fire Soon: Small business credit stress fluctuates with economic cycles and policy changes.

## Required Keys
- None
