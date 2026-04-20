# Consumer Discretionary Google Trends Surge For Sale Keywords

**Idea ID:** `consumer-discretionary-google-trends-surge-for-sale-keywords`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden 15%+ weekly increase in search interest for 'sale' often correlates with rising consumer spending and positive momentum in discretionary stocks. Higher consumer interest in sales can indicate upcoming retail strength.

## Universe
- XLY

## Data Sources
- Google Trends weekly data for 'sale' keyword in US

## Signal Logic
Enter long if weekly 'sale' search interest rises more than 15% vs prior week

## Entry / Exit
Entry: Enter long if weekly 'sale' search interest rises more than 15% vs prior week Exit: Exit after 3 weeks or if XLY drops 3% from entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'sale' keyword in US via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends data frequently shows spikes in consumer interest around holidays and promotions.

## Required Keys
- None
