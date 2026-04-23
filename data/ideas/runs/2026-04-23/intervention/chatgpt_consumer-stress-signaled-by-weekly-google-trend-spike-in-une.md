# Consumer Stress Signaled By Weekly Google Trend Spike In Unemployment Benefits Searches Bearish Xlf

**Idea ID:** `consumer-stress-signaled-by-weekly-google-trend-spike-in-une`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest in unemployment benefits signals growing consumer financial stress, often pressuring financial sector stocks. Consumer stress reduces credit demand and loan performance, negatively affecting financials.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLF when 'unemployment benefits' searches rise 20%+ over prior 3 weeks

## Entry / Exit
Entry: Enter short XLF when 'unemployment benefits' searches rise 20%+ over prior 3 weeks Exit: Exit after 5 weeks or when searches revert below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Economic fluctuations cause frequent weekly variations in unemployment benefit searches.

## Required Keys
- None
