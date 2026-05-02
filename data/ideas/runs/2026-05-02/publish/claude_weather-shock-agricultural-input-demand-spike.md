# Weather Shock Agricultural Input Demand Spike

**Idea ID:** `weather-shock-agricultural-input-demand-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Severe drought (>2 weeks below -1.5σ precipitation) or unexpected freeze events trigger emergency demand for crop inputs, fertilizers, and irrigation—driving materials and industrial stocks. Ag input shocks drive demand for fertilizers, chemicals, and equipment—core XLB constituents.

## Universe
- XLB

## Data Sources
- Open-Meteo daily precipitation and temperature anomalies for major US agricultural regions

## Signal Logic
If 5-day rolling precipitation anomaly for Corn Belt drops below -1.5σ OR temperature swings >8°C below seasonal norm for 3+ consecutive days

## Entry / Exit
Entry: If 5-day rolling precipitation anomaly for Corn Belt drops below -1.5σ OR temperature swings >8°C below seasonal norm for 3+ consecutive days Exit: After 8 trading days or when weather normalizes toward seasonal mean

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily precipitation and temperature anomalies for major US agricultural regions via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather volatility is frequent; drought/freeze shocks occur 4-6 times per growing season across US regions.

## Required Keys
- None
