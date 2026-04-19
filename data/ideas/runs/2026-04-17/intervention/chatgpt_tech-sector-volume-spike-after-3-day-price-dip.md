# Tech Sector Volume Spike After 3-day Price Dip

**Idea ID:** `tech-sector-volume-spike-after-3-day-price-dip`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
After a 3-day consecutive decline in XLK price, a sudden volume surge signals a potential short-term rebound. High volume after brief selloff often indicates institutional buying in tech.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily prices and volume for XLK through price_only adapter

## Signal Logic
If XLK price falls 3 days in a row and on day 4 volume increases by 50% vs 10-day average

## Entry / Exit
Entry: If XLK price falls 3 days in a row and on day 4 volume increases by 50% vs 10-day average Exit: After 7 trading days or price gains 5%, whichever comes first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices and volume for XLK through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: 3-day pullbacks followed by volume spikes occur regularly in tech ETFs.

## Required Keys
- None
