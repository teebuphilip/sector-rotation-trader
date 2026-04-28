# Weekly Google Trends Surge In Energy Bill Shock Signals Consumer Stress Impacting Utilities

**Idea ID:** `weekly-google-trends-surge-in-energy-bill-shock-signals-cons`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for energy bill shock point to consumer cost pressure that can depress discretionary spending but support utilities demand. Utilities sector typically benefits as consumers prioritize essential services amid stress.

## Universe
- XLU

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLU if weekly search interest for 'energy bill shock' rises 20% week-over-week

## Entry / Exit
Entry: Enter long XLU if weekly search interest for 'energy bill shock' rises 20% week-over-week Exit: Exit after 4 weeks or if search interest declines by 15% week-over-week

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
- Why It Should Fire Soon: Energy cost concerns ebb and flow seasonally and with price volatility, causing repeated search spikes.

## Required Keys
- None
