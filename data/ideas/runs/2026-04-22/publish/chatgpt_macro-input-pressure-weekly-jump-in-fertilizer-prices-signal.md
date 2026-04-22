# Macro Input Pressure Weekly Jump In Fertilizer Prices Signals Agricultural Sector Rotation

**Idea ID:** `macro-input-pressure-weekly-jump-in-fertilizer-prices-signal`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Fertilizer price spikes often anticipate agricultural sector input cost pressures and supply chain shifts. Materials sector benefits from commodity price momentum.

## Universe
- XLB

## Data Sources
- Yahoo Finance weekly prices for major fertilizer ETFs

## Signal Logic
Enter long XLB if fertilizer ETF prices rise >8% week-over-week

## Entry / Exit
Entry: Enter long XLB if fertilizer ETF prices rise >8% week-over-week Exit: Exit after 4 weeks or when weekly gains fall below 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly prices for major fertilizer ETFs via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Fertilizer prices often jump due to seasonal and geopolitical factors.

## Required Keys
- None
