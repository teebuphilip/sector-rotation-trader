# Consumer Staples Relative Weakness Reversion

**Idea ID:** `consumer-staples-relative-weakness-reversion`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLP underperforms SPY by 2%+ over 7 trading days while VIX remains <20, it signals defensive crowding followed by tactical rotation back to beaten-down risk assets. Staples underperformance in low-VIX environments typically reverts as risk appetite returns.

## Universe
- XLP

## Data Sources
- Yahoo Finance daily returns for XLP and SPY via price_only adapter

## Signal Logic
If XLP lags SPY by >2% over 7 days AND VIX <20 AND XLP shows intra-day bounce

## Entry / Exit
Entry: If XLP lags SPY by >2% over 7 days AND VIX <20 AND XLP shows intra-day bounce Exit: After 6 trading days or when XLP outperforms SPY over 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily returns for XLP and SPY via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Staples/market relative weakness occurs in 40% of rolling 7-day windows; frequent tactical reversal opportunity.

## Required Keys
- None
