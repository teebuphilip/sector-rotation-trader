# Restaurant Expansion Announcement Clustering

**Idea ID:** `restaurant-expansion-announcement-clustering`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of restaurant expansion announcements signal optimistic consumer outlook, real estate availability, and labor market confidence—bullish signals for consumer discretionary and hospitality. Restaurant expansion waves signal consumer confidence, foot traffic expectations, and real estate market health.

## Universe
- XLY

## Data Sources
- RSS feed count for 'restaurant chain opening', 'new restaurant location announcement', 'restaurant franchise expansion' via rss_count adapter

## Signal Logic
If daily RSS count for restaurant expansion announcements exceeds 10 for 3 consecutive days, go long XLY

## Entry / Exit
Entry: If daily RSS count for restaurant expansion announcements exceeds 10 for 3 consecutive days, go long XLY Exit: After 3 weeks or if daily RSS count falls below 6 for 5 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count for 'restaurant chain opening', 'new restaurant location announcement', 'restaurant franchise expansion' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Quarterly earnings announcements and franchise disclosure documents release expansion plans in clusters; seasonal tourism and holiday planning drive announcement waves regularly.

## Required Keys
- None
