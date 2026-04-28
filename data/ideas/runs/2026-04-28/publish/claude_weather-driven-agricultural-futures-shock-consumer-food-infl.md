# Weather-driven Agricultural Futures Shock Consumer Food Inflation

**Idea ID:** `weather-driven-agricultural-futures-shock-consumer-food-infl`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When grain belt precipitation falls >50% below normal for 14+ consecutive days AND FRED agricultural commodity indices spike >2.5% in a single week, food input costs surge. Consumer staples pricing power tested. Food inflation pressures staples consumers; if staples raise prices too much, volume declines. If they absorb costs, margins compress. Either way, equity returns suffer.

## Universe
- XLP

## Data Sources
- Open-Meteo precipitation and temperature daily data for US grain belt; cross-reference FRED agricultural commodity prices weekly

## Signal Logic
Grain belt precip <50% of 30-year normal for 14+ days AND ag commodity index +2.5% weekly

## Entry / Exit
Entry: Grain belt precip <50% of 30-year normal for 14+ days AND ag commodity index +2.5% weekly Exit: Precip rebounds to >70% normal or commodity index declines >1% or 20 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo precipitation and temperature daily data for US grain belt; cross-reference FRED agricultural commodity prices weekly via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal dry spells and commodity spikes occur predictably; signal fires 3–5 times per year, especially during growing season (May–August).

## Required Keys
- None
