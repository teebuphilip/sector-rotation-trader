# Daily Spike In Rss Counts For New Industrial Safety Compliance Announcements Signals Short-term Industrial Sector Boost

**Idea ID:** `daily-spike-in-rss-counts-for-new-industrial-safety-complian`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
An increase in safety compliance news often triggers immediate industrial activity related to upgrades and equipment purchases. Industrial companies supplying safety and compliance equipment benefit from regulatory-driven demand surges.

## Universe
- XLI

## Data Sources
- RSS feed counts for industrial safety regulation announcements

## Signal Logic
Enter long XLI when daily RSS counts for industrial safety news rise 50%+ above 7-day average

## Entry / Exit
Entry: Enter long XLI when daily RSS counts for industrial safety news rise 50%+ above 7-day average Exit: Exit after 7 trading days or when counts return to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts for industrial safety regulation announcements via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regulatory announcements and related news spikes occur regularly, especially quarterly.

## Required Keys
- None
