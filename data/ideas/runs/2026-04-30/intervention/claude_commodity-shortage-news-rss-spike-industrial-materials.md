# Commodity Shortage News Rss Spike Industrial Materials

**Idea ID:** `commodity-shortage-news-rss-spike-industrial-materials`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily RSS article count for commodity shortage news rises 50%+ from 10-day moving average, signaling media focus on supply tightness. Supply shortages increase commodity prices and material producer margins; media surge precedes price moves by 1-3 weeks.

## Universe
- XLB

## Data Sources
- RSS feed count from energy, mining, and commodities news sources mentioning 'shortage' OR 'supply constraint' through rss_count adapter

## Signal Logic
If daily RSS count for 'shortage' + 'supply constraint' is 50%+ above 10-day MA and XLB volume is 20%+ above average

## Entry / Exit
Entry: If daily RSS count for 'shortage' + 'supply constraint' is 50%+ above 10-day MA and XLB volume is 20%+ above average Exit: After 8 trading days or once daily RSS count normalizes to 10-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count from energy, mining, and commodities news sources mentioning 'shortage' OR 'supply constraint' through rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Supply news cycles spike weekly; 50% threshold fires 2-3 times per month across different commodities.

## Required Keys
- None
