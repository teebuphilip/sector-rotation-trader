# Daily Spike In Google Trends For Data Breach Class Action Signals Bearish Xlk

**Idea ID:** `daily-spike-in-google-trends-for-data-breach-class-action-si`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increasing interest in data breach lawsuits signals negative sentiment and potential regulatory risks for tech stocks. Legal and regulatory concerns weigh on technology sector valuations.

## Universe
- XLK

## Data Sources
- Google Trends daily data for 'data breach class action'

## Signal Logic
Enter short if daily search interest spikes 50%+ day-over-day

## Entry / Exit
Entry: Enter short if daily search interest spikes 50%+ day-over-day Exit: Exit after 5 trading days or when search interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily data for 'data breach class action' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Data breach legal news and class actions flare unpredictably but frequently.

## Required Keys
- None
