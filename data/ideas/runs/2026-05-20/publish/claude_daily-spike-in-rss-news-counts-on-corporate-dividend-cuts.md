# Daily Spike In Rss News Counts On Corporate Dividend Cuts

**Idea ID:** `daily-spike-in-rss-news-counts-on-corporate-dividend-cuts`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in dividend cut announcements signal deteriorating corporate cash flow, recession expectations, and capital preservation; correlates with broad market weakness. Dividend cuts, especially from financial and dividend-reliant sectors, signal earnings stress and recession fears; pressures equity valuations.

## Universe
- XLF

## Data Sources
- RSS feed count aggregation for 'dividend cut', 'dividend suspension' across financial news via rss_count adapter

## Signal Logic
When daily RSS count for dividend-cut stories rises 45% above the 5-day rolling average

## Entry / Exit
Entry: When daily RSS count for dividend-cut stories rises 45% above the 5-day rolling average Exit: After 8 trading days or once count returns within 10% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count aggregation for 'dividend cut', 'dividend suspension' across financial news via rss_count adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Dividend cuts cluster around earnings seasons and credit stress events; fires 2–3 times per quarter.

## Required Keys
- None
