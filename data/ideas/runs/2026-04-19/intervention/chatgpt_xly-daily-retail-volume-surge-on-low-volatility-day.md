# Xly Daily Retail Volume Surge On Low Volatility Day

**Idea ID:** `xly-daily-retail-volume-surge-on-low-volatility-day`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden volume spike on a day of unusually low price volatility may indicate retail accumulation before a breakout. Retail sector ETFs respond to retail investor buying interest.

## Universe
- XLY

## Data Sources
- Yahoo Finance daily volume and price data for XLY

## Signal Logic
Enter long if daily volume is 40% above 20-day average while daily price range (high-low) is below 20-day average range

## Entry / Exit
Entry: Enter long if daily volume is 40% above 20-day average while daily price range (high-low) is below 20-day average range Exit: Exit after 5 trading days or if price drops below entry price

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily volume and price data for XLY via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Such volume/volatility divergences occur frequently during retail consolidation phases.

## Required Keys
- None
