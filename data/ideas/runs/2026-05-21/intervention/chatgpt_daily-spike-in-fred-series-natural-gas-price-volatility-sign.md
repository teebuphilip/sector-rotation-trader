# Daily Spike In Fred Series Natural Gas Price Volatility Signals Energy Sector Stress

**Idea ID:** `daily-spike-in-fred-series-natural-gas-price-volatility-sign`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sharp daily swings in natural gas prices indicate energy market volatility and supply concerns. Energy sector valuation is sensitive to input price volatility and supply risk.

## Universe
- XLE

## Data Sources
- FRED daily natural gas prices

## Signal Logic
Enter short when daily natural gas price change exceeds 5% absolute move

## Entry / Exit
Entry: Enter short when daily natural gas price change exceeds 5% absolute move Exit: Exit after 5 trading days or when volatility subsides below 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED daily natural gas prices via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Natural gas prices routinely exhibit sharp moves due to weather, geopolitical events, and inventory reports.

## Required Keys
- None
