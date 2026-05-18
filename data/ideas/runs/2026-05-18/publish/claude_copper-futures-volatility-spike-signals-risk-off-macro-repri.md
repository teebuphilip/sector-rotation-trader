# Copper Futures Volatility Spike Signals Risk-off Macro Repricing

**Idea ID:** `copper-futures-volatility-spike-signals-risk-off-macro-repri`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Copper volatility spikes often precede broad industrial and emerging market stress, as copper is a leading macroeconomic risk proxy due to its use in construction and manufacturing. High copper volatility signals macro uncertainty, reducing industrial capex and equipment demand.

## Universe
- XLI

## Data Sources
- Copper futures daily prices and 20-day volatility through price_only adapter

## Signal Logic
If 20-day copper futures volatility rises 40% or more above its 60-day MA, short XLI.

## Entry / Exit
Entry: If 20-day copper futures volatility rises 40% or more above its 60-day MA, short XLI. Exit: Exit after 7 trading days or when copper volatility mean-reverts below MA + 20%.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Copper futures daily prices and 20-day volatility through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Copper volatility swings 40%+ on macro headlines and Fed announcements 2–4 times per month.

## Required Keys
- None
