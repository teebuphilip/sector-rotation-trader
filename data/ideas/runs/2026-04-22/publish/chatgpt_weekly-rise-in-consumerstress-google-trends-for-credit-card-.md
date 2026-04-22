# Weekly Rise In Consumerstress Google Trends For Credit Card Hardship Indicates Financial Strain

**Idea ID:** `weekly-rise-in-consumerstress-google-trends-for-credit-card-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Elevated interest in credit card hardship reflects consumer debt stress which typically pressures discretionary spending. Consumer financial stress negatively impacts retail and discretionary sectors.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'credit card hardship'

## Signal Logic
Entry when search interest increases more than 20% week-over-week

## Entry / Exit
Entry: Entry when search interest increases more than 20% week-over-week Exit: Exit when interest declines below 5% increase or after 6 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'credit card hardship' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Credit-related search terms frequently spike with economic stress.

## Required Keys
- None
