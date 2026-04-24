# r/investing — Launch Post Template
# Run: python scripts/refresh_reddit_drafts.py
# Output lands in drafts/reddit_launch/YYYY-MM-DD/investing.md with numbers filled in

---

**Title:** I built a public paper-trading lab using weird economic data — TSA counts, bankruptcy rates, the misery index — as market signals. Here's what {days_running} days of results looks like.

---

For the past {weeks_running} weeks I've been running a public paper-trading experiment called Stockarithm. The idea is simple: use alternative economic data — not price charts, not earnings — as signals for rotating between sector ETFs.

Examples of what I'm tracking:

- TSA airport checkpoint counts (travel demand proxy → XLY, XLI rotation)
- Bankruptcy filing rate (consumer stress → defensive sectors)
- Consumer misery index (unemployment + inflation → cash or XLP)
- Freight rail carload volumes (industrial activity → XLI, XLB)
- EV charger installation velocity (tech adoption → XLK)

Each signal has fixed rules. If it fires, rotate. If it reverses, rotate back. No discretion, no overrides.

**The honest results after {days_running} days**

{total_algos} signals running. {beating_spy} are beating SPY. The rest are flat or underperforming.

I'm not going to spin that. Most of these signals need more time. A month of data is a starting point, not a verdict. But the ones that aren't working are public and on the leaderboard alongside the ones that are.

The most interesting one right now: **Biscotti**, named after my dog who died in April 2025 while I was building this. It's ranked #{biscotti_rolling_rank} on the last 30 days ({biscotti_30d_return}%) but sits at #{biscotti_force_rank} overall. Good month, bad long-run record. I'm watching it, not celebrating it.

The worst: **{worst_name}** at {worst_return}% return. Still running. Removing underperformers after 30 days is exactly how survivorship bias works.

The whole point of this project is radical transparency — I publish the losing signals because anyone can build a track record that conveniently starts after the losses.

Everything is free to look at. No account, no paywall.

stockarithm.com — take a look and tell me what you think.
