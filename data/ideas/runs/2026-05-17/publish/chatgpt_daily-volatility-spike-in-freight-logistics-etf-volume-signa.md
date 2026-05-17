# Daily Volatility Spike In Freight Logistics Etf Volume Signals Short-term Supply Chain Stress

**Idea ID:** `daily-volatility-spike-in-freight-logistics-etf-volume-signa`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden volume and volatility spikes in freight ETFs often precede short-term supply chain adjustments. Freight and logistics sectors react quickly to supply chain stress and demand shocks.

## Universe
- XLI

## Data Sources
- Yahoo Finance daily volume and price for IYT ETF through price_only adapter

## Signal Logic
Enter short XLI if daily volume for IYT ETF spikes above 150% 20-day average and daily return volatility spikes above 2x 20-day average

## Entry / Exit
Entry: Enter short XLI if daily volume for IYT ETF spikes above 150% 20-day average and daily return volatility spikes above 2x 20-day average Exit: Exit after 3 trading days or when volume and volatility normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily volume and price for IYT ETF through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: ETF volume and volatility routinely spike due to short-term supply chain headlines.

## Required Keys
- None
