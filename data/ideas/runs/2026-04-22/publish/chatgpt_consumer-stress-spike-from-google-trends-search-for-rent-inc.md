# Consumer Stress Spike From Google Trends Search For Rent Increase Notice

**Idea ID:** `consumer-stress-spike-from-google-trends-search-for-rent-inc`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in rent increase searches indicates rising consumer cost pressure and potential discretionary spending cutbacks. Higher housing costs reduce disposable income for discretionary purchases.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'rent increase notice'

## Signal Logic
If weekly search interest rises by 15% over prior 2 weeks

## Entry / Exit
Entry: If weekly search interest rises by 15% over prior 2 weeks Exit: After 4 weeks or if search interest falls below 5% gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'rent increase notice' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Rent-related stress is common and tends to surge around lease renewal seasons.

## Required Keys
- None
