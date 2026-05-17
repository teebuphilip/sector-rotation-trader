# Lumber Futures Volatility Spike Signals Construction Cost Shock

**Idea ID:** `lumber-futures-volatility-spike-signals-construction-cost-sh`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Lumber prices swing sharply on housing demand shocks and forestry disruptions. A 5%+ daily move in lumber signals incoming margin pressure for homebuilders and building materials suppliers. Industrials and building-materials companies face near-term input cost inflation; the market reprices earnings downward.

## Universe
- XLI

## Data Sources
- Yahoo Finance continuous lumber futures (CL=F) daily price via price_only adapter

## Signal Logic
CL=F rises or falls >5% in a single day; simultaneously XLI closes down >0.8%

## Entry / Exit
Entry: CL=F rises or falls >5% in a single day; simultaneously XLI closes down >0.8% Exit: XLI outperforms SPY by >1% over 2 consecutive days or 10 calendar days pass

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance continuous lumber futures (CL=F) daily price via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Lumber futures exhibit >5% swings 2–4 times monthly due to weather, mills, and inventory news.

## Required Keys
- None
