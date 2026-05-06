# Weekly Google Trends Surge In Searches For Diesel Fuel Price Increase

**Idea ID:** `weekly-google-trends-surge-in-searches-for-diesel-fuel-price`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising consumer interest in diesel fuel price hikes signals growing input cost pressures on transport and industrial sectors. Input cost pressure hurts industrial profitability and margins.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches for 'diesel fuel price increase' rise more than 20% week-over-week

## Entry / Exit
Entry: If weekly searches for 'diesel fuel price increase' rise more than 20% week-over-week Exit: After 4 weeks or when growth slows below 5%

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
- Why It Should Fire Soon: Fuel price concerns fluctuate with global oil price volatility and seasonal demand shifts.

## Required Keys
- None
