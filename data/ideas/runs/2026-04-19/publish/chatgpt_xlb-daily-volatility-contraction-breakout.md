# Xlb Daily Volatility Contraction Breakout

**Idea ID:** `xlb-daily-volatility-contraction-breakout`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Periods of low volatility contraction in materials ETFs often precede explosive directional moves. Breakouts from volatility compression signal new trends in materials stocks.

## Universe
- XLB

## Data Sources
- Yahoo Finance daily price volatility for XLB

## Signal Logic
Enter long when 10-day volatility drops below 50% of 60-day volatility and next day price breaks above prior 5-day high

## Entry / Exit
Entry: Enter long when 10-day volatility drops below 50% of 60-day volatility and next day price breaks above prior 5-day high Exit: Exit after 10 days or if price closes below 5-day low

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily price volatility for XLB via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Volatility contractions and breakouts occur regularly in XLB throughout the year.

## Required Keys
- None
