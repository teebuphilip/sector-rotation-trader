# Healthcare Cost Sentiment Rss News Volume Spike Volatility Play

**Idea ID:** `healthcare-cost-sentiment-rss-news-volume-spike-volatility-p`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS news mentions of healthcare costs, drug prices, or insurance premiums spike 60%+ above rolling 30-day average, it signals public outcry and policy risk; XLV volatility spikes 20%+. Sudden healthcare cost sentiment surges trigger regulatory risk fears and sector repricing; short-term volatility crushes buyer confidence.

## Universe
- XLV

## Data Sources
- RSS feed count daily aggregation for 'healthcare cost', 'drug price', 'insurance premium' from major news sources

## Signal Logic
If daily healthcare cost RSS count spikes 60%+ above 30-day avg, short XLV or buy XLV puts.

## Entry / Exit
Entry: If daily healthcare cost RSS count spikes 60%+ above 30-day avg, short XLV or buy XLV puts. Exit: After 5 trading days or if RSS count normalizes below 20% above avg.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count daily aggregation for 'healthcare cost', 'drug price', 'insurance premium' from major news sources via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare policy news and cost debates are frequent; RSS spikes fire 2-3 times per month as political cycles and earnings events trigger discussion surges.

## Required Keys
- None
