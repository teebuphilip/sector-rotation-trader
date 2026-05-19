# Vix-to-realized Volatility Contraction Signals Mean Reversion Opportunity In Large Caps

**Idea ID:** `vix-to-realized-volatility-contraction-signals-mean-reversio`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When VIX futures curve inverts (short-term > long-term) while 20-day realized vol on SPY is <50% of VIX level, market is overpricing tail risk; mean reversion long bias. Volatility contraction and fear premium collapse drive equity risk appetite rotation into growth and technology.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily prices for SPY and VIX close through price_only adapter

## Signal Logic
When VIX closes >15% above 20-day realized volatility of SPY and VIX is in top quartile of 252-day range

## Entry / Exit
Entry: When VIX closes >15% above 20-day realized volatility of SPY and VIX is in top quartile of 252-day range Exit: When VIX-to-realized ratio normalizes to median or after 7 trading days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for SPY and VIX close through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Volatility term structure inversions and fear premium spikes occur 2-3 times per month in normal market regimes.

## Required Keys
- None
