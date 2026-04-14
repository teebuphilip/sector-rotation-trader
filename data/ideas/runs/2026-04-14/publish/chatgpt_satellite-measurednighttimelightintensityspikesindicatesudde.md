# Satellite-measurednighttimelightintensityspikesindicatesuddensurgesindatacenteractivity

**Idea ID:** `satellite-measurednighttimelightintensityspikesindicatesudde`
**Source:**  / 
**Frequency:** weekly

## Thesis
A sudden increase in nighttime light intensity around major data center hubs suggests heightened cloud computing demand and infrastructure use. Technology sector, especially cloud and data infrastructure companies, benefit from increased data center utilization.

## Universe
- XLK

## Data Sources
- NASA Black Marble Night Lights dataset

## Signal Logic
If weekly nighttime light intensity around top 5 US data center locations rises >3% from prior week

## Entry / Exit
Entry: If weekly nighttime light intensity around top 5 US data center locations rises >3% from prior week Exit: After 15 trading days or if intensity drops below entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use NASA Black Marble Night Lights dataset via api (weekly).

## Required Keys
- None
