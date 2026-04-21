# Professional Backtest V1

- Run date: 2026-04-21
- Window: 2024-01-01 to 2026-04-15
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- BACKTEST_FAIL: 2
- BACKTEST_WEAK: 7
- INSUFFICIENT_ACTIVITY: 5
- UNSUPPORTED_DATA: 83

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Faber Momentum Rotation | normal | BACKTEST_WEAK | -31.66 | 60 | Backtest completed |
| Antonacci Dual Momentum Sector Rotation | normal | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AGG |
| Quantified Simple Monthly Rotation | normal | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: EEM, TLT |
| Algo Biscotti (Unconditional Loyalty) | normal | BACKTEST_WEAK | -48.05 | 21 | Backtest completed |
| Algo Baileymol (Chaos Monger) | normal | BACKTEST_WEAK | -36.14 | 291 | Backtest completed |
| TSA Body Count | crazy | UNSUPPORTED_DATA |  |  | Uses direct safe_download; V1 requires refactor to point-in-time cached prices |
| Cardboard Box Index | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Craigslist Desperation Index | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: GLD |
| Glassdoor Misery Gradient | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| 311 Call Rotation | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Liquor Store Leading Indicator | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| LinkedIn Layoff Propagation | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Congress Trading Fade | crazy | UNSUPPORTED_DATA |  |  | Historical seed exists, but V1 cannot prove point-in-time price-only behavior |
| Algo Biscotti (Unconditional Loyalty) | crazy | UNSUPPORTED_DATA |  |  | Uses direct safe_download; V1 requires refactor to point-in-time cached prices |
| Chaos Rotation Lab | crazy | UNSUPPORTED_DATA |  |  | Uses direct safe_download; V1 requires refactor to point-in-time cached prices |
| Reddit Gaming Thread Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: EA, MSFT, NVDA, RBLX, TTWO |
| Airport Shopping Spree | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: EXPE, MAR, TCOM |
| Cloud Storage Demand Surge | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: BOX, DBX, GOOGL, MSFT |
| Crypto Derivative Arbitrage | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: BTC-USD, ETH-USD, LINK-USD, LTC-USD, XRP-USD |
| Earthquake Energy Demand Indicator | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: UNG, USO |
| Electric Vehicle Charge Station Density | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: BLNK, CHPT, EVGO, TSLA |
| Insider Trading Signals | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: IWV |
| Online Ad Impression Volatility Trader | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: GOOG, META, PINS, SNAP, TTD |
| Pet Food Supply Chain Disruption | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: CENT, CENTA, CHWY, PETS |
| Reddit Emoji Sentiment Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMC, AMD, GME, MSFT, NFLX, NVDA, TSLA |
| Reddit Mentions Volatility Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMC, AMD, BABA, GME, META, MSFT, NFLX, NVDA, TSLA |
| Reddit Sentiment Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMD, AMZN, BABA, GOOGL, META, MSFT, NFLX, NVDA, TSLA |
| Reddit Sentiment Spike Trend | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMD, AMZN, GME, MSFT, NFLX, NVDA, PLTR, TSLA |
| Reddit Sentiment Volatility Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMZN, GME, MSFT, NVDA, TSLA |
| Reddit Subreddit Mention Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMC, AMD, GME, MSFT, NVDA, TSLA |
| Reddit Subreddit Sentiment Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMC, GME, MSFT, TSLA |
| Reddit Subreddit Surge Momentum | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMC, AMD, GME, MSFT, NFLX, NIO, NVDA, PLTR, TSLA |
| Reddit Volatility Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMC, AMD, GME, GOOGL, META, MSFT, NFLX, NVDA, TSLA |
| Social Media Sentiment Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMZN, GOOGL, META, MSFT, NFLX, NVDA, TSLA |
| Superbowl Futures Trade | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Twitter Sentiment Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMD, AMZN, BABA, GOOGL, META, MSFT, NFLX, NVDA, TSLA |
| Volatility Spike Follow-Through | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: AAPL, AMD, AMZN, GOOG, META, MSFT, NFLX, NVDA, TSLA |
| Weather Volatility Spike | crazy | UNSUPPORTED_DATA |  |  | V1 only supports SPY/sector ETFs; unsupported tickers: QQQ, UVXY, VXX |
| Truck Tonnage Index | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Misery Rotation | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Uber Mobility Index | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Job Posting Acceleration | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Bankruptcy Filing Rate | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Small Business Formation | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Credit Card Delinquency | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Consumer Sentiment | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Retail Sales Momentum | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Freight Rail Carloads | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.fred_series |
| Housing Permit Velocity | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.fred_series |
| Mortgage Rate Housing Proxy | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.fred_series |
| Copper Momentum | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.fred_series |
| Lumber Momentum | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.fred_series |
| Yield Curve Regime | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.fred_series |
| High Yield Spread Regime | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.fred_series |
| Electricity Consumption | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Port Container Volume | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Airline Load Factor Proxy | crazy | UNSUPPORTED_DATA |  |  | No supported V1 price-only backtest path |
| Real Estate Sector Weekly Google Trends Home Buying Surge | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Utilities Sector Weekly Temperature Drop Signal | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.weather_series |
| Airport Security Surge | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.tsa_table |
| Ev Charging Boom | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Fintech Disruption Wave | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Global Tech Earnings Momentum | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Port Congestion Squeeze | crazy | UNSUPPORTED_DATA |  |  | Historical seed exists, but V1 cannot prove point-in-time price-only behavior |
| Retail Rush Ahead Of Holidays | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Utility Power Grid Stress | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Weather Disruption Ripple Effects | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.weather_series |
| Work From Home Frenzy | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Xlb Daily Volatility Contraction Breakout | crazy | INSUFFICIENT_ACTIVITY | -50.97 | 0 | Backtest completed |
| Xlb Weekly Rss News Count Spike On Commodity Shortage | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Xlc Weekly Google Trends Surge In 5g Rollout | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Xle Weekly Drawdown Rebound Signal | crazy | BACKTEST_FAIL | -51.35 | 74 | Backtest completed |
| Xlu Daily Electricity Demand Surge | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Xlu Weekly Cold Snap Weather Correlation | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.weather_series |
| Xlv Google Trends Flu Search Spike | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Electricity Enlightenment | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Ev Euphoria | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Google Gusts | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Retail Roulette | crazy | BACKTEST_FAIL | -51.32 | 87 | Backtest completed |
| Rss Roar | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Tremor Tension | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Weather Windfall | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.weather_series |
| Consumer Discretionary Google Trends Surge For Sale Keywords | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Energy Sector Weekly Drawdown Exhaustion | crazy | BACKTEST_WEAK | -50.21 | 12 | Backtest completed |
| Financial Sector Momentum Divergence With Spy | crazy | INSUFFICIENT_ACTIVITY | -50.97 | 0 | Backtest completed |
| Healthcare Sector Google Trends Spike In Flu Symptoms | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Industrial Sector Weekly Earthquake Activity Correlation Dip | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Materials Sector Weekly Positive Correlation Breakdown With Xlb | crazy | INSUFFICIENT_ACTIVITY | -50.92 | 2 | Backtest completed |
| Staples Sector Drawdown Rapid Recovery | crazy | BACKTEST_WEAK | -50.95 | 10 | Backtest completed |
| Technology Sector Daily Ev Charger Count Surge | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Utilities Sector Negative Price Gap Fill | crazy | BACKTEST_WEAK | -50.82 | 118 | Backtest completed |
| Crypto Capitulation Countdown | crazy | INSUFFICIENT_ACTIVITY | -50.97 | 0 | Backtest completed |
| Earthquake Aftershock Amplifier | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Ev Charging Station Stampede | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Lumber Futures Rollercoaster | crazy | INSUFFICIENT_ACTIVITY | -50.97 | 0 | Backtest completed |
| Semiconductor Moonshot Warning | crazy | BACKTEST_WEAK | -50.82 | 24 | Backtest completed |
| Solar Storm Scorcher | crazy | UNSUPPORTED_DATA |  |  | Uses non-price adapter: crazy.adapters.weather_series |

This is experimental research, not investment advice. Past performance does not predict future results.
