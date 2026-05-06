# Natural Gas Temperature Demand Surprise Reversal

**Idea ID:** `natural-gas-temperature-demand-surprise-reversal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When weekly heating/cooling degree day anomalies diverge sharply from natural gas consumption trends, mean reversion in energy demand and utility margins typically follows within 5-7 days. Temperature-demand mismatches resolve quickly, creating margin expansion opportunities for utilities as demand normalizes.

## Universe
- XLU

## Data Sources
- Open-Meteo daily global temperature anomaly plus FRED series GASDESW (natural gas demand) weekly through weather_series + fred_series adapters

## Signal Logic
If temperature anomaly diverges 1.5+ SD from GASDESW trend, enter long utilities on next Monday

## Entry / Exit
Entry: If temperature anomaly diverges 1.5+ SD from GASDESW trend, enter long utilities on next Monday Exit: Exit after 10 trading days or if anomaly reverses

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily global temperature anomaly plus FRED series GASDESW (natural gas demand) weekly through weather_series + fred_series adapters via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal temperature swings and demand volatility create 1.5+ SD divergences 2-3 times per quarter.

## Required Keys
- None
