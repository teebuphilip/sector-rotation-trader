# Earthquake Energy Demand Indicator

**Idea ID:** `earthquake-energy-demand`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Earthquakes can significantly impact energy demand as businesses and residents react to the event. By tracking changes in real-time energy consumption data, we can identify potential trading opportunities in energy-related assets.

## Universe
- CL1!
- NG1!
- EL1!

## Data Sources
- US Energy Information Administration (EIA) - Real-time electricity demand data
- USGS Earthquake Hazards Program - Real-time earthquake data

## Signal Logic
Monitor the EIA's real-time electricity demand data for a region. When a significant earthquake is detected by USGS in that region, look for a sudden spike or drop in energy demand over the following 1-2 days. The magnitude of the demand change can signal the scale of the event's impact.

## Entry / Exit
Buy or sell energy-related assets (e.g., oil, natural gas, electricity futures) based on the direction and magnitude of the post-earthquake energy demand shift.

## Position Sizing
Scale position size based on the earthquake's magnitude and the resulting energy demand change. Larger earthquakes with bigger demand impacts warrant larger positions.

## Risks
Earthquakes can have unpredictable effects on energy demand, and the relationship may be affected by other factors like weather, time of day, or infrastructure damage. False signals are possible, and the strategy may have limited applicability to small or remote earthquakes.

## Implementation Notes
1. Continuously monitor EIA's real-time electricity demand data for target regions. 2. When a significant earthquake is detected by USGS, analyze the subsequent energy demand changes. 3. Execute buy/sell orders for energy assets based on the direction and magnitude of the demand shift.

## Required Keys
- None
