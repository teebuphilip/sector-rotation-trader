# Weekly Spike In Google Trends For Corporate Layoff Announcement Searches Signals Labor Market Weakness

**Idea ID:** `weekly-spike-in-google-trends-for-corporate-layoff-announcem`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased search interest for corporate layoff announcements signals rising labor market weakness. Labor weakness can reduce consumer spending and increase credit risk, affecting financials.

## Universe
- XLF

## Data Sources
- Google Trends weekly corporate layoff announcement searches

## Signal Logic
Enter short when weekly searches rise 20% above 5-week average

## Entry / Exit
Entry: Enter short when weekly searches rise 20% above 5-week average Exit: Exit when weekly searches decline below 10% above 5-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly corporate layoff announcement searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Layoff news and related search interest regularly spike due to earnings season and economic data.

## Required Keys
- None
