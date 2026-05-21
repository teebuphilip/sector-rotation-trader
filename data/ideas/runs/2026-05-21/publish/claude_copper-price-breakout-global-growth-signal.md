# Copper Price Breakout Global Growth Signal

**Idea ID:** `copper-price-breakout-global-growth-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Copper price breaks above 90-day high, signaling broad industrial demand recovery and infrastructure spending. Copper is the ultimate cycle barometer; breakouts correlate with capex uptake and manufacturing momentum.

## Universe
- XLI

## Data Sources
- Yahoo Finance daily copper futures (GC or equivalent proxy) via price_only adapter

## Signal Logic
If copper closes above 90-day high with 3-day average volume >median

## Entry / Exit
Entry: If copper closes above 90-day high with 3-day average volume >median Exit: After 14 days or on close below 20-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily copper futures (GC or equivalent proxy) via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Copper oscillates frequently; 90-day breakouts fire 2-3 times per month in typical volatility regimes.

## Required Keys
- None
