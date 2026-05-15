# Daily Spike In Google Trends For Flu Symptom Searches Boosting Healthcare Services Demand

**Idea ID:** `daily-spike-in-google-trends-for-flu-symptom-searches-boosti`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased flu symptom search activity predicts higher healthcare utilization and pharmaceutical sales. Healthcare sector benefits from spikes in illness-related demand.

## Universe
- XLV

## Data Sources
- Google Trends daily search interest for flu symptoms

## Signal Logic
If daily search volume exceeds 25% above 7-day average

## Entry / Exit
Entry: If daily search volume exceeds 25% above 7-day average Exit: When volume normalizes below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for flu symptoms via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Flu incidence and related searches show strong seasonality and daily fluctuations.

## Required Keys
- None
