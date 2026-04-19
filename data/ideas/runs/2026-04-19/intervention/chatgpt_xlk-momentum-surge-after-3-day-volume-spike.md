# Xlk Momentum Surge After 3-day Volume Spike

**Idea ID:** `xlk-momentum-surge-after-3-day-volume-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden 50%+ increase in trading volume over 3 days often precedes a momentum-driven price surge in technology stocks. Heavy volume signals renewed buying interest in technology sector ETFs.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily prices and volume for XLK

## Signal Logic
Enter long if 3-day average volume is at least 50% higher than prior 20-day average volume and price closes up on the 3rd day

## Entry / Exit
Entry: Enter long if 3-day average volume is at least 50% higher than prior 20-day average volume and price closes up on the 3rd day Exit: Exit after 7 trading days or if price falls below 3-day moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices and volume for XLK via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: XLK trades daily with volume variations that often surpass 50% spikes multiple times a month.

## Required Keys
- None
