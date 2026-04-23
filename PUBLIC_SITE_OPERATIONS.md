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

## Creating `PUBLIC_SITE_PUSH_TOKEN`

The nightly publisher needs a GitHub token that can push to `teebuphilip/stockarithm-site` from the private `sector-rotation-trader` workflow.

Recommended: use a fine-grained personal access token.

### 1. Create The Token

1. Go to GitHub.
2. Click your profile photo.
3. Open `Settings`.
4. Open `Developer settings`.
5. Open `Personal access tokens`.
6. Choose `Fine-grained tokens`.
7. Click `Generate new token`.
8. Token name: `stockarithm-site-publisher`.
9. Expiration: choose `90 days` or `180 days` to start. Do not use forever unless you have a reason.
10. Resource owner: `teebuphilip`.
11. Repository access: choose `Only select repositories`.
12. Select only `stockarithm-site`.

### 2. Set Token Permissions

Repository permissions:

- `Contents`: `Read and write`
- `Metadata`: `Read-only` (GitHub adds this automatically)

No other permissions should be needed.

Do not grant:

- Actions write
- Administration
- Secrets
- Pull requests
- Issues
- Packages
- Workflows

The token only needs to clone/fetch and push commits to the public static site repo.

### 3. Copy The Token Once

After clicking `Generate token`, copy the token immediately. GitHub will not show it again.

### 4. Add It To `sector-rotation-trader`

1. Go to `https://github.com/teebuphilip/sector-rotation-trader`.
2. Open `Settings`.
3. Open `Secrets and variables`.
4. Open `Actions`.
5. Click `New repository secret`.
6. Name:

```text
PUBLIC_SITE_PUSH_TOKEN
```

7. Value: paste the fine-grained token.
8. Save.

### 5. Verify It Works

After the next nightly run, check the `Daily Sector Rotation Run` workflow logs for:

```text
Publish public site repo
```

Expected behavior:

- clones or updates `stockarithm-site`
- runs `scripts/publish_public_site.py`
- commits only if public files changed
- pushes to `teebuphilip/stockarithm-site`

You can also trigger the workflow manually from GitHub Actions after adding the secret.

### 6. Rotation Rule

When the token expires:

1. Generate a new fine-grained token with the same repo-only `Contents: Read and write` permission.
2. Replace the `PUBLIC_SITE_PUSH_TOKEN` secret in `sector-rotation-trader`.
3. Delete/revoke the old token in GitHub Developer settings.

### 7. If It Fails

Common failures:

- `403`: token lacks `Contents: Read and write` on `stockarithm-site`.
- `Repository not found`: token was not granted access to `stockarithm-site`.
- `Authentication failed`: token pasted incorrectly or expired.
- Workflow skips publish step: secret is missing or empty.

Do not solve this by making the main repo public. Fix the token permission instead.

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
