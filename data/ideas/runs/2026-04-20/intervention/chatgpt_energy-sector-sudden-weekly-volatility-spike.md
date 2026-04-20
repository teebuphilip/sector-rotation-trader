# Energy Sector Sudden Weekly Volatility Spike

**Idea ID:** `energy-sector-sudden-weekly-volatility-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 50%+ weekly spike in realized volatility often precedes strong directional moves in energy stocks. Volatility spikes frequently lead to breakouts in energy sector prices.

## Universe
- XLE

## Data Sources
- Yahoo Finance weekly realized volatility for XLE

## Signal Logic
Enter long XLE when weekly realized volatility increases >50% compared to prior week

## Entry / Exit
Entry: Enter long XLE when weekly realized volatility increases >50% compared to prior week Exit: Exit after 3 weeks or if XLE drops 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly realized volatility for XLE via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy markets regularly experience volatility bursts tied to geopolitical and supply news.

## Required Keys
- None
