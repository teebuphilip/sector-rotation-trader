# Weekly Surge In Freight Logistics Google Trends Search For Rail Delays

**Idea ID:** `weekly-surge-in-freight-logistics-google-trends-search-for-r`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest signals growing rail logistics issues impacting supply chains. Rail delays hurt industrial supply chains and transportation firms.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'rail delays'

## Signal Logic
If weekly search interest is 30% higher than 4-week average

## Entry / Exit
Entry: If weekly search interest is 30% higher than 4-week average Exit: After 3 weeks or interest drops below 10% over average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'rail delays' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Rail delay concerns surge regularly with weather and labor conditions.

## Required Keys
- None
