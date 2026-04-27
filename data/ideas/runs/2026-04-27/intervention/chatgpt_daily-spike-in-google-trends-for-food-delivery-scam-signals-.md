# Daily Spike In Google Trends For Food Delivery Scam Signals Bearish Xly

**Idea ID:** `daily-spike-in-google-trends-for-food-delivery-scam-signals-`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increasing searches for food delivery scams reflect consumer distrust and negative sentiment impacting discretionary spending. Consumer skepticism on food delivery can reduce usage and revenue for discretionary consumption.

## Universe
- XLY

## Data Sources
- Google Trends daily data for 'food delivery scam'

## Signal Logic
Enter short if daily search interest rises 50%+ day-over-day

## Entry / Exit
Entry: Enter short if daily search interest rises 50%+ day-over-day Exit: Exit after 5 trading days or when interest falls below 3-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily data for 'food delivery scam' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer trust issues and scams flare periodically causing search spikes.

## Required Keys
- None
