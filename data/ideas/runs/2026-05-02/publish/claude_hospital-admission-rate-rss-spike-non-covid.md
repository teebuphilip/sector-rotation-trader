# Hospital Admission Rate Rss Spike Non-covid

**Idea ID:** `hospital-admission-rate-rss-spike-non-covid`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Sudden spikes in RSS mentions of hospital admission surges (>2x rolling average) signal seasonal flu, RSV, or accident clusters, driving healthcare utilization and equipment demand. Hospital admission surges boost pharmaceutical demand, diagnostic testing, and medical device utilization—benefiting healthcare sector.

## Universe
- XLV

## Data Sources
- RSS feeds from health department and hospital network news mentioning 'admission surge' or 'bed occupancy'

## Signal Logic
If daily RSS count for hospital admission-related terms exceeds 2x the 20-day rolling median

## Entry / Exit
Entry: If daily RSS count for hospital admission-related terms exceeds 2x the 20-day rolling median Exit: After 8 trading days or when RSS mention count returns to rolling baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feeds from health department and hospital network news mentioning 'admission surge' or 'bed occupancy' via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal flu/RSV surges occur Oct-Mar annually; unexpected accident clusters and disease spikes trigger signals 4-6 times per year.

## Required Keys
- None
