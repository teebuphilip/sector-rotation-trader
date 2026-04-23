# Consumer Stress Detected By Daily Spike In Google Trends Searches For Budget Credit Cards Bearish Xlf

**Idea ID:** `consumer-stress-detected-by-daily-spike-in-google-trends-sea`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising interest in budget credit cards signals increased consumer credit stress, pressuring financial stocks. Stress in consumer credit markets reduces bank profitability.

## Universe
- XLF

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter short XLF when daily searches for 'budget credit cards' spike 50%+ over 5-day average

## Entry / Exit
Entry: Enter short XLF when daily searches for 'budget credit cards' spike 50%+ over 5-day average Exit: Exit after 7 trading days or when searches normalize below 20% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Credit stress-related search spikes occur frequently around economic news.

## Required Keys
- None
