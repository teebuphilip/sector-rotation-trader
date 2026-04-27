# Changelog

## 2026-04-27 (session 1 — landing copy pass kickoff)

### feat: start the landing-page conversion copy pass in the page generator
- `scripts/build_public_pages.py` now uses `StockArithm` in the landing title and hero copy, tightens the hero language around the public paper-trading lab, and changes the secondary CTA to `Get the weekly lab notes`.
- Replaced the redundant `public signals` proof pill with `Updated nightly`, changed `Paper-traded only` to `Paper-traded in public`, and rewrote the two top cards into the agreed explainer + leaderboard bridge copy.
- Softened the premium teaser so it reads like a future layer instead of a half-open offer.
- Completed the wider public-facing brand sweep in generated page titles plus static `docs/blog/index.html`, `docs/app.html`, and `docs/signals/lookup.html`, keeping `stockarithm.com` lowercase only for the domain/API URL.
- Tightened the first-read tone based on review feedback by changing the landing hero from `weird market signals` to `alternative data signals`, and restyled the footer attribution into a centered, smaller, italic line so it reads like attribution instead of a second banner.

### feat: add footer attribution across generated public pages
- `_footer_html(...)` now renders `StockArithm powered by R&B AlgoLabs, LLC.` ahead of the footer label.
- This applies to every public/generated page that uses the shared footer helper.
- Added the same attribution to the static blog index and premium app shell footer.

Files: `scripts/build_public_pages.py`, `CHANGELOG.md`

## 2026-04-25 (session 1 — fix public/preview publish git identity)

### fix: configure bot git identity inside public-site publisher repos
- `scripts/publish_public_site.py` now sets repo-local `git config user.name/user.email` before committing to `stockarithm-site`.
- `scripts/publish_preview_site.py` now does the same before committing to `stockarithm-preview`.
- This fixes the overnight GitHub Actions failures where both publish jobs cloned successfully but died at `git commit` with `Author identity unknown`.

Files: `scripts/publish_public_site.py`, `scripts/publish_preview_site.py`, `CHANGELOG.md`

## 2026-04-24 (session 8 — Reddit launch copy/script hardening)

### fix: tighten Reddit launch draft refresh around canonical ranks and stale-copy checks
- `scripts/refresh_reddit_drafts.py` now reads `data/rank_history.csv` for canonical force-rank positions and `docs/leaderboards/rolling_30d.json` for canonical rolling-30D ranks instead of approximating both from public leaderboard sorting.
- It now also reads `docs/data/public/daily.json` for current sector-summary language, supports optional manual overrides from `drafts/reddit_launch/overrides/YYYY-MM-DD.json`, and fails if unresolved placeholders or known stale canned phrases remain.
- Updated the launch templates under `drafts/reddit_launch/` to remove stale hardcoded claims, tighten channel-specific wording, and use `StockArithm` in prose while keeping `stockarithm.com` lowercase.

### fix: align social draft generator with the real deep-validation report schema
- `scripts/social_content_generator.py` now reads `system_state`, `force_rank.top_10`, `rolling_30d.top_10`, and related current keys from `reports/deep_validation/latest.json`.
- Added deterministic `temperature=0` and output linting for URL presence, stale `Stockarithm` casing, and unresolved placeholders before drafts are written.

### chore: schedule pre-launch LLM revalidation of Reddit copy
- Added a May 13 CSV task to run the Reddit launch copy back through LLM reviewers using fresh public numbers and current positioning before the May 15 post.

Files: `scripts/refresh_reddit_drafts.py`, `scripts/social_content_generator.py`, `drafts/reddit_launch/*.md`, `drafts/reddit_launch/PERSONAL_TOUCH.md`, `stockarithm_execution_plan.csv`, `content-generation.md`, `architecture.md`, `tldr-architecture.md`, `CHANGELOG.md`

## 2026-04-24 (session 7 — wire EIA key into nightly run)

### fix: export `EIA_API_KEY` in the main nightly workflow
- Added `EIA_API_KEY: ${{ secrets.EIA_API_KEY }}` to `.github/workflows/daily_run.yml`.
- The secret already existed in GitHub, but the main nightly job was not injecting it into the runner environment.
- Result: `electricity-consumption` was being recorded as blocked during `daily_run`, `cleanup_blocked_keys.py` could not clear it, and the email/quality outputs kept reporting `EIA_API_KEY` as missing.

Files: `.github/workflows/daily_run.yml`, `CHANGELOG.md`

## 2026-04-24 (session 6 — separate preview-site publish workflow)

### feat: add independent preview-site publisher
- Added `scripts/publish_preview_site.py` to build the private public+premium preview bundle and push it to `stockarithm-preview`.
- Added `.github/workflows/preview_site_publish.yml` so the preview repo can refresh on its own nightly schedule and via manual dispatch, without depending on or blocking the main trading workflow.
- Documented the new `PREVIEW_SITE_PUSH_TOKEN` secret in `PUBLIC_SITE_OPERATIONS.md`.

Files: `scripts/publish_preview_site.py`, `.github/workflows/preview_site_publish.yml`, `PUBLIC_SITE_OPERATIONS.md`, `CHANGELOG.md`

## 2026-04-24 (session 5 — restore live Yahoo runtime + stage proper migration design)

### chore: restore the live runtime path to the original Yahoo-backed implementation
- Reverted the active nightly/runtime entrypoints back to the original `scanner`/`precompute_signals.py` path for launch reliability.
- Restored the live workflow steps and helper scripts that had been pointed at the partial Polygon/Massive cutover.
- This keeps the nightly pipeline stable while the proper shared-snapshot migration is designed and built in parallel.

### docs: stage Polygon/Massive migration assets and write the real design
- Added `staging/polygon_massive_cutover/` with the staged Polygon/Massive files preserved for reference.
- Added `staging/polygon_massive_cutover/DESIGN.md` documenting the correct strategy: one shared market snapshot builder, one loader, and runtime consumers reading cached data instead of making repeated live fetches.
- Extended the design with a Yahoo-vs-Polygon shadow-run parity strategy so the migration can be validated nightly before production cutover.

Files: `daily_run.py`, `seed.py`, `.github/workflows/daily_run.yml`, `.github/workflows/crazy_daily_builds.yml`, `scripts/rolling_30d_leaderboard.py`, `scripts/backfill_spy_equity.py`, `scripts/autogen_crazy_factory.py`, `staging/polygon_massive_cutover/`, `CHANGELOG.md`

## 2026-04-24 (session 4 — ops integrity scan follow-up)

### fix: morning stats email header now matches the report date
- `scripts/daily_stats_email.py` now uses `AFH_RUN_DATE` for the top-of-email header instead of `datetime.utcnow()`.
- The subject already used `AFH_RUN_DATE`; this makes the body consistent with the intended previous-day report.

Files: `scripts/daily_stats_email.py`, `CHANGELOG.md`

## 2026-04-24 (session 3 — social content pipeline + Reddit launch drafts)

### feat: add daily social content generator
- Added `scripts/social_content_generator.py`: generates 5 Reddit channel variants (r/algotrading, r/investing, r/stocks, r/quant, r/SecurityAnalysis) and one Twitter/X post daily from the deep validation report. One LLM call per channel, facts-only, nothing invented. Outputs to `drafts/social/YYYY-MM-DD/`.
- Wired into `morning_content_email.yml` after `post_generator.py` so all 7 drafts land in one daily batch.

### feat: Reddit launch post templates + daily number refresh
- Added 5 channel-specific Reddit launch post templates in `drafts/reddit_launch/` with `{variable}` placeholders.
- Added `scripts/refresh_reddit_drafts.py`: reads `docs/data/public/leaderboard.json`, fills in all live numbers (algo count, beating SPY, top performers, Biscotti rank, worst performer, sector consensus), writes dated copies to `drafts/reddit_launch/YYYY-MM-DD/`.
- Added `drafts/reddit_launch/PERSONAL_TOUCH.md`: documents exactly which sections need Teebu's voice before posting — the Biscotti decision, the gut-check questions in r/algotrading and r/quant, and the macro commentary in r/SecurityAnalysis.
- Added `.github/workflows/reddit_draft_refresh.yml`: runs daily at 14:00 UTC, auto-stops after May 15 via date check. No manual disable needed.

Files: `scripts/social_content_generator.py`, `scripts/refresh_reddit_drafts.py`, `.github/workflows/morning_content_email.yml`, `.github/workflows/reddit_draft_refresh.yml`, `drafts/reddit_launch/`, `content-generation.md`, `architecture.md`, `tldr-architecture.md`, `CHANGELOG.md`

## 2026-04-24 (session 2 — Polygon signal coverage fix)

### fix: prevent Polygon/Massive signal precompute from collapsing under free-tier limits
- `precompute_signals_poly.py` no longer caches `None` sector mappings on transient lookup failures.
- Nightly callers now run `precompute_signals_poly.py --no-wiki` so the Polygon path uses the seeded fallback ticker list instead of trying to classify the full Wikipedia S&P 500 universe every run.
- Added the seeded `cache/ticker_sectors.json` mapping to the repo so GitHub Actions starts with known sector mappings for the nightly ticker set.
- Local dry-run sanity check now writes `105` ticker signals instead of the broken low-single-digit output seen in CI.

Files: `precompute_signals_poly.py`, `.github/workflows/daily_run.yml`, `.github/workflows/crazy_daily_builds.yml`, `scripts/autogen_crazy_factory.py`, `.gitignore`, `cache/ticker_sectors.json`, `CHANGELOG.md`

## 2026-04-24 (session 1 — Polygon/Massive cutover)

### feat: cut the live nightly pipeline over to Polygon/Massive
- Swapped `daily_run.py` and `seed.py` to import `scanner_polygon` instead of the old Yahoo-backed scanner.
- Updated `.github/workflows/daily_run.yml` and `.github/workflows/crazy_daily_builds.yml` to run `precompute_signals_poly.py`.
- Updated `scripts/rolling_30d_leaderboard.py` and `scripts/backfill_spy_equity.py` to use `scanner_polygon.safe_download`, removing remaining Yahoo exposure from the nightly leaderboard/SPY benchmark path.
- Updated `scripts/autogen_crazy_factory.py` so the factory refresh step now rebuilds signals through `precompute_signals_poly.py`.
- Verified the changed Python entrypoints compile cleanly.

Files: `daily_run.py`, `seed.py`, `.github/workflows/daily_run.yml`, `.github/workflows/crazy_daily_builds.yml`, `scripts/rolling_30d_leaderboard.py`, `scripts/backfill_spy_equity.py`, `scripts/autogen_crazy_factory.py`, `CHANGELOG.md`, `stockarithm_execution_plan.csv`

## 2026-04-23 (session 15 — feature generation pipeline)

### feat: wire virality scoring into weekly feature generation workflow
- Added `scripts/score_feature_virality.py`: one-shot per-run scorer, writes `reports/virality/YYYY-MM-DD.md` with per-feature dimension breakdown.
- Added `scripts/rank_features_nightly.py`: incremental ranker, caches scores by file MD5 (edits trigger rescore; unchanged files are free), force-ranks all unbuilt features into `reports/virality/master_rank.md` and `master_rank.json`.
- Added `scripts/mark_feature_built.py`: moves a PRD to `drafts/features/built/` (excluded from ranker's dated-subdir scan), removes cache entry. Supports partial name match and `--list` flag.
- Updated `.github/workflows/feature_ideas.yml` to score/rank after PRD generation and append V-Factor top-10 to the summary email.
- Fixed `scripts/feature_idea_generator.py`: `OPENAI_MODEL` / `ANTHROPIC_MODEL` now use `os.getenv() or default` so empty-string GitHub secrets fall back to model defaults.
- Set `temperature=0` in both scorer and ranker for deterministic, cache-stable results.
- Both scripts fixed: invalid model ID → `claude-haiku-4-5-20251001`, brand references updated to Stockarithm.

### docs: add feature-generation.md
- Documents the full pipeline: overview, files table, output layout, V-Factor scoring framework, local commands, workflow sequence, required secrets.

Files: `scripts/score_feature_virality.py`, `scripts/rank_features_nightly.py`, `scripts/mark_feature_built.py`, `scripts/feature_idea_generator.py`, `.github/workflows/feature_ideas.yml`, `feature-generation.md`, `README.md`, `tldr-architecture.md`, `CHANGELOG.md`

## 2026-04-23 (session 14 — private Vercel preview repo)

### feat: add temporary preview bundle builder for Vercel review
- Added `scripts/build_vercel_preview_site.py` to assemble a private review bundle from generated static artifacts in `docs/`.
- The preview bundle includes both the public site surface and premium/internal static pages so the full static experience can be inspected in Vercel before launch.
- It writes `_preview_index.html`, `vercel.json`, and `robots.txt` so the preview is easy to browse and is marked `noindex`.

### chore: create and seed private `stockarithm-preview` repo
- Created `teebuphilip/stockarithm-preview` as a private static preview repo.
- Published the first preview bundle there for Vercel import.
- Updated `PUBLIC_SITE_OPERATIONS.md` with preview-repo rules, manual publish steps, and Vercel setup notes.

Files: `scripts/build_vercel_preview_site.py`, `PUBLIC_SITE_OPERATIONS.md`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-23 (session 13 — public publish token docs)

### docs: explain how to create `PUBLIC_SITE_PUSH_TOKEN`
- Added exact fine-grained GitHub PAT steps to `PUBLIC_SITE_OPERATIONS.md`.
- Documented required permission: `Contents: Read and write` on only `stockarithm-site`.
- Added verification, rotation, and common failure notes.

Files: `PUBLIC_SITE_OPERATIONS.md`, `CHANGELOG.md`

## 2026-04-23 (session 12 — repo split seed + public publisher)

### chore: seed split repos
- Seeded private `stockarithm-api` with the FastAPI backend, backend architecture doc, README, requirements, and gitignore.
- Published the first allowlisted static bundle to public `stockarithm-site`.

### feat: add allowlist-only public site publisher
- Added `scripts/publish_public_site.py` to copy only public-safe files to `stockarithm-site`.
- The script validates the bundle for banned paths and secret-looking strings before commit.
- Wired `daily_run.yml` to publish the public site after the nightly commit when `PUBLIC_SITE_PUSH_TOKEN` is configured.
- Updated `PUBLIC_SITE_OPERATIONS.md` and `architecture.md` with publish/rollback notes.

Files: `scripts/publish_public_site.py`, `.github/workflows/daily_run.yml`, `PUBLIC_SITE_OPERATIONS.md`, `architecture.md`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-23 (session 11 — public site rollback script)

### feat: add safe rollback helper for public site repo
- Added `scripts/rollback_public_site.py` for reverting bad `stockarithm-site` publishes with `git revert`.
- The script refuses dirty repos, wrong branches, and local checkouts that are behind/ahead of `origin/main`.
- It does not use `reset --hard` or force-push.
- Added `PUBLIC_SITE_OPERATIONS.md` with rollback commands and safety rules.
- Added the public rollback task as `DONE` in `stockarithm_execution_plan.csv`.

Files: `scripts/rollback_public_site.py`, `PUBLIC_SITE_OPERATIONS.md`, `architecture.md`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-23 (session 10 — backend architecture docs)

### docs: document the premium backend at three levels
- Added `backend/BACKEND_ARCHITECTURE.md` with the detailed Railway/FastAPI/Stripe entitlement design, endpoint contract, runtime stores, cookie model, deployment plan, test plan, and staged-vs-done status.
- Updated `architecture.md` with the medium-depth backend summary: what Railway owns, why Auth0 is skipped, Stripe flow, webhook flow, and open launch items.
- Updated `tldr-architecture.md` with the plain-English version: static public site plus tiny paid-access API.

Files: `backend/BACKEND_ARCHITECTURE.md`, `architecture.md`, `tldr-architecture.md`, `CHANGELOG.md`

## 2026-04-23 (session 9 — Stripe test-mode premium backend)

### feat: stage Railway/FastAPI premium backend
- Added `backend/stockarithm_api.py`, a small FastAPI service for Stripe-backed premium access without Auth0.
- Supports Stripe test-mode checkout verification through `/unlock`, signed HTTP-only session cookies, `/api/me/status`, and Stripe signature-verified `/webhook`.
- Webhook records processed event IDs and handles checkout completion plus subscription cancel/pause/update events.
- Premium endpoints are gated by entitlement: leaderboard, per-signal detail, per-ticker detail, and CSV downloads.
- Added `docs/app.html` as the static premium frontend shell that checks entitlement and renders the gated leaderboard.
- Added `backend/README.md` with Railway/test-mode environment variables and endpoint notes.

### chore: mark backend-related V2 tasks as staged
- Marked Railway API service, Stripe webhook, magic-link/session auth, premium endpoints, app.html, and CSV downloads as `STAGED` in `stockarithm_execution_plan.csv`.
- These are not `DONE` until Railway deploy, Stripe test webhook setup, and end-to-end checkout validation are complete.

Files: `backend/stockarithm_api.py`, `backend/README.md`, `docs/app.html`, `requirements.txt`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-23 (session 8 — homepage hero copy)

### copy: write and apply Stockarithm homepage hero
- Added `drafts/homepage_hero.md` with the chosen hero, backup variant, CTA copy, proof strip, rationale, and phrases to avoid.
- Applied the chosen hero to the generated landing/index pages: "Weird market signals, run in public."
- Kept the copy away from AI stock-picking claims and pointed the visitor to the public leaderboard plus weekly lab notes.
- Marked `MARKETING: Write homepage hero text` as `DONE` in `stockarithm_execution_plan.csv`.

Files: `drafts/homepage_hero.md`, `scripts/build_public_pages.py`, `docs/index.html`, `docs/landing.html`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-23 (session 7 — Stockarithm rename)

### chore: replace legacy public branding with Stockarithm
- Updated public page generator titles and footer domain to `Stockarithm` / `stockarithm.com`.
- Regenerated public HTML pages so the live site surface uses `Stockarithm` / `stockarithm.com`.
- Updated launch/domain CSV tasks, MailerLite setup note, blog/signals static pages, LLM prompt copy, and the BTS user-agent string.

Files: `scripts/build_public_pages.py`, `docs/*.html`, `docs/blog/index.html`, `docs/signals/lookup.html`, `docs/marketing/mailerlite_setup.md`, `scripts/post_generator.py`, `scripts/feature_idea_generator.py`, `crazy/adapters/bts_airline_load_factor.py`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-23 (session 6 — public conversion proof blocks)

### feat: add live proof copy to public pages
- `scripts/build_public_pages.py` now emits a "Today in the Lab" pulse block on the leaderboard and daily report.
- The pulse uses real nightly public data: current leader, SPY-beating count when available, strongest/weakest sector consensus, and run date.
- The landing page hero now leads with concrete proof points: algos tracked, public signals, paper-traded only, and failures staying visible.

### copy: tighten mailing-list conversion language
- Replaced generic "join mailing list" copy with "Get the weekly lab notes."
- Changed the risky "0 deleted failures" claim to the safer, accurate "failures stay visible."
- Rebuilt generated public pages from the updated generator.

Files: `scripts/build_public_pages.py`, `docs/index.html`, `docs/landing.html`, `docs/leaderboard.html`, `docs/daily.html`, `docs/premium.html`, `docs/legal.html`, `CHANGELOG.md`

## 2026-04-23 (session 5 — May 15 Reddit learning post)

### chore: pull first Reddit learning post forward
- Updated `stockarithm_execution_plan.csv` so the first Reddit learning post is scheduled for `2026-05-15` instead of the later June window.
- Pulled supporting work earlier: homepage hero copy, Reddit draft, and landing-page conversion proof blocks now land before the May 15 post.
- The May 15 post is framed as a learning/discovery post, not the final paid launch.

Files: `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-23 (session 4 — quality check HOLD semantics)

### fix: quality check no longer treats normal HOLD-with-positions as warning noise
- `scripts/quality_check.py` now reads `meta[algo_id].last_signal` when available instead of falling back to snapshot-only `HOLD`.
- `POSITIONS WITH HOLD` is no longer emitted as a warning by default because `HOLD` means maintain/no rebalance in this simulator, not forced exit.
- Held-position/HOLD cases are now reported under `Context Notes`, leaving `Flags & Warnings` focused on actionable issues like churn, stale state, bad dates, or extreme losses.

Files: `scripts/quality_check.py`, `CHANGELOG.md`

## 2026-04-23 (session 3 — comparator data fix)

### fix: comparator suite now extracts yfinance close data robustly
- `scripts/comparison_nightly.py` now handles yfinance's single-ticker MultiIndex/DataFrame shape for `Close`.
- This removes the scalar-conversion warning path and prevents comparator rows from collapsing into `NEUTRAL` / `insufficient_data` when close data is actually present.
- Regenerated `docs/comparison/today.json` for `2026-04-22`; both momentum comparators now produce real UP/DOWN output across the 11 sector ETFs.

### chore: refresh public artifacts with working comparator context
- Rebuilt `docs/data/public/*` and static public pages after regenerating comparator output.

Files: `scripts/comparison_nightly.py`, `docs/comparison/today.json`, `docs/comparison/history.json`, `docs/data/public/*`, `docs/*.html`, `CHANGELOG.md`

## 2026-04-23 (session 2 — refresh deep validation nightly)

### fix: deep validation report is now regenerated by the nightly run
- `.github/workflows/daily_run.yml` now runs `scripts/write_deep_validation_report.py` after public pages are generated.
- The daily commit step now stages `reports/deep_validation/` so `latest.json` and `latest.md` stay current for downstream content automation.
- Regenerated `reports/deep_validation/2026-04-22.{json,md}` and refreshed `reports/deep_validation/latest.{json,md}`.

Why this matters:

- `scripts/post_generator.py` reads `reports/deep_validation/latest.json`.
- Before this fix, `latest.json` was stuck on `2026-04-15`, so the morning content email could use stale facts even while the trading pipeline was current.

Files: `.github/workflows/daily_run.yml`, `reports/deep_validation/2026-04-22.json`, `reports/deep_validation/2026-04-22.md`, `reports/deep_validation/latest.json`, `reports/deep_validation/latest.md`, `CHANGELOG.md`

## 2026-04-23 (session 1 — quality check #3)

### chore: complete Quality Check #3 early
- Added `quality_check_2026-04-27.md` with the current read on pipeline health, force-rank performance, crazy algo activity, blocked keys, comparator state, and warning items.
- Marked `Quality check #3` as `DONE` in `stockarithm_execution_plan.csv`.
- Pulled the staged Polygon cutover task forward from `2026-04-28` to `2026-04-27`.

Key findings:

- pipelines were green on the 2026-04-23 start-of-day check
- 112 algos are tracked: 5 normal, 107 crazy
- only 2 algos are currently beating SPY by force-rank
- crazy universe is mostly evidence collection: 33 active, 74 idle
- comparator suite is wired but currently all `insufficient_data`
- `reports/deep_validation/latest.json` is stale and needs follow-up before content automation should be trusted
- VIX family churn remains a watch item

Files: `quality_check_2026-04-27.md`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-22 (session 17 — ops integrity check + factory seed fix)

### fix: direct file-based crazy seeding no longer depends on registry presence
- `crazy_seed.py --algo-file ...` was previously converting the file path into an algo id and then asking the registry loader to find it.
- After the anti-orphan registry change, newly built algos were not appended to the registry until seed succeeded, so factory seeds failed with `No matching crazy algos found to seed`.
- `crazy_seed.py` now imports the provided file directly, finds the single `CrazyAlgoBase` subclass in that module, and seeds it without requiring a pre-existing registry entry.

### chore: record first recurring ops integrity scan
- Added `ops_integrity_2026-04-22.md` with the scan findings across ideation, tactical, and factory paths.
- Marked the first recurring `Validate ops/pipeline integrity — deep scan/check` CSV task as `DONE`.

Files: `crazy_seed.py`, `ops_integrity_2026-04-22.md`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-22 (session 16 — morning content email + post generator)

### feat: LLM post generator (scripts/post_generator.py)
- Reads `reports/deep_validation/latest.json` (or dated version), calls Claude API with locked facts only, writes `drafts/YYYY-MM-DD.md`.
- 300-400 word Substack draft: headline, lede, top 3 signals, weird signal/divergence, honest observation, CTA.
- Strictly facts-only — no invention, no metrics not in the report. Voice rules from content-generation.md enforced in system prompt.
- Defaults to `claude-haiku-4-5-20251001` via ANTHROPIC_MODEL secret.

### feat: morning content email (scripts/morning_content_email.py + morning_content_email.yml)
- New workflow runs at 09:30 UTC (4:30am EST) — 1 hour after morning stats email.
- Runs post_generator.py, commits draft to `drafts/`, emails full text to operator.
- On wake: two emails — 3:30am ops stats, 4:30am content draft ready to copy-paste to Substack.
- Substack push (cookie-auth) stays as a post-launch task in the CSV.

Files: `scripts/post_generator.py`, `scripts/morning_content_email.py`, `.github/workflows/morning_content_email.yml`

## 2026-04-22 (session 15 — public JSON schema v1)

### feat: define and version the public artifact contract
- Added `docs/data/public/SCHEMA.md` as the canonical field-level contract for the nightly public site payloads.
- The contract now explicitly documents shared algo row fields, daily snapshot fields, family payloads, benchmark payloads, and teaser-safe signal payloads.
- `scripts/build_public_artifacts.py` now stamps `schema_version: "v1"` onto public outputs so downstream consumers can rely on a declared contract version.

### chore: update core docs and task list to match the new public contract
- `docs/data/public/README.md`, `README.md`, `architecture.md`, and `tldr-architecture.md` now point to the versioned public schema documentation.
- Marked `V2 ARCH: Define public JSON schema` as `DONE` in `stockarithm_execution_plan.csv`.

Files: `scripts/build_public_artifacts.py`, `docs/data/public/SCHEMA.md`, `docs/data/public/README.md`, `README.md`, `architecture.md`, `tldr-architecture.md`, `stockarithm_execution_plan.csv`, `CHANGELOG.md`

## 2026-04-22 (session 14 — morning stats email clarity fixes)

### fix: idea rows in morning stats email now handle mixed raw schemas
- `scripts/daily_stats_email.py` no longer assumes every raw idea row has `idea_id` and `title`.
- Older raw idea runs that used `idea` now render with a derived slug instead of showing `(unknown)`.
- This fixes the morning email's `Ideas generated` section across mixed historical run formats.

### fix: force-rank section now uses market run date instead of latest idea-run date
- The morning email was reusing one mutable `run_date` for both idea-run reporting and market force-rank reporting.
- If the latest idea run directory was newer than the market data date, the email incorrectly printed `Force Rank: no rows for today`.
- The force-rank section now uses a separate `market_run_date` sourced from `AFH_RUN_DATE`/the intended reporting date.

### chore: clarify comparator and validation bookkeeping in morning email
- Comparator section now explicitly says it covers `11 sector ETFs` and shows `insufficient_data` counts.
- `Validation cache` wording was replaced with `Nightly validation snapshot tracker` plus a short note that it is internal validator bookkeeping.

Files: `scripts/daily_stats_email.py`, `CHANGELOG.md`

## 2026-04-22 (session 13 — Claude default model fallback)

### fix: crazy Claude generator now defaults to a current Anthropic model alias
- `scripts/crazy_generate_claude.sh` previously defaulted to `claude-3-haiku-20240307`, which now returns `404 not_found_error` for this repo's Anthropic setup when `ANTHROPIC_MODEL` is unset.
- The fallback now uses `claude-3-7-sonnet-20250219`, and the repo secret should also be set to that explicit model name.
- This avoids relying on stale Haiku defaults or moving aliases when the workflow secret is blank or unreadable.

Files: `scripts/crazy_generate_claude.sh`, `CHANGELOG.md`

## 2026-04-22 (session 12 — crazy idea failure visibility)

### fix: failed crazy idea runs now leave evidence in git and workflow logs
- `.github/workflows/crazy_ideas_daily.yml` now runs generation with `continue-on-error: true`, dumps `errors/*.txt` and response-code files, commits partial run outputs even on failure, then fails the workflow explicitly at the end.
- This prevents the previous blind spot where a failed idea run left no same-day directory in git and the tactical pipeline only reported `No crazy idea run found for today`.

### fix: crazy idea generator now prints provider error summaries before exiting
- `scripts/crazy_generate_high_action_ideas.py` now emits `[error-summary]` lines from `data/ideas/runs/<date>/errors/*.txt` when both providers fail.
- Future workflow logs will show the actual provider-side failure string instead of only `Both generators failed`.

### fix: nightly validation now distinguishes missing run vs failed run
- `scripts/validate_nightly.py` now checks `data/ideas/runs/<date>/errors/*.txt` when a same-day run exists but generated zero ideas.
- Validation now reports `crazy idea run failed; see errors/` instead of collapsing that case into a generic zero-ideas failure.

Files: `.github/workflows/crazy_ideas_daily.yml`, `scripts/crazy_generate_high_action_ideas.py`, `scripts/validate_nightly.py`, `CHANGELOG.md`

## 2026-04-21 (session 11 — factory backtest visibility)

### fix: factory backtest summary now exposes seeded vs matched vs reviewed
- `scripts/run_factory_backtests.py` now writes `seeded_ids`, `matched_algos`, and `missing_algo_ids` into `factory_results/summary.json`.
- Missing registry matches are no longer just a buried counter; the exact missing IDs are preserved in the summary.
- Zero-seeded runs now still write a fully shaped backtest summary block.

### fix: crazy build email now surfaces missing backtest visibility
- `scripts/crazy_build_email.py` now prints seeded IDs, matched algos, reviewed algos, and missing algo IDs from the factory backtest summary.
- If the backtest block is missing entirely, the email says so explicitly instead of silently skipping the section.

Files: `scripts/run_factory_backtests.py`, `scripts/crazy_build_email.py`, `CHANGELOG.md`

## 2026-04-21 (session 10 — ideation parse-failure hardening)

### fix: schema gate no longer crashes on one malformed JSONL line
- `scripts/crazy_schema_gate.py` now catches per-line `JSONDecodeError` instead of crashing the whole batch.
- Invalid lines are written to rejects with `invalid_json`, line number, reason, and raw line preview.
- The gate now prints `parse_failures=N` so partial-batch damage is visible in logs.

### fix: final publish gate now surfaces LLM parse fallbacks explicitly
- `scripts/final_publish_llm_gate.py` now prints a warning when the LLM response fails to parse and the spec is forced into `INTERVENTION`.
- The final-gate summary now includes `parse_failures`, and each file record includes `parse_failed`.
- This separates true intervention from parser failure in the operator view without changing the file-placement model yet.

Files: `scripts/crazy_schema_gate.py`, `scripts/final_publish_llm_gate.py`, `CHANGELOG.md`

## 2026-04-21 (session 9 — morning email comparator section)

### feat: daily_stats_email now reports comparator context
- Added a comparator section to `scripts/daily_stats_email.py`.
- If `docs/comparison/today.json` exists, the morning email now reports comparator direction counts plus mapped algos that look comparator-aligned or like potential comparator beaters.
- If comparator output is missing, the email says so explicitly instead of implying the data exists.

Files: `scripts/daily_stats_email.py`, `CHANGELOG.md`

## 2026-04-21 (session 8 — margin interest closeout fix)

### fix: margin interest allocation no longer depends on close order
- `portfolio.py:close_position` now snapshots opening borrowed principal and accrued interest for each close date and allocates interest against that batch snapshot.
- When multiple margin positions close on the same day, each close now receives its intended share regardless of which ticker closes first.
- Clears the batch helper once margin positions are gone or the date changes.

Files: `portfolio.py`, `CHANGELOG.md`

## 2026-04-21 (session 7 — leaderboard comparator badges)

### feat: show comparator context on the public leaderboard
- Added comparator summaries to the public artifact layer so leaderboard rows can carry simple baseline context when a clean sector-ETF mapping exists.
- `scripts/build_public_pages.py` now renders a compact `Comparators` column on `docs/leaderboard.html`.
- Current comparator badges are `5D` and `20D`, driven from `docs/comparison/today.json` when the nightly comparison run has produced data.
- If comparator data is missing or an algo cannot be cleanly mapped to a primary sector ETF, the page shows `n/a` instead of inventing a grade.

Files: `scripts/build_public_artifacts.py`, `scripts/build_public_pages.py`, `docs/data/public/leaderboard.json`, `docs/leaderboard.html`
- Added one small comparator explainer block to `docs/leaderboard.html` and `docs/daily.html` so the public site explains why these baseline badges exist.

## 2026-04-21 (session 6 — Kronos postpone + momentum baseline)

### feat: nightly comparator suite (comparison_nightly.py)
- `scripts/comparison_nightly.py` runs all baseline comparators against all 11 sector ETFs nightly.
- Current comparators: `momentum_5d` (5-day return) and `momentum_20d` (20-day return). Adding Kronos or any other baseline is one function + one COMPARATORS entry.
- Outputs `docs/comparison/today.json` and `docs/comparison/history.json` with a `comparators` dict keyed by name.
- Wired into `daily_run.yml` with `continue-on-error: true` — never blocks the main pipeline.
- Algo grading can score against all comparators simultaneously; an algo beating both momentum_5d and Kronos = strongest ALPHA signal.

### chore: postpone all Kronos tasks pending server provisioning
- Moved 5 Kronos CSV tasks to POSTPONED. NeoQuasar/Kronos-mini is not hosted on HuggingFace Inference API (local-only model requiring torch). Running it in GitHub Actions free tier would OOM.
- When the $6.99/mo server is provisioned, uncomment `_run_kronos` in `comparison_nightly.py` — zero other changes.

Files: `scripts/comparison_nightly.py`, `.github/workflows/daily_run.yml`, `stockarithm_execution_plan.csv`

## 2026-04-21 (session 5 — morning stats email)

### chore: shift morning stats email trigger to 08:30 UTC (3:30am EST)
- Changed cron from `0 8 * * *` to `30 8 * * *`.
- Note: shifts to 4:30am during EDT (UTC-4); change to `30 7 * * *` in spring if you want it pinned to 3:30am year-round.

Files: `.github/workflows/morning_stats_email.yml`


### feat: wire up daily_stats_email.py as a morning stats workflow
- New `.github/workflows/morning_stats_email.yml` runs daily and now fires at 08:30 UTC.
- Passes `AFH_RUN_DATE=yesterday` so the email reports on the previous day's completed runs (nightly book closes at 22:30 UTC, so all data is in place by the morning run).
- Supports `workflow_dispatch` with optional `run_date` override for replays.
- Uses existing `ALERT_EMAIL_TO`, `ALERT_EMAIL_USER`, `ALERT_EMAIL_PASS` secrets.

### fix: force rank section in daily_stats_email.py used hardcoded utcnow() date
- Line 331 was filtering `rank_history.csv` by `datetime.utcnow()` instead of `run_date`.
- When run in the morning for yesterday's data, force rank always showed "no rows for today".
- Now uses `run_date` (which respects `AFH_RUN_DATE`) consistently.

Files: `scripts/daily_stats_email.py`, `.github/workflows/morning_stats_email.yml`

## 2026-04-21 (session 4 — P2 operational pipeline fixes)

### fix: template-built algo is syntax-checked before being marked as built
- `build_template_algo.py` now runs `compile()` on the generated Python file immediately after writing it.
- If the generated code has syntax errors (e.g., unescaped quotes in idea name or adapter call), the file is removed and the script exits with code 1.
- The factory's existing `build_proc.returncode != 0` check catches this and marks the spec as `failed_build` instead of proceeding to a seed that would fail on import.

Files: `scripts/build_template_algo.py`

### fix: factory crash before summary.json is written now fails the workflow visibly
- Added "Verify factory summary written" step in `crazy_daily_builds.yml` immediately after the autogen step.
- If `summary.json` is missing (autogen crashed before completion), the job fails before the commit and email steps run.
- Previously, the email reported job success even when autogen crashed, because `continue-on-error: true` swallowed the failure and the only check was in a late "Assess" step that ran after the email.

Files: `.github/workflows/crazy_daily_builds.yml`

## 2026-04-21 (session 3 — P1 operational pipeline fixes)

### fix: registry entry now written only after seed succeeds, not after build
- `autogen_crazy_factory.py` was appending to `data/algos_registry_crazy.txt` immediately after a successful build, before `crazy_seed.py` ran.
- If seed failed, the algo was in the registry but unloadable — silently skipped on every future run.
- Registry append now happens only after both build and seed succeed (just before spec is moved to completed/).
- `--seed-only` mode skips the append since the algo was already registered in a prior build run.

Files: `scripts/autogen_crazy_factory.py`

### fix: single LLM generator failure now prints a warning
- `crazy_generate_high_action_ideas.py` previously swallowed ChatGPT or Claude failures silently — error written to file, nothing on stderr.
- Now prints `[warn] <generator> generator failed: <reason>` to stderr on each individual failure.
- Both-fail path already returned exit code 1; this adds visibility for the partial-failure case.

Files: `scripts/crazy_generate_high_action_ideas.py`

## 2026-04-21 (session 2 — P0 operational pipeline fixes)

### fix: state.json corruption no longer crashes the daily run
- `portfolio.py:load_state_from` now wraps `json.load()` in try/except for `JSONDecodeError`/`ValueError`.
- On corruption, prints a CRITICAL warning to stderr and falls back to `_default_state()` instead of raising.
- Previously a truncated state file (e.g. mid-write crash) would hard-fail the entire daily run.

Files: `portfolio.py`

### fix: stock data download failure with open positions now aborts instead of continuing silently
- `daily_run.py` previously continued with empty `prices_all` when yfinance failed on stock data.
- Exit signals would never fire (all tickers skipped), positions held indefinitely with no action.
- Now: if download fails and positions are open, exits with code 1. If no positions, continues with entry-only skip as before.

Files: `daily_run.py`

### fix: zero/negative price guard in open_position
- `portfolio.py:open_position` now rejects prices <= 0 before computing shares.
- Prevents `shares = inf` from corrupting state if yfinance returns a bad close price.

Files: `portfolio.py`

## 2026-04-21 (session 1 — crazy idea dedupe + prompt memory)

### feat: deterministic dedupe gate for crazy ideation
- Added `scripts/dedup_crazy_ideas.py` and wired it into the high-action idea pipeline after schema validation and before scoring/publish.
- Duplicate checks now compare the current run, existing algos, and recent idea history using normalized titles, structural fingerprints, and token overlap.
- New artifacts: `data/ideas/runs/YYYY-MM-DD/deduped/` and `data/ideas/runs/YYYY-MM-DD/duplicates/report.json`.
- `scripts/crazy_build_email.py` now reports dedupe keep/remove counts.

Files: `scripts/dedup_crazy_ideas.py`, `scripts/crazy_generate_high_action_ideas.py`, `scripts/crazy_score_ideas.py`, `scripts/crazy_publish_markdown.py`, `scripts/crazy_build_email.py`, `prompts/high_action_crazy_ideas_prompt.txt`, `prompts/high_action_crazy_ideas_prompt_claude.txt`

### feat: inject existing idea history into generator prompts
- `scripts/crazy_generate_high_action_ideas.py` now appends an `ANTI-DUPLICATE CONTEXT` block to both ChatGPT and Claude prompts.
- That context includes compact existing algo titles plus recent idea titles so the generators see prior work before proposing new ideas.
- This adds prompt-level prevention on top of the deterministic dedupe gate.

Files: `scripts/crazy_generate_high_action_ideas.py`
