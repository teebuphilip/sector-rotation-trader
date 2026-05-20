# Daily Surge In Rss News Counts For Corporate Bond Downgrade Signals Credit Stress Rotation

**Idea ID:** `daily-surge-in-rss-news-counts-for-corporate-bond-downgrade-`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A spike in downgrade news signals rising credit risk perception and possible sector rotation to defensive assets. Financials can be negatively impacted by credit stress, signaling risk-off rotations.

## Universe
- XLF

## Data Sources
- RSS news feed counts

## Signal Logic
If daily RSS news counts for 'corporate bond downgrade' rise 60% vs 7-day average

## Entry / Exit
Entry: If daily RSS news counts for 'corporate bond downgrade' rise 60% vs 7-day average Exit: After 5 trading days or if news count drops below 30% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Credit rating changes and related news flow frequently spike with market volatility.

## Required Keys
- None
