# Features From Reddit

## Purpose

This file captures product or research ideas that came directly from Reddit feedback.

Rule:
- Only add items that could plausibly change StockArithm's product, analysis layer, or validation discipline.
- Do not add generic trading philosophy unless it implies a concrete feature or workflow.
- Score later. Do not force prioritization while the idea is still fresh.

## Status Key

- `candidate` = worth keeping around
- `score-next` = should be scored soon
- `rejected` = not worth building

## Items

### Regime Tagging On Trades
- Status: `score-next`
- Earliest target: `by July 1 if tractable, otherwise immediately after`
- Source: Reddit comment about classifying strategy performance by trend strength and volatility regime.
- What it means:
  - Tag every trade with a regime bucket.
  - Example framework:
    - trend strength from ADX
    - volatility from ATR percentile
    - cross the two into regime buckets
  - Then evaluate each algo by regime, not just total P&L.
- Why it matters:
  - Explains why a signal can look dead overall but strong in a narrow environment.
  - Makes force-rank vs rolling-30D less blunt by adding explicit context.
  - Could become premium-worthy on algo pages and weekly notes.
- Product implications:
  - regime tags on trades
  - per-algo regime heatmaps
  - "works in X / fails in Y" summaries
  - possible premium family/regime analysis
- Notes:
  - High conceptual value.
  - Do not rush into a bad implementation just because the idea is good.

### Lookahead / Leakage Validation Pass
- Status: `score-next`
- Earliest target: `by July 1`
- Source: Reddit comment warning that tiny backtest code mistakes can create absurd fake returns.
- What it means:
  - Add a formal validation pass for promoted or premium-facing signals:
    - date alignment
    - missing data handling
    - benchmark alignment
    - trigger timing
    - no future information leakage
- Why it matters:
  - This is credibility-critical.
  - A single bad leak would undermine the public experiment.
- Product implications:
  - validation checklist
  - bias-sanity report
  - possible "validation passed" badge for stronger signals
- Notes:
  - This is closer to a validation feature than a user-facing feature, but it matters enough to track here.

### Separate Signal Edge From Risk Wrapper
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit comments saying not to mix signal discovery, position sizing, and risk in one evaluation.
- What it means:
  - Separate:
    - signal thesis quality
    - entry/exit wrapper
    - position sizing
    - portfolio/risk management
  - Compare signals without assuming the wrapper is the edge.
- Why it matters:
  - Reduces false conclusions about whether a signal is good or bad.
  - Could explain why some ideas fail under one wrapper but not another.
- Product implications:
  - separate evaluation layers
  - "signal edge vs wrapper edge" analysis
  - cleaner premium research notes

### Risk Wrapper Comparison
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit comment about ATR-based volatility-adjusted sizing versus fixed sizing.
- What it means:
  - Test fixed sizing against alternative sizing methods instead of assuming one is correct.
  - Keep it as a controlled comparison, not a blind system rewrite.
- Why it matters:
  - Could improve survivability and reduce misleading results from arbitrary sizing.
- Product implications:
  - risk-wrapper comparison tables
  - optional premium note on whether a signal is weak or just poorly wrapped
- Notes:
  - Useful, but lower urgency than regime tagging and leakage checks.

### Crowded Signal Decay / Originality Lens
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit comment claiming public/generic signals get overtraded and that original signals matter more.
- What it means:
  - Track whether a signal is:
    - common/public/crowded
    - less-common/original/weird
  - Later test whether originality correlates with persistence or edge durability.
- Why it matters:
  - Fits StockArithm's identity as an alternative-data signal lab.
  - Could become a useful explanatory layer for why certain ideas decay.
- Product implications:
  - originality tagging
  - crowded-vs-weird signal cohorts
  - premium research around signal decay

### Walk-Forward Validation Framework
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit advice to use rolling train/test windows rather than simple split thinking.
- What it means:
  - Add a more explicit rolling validation framework for signals that graduate into stronger claims.
- Why it matters:
  - Better robustness language across years and regimes.
- Product implications:
  - walk-forward report
  - regime robustness notes
- Notes:
  - Good discipline, but not launch-critical.

### Entry Score Calibration / Tiering
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit-style idea around ranking entries, bucketing them, and validating whether top-ranked entries materially outperform low-ranked entries.
- What it means:
  - Score each entry with one or more models.
  - Rank or bucket entries into tiers, percentiles, or deciles.
  - Track realized outcomes by bucket:
    - win rate
    - average return
    - days to close
    - open vs closed behavior
  - Test whether high-ranked entries are actually better than low-ranked ones.
- Why it matters:
  - Converts vague "good setup" intuition into measurable rank-order validation.
  - Creates a cleaner path to selective execution:
    - take aggressively
    - take selectively
    - avoid
  - Helps distinguish descriptive scoring from genuinely decision-useful scoring.
- Product implications:
  - entry leaderboard
  - confidence tiers
  - top-bucket vs bottom-bucket outcome summaries
  - possible comparison between handwritten scores and model-generated scores
- Notes:
  - Strong concept, but sample size can lie badly.
  - Only worth trusting if it holds out-of-sample and stays stable over time.

### Execution Realism / Slippage Modeling
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit warning that bar-based backtests can assume impossible fills and ignore slippage that compounds on every entry and exit.
- What it means:
  - Stress-test signals against more realistic execution assumptions.
  - Compare clean paper fills to slippage-adjusted or execution-degraded outcomes.
  - Be explicit about where paper trading is likely flattering reality.
- Why it matters:
  - Prevents overclaiming precision from simplified fills.
  - Helps distinguish a genuinely robust signal from one that only works under idealized execution.
  - Improves credibility if/when stronger premium or deployed claims are made.
- Product implications:
  - slippage assumption layer
  - execution realism notes on stronger signals
  - net-of-slippage scenario comparisons
  - future validation badge or caveat for execution sensitivity
- Notes:
  - Higher relevance for more active systems than for slower sector-rotation systems.
  - Still worth tracking as a future validation discipline.

### Alternative Validation Metrics / Calibration Layer
- Status: `score-next`
- Earliest target: `by July 1 if scope stays tight, otherwise immediately after`
- Source: Reddit cross-market advice that raw P&L converges slowly and that calibration or non-P&L validation metrics can reveal signal quality faster.
- What it means:
  - Add validation views beyond simple P&L:
    - calibration against realized outcomes
    - prediction-quality metrics
    - benchmark-relative distribution checks
  - Use these to judge whether a signal is informative before waiting for long P&L histories.
- Why it matters:
  - P&L can look like noise for a long time at small sample sizes.
  - A cleaner validation layer could help distinguish dead signals from early-but-valid signals.
  - This is highly relevant to the "good month / bad long-run record" problem already visible in the board.
- Product implications:
  - validation panel on stronger signals
  - premium "signal quality vs realized outcome" notes
  - faster internal go/no-go read on new algos
- Notes:
  - Very relevant conceptually.
  - Keep implementation tight; do not invent fake precision.

### Fractional Kelly Under Edge Uncertainty
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit advice that fractional Kelly is as much about uncertainty in edge estimates as it is about variance control.
- What it means:
  - Treat sizing as a function of confidence in the model's edge estimate, not just return volatility.
  - Compare fixed sizing with uncertainty-aware sizing rules.
- Why it matters:
  - Prevents overbetting when estimated edge is noisy or unstable.
  - Fits the broader need to separate signal edge from risk wrapper quality.
- Product implications:
  - confidence-aware sizing experiments
  - wrapper comparison research
  - premium notes on "edge confidence vs position size"
- Notes:
  - Strong idea, but not a launch-phase change.
  - Needs disciplined comparison, not intuition.

### Selection-Bias / Research Trail Ledger
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit warning that public methodology posts and personal backtests both hide abandoned variants and hyperparameter dead ends.
- What it means:
  - Track research history explicitly:
    - attempted variants
    - rejected versions
    - parameter sweeps
    - why a signal advanced or died
  - Make it harder to accidentally treat survivor strategies as if they emerged cleanly.
- Why it matters:
  - Reduces false confidence from silent iteration.
  - Fits StockArithm's public-honesty positioning.
- Product implications:
  - internal experiment ledger
  - future public "research trail" or "graveyard lineage" views
  - stronger premium autopsy content
- Notes:
  - More governance than flashy feature, but important.

### Capacity / Friction Awareness
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit note that edge discovery is often easier than scaling through real market frictions and capacity limits.
- What it means:
  - Add explicit awareness of where a signal's theoretical edge may not scale cleanly.
  - Track whether a strategy is likely robust only at small notional size.
- Why it matters:
  - Prevents confusing paper edge with scalable deployment edge.
  - Useful if the product ever moves from public proof into stronger deployment claims.
- Product implications:
  - capacity notes on advanced signals
  - friction caveats in premium research
  - future deployment checklist item
- Notes:
  - Lower urgency than calibration and leakage validation, but worth preserving.

### No-Trade / Selective Activation Discipline
- Status: `score-next`
- Earliest target: `by July 1 if kept simple, otherwise immediately after`
- Source: Reddit comment that the best systems are often flat most of the time and that the edge is frequently in knowing when not to trade.
- What it means:
  - Explicitly model when a signal should be inactive, filtered, or sidelined.
  - Treat "do nothing" as a first-class decision rather than a failure to find a setup.
- Why it matters:
  - Could materially improve weak signals that only work in narrow conditions.
  - Fits directly with the regime-tagging and wrapper-separation ideas already in this file.
- Product implications:
  - no-trade zones
  - activation filters
  - "signal should be flat here" explanations
  - tighter premium notes around selective deployment
- Notes:
  - High conceptual value.
  - Do not bolt on random filters without validation.

### Pre-Committed Kill Criteria
- Status: `score-next`
- Earliest target: `by July 1`
- Source: Reddit advice to define kill thresholds before seeing out-of-sample results.
- What it means:
  - Set explicit failure criteria in advance for signals:
    - minimum out-of-sample Sharpe
    - max drawdown tolerance
    - minimum sample size
    - time-to-prove window
  - Then enforce those rules instead of rationalizing weak survivors.
- Why it matters:
  - Prevents attachment to bad signals.
  - Strengthens the public honesty model because promotion and graveyard decisions become rule-based.
- Product implications:
  - promotion / graveyard gate policy
  - per-signal kill-criteria metadata
  - future proof page showing what qualifies a signal to stay live
- Notes:
  - This is one of the stronger post-launch product/trust ideas from Reddit so far.

### Research / Execution Journal Layer
- Status: `score-next`
- Earliest target: `by July 1 if implemented narrowly, otherwise immediately after`
- Source: Reddit comment that the bottleneck has shifted from coding to data quality, execution, and disciplined journaling.
- What it means:
  - Journal the important parts of the system continuously:
    - data source quality issues
    - adapter outages
    - execution assumptions
    - signal promotions/demotions
    - manual interventions or anomalies
- Why it matters:
  - Creates an audit trail instead of relying on memory.
  - Helps separate "bad signal" from "bad plumbing" or "bad data day."
  - Fits StockArithm's public honesty model and premium research direction.
- Product implications:
  - operator journal
  - signal-level notes
  - visible public ops notes page / daily changelog
  - premium weekly change notes
  - cleaner graveyard autopsies
- Notes:
  - Strong and practical.
  - Can start simple before it becomes a full product surface.

### Execution Wrapper Reliability
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit comment emphasizing that profitability often depends more on boring execution wrappers than on clever coding.
- What it means:
  - Treat execution plumbing as a first-class system component:
    - retries
    - data integrity checks
    - adapter reliability
    - stale-data detection
    - notification on failures
- Why it matters:
  - Prevents false conclusions caused by bad operational plumbing.
  - Strengthens the gap between "interesting demo" and "reliable system."
- Product implications:
  - wrapper health checks
  - adapter reliability reporting
  - execution/error telemetry
  - stronger ops dashboarding
- Notes:
  - More operational than front-end, but very real.

### Synthetic Clock / Time-Replay Validation
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit engineering advice to build around a synthetic clock so time can be emulated cleanly in backtests and replays.
- What it means:
  - Introduce a cleaner replay/time-emulation layer so signals and validations can be tested under controlled historical progression rather than loose ad hoc scripts.
- Why it matters:
  - Helps reduce accidental lookahead behavior.
  - Makes backtest and replay logic more rigorous.
  - Supports stronger validation if the system grows more complex.
- Product implications:
  - replay harness
  - time-aware validation tools
  - more disciplined historical testing
- Notes:
  - Real engineering value.
  - Not worth touching before launch.

### Plain-English Strategy Spec Before Build
- Status: `score-next`
- Earliest target: `by July 1 if kept lightweight, otherwise immediately after`
- Source: Reddit point that every strategy/system should have a normal-language document explaining what it is trying to do before coding starts.
- What it means:
  - Write a short human-readable spec before implementation:
    - what the signal is
    - what data it uses
    - what triggers it
    - what invalidates it
    - how it should fail safely
- Why it matters:
  - Forces clarity before code.
  - Reduces accidental scope drift and hidden assumptions.
  - Makes debugging and later review much easier.
- Product implications:
  - per-signal spec template
  - publishable plain-English spec on the algo page
  - cleaner thesis pages
  - better handoff between ideation, implementation, and validation
- Notes:
  - Strong discipline idea.
  - Cheap enough that it may be worth adopting early.

### Robust Logging / State Trace
- Status: `score-next`
- Earliest target: `by July 1 if implemented narrowly, otherwise immediately after`
- Source: Reddit advice that algo systems need very verbose logs, state traceability, and controllable verbosity for debugging and ops.
- What it means:
  - Capture detailed logs around:
    - market data inputs
    - signal state
    - trade decisions
    - execution attempts
    - failures and recoveries
  - Support verbosity levels so logs stay usable as the system matures.
- Why it matters:
  - Many failures are only diagnosable from detailed state/log history.
  - Helps separate signal bugs from data bugs from infrastructure bugs.
- Product implications:
  - richer ops logs
  - replayable decision traces
  - premium/internal "why did this happen?" diagnostics
- Notes:
  - Very practical.
  - Overlaps well with the research/execution journal item, but is more system-level.

### Unified Alert / Announcement Facility
- Status: `candidate`
- Earliest target: `post July 1`
- Source: Reddit suggestion to centralize urgent trading-system alerts into one announcer/notification channel.
- What it means:
  - Create a common path for important events from multiple processes:
    - failed data feed
    - publish failure
    - execution anomaly
    - graveyard/promotion event
    - domain or MailerLite breakage
- Why it matters:
  - Prevents important failures from getting buried in scattered logs.
  - Reduces operator latency when something actually needs attention.
- Product implications:
  - internal alert bus
  - phone/text/TTS hooks later
  - centralized operational notifications
- Notes:
  - Strong ops idea.
  - Not launch-critical, but very worth preserving.

## Rejected / Do Not Build

### "Anything Is Possible If You're Stubborn Enough"
- Status: `rejected`
- Reason:
  - not a feature
  - not a useful product principle

### "EMH Is Bullshit"
- Status: `rejected`
- Reason:
  - ideological
  - not directly translatable into product or validation work
