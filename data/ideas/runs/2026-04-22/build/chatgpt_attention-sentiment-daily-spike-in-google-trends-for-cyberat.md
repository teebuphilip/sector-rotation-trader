# Attention Sentiment Daily Spike In Google Trends For Cyberattack Searches Boosts Cybersecurity Etf

**Idea ID:** `attention-sentiment-daily-spike-in-google-trends-for-cyberat`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising cyberattack search interest reflects heightened threat perception, often lifting cybersecurity stocks. Cybersecurity sector benefits from elevated threat awareness.

## Universe
- XLC

## Data Sources
- Google Trends daily search interest for 'cyberattack'

## Signal Logic
Enter long XLC if daily search interest jumps >30% day-over-day and exceeds 3-day moving average

## Entry / Exit
Entry: Enter long XLC if daily search interest jumps >30% day-over-day and exceeds 3-day moving average Exit: Exit after 7 days or if search interest falls below 3-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'cyberattack' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cyberattack news causes daily search spikes multiple times per year.

## Required Keys
- None
