# Rss News Volume Spike On Corporate Bond Downgrades Signals Credit Stress Rotation

**Idea ID:** `rss-news-volume-spike-on-corporate-bond-downgrades-signals-c`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily spike in downgrade-related news articles (>150% of 20-day average) predicts 3-5 day financials sector weakness as credit risk reprices. Downgrade news cascades trigger flight-to-quality and de-risking in credit-sensitive financials.

## Universe
- XLF

## Data Sources
- RSS feed counts mentioning 'credit downgrade' OR 'bond rating cut' through rss_count adapter

## Signal Logic
When daily RSS count exceeds 150% of 20-day moving average for 'credit downgrade' keywords

## Entry / Exit
Entry: When daily RSS count exceeds 150% of 20-day moving average for 'credit downgrade' keywords Exit: After 5 trading days or when RSS count normalizes below 110% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts mentioning 'credit downgrade' OR 'bond rating cut' through rss_count adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Credit events and rating changes occur multiple times per month across corporate universe; news spikes reliably follow.

## Required Keys
- None
