# Daily Spike In Google Trends For Emergency Vehicle Repair Predicts Industrials Sector Strength

**Idea ID:** `daily-spike-in-google-trends-for-emergency-vehicle-repair-pr`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased emergency vehicle repair searches reflect stress-induced maintenance needs, benefiting industrials related to automotive parts and services. Industrial sector firms gain from higher demand for emergency vehicle repairs and parts.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long if daily search interest jumps more than 25% above 7-day average

## Entry / Exit
Entry: Enter long if daily search interest jumps more than 25% above 7-day average Exit: Exit after 7 days or if interest declines below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 14
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Vehicle repair emergencies arise frequently due to accidents and wear.

## Required Keys
- None
