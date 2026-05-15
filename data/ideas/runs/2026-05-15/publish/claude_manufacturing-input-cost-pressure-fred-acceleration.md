# Manufacturing Input Cost Pressure Fred Acceleration

**Idea ID:** `manufacturing-input-cost-pressure-fred-acceleration`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Week-over-week acceleration in PPI for inputs signals rising cost pressures, which trigger equity rotation out of materials and into defensive sectors. Materials companies face margin compression when input costs accelerate faster than they can pass through prices.

## Universe
- XLB

## Data Sources
- FRED series PPI for intermediate materials (PPIICMM) weekly aggregation

## Signal Logic
If 2-week change in PPI intermediate materials exceeds the 26-week rolling average change by 0.3% or more

## Entry / Exit
Entry: If 2-week change in PPI intermediate materials exceeds the 26-week rolling average change by 0.3% or more Exit: Exit after 2 weeks or when acceleration reverses below median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series PPI for intermediate materials (PPIICMM) weekly aggregation via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: FRED PPI data releases weekly; commodity and energy volatility produce input cost swings frequently enough to trigger monthly.

## Required Keys
- None
