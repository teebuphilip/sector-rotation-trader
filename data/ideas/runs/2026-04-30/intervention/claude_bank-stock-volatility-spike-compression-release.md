# Bank Stock Volatility Spike Compression Release

**Idea ID:** `bank-stock-volatility-spike-compression-release`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
30-day rolling volatility on XLF drops to lowest level in 90 days, followed by close above upper Bollinger Band, signaling compression breakout. Volatility compression in financial sector often precedes relief rallies when risk appetite returns or rate environment stabilizes.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily prices and intraday volatility for XLF (Financials ETF) through price_only adapter

## Signal Logic
If XLF 30-day volatility is lowest in 90 days AND XLF closes above 20-day Bollinger upper band

## Entry / Exit
Entry: If XLF 30-day volatility is lowest in 90 days AND XLF closes above 20-day Bollinger upper band Exit: After 6 trading days or once XLF volume drops below 20-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices and intraday volatility for XLF (Financials ETF) through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Volatility compression cycles in XLF occur every 3-6 weeks; threshold fires 1-2 times per month.

## Required Keys
- None
