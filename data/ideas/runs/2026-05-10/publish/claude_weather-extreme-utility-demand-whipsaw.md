# Weather Extreme Utility Demand Whipsaw

**Idea ID:** `weather-extreme-utility-demand-whipsaw`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Extreme temperature swings (>15°F deviation from seasonal normal across multiple regions) drive sudden utility demand spikes and grid stress, boosting energy and utilities sector volatility. Weather extremes force emergency grid operations and spot market pricing spikes, benefiting utilities operators.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature extremes (max/min) for top 20 US metros, aggregated deviation from 30-year normal

## Signal Logic
If 8+ metros show temperature deviation >15°F from 30-year normal on same day, enter long utilities

## Entry / Exit
Entry: If 8+ metros show temperature deviation >15°F from 30-year normal on same day, enter long utilities Exit: Exit after 6 trading days or if temperature volatility normalizes (deviations <8°F for 3 consecutive days)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature extremes (max/min) for top 20 US metros, aggregated deviation from 30-year normal via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Synchronized multi-region temperature extremes occur 8–12 times per year; seasonal transitions (spring/fall) generate daily crossings.

## Required Keys
- None
