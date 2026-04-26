# Tech Layoff Announcement Velocity

**Idea ID:** `tech-layoff-announcement-velocity`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in tech layoff announcement frequency signal macro weakness, margin compression, and capital allocation collapse—driving sector rotation away from high-growth tech toward value. Tech layoff waves precede earnings misses, valuation compression, and reduced enterprise IT spending.

## Universe
- XLK

## Data Sources
- RSS feed count for 'technology company layoff announcement', 'tech sector hiring freeze', 'software engineer severance' via rss_count adapter

## Signal Logic
If daily RSS count for layoff announcements exceeds 12 for 2 consecutive days, short XLK

## Entry / Exit
Entry: If daily RSS count for layoff announcements exceeds 12 for 2 consecutive days, short XLK Exit: After 3 weeks or if daily RSS count remains below 6 for 10 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count for 'technology company layoff announcement', 'tech sector hiring freeze', 'software engineer severance' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Tech sector earnings cycles, macro recessions, and strategic restructuring announcements generate layoff news regularly; thresholds breach multiple times per quarter.

## Required Keys
- None
