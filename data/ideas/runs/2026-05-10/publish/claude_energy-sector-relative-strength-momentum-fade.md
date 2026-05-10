# Energy Sector Relative Strength Momentum Fade

**Idea ID:** `energy-sector-relative-strength-momentum-fade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLE outperforms SPY by >4% over 10 days but XLE daily close falls below its 5-day moving average, mean reversion pullback often follows within days. Energy momentum exhaustion signals profit-taking and demand concerns in commodity-linked sectors.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily prices for XLE and SPY, relative strength index (XLE vs SPY 20-day momentum), price_only adapter

## Signal Logic
If XLE leads SPY >4% over 10 days AND XLE closes below 5-day MA AND MACD(12,26) turns negative, short energy

## Entry / Exit
Entry: If XLE leads SPY >4% over 10 days AND XLE closes below 5-day MA AND MACD(12,26) turns negative, short energy Exit: Exit after 6 trading days or if XLE closes above 10-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLE and SPY, relative strength index (XLE vs SPY 20-day momentum), price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy outperformance spikes >4% over 10-day windows occur 3–5 times per quarter; momentum exhaustion patterns fire weekly.

## Required Keys
- None
