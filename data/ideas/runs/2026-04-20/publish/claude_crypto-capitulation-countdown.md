# Crypto Capitulation Countdown

**Idea ID:** `crypto-capitulation-countdown`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Cryptocurrency prices often experience sharp sell-offs in times of market stress, signaling a broader retreat from risk assets. Cryptocurrencies are a high-risk, high-volatility asset class that is tightly correlated with technology and consumer discretionary stocks.

## Universe
- XLC

## Data Sources
- Yahoo Finance daily prices for BTC-USD and SPY through price_only adapter

## Signal Logic
If BTC-USD closes down more than 5% for 3 consecutive days

## Entry / Exit
Entry: If BTC-USD closes down more than 5% for 3 consecutive days Exit: After 7 trading days or once BTC-USD outperforms SPY by 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for BTC-USD and SPY through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cryptocurrency markets are known for their volatility, and sharp selloffs often occur in times of broader market stress or uncertainty.

## Required Keys
- None
