# Weekly Surge In Google Trends For Diy Home Improvement Combined With Xlp Relative Strength

**Idea ID:** `weekly-surge-in-google-trends-for-diy-home-improvement-combi`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in interest in DIY home improvement often precedes increased demand for consumer staples related to home care and building materials. Consumer staples benefit from increased home improvement spending signals.

## Universe
- XLP

## Data Sources
- Google Trends weekly for 'home improvement' and Yahoo Finance weekly prices for XLP

## Signal Logic
Enter long XLP when Google Trends for 'home improvement' rises more than 15% week-over-week and XLP outperforms SPY over prior week

## Entry / Exit
Entry: Enter long XLP when Google Trends for 'home improvement' rises more than 15% week-over-week and XLP outperforms SPY over prior week Exit: Exit after 3 weeks or if Google Trends decline by 10% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly for 'home improvement' and Yahoo Finance weekly prices for XLP via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends data frequently show interest bursts around seasonal home projects.

## Required Keys
- None
