# Weekly Rise In Macro Input Pressure Fred Producer Price Index Spike Signals Inflation Stress

**Idea ID:** `weekly-rise-in-macro-input-pressure-fred-producer-price-inde`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A rising producer price index signals increasing input costs that pressure margins across sectors. Materials sector margins compress when input inflation spikes sharply.

## Universe
- XLB

## Data Sources
- FRED PPI monthly data

## Signal Logic
If weekly PPI increase exceeds 0.3% month-over-month

## Entry / Exit
Entry: If weekly PPI increase exceeds 0.3% month-over-month Exit: When PPI growth slows below 0.1% monthly

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED PPI monthly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: PPI data updates regularly with inflation dynamics causing repeat signals.

## Required Keys
- None
