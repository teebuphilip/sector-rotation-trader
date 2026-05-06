# Weekly Google Trends Spike For Small Business Loan Default Searches

**Idea ID:** `weekly-google-trends-spike-for-small-business-loan-default-s`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for small business loan defaults indicate growing financial stress in small business sector. Financial sector may face increased credit risk and provisioning pressure.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches for 'small business loan default' grow by more than 15% week-over-week

## Entry / Exit
Entry: If weekly searches for 'small business loan default' grow by more than 15% week-over-week Exit: After 4 weeks or when growth falls below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Small business financial distress tends to fluctuate seasonally and with economic cycles.

## Required Keys
- None
