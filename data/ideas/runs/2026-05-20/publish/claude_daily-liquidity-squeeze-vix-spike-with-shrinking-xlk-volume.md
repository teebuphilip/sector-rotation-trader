# Daily Liquidity Squeeze Vix Spike With Shrinking Xlk Volume

**Idea ID:** `daily-liquidity-squeeze-vix-spike-with-shrinking-xlk-volume`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
VIX spikes paired with collapsing tech sector volume signal forced liquidations and panic; precedes sharp mean-reversion bounces in growth stocks. Panic-driven tech sector volume collapses often reverse sharply as liquidity dries up and forced sellers capitulate; mean reversion opportunity.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily VIX, SPY, XLK prices and volume via price_only adapter

## Signal Logic
When VIX rises 25% above prior close AND XLK volume falls 30% below 20-day average on same day

## Entry / Exit
Entry: When VIX rises 25% above prior close AND XLK volume falls 30% below 20-day average on same day Exit: After 5 trading days or once VIX falls 10% from spike close

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily VIX, SPY, XLK prices and volume via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Market panic events with liquidity drains occur regularly during equity sell-offs; fires 1–2 times per month during volatile regimes.

## Required Keys
- None
