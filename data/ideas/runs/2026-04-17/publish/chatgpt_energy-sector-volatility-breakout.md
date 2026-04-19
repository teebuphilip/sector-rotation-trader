# Energy Sector Volatility Breakout

**Idea ID:** `energy-sector-volatility-breakout`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden jump in XLRE price volatility often signals a rapid directional move in energy-related real estate investments. Volatility spikes can indicate energy price shocks impacting the sector positively.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily XLRE prices and 10-day realized volatility via price_only adapter

## Signal Logic
If 10-day realized volatility of XLE increases more than 30% compared to prior 20-day average

## Entry / Exit
Entry: If 10-day realized volatility of XLE increases more than 30% compared to prior 20-day average Exit: After 10 trading days or 7% price gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily XLRE prices and 10-day realized volatility via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy volatility surges frequently on geopolitical or supply news.

## Required Keys
- None
