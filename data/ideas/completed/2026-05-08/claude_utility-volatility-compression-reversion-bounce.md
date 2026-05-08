# Utility Volatility Compression Reversion Bounce

**Idea ID:** `utility-volatility-compression-reversion-bounce`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLU 20-day realized volatility drops below 10% (multi-year low for defensive sector), and the ETF declines 3%+ from recent 20-day high, mean-reversion bias favors 5-10 day bullish rebounds as fear premiums collapse and dividend yields reactivate portfolio flows. Utilities compress during market risk-off; low volatility + small declines create mechanical dividend-capture and rotation-back-to-safety setups.

## Universe
- XLU

## Data Sources
- XLU price_only daily (volatility, drawdown, momentum via price_only adapter)

## Signal Logic
XLU 20-day volatility <10%; XLU down 3%+ from 20-day high; enter long XLU

## Entry / Exit
Entry: XLU 20-day volatility <10%; XLU down 3%+ from 20-day high; enter long XLU Exit: After 8 trading days OR if XLU 20-day volatility rises above 15%, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use XLU price_only daily (volatility, drawdown, momentum via price_only adapter) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Volatility compression in XLU occurs monthly; 3% declines are routine in market turbulence; 8-day windows capture reversion peaks; setup fires 1-2x per month.

## Required Keys
- None
