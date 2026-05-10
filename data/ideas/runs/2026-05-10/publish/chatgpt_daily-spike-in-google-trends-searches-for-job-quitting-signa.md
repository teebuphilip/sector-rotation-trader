# Daily Spike In Google Trends Searches For Job Quitting Signals Labor Market Stress Lifting Financials

**Idea ID:** `daily-spike-in-google-trends-searches-for-job-quitting-signa`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid increases in quitting-related searches indicate rising worker confidence or stress, often preceding wage inflation. Stronger labor markets tend to boost financial sector loan demand and credit quality.

## Universe
- XLF

## Data Sources
- Google Trends daily search interest for 'job quitting' via google_trends adapter

## Signal Logic
If daily search volume exceeds 10% above 20-day average

## Entry / Exit
Entry: If daily search volume exceeds 10% above 20-day average Exit: When daily search volume falls below 5% above 20-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'job quitting' via google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Worker sentiment fluctuations cause frequent daily search volume spikes.

## Required Keys
- None
