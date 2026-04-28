# Daily Spike In Rss News Counts Mentioning Labor Union Contract Talks Triggers Financial Sector Volatility

**Idea ID:** `daily-spike-in-rss-news-counts-mentioning-labor-union-contra`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden rise in news about labor union contract talks raises concerns about wage inflation and operational disruption. Financial sector sensitive to wage inflation expectations and uncertain labor conditions.

## Universe
- XLF

## Data Sources
- RSS news feed counts

## Signal Logic
Enter short XLF if daily RSS news counts on labor union contract talks rise 40% above 10-day average

## Entry / Exit
Entry: Enter short XLF if daily RSS news counts on labor union contract talks rise 40% above 10-day average Exit: Exit after 5 trading days or if news counts fall below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor contract negotiations news often intensifies and fades repeatedly during negotiation windows.

## Required Keys
- None
