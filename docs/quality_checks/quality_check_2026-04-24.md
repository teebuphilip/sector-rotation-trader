# Quality Check — 2026-04-24

## SPY Benchmark
- Current Price: $709.78
- YTD Return: +4.18%
- YTD High: $711.21
- YTD Low: $631.97
- Max Drawdown: -11.14%

## Baseline (NRWise)
- Equity: $100,045.55 (+0.05%)
- Sector: XLU
- Last Snapshot: 2026-04-24
- Snapshots: 86
- Trades: 11
- Positions: 1
- Alpha vs SPY: -4.13%

## Normal Algos
  Algo                        Equity       YTD     Alpha  Trades      Signal    Last Run
  --------------------------------------------------------------------------------------
  baileymol              $106,500.29     6.50%     2.32%      30  XLE,XLK,XLY  2026-04-24
  dmsr                   $104,846.72     4.85%     0.67%      15        CASH  2026-04-24
  faber                  $103,846.61     3.85%    -0.33%       8        CASH  2026-04-24
  simple_monthly         $100,000.00     0.00%    -4.18%       0        CASH  2026-04-24
  biscotti                $98,853.69    -1.15%    -5.33%       5        CASH  2026-04-24

## Crazy Algos — Active (35/110)
  Algo                        Equity       YTD     Alpha  Trades      Signal    Last Run
  --------------------------------------------------------------------------------------
  finra-dark-pool-signal   $101,753.40     1.75%    -2.43%       2  HIGH_SHORT  2026-04-24
  uber-mobility          $101,156.04     1.16%    -3.02%       6    RISK_OFF  2026-04-24
  insider-trading-signals   $101,108.09     1.11%    -3.07%       1  INSIDER_DROUGHT  2026-04-24
  retail-sales-momentum   $100,551.33     0.55%    -3.63%       2   EXPANDING  2026-04-24
  mortgage-rate-housing-proxy   $100,520.73     0.52%    -3.66%       2  HOUSING_HEADWIND  2026-04-24
  earthquake-aftershock-amplifier   $100,047.52     0.05%    -4.13%       2        HOLD  2026-04-24
  semiconductor-moonshot-warning   $100,045.62     0.05%    -4.13%       6        HOLD  2026-04-24
  materials-sector-weekly-positive-correlation-breakdown-with-   $100,025.87     0.03%    -4.15%       2        HOLD  2026-04-24
  staples-sector-drawdown-rapid-recovery   $100,024.70     0.02%    -4.15%       2        HOLD  2026-04-24
  attention-sentiment-spike-daily-surge-in-news-rss-counts-men    $99,969.89    -0.03%    -4.21%       3     RISK_ON  2026-04-24
  consumer-discretionary-google-trends-surge-for-sale-keywords    $99,960.96    -0.04%    -4.22%       6        HOLD  2026-04-24
  real-estate-sector-weekly-google-trends-home-buying-surge    $99,954.77    -0.05%    -4.22%       2        HOLD  2026-04-24
  industrial-sector-weekly-earthquake-activity-correlation-dip    $99,938.06    -0.06%    -4.24%       7     RISK_ON  2026-04-24
  news-sentiment-rotation-fade-trade    $99,929.81    -0.07%    -4.25%       2        HOLD  2026-04-24
  utilities-sector-negative-price-gap-fill    $99,921.53    -0.08%    -4.26%      14        HOLD  2026-04-24
  healthcare-sector-google-trends-spike-in-flu-symptoms    $99,917.38    -0.08%    -4.26%       6        HOLD  2026-04-24
  retail-roulette         $99,913.43    -0.09%    -4.27%      12        HOLD  2026-04-24
  xlu-daily-electricity-demand-surge    $99,898.68    -0.10%    -4.28%      12        HOLD  2026-04-24
  xlb-weekly-rss-news-count-spike-on-commodity-shortage    $99,890.61    -0.11%    -4.29%       6        HOLD  2026-04-24
  google-gusts            $99,871.97    -0.13%    -4.31%       4        HOLD  2026-04-24
  tremor-tension          $99,864.21    -0.14%    -4.31%       8        HOLD  2026-04-24
  seismic-activity-construction-halt-signal    $99,861.92    -0.14%    -4.32%       6        HOLD  2026-04-24
  electricity-enlightenment    $99,857.33    -0.14%    -4.32%      10        HOLD  2026-04-24
  grocery-store-foot-traffic-collapse-signal    $99,678.41    -0.32%    -4.50%      21     RISK_ON  2026-04-24
  xle-weekly-drawdown-rebound-signal    $99,667.30    -0.33%    -4.51%      32        HOLD  2026-04-24
  healthcare-cost-shock-google-search-spike    $99,617.84    -0.38%    -4.56%      22        HOLD  2026-04-24
  copper-momentum         $99,599.26    -0.40%    -4.58%       2  GLOBAL_GROWTH  2026-04-24
  xlc-weekly-google-trends-surge-in-5g-rollout    $99,592.39    -0.41%    -4.59%      46        HOLD  2026-04-24
  lumber-momentum         $99,487.23    -0.51%    -4.69%       2  BUILDING_DEMAND  2026-04-24
  electricity-consumption    $99,486.11    -0.51%    -4.69%      10  INDUSTRIAL_POWER_DEMAND  2026-04-24
  weekly-surge-in-google-trends-searches-for-diy-home-repair-s    $99,220.52    -0.78%    -4.96%      34        HOLD  2026-04-24
  biscotti                $98,009.55    -1.99%    -6.17%       5        HOLD  2026-04-24
  vix-term-structure      $94,548.66    -5.45%    -9.63%     106        HOLD  2026-04-24
  baileymol               $93,765.37    -6.23%   -10.41%      64  FRIDAY_EXIT  2026-04-24
  vix-fear-rotation       $92,745.94    -7.25%   -11.43%     118        HOLD  2026-04-24

## Crazy Algos — Idle (75/110)
  These algos are running but have no recorded trades in the current state history.
  That is not a crash; it means the trigger has not fired yet, the adapter returned no usable signal, or the strategy is still waiting for live evidence.

  airline-load-factor                  airport-security-surge               airport-shopping-spree               bankruptcy-filing-rate             
  calls311                             cardboard                            cloud-storage-demand-surge           congress                           
  consumer-sentiment                   craigslist                           credit-card-delinquency              crypto-capitulation-countdown      
  crypto-derivative-arbitrage          earthquake-energy-demand             electric-vehicle-charge-station-density  energy-sector-sudden-weekly-volatility-spike
  energy-sector-weekly-drawdown-exhaustion  ev-charger-density-saturation-play   ev-charging-boom                     ev-charging-station-stampede       
  ev-euphoria                          financial-sector-momentum-divergence-with-spy  fintech-disruption-wave              freight-rail-carloads              
  glassdoor                            global-tech-earnings-momentum        high-yield-spread-regime             housing-permit-velocity            
  job-posting-acceleration             linkedin                             liquor                               lumber-futures-rollercoaster       
  materials-sector-weekly-volatility-contraction-breakout  misery-rotation                      online-ad-impression-volatility      patent-filing-velocity             
  pet-food-supply-chain                port-congestion-squeeze              port-container-volume                reddit-emoji-sentiment-spike       
  reddit-gaming-thread-spike           reddit-mentions-volatility-spike     reddit-sentiment-spike-trend         reddit-sentiment-spike             
  reddit-sentiment-volatility-spike    reddit-subreddit-mention-spike       reddit-subreddit-sentiment-spike     reddit-subreddit-surge-momentum    
  reddit-volatility-spike              rental-car-shortage-volatility-spike  retail-rush-ahead-of-holidays        rss-roar                           
  shipping-container-squeeze-play      small-business-formation             social-media-sentiment-spike         solar-storm-scorcher               
  superbowl-futures-trade              technology-sector-daily-ev-charger-count-surge  temperature-shock-energy-demand-flip  truck-tonnage                      
  tsa                                  twitter-sentiment-spike              utilities-sector-weekly-temperature-drop-signal  utility-power-grid-stress          
  volatility-spike-follow-through      weather-disruption-ripple-effects    weather-volatility-spike             weather-windfall                   
  weekly-surge-in-openchargemap-ev-charger-installations-signa  work-from-home-frenzy                xlb-daily-volatility-contraction-breakout  xlu-weekly-cold-snap-weather-correlation
  xlv-google-trends-flu-search-spike   yelp-closure-velocity                yield-curve-regime                 

## Blocked Algos
- **EIA_API_KEY** (1 algos): Electricity Consumption
- **GLASSDOOR_KEY** (1 algos): Glassdoor Misery Gradient
- **GLASSDOOR_PARTNER_ID** (1 algos): Glassdoor Misery Gradient
- **YELP_API_KEY** (1 algos): Yelp Closure Velocity

## Flags & Warnings
- Total algos: 115
- Beating SPY: 2/115 (but only 2 have actually traded)
- Best: baileymol at +6.50%
- Worst: vix-fear-rotation at -7.25%

- CHURNING: baileymol has 64 trades but is down -6.23% — overtrading?
- CHURNING: vix-fear-rotation has 118 trades but is down -7.25% — overtrading?
- CHURNING: vix-term-structure has 106 trades but is down -5.45% — overtrading?

## Context Notes
- HELD POSITIONS WITH HOLD SIGNAL: 3 algos. HOLD means maintain/no rebalance here, not forced exit.
-   - biscotti (crazy) has 1 open positions
-   - vix-fear-rotation (crazy) has 2 open positions
-   - vix-term-structure (crazy) has 2 open positions

---
_Generated by `scripts/quality_check.py` at 2026-04-24 14:30 UTC_