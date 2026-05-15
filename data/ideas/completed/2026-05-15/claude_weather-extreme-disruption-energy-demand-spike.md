# Weather Extreme Disruption Energy Demand Spike

**Idea ID:** `weather-extreme-disruption-energy-demand-spike`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Days with extreme heat/cold >2 std dev from normal drive electricity demand spikes and boost utility/energy pricing. Extreme weather drives peak electricity demand and margin expansion for utilities and power generators.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature anomaly by region + EIA electricity demand

## Signal Logic
If daily temperature anomaly >2 std dev from 20-year normal for region AND EIA electricity demand spike >8% from prior day

## Entry / Exit
Entry: If daily temperature anomaly >2 std dev from 20-year normal for region AND EIA electricity demand spike >8% from prior day Exit: Exit after 3 trading days or when temperature normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature anomaly by region + EIA electricity demand via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal temperature extremes produce 3–6 multi-day heat/cold waves annually; each fires signal reliably.

## Required Keys
- None
