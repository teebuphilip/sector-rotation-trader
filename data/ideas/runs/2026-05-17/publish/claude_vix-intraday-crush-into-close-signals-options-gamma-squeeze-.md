# Vix Intraday Crush Into Close Signals Options Gamma Squeeze Bounce

**Idea ID:** `vix-intraday-crush-into-close-signals-options-gamma-squeeze-`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When VIX drops >15% from intraday high to close (gamma squeeze), options dealers are forced to buy equity hedges into close, triggering a momentum bounce the next day. Gamma-driven rallies lift risk appetite; consumer discretionary and growth sectors lead the bounce.

## Universe
- XLY

## Data Sources
- Yahoo Finance intraday VIX price (^VIX) via price_only adapter, 15-minute bars

## Signal Logic
VIX intraday high to close decline >15%; SPY closes flat or down; buy SPY at close

## Entry / Exit
Entry: VIX intraday high to close decline >15%; SPY closes flat or down; buy SPY at close Exit: SPY closes up >0.8% from entry or 3 trading days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance intraday VIX price (^VIX) via price_only adapter, 15-minute bars via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: VIX intraday volatility and gamma squeezes occur 2–4 times per week on average.

## Required Keys
- None
