# Weather-driven Utility Demand Spike

**Idea ID:** `weather-driven-utility-demand-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Extreme heat or cold days significantly above/below seasonal average drive peak electricity and natural gas demand, improving utility operating margins and signaling commodity pressure. Peak demand days increase revenue and earnings potential for utility operators; commodity hedges also improve pricing power.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature and humidity for major US metros; compare to 10-year seasonal norms

## Signal Logic
If temperature deviation exceeds +15°F or -15°F from 10-year daily average in 3+ major metros simultaneously

## Entry / Exit
Entry: If temperature deviation exceeds +15°F or -15°F from 10-year daily average in 3+ major metros simultaneously Exit: Exit after 5 trading days or when temperatures normalize within ±5°F of seasonal average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature and humidity for major US metros; compare to 10-year seasonal norms via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal temperature extremes occur regularly; winter and summer spike seasons guarantee multiple triggering events per month.

## Required Keys
- None
