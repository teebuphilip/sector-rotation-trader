# Weekly Surge In Google Trends For Inflation Hedge With Bullish Xlb Relative Strength

**Idea ID:** `weekly-surge-in-google-trends-for-inflation-hedge-with-bulli`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in inflation hedges corresponds with increased demand for basic materials and commodities. Basic materials benefit from inflation hedge demand.

## Universe
- XLB

## Data Sources
- Google Trends weekly for 'inflation hedge' and Yahoo Finance weekly XLB prices

## Signal Logic
Enter long XLB when 'inflation hedge' searches rise >20% week-over-week and XLB outperforms SPY

## Entry / Exit
Entry: Enter long XLB when 'inflation hedge' searches rise >20% week-over-week and XLB outperforms SPY Exit: Exit after 4 weeks or when search interest declines

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly for 'inflation hedge' and Yahoo Finance weekly XLB prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Inflation concerns regularly spike seasonally or in response to data.

## Required Keys
- None
