# Industrial Metals Price Momentum Divergence Snap

**Idea ID:** `industrial-metals-price-momentum-divergence-snap`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLB momentum diverges negatively from copper price momentum over 10 days (copper rises, XLB lags by 2%+), mean reversion in materials leadership typically snaps back within 5-8 trading days. Materials sector catches up to commodity price strength after brief momentum lag, driven by margin expansion expectations.

## Universe
- XLB

## Data Sources
- Yahoo Finance daily prices for XLB (materials ETF) and spot copper (via price_only adapter) plus FRED industrial production index

## Signal Logic
If copper outperforms XLB by 2%+ over 10 days and volatility is rising, enter long XLB

## Entry / Exit
Entry: If copper outperforms XLB by 2%+ over 10 days and volatility is rising, enter long XLB Exit: Exit after 8 trading days or if divergence widens beyond 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLB (materials ETF) and spot copper (via price_only adapter) plus FRED industrial production index via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commodity and equity momentum divergences are common during risk-on/risk-off cycles; 2%+ divergences occur every 2-3 weeks.

## Required Keys
- None
