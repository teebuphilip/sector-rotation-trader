# Professional Backtest V1

- Run date: 2026-05-13
- Window: 2024-01-01 to 2026-05-13
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- LIVE_ONLY_NON_PRICE: 16
- NEEDS_HISTORY: 1

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Daily Jump In Google Trends For Emergency Dental Care Signals Consumer Stress Lifting Healthcare Sector Demand | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Jump In Google Trends For Home Appliance Repair Signals Consumer Stress Lifting Consumer Staples | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Jump In Google Trends For Home Building Permit Delay Signals Local Economy Construction Stress Hurting Real Estate Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Jump In Google Trends Searches For Job Quitting Signals Labor Market Tightness Benefiting Consumer Discretionary | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Surge In Google Trends For Car Rental Price Spike Triggers Travel Mobility Sector Pullback | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Surge In Rss News Counts For New Labor Union Formations Signals Labor Market Pressure On Industrial Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Electricity Demand Spike During Extreme Cold Snap Triggers Utility Sector Rally | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Ev Charger Network Contraction Signals Electric Vehicle Adoption Slowdown | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Google Trends Spike In Bankruptcy Filing And Debt Consolidation Signals Consumer Default Risk Surge | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Port Container Volume Surge Signals Import Demand Recovery And Consumer Spending Rebound | crazy | NEEDS_HISTORY |  |  | Historical seed exists, but V1 cannot prove point-in-time price-only behavior |
| Weekly Google Trends Surge For Truck Driver Shortage Signals Freight Logistics Risk And Industrial Cost Pressure | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge In Home Heating Oil Shortage Signals Winter Utility Stress Favoring Utilities Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Jump In Google Trends For Warehouse Labor Shortage Signals Supply Chain Labor Stress And Industrial Sector Risk | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Rise In Rss Count For Labor Strike News Signals Industrial Sector Risk | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Weekly Spike In Earthquake Activity In Port Regions Signals Potential Freight Logistics Disruption | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Weekly Spike In Google Trends For Fuel Shortage Predicts Energy Sector Volatility | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends Searches For Freight Container Backlog Signals Industrial Sector Pressure | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.
