# Daily Spike In Google Trends For Industrial Chemical Spill Signals Bearish Xlb

**Idea ID:** `daily-spike-in-google-trends-for-industrial-chemical-spill-s`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased searches on chemical spills reflect local industrial accidents pressuring materials sector stocks. Environmental incidents disrupt production and create regulatory risks for materials companies.

## Universe
- XLB

## Data Sources
- Google Trends daily searches

## Signal Logic
Enter short XLB if daily search interest for 'industrial chemical spill' rises 30%+ above 10-day average

## Entry / Exit
Entry: Enter short XLB if daily search interest for 'industrial chemical spill' rises 30%+ above 10-day average Exit: Exit after 7 trading days or when interest reverts

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily searches via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Industrial accidents happen regularly and cause short-term search spikes.

## Required Keys
- None
