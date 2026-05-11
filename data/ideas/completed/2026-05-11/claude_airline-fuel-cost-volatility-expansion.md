# Airline Fuel Cost Volatility Expansion

**Idea ID:** `airline-fuel-cost-volatility-expansion`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLE 20-day volatility exceeds 25% while XLU 20-day volatility stays <15%, airline cost uncertainty spikes, pressuring airline margins and travel demand. Energy volatility without utility hedging signals fuel cost unpredictability, pressuring airline profitability and consumer travel spending.

## Universe
- XLY

## Data Sources
- Yahoo Finance daily prices for XLU (utilities) and XLE (energy) via price_only adapter; calculate rolling 20-day volatility

## Signal Logic
If XLE 20-day volatility >25% and XLU 20-day volatility <15% for 2 consecutive days

## Entry / Exit
Entry: If XLE 20-day volatility >25% and XLU 20-day volatility <15% for 2 consecutive days Exit: After 7 trading days or if XLE volatility falls to <20%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLU (utilities) and XLE (energy) via price_only adapter; calculate rolling 20-day volatility via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy volatility is structural; 20%+ spikes occur weekly during geopolitical shocks, OPEC news, or production disruptions.

## Required Keys
- None
