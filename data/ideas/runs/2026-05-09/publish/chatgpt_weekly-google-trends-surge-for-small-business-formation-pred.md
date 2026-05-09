# Weekly Google Trends Surge For Small Business Formation Predicts Consumer Discretionary Strength

**Idea ID:** `weekly-google-trends-surge-for-small-business-formation-pred`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in small business formation signals economic optimism and increased discretionary spending. Consumer discretionary stocks benefit from increased entrepreneurial activity and spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long if weekly search interest for 'small business formation' rises by 30% week-over-week

## Entry / Exit
Entry: Enter long if weekly search interest for 'small business formation' rises by 30% week-over-week Exit: Exit after 6 weeks or if interest falls 20% from peak

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
- Why It Should Fire Soon: Small business formation interest varies with economic cycles and policy news.

## Required Keys
- None
