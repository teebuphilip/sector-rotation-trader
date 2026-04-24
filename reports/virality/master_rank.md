# Feature Virality Force Rank — 2026-04-24
Total features ranked: 20

## Scoring Key
- **Adjusted Score** = viral_total × (6 − build_complexity) × stockarithm_fit / 25
- **Verdict**: BUILD_NOW | BUILD_LATER | SKIP
- **Detail**: link to the dated score report for full dimension breakdown

---

| Rank | Feature | Adj Score | Viral/20 | Complexity | Fit | Verdict | Detail |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Receipts Guy's Trade History Scroll | 11.2 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#receipts-guy-s-trade-history-scroll) |
| 2 | Bucket Thesis Statement | 9.6 | 8 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#bucket-thesis-statement) |
| 3 | Alt-Data Nerd's Divergence Spotlight | 9.6 | 8 | 2 | 4 | BUILD_NOW | [scores](2026-04-23.md#alt-data-nerd-s-divergence-spotlight) |
| 4 | Trade Log Receipts | 9.6 | 8 | 2 | 5 | BUILD_NOW | [scores](2026-04-24.md#trade-log-receipts) |
| 5 | Biscotti's Blunder Board | 9.6 | 10 | 2 | 5 | BUILD_NOW | [scores](2026-04-24.md#biscotti-s-blunder-board) |
| 6 | Receipts Export | 9.0 | 9 | 2 | 5 | BUILD_NOW | [scores](2026-04-22.md#receipts-export) |
| 7 | Force Rank Divergence View | 8.96 | 7 | 2 | 4 | BUILD_NOW | [scores](2026-04-23.md#force-rank-divergence-view) |
| 8 | Divergence View | 8.75 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-22.md#divergence-view) |
| 9 | Bucket Audit Log | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-22.md#bucket-audit-log) |
| 10 | Trade-Level Signal Audit Trail | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#trade-level-signal-audit-trail) |
| 11 | Receipts Ledger: Loss Flags | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#receipts-ledger-loss-flags) |
| 12 | Drawdown Diary | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-24.md#drawdown-diary) |
| 13 | Signal Bucket Tags | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-24.md#signal-bucket-tags) |
| 14 | Trade History Time Machine | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-24.md#trade-history-time-machine) |
| 15 | Signal Bucket Explorer | 7.68 | 6 | 2 | 4 | BUILD_NOW | [scores](2026-04-24.md#signal-bucket-explorer) |
| 16 | Signal Hunter's Bucket View | 7.2 | 6 | 2 | 4 | BUILD_LATER | [scores](2026-04-23.md#signal-hunter-s-bucket-view) |
| 17 | Signal Decay Curves | 6.72 | 7 | 2 | 4 | BUILD_LATER | [scores](2026-04-24.md#signal-decay-curves) |
| 18 | Cross-Algo Pattern Spotter | 6.4 | 8 | 2 | 5 | BUILD_LATER | [scores](2026-04-22.md#cross-algo-pattern-spotter) |
| 19 | Bucket Migration Log | 5.76 | 6 | 2 | 4 | BUILD_LATER | [scores](2026-04-23.md#bucket-migration-log) |
| 20 | Streak & Fade View | 4.8 | 5 | 2 | 4 | BUILD_LATER | [scores](2026-04-24.md#streak-fade-view) |

---

## BUILD_NOW List

### 1. Receipts Guy's Trade History Scroll (score=11.2)
- **Top mechanic:** Foregrounds losses publicly with red/green color coding, exploiting stockarithm's radical transparency angle to let power users prove their due diligence to skeptical communities.
- **Weakness:** Zero network effects or invitation mechanics—a Receipts Guy auditing trades alone doesn't create incentive or reason to share with others, making it purely consumptive.
- **Source:** `drafts/features/2026-04-23/openai-feature-04-receipts-guy-s-trade-history-scroll.md`

### 2. Bucket Thesis Statement (score=9.6)
- **Top mechanic:** Operator thesis becomes a public proof artifact—readers can screenshot/share the explicit failure logic and prediction criteria, which is rare and credible in fintech.
- **Weakness:** No incentive for users to *invite others* to see theses; it's consumption-only and doesn't leverage the two-sided market (winners/losers) as a shared discovery mechanism.
- **Source:** `drafts/features/2026-04-23/anthropic-feature-03-bucket-thesis-statement.md`

### 3. Alt-Data Nerd's Divergence Spotlight (score=9.6)
- **Top mechanic:** Lets expert traders spot anomalies others miss and share 'Biscotti found a weird pattern' moments that prove their edge.
- **Weakness:** No built-in sharing mechanism or leaderboard footprint—divergence discovery stays private unless user manually screenshots and posts.
- **Source:** `drafts/features/2026-04-23/openai-feature-03-alt-data-nerd-s-divergence-spotlight.md`

### 4. Trade Log Receipts (score=9.6)
- **Top mechanic:** Receipts Guys can download auditable trade logs and publicly verify the lab isn't gaming numbers—this is proof-of-work currency in a skeptical community that despises hidden losses.
- **Weakness:** Zero network effects or invitation loops; one user downloading a CSV doesn't pull in others, and there's no natural sharing mechanism beyond 'I checked the receipts myself.'
- **Source:** `drafts/features/2026-04-24/anthropic-feature-04-trade-log-receipts.md`

### 5. Biscotti's Blunder Board (score=9.6)
- **Top mechanic:** Failure leaderboard with zero euphemisms directly contradicts fintech norms, making users who share it look intellectually honest to skeptical communities like r/algotrading.
- **Weakness:** No invitation loop or network effect—users consume failure data but have zero reason to recruit others; it's a spectator feature, not a participation multiplier.
- **Source:** `drafts/features/2026-04-24/openai-feature-02-biscotti-s-blunder-board.md`

### 6. Receipts Export (score=9.0)
- **Top mechanic:** Data exports with explicit 'no survivorship bias' headers let skeptical traders prove to peers that stockarithm is genuinely transparent—the anti-hype flex in a hype category.
- **Weakness:** Zero network effects or invitation mechanics; a user exporting data doesn't pull anyone else into the product, so growth is entirely dependent on individual conversion.
- **Source:** `drafts/features/2026-04-22/anthropic-feature-04-receipts-export.md`

### 7. Force Rank Divergence View (score=8.96)
- **Top mechanic:** Lets skeptical traders spot and share algos that are visibly recovering from failure — pure narrative ammunition for the 'receipts guy' archetype who loves proving others wrong with data.
- **Weakness:** No incentive loop or sharing mechanic; a user finds a hot divergence but has zero reason to tell anyone else — it's pure consumption, not co-creation or social proof.
- **Source:** `drafts/features/2026-04-23/anthropic-feature-01-force-rank-divergence-view.md`

### 8. Divergence View (score=8.75)
- **Top mechanic:** Data-literate traders can spot and call out algos caught in lucky streaks, creating native credibility plays on r/algotrading by showing they read the fine print.
- **Weakness:** No incentive to share the finding—spotting a divergence is personal alpha, not social proof, so users hoard rather than broadcast.
- **Source:** `drafts/features/2026-04-22/anthropic-feature-01-divergence-view.md`

### 9. Bucket Audit Log (score=8.4)
- **Top mechanic:** Transparency of failure reasons (algo moved to noise: 40% win rate) lets users share audit logs as proof of rigorous methodology, exploiting the core unfair advantage of publishing failures.
- **Weakness:** No invitation mechanic or network effect—users audit algos alone; sharing a bucket transition log is interesting only to existing users, not a recruitment tool.
- **Source:** `drafts/features/2026-04-22/anthropic-feature-02-bucket-audit-log.md`

### 10. Trade-Level Signal Audit Trail (score=8.4)
- **Top mechanic:** Inspection-level transparency (signal conditions, SPY comparison) lets alt-data nerds prove signal legitimacy publicly in Reddit debates without screenshots—'Biscotti fired on [condition] while SPY did [this]' is shareable proof.
- **Weakness:** Read-only audit with no export or share button means users must manually transcribe findings to social; feature lives inside the product and doesn't naturally become a social artifact or conversation starter.
- **Source:** `drafts/features/2026-04-23/anthropic-feature-02-trade-level-signal-audit-trail.md`

### 11. Receipts Ledger: Loss Flags (score=8.4)
- **Top mechanic:** Loss flags directly amplify stockarithm's core unfair advantage (transparency) and give skeptical traders proof-of-honesty social currency when they cite it to peers.
- **Weakness:** Loss flags are table stakes for credibility, not shareable content—users don't screenshot loss data to flex or tell friends about, so invitation loop and public evidence are near zero.
- **Source:** `drafts/features/2026-04-23/openai-feature-01-receipts-ledger-loss-flags.md`

### 12. Drawdown Diary (score=8.4)
- **Top mechanic:** Transparency-first leaderboard column directly proves stockarithm publishes failures, turning the core unfair advantage into a visible, shareable proof point that skeptical traders can screenshot and cite.
- **Weakness:** Zero network effects or invitation mechanics—users don't need to recruit others to see drawdowns, and the feature doesn't create a reason to share or collaborate with peers.
- **Source:** `drafts/features/2026-04-24/anthropic-feature-01-drawdown-diary.md`

### 13. Signal Bucket Tags (score=8.4)
- **Top mechanic:** Operator's honest classification (ALPHA/NOISE/UNRESOLVED/DEAD) with visible override notes lets users cite the lab's own skepticism as proof they're not following hype—high social currency in anti-hype communities.
- **Weakness:** No incentive for users to invite others or share their bucket discoveries; filtering and categorization are personal utility, not network effects or public artifacts.
- **Source:** `drafts/features/2026-04-24/anthropic-feature-02-signal-bucket-tags.md`

### 14. Trade History Time Machine (score=8.4)
- **Top mechanic:** Transparent failure logging with zero obfuscation directly contradicts fintech norms and gives data-literate traders credibility ammunition to share ('look how honest this lab is').
- **Weakness:** No built-in sharing mechanism, invitation loop, or network effect—users consume the timeline privately; it doesn't naturally propagate to their networks or require others to join.
- **Source:** `drafts/features/2026-04-24/openai-feature-04-trade-history-time-machine.md`

### 15. Signal Bucket Explorer (score=7.68)
- **Top mechanic:** Torn-paper lab-notebook aesthetic + unfiltered failure language creates authentic credibility that skeptical traders want to screenshot and share as proof of non-hype.
- **Weakness:** Hover overlay is a passive information tool with zero incentive for users to invite others or create shareable moments—it solves friction but doesn't create word-of-mouth.
- **Source:** `drafts/features/2026-04-24/openai-feature-03-signal-bucket-explorer.md`

---

## BUILD_LATER List

- **Signal Hunter's Bucket View** (score=7.2) — Bucket classification directly leverages stockarithm's unique failures-published transparency—users can visibly filter ALPHA signals and share their curation, turning data triage into credible signal curation.
- **Signal Decay Curves** (score=6.72) — Visualizing failures with equal weight to wins directly exploits stockarithm's transparency unfair advantage and lets data-literate users spot contrarian signals worth discussing in r/algotrading.
- **Cross-Algo Pattern Spotter** (score=6.4) — Users can publicly claim they spotted a signal-type pattern before others (e.g., 'I saw weather algos were noise 3 months ago'), turning data analysis into social proof.
- **Bucket Migration Log** (score=5.76) — Shows classification volatility as proof of rigor—users can cite 'Biscotti bounced 4x in 60 days' to warn peers, leveraging the failures-published credibility angle.
- **Streak & Fade View** (score=4.8) — Exposes algo fade-outs and hot streaks in a way that rewards skeptical users who distrust all-time rankings—fits the transparency ethos perfectly.

---

## SKIP List

_None._
