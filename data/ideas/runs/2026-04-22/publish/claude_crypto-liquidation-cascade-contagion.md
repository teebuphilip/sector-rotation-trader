# Crypto Liquidation Cascade Contagion

**Idea ID:** `crypto-liquidation-cascade-contagion`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When crypto price drawdowns exceed 15% weekly AND liquidation search volume spikes, it signals forced selling, margin calls, and contagion risk to tech/growth. Tech and fintech firms are exposed to crypto ecosystem; crypto crashes precede tech volatility and venture funding contraction.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily Bitcoin and Ethereum volatility (price_only adapter) + Google Trends crypto liquidation mentions through google_trends adapter

## Signal Logic
When Bitcoin weekly drawdown >15% AND 'crypto liquidation' search interest exceeds 80th percentile of 13-week rolling average

## Entry / Exit
Entry: When Bitcoin weekly drawdown >15% AND 'crypto liquidation' search interest exceeds 80th percentile of 13-week rolling average Exit: After 3 trading days or when Bitcoin recovers >8% from entry signal

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily Bitcoin and Ethereum volatility (price_only adapter) + Google Trends crypto liquidation mentions through google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Crypto volatility clusters; 15% weekly drawdowns occur 3–4 times per quarter, and liquidation spikes follow predictably within 48 hours.

## Required Keys
- None
