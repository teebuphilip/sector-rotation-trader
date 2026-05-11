# Weekly Surge In Google Trends For Small Business Loan Default Signals Rising Local Economic Stress

**Idea ID:** `weekly-surge-in-google-trends-for-small-business-loan-defaul`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spikes in small business loan default searches indicate rising financial stress on local economies. Financial sector is exposed to credit risk from small business defaults.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLF when weekly Google Trends for 'small business loan default' rises 30%+ week-over-week

## Entry / Exit
Entry: Enter short XLF when weekly Google Trends for 'small business loan default' rises 30%+ week-over-week Exit: Exit after 4 weeks or when trend drops below 15% increase

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
- Why It Should Fire Soon: Small business financial stress fluctuates regularly with economic cycles.

## Required Keys
- None
