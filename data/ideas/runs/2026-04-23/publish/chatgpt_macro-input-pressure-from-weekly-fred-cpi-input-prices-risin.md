# Macro Input Pressure From Weekly Fred Cpi Input Prices Rising Signals Bearish Xlp

**Idea ID:** `macro-input-pressure-from-weekly-fred-cpi-input-prices-risin`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising CPI input prices indicate cost pressures on consumer staples, squeezing margins. Higher input costs reduce profitability in staples sector.

## Universe
- XLP

## Data Sources
- FRED weekly CPI input price indices

## Signal Logic
Enter short XLP when CPI input price index rises 2%+ over prior 4 weeks

## Entry / Exit
Entry: Enter short XLP when CPI input price index rises 2%+ over prior 4 weeks Exit: Exit after 6 weeks or when index falls below 1% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly CPI input price indices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Input price indices regularly move with commodity and supply chain shifts.

## Required Keys
- None
