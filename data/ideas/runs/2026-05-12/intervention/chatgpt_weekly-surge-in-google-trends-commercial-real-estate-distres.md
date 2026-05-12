# Weekly Surge In Google Trends Commercial Real Estate Distress Searches Signals Bearish Real Estate Sector

**Idea ID:** `weekly-surge-in-google-trends-commercial-real-estate-distres`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising public concern about commercial real estate troubles often leads to sector price declines. Negative sentiment and distress signals weigh on commercial real estate valuations.

## Universe
- XLRE

## Data Sources
- Google Trends weekly search interest for commercial real estate distress

## Signal Logic
Enter short XLRE when weekly search interest rises 25%+ over prior week

## Entry / Exit
Entry: Enter short XLRE when weekly search interest rises 25%+ over prior week Exit: Exit after 6 weeks or when search interest falls below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for commercial real estate distress via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commercial real estate distress news and concern spikes regularly with market cycles.

## Required Keys
- None
