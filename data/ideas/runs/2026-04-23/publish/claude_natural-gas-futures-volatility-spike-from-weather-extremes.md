# Natural Gas Futures Volatility Spike From Weather Extremes

**Idea ID:** `natural-gas-futures-volatility-spike-from-weather-extremes`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Extreme temperature swings (heating/cooling demand shocks) drive natural gas price spikes. When daily temp anomaly exceeds ±2 standard deviations AND UNG volume surges 40% above 20-day average, supply anxiety triggers bullish energy positioning. Natural gas is a primary energy input; supply stress immediately lifts integrated energy and downstream utility hedges.

## Universe
- XLE

## Data Sources
- Open-Meteo daily temperature anomalies (5-day rolling avg deviation from 30-year baseline) plus Yahoo Finance UNG daily close via price_only adapter

## Signal Logic
When 5-day rolling temp anomaly exceeds ±2σ AND UNG volume > 1.4× 20-day MA AND UNG closes up >2% on the day

## Entry / Exit
Entry: When 5-day rolling temp anomaly exceeds ±2σ AND UNG volume > 1.4× 20-day MA AND UNG closes up >2% on the day Exit: After 7 calendar days OR when temp anomaly returns to within ±1σ for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature anomalies (5-day rolling avg deviation from 30-year baseline) plus Yahoo Finance UNG daily close via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal weather swings occur reliably; temperature anomalies cross 2σ multiple times per quarter in most climates.

## Required Keys
- None
