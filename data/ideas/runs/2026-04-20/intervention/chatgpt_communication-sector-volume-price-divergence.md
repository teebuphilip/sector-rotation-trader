# Communication Sector Volume-price Divergence

**Idea ID:** `communication-sector-volume-price-divergence`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
If volume increases 25%+ compared to 20-day average but price falls less than 0.3%, it often signals accumulation ahead of a bullish move. Volume rises without price decline suggest buying interest in communication stocks.

## Universe
- XLC

## Data Sources
- Yahoo Finance daily volume and price for XLC

## Signal Logic
Enter long XLC when daily volume >125% of 20-day average and price change between -0.3% and +0.3%

## Entry / Exit
Entry: Enter long XLC when daily volume >125% of 20-day average and price change between -0.3% and +0.3% Exit: Exit after 6 trading days or if price falls 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily volume and price for XLC via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Volume-price divergence is a common short-term pattern in XLC.

## Required Keys
- None
