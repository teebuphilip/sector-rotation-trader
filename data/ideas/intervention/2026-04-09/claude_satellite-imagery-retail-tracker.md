# Satellite Imagery Retail Tracker

**Idea ID:** `satellite-imagery-retail-tracker`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Retail foot traffic can be estimated using satellite imagery of parking lots. By tracking changes in parking lot occupancy, we can identify rising or falling foot traffic at major retail chains, which can signal changes in consumer spending and same-store sales.

## Universe
- WMT
- TGT
- COST
- AMZN
- TSLA

## Data Sources
- Planet Labs satellite imagery
- OpenStreetMap parking lot data

## Signal Logic
Analyze satellite imagery of major retail chains' parking lots to calculate occupancy rates. Look for significant deviations from historical trends as a signal of changing foot traffic.

## Entry / Exit
Buy when parking lot occupancy is rising, indicating increased foot traffic and potentially higher sales. Sell when occupancy starts to decline.

## Position Sizing
Size positions based on the magnitude of the parking lot occupancy change, with larger positions for more significant deviations from the norm.

## Risks
Potential lags between foot traffic changes and financial results, difficulties in accurately measuring parking lot occupancy, and the impact of weather, holidays, and other factors on foot traffic.

## Implementation Notes
Obtain satellite imagery from Planet Labs, identify major retail locations using OpenStreetMap data, and develop computer vision models to track parking lot occupancy over time. Analyze the data to identify significant deviations from historical norms.

## Required Keys
- Planet Labs API key
