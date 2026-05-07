# Daily Increase In Google Trends For Online Job Scam Signals Labor Market Stress Impacting Tech

**Idea ID:** `daily-increase-in-google-trends-for-online-job-scam-signals-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising scam-related searches indicate labor market distress and potential tech sector reputational risk. Labor market stress and fraud concerns can weigh on technology hiring and sentiment.

## Universe
- XLK

## Data Sources
- Google Trends daily searches for 'online job scam'

## Signal Logic
Enter short XLK if daily searches rise 40% above 10-day average

## Entry / Exit
Entry: Enter short XLK if daily searches rise 40% above 10-day average Exit: Exit after 7 days or if searches fall below 20% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily searches for 'online job scam' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Scam-related search spikes happen often during economic uncertainty or layoffs.

## Required Keys
- None
