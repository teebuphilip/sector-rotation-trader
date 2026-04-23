# Public Site Operations

## Repos

Target split:

- `sector-rotation-trader`: private trading engine, pipeline, source logic, backend staging, artifact generation.
- `stockarithm-site`: public static site only.
- `stockarithm-api`: private Railway backend only.

The public site repo should never receive trading source code, backend code, raw state, raw idea runs, ledgers, or private artifacts.


## Publish Script

Script:

```bash
python scripts/publish_public_site.py
```

The publisher copies only an explicit allowlist from this private repo into `stockarithm-site`:

- public HTML pages
- `docs/blog/`
- `docs/data/public/`
- `docs/signals/lookup.html`
- `CNAME`
- `.nojekyll`

It does not mirror `docs/` wholesale. It validates the bundle for banned paths and secret-looking strings before commit.

Dry run:

```bash
python scripts/publish_public_site.py --dry-run
```

Manual publish:

```bash
python scripts/publish_public_site.py --repo-dir ../stockarithm-site --push
```

Nightly publish uses `PUBLIC_SITE_PUSH_TOKEN` as a GitHub Actions secret. The token needs write access to `teebuphilip/stockarithm-site`.

## Rollback Script

Script:

```bash
python scripts/rollback_public_site.py
```

Purpose:

- safely rollback a bad public-site publish
- operate on the public `stockarithm-site` repo
- use `git revert`, not `git reset --hard` or force-push
- optionally push after review

Default remote:

```text
git@github.com:teebuphilip/stockarithm-site.git
```

Default branch:

```text
main
```

## Dry Run

Use this first:

```bash
python scripts/rollback_public_site.py --repo-dir ../stockarithm-site --dry-run
```

If no local checkout exists, the script can clone to a temp directory:

```bash
python scripts/rollback_public_site.py --dry-run
```

## Roll Back Latest Public Publish

Review first:

```bash
python scripts/rollback_public_site.py --repo-dir ../stockarithm-site --count 1
```

Then push:

```bash
python scripts/rollback_public_site.py --repo-dir ../stockarithm-site --count 1 --push --reason "bad nightly public publish"
```

## Roll Back A Specific Commit

```bash
python scripts/rollback_public_site.py \
  --repo-dir ../stockarithm-site \
  --commit <commit_sha> \
  --push \
  --reason "revert broken leaderboard publish"
```

## Safety Checks

The script refuses to proceed if:

- target is not a git repo
- target repo has uncommitted changes
- target repo is not on the expected branch
- local `HEAD` is not equal to `origin/main`

The script intentionally does not use destructive git commands.

## Operational Rule

Rollback is for the public display repo only. Do not use this script against `sector-rotation-trader`.
