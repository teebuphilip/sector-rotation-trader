# Weekly Jump In Google Trends For Small Business Layoffs Signals Consumer Discretionary Downturn

**Idea ID:** `weekly-jump-in-google-trends-for-small-business-layoffs-sign`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for small business layoffs reflect stress in the labor market at the local level, often preceding reduced consumer spending. Small business layoffs indicate consumer income pressure and likely reduced discretionary spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends interest for 'small business layoffs' increases by more than 20% vs prior 4-week average

## Entry / Exit
Entry: If weekly Google Trends interest for 'small business layoffs' increases by more than 20% vs prior 4-week average Exit: After 6 weeks or when interest falls below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor stress signals on Google Trends for layoffs often spike multiple times a year in reaction to economic shifts.

## Required Keys
- None
