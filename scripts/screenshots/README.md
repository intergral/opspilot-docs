# Documentation screenshots

Automated capture of app screenshots straight into the docs image folders,
using [Playwright](https://playwright.dev/python/).

## Setup

```bash
pip install playwright
python -m playwright install chromium
```

## Log in (one time)

Login is **Google SSO**, which can't be scripted reliably, so you log in once
by hand and the session is saved for reuse:

```bash
python scripts/screenshots/capture.py login
```

This opens a real browser window — complete the Google login, and the session
is saved to `.auth/state.json`. That file holds live auth cookies: it is
**gitignored and must never be committed**. Re-run this when the session expires.

Optional — target a different environment:

```bash
export OPSPILOT_BASE_URL=https://app.staging.opspilot.com   # default
```

## Capture

```bash
python scripts/screenshots/capture.py
```

Reuses the saved session (headless), opens each page in `ROUTES` (in
`capture.py`) in dark mode at a fixed viewport, and saves to its `out` path
under `docs/`.

## Status: prototype

Confirm/adjust before relying on it:

1. **`LOGGED_IN_MARKER`** — a selector that only appears when logged in. Set to
   `text=Alerting`; adjust if that nav label differs.
2. **App sub-route paths** — only `/alerting/` is confirmed; the rest are
   guesses. Verify them, or navigate by clicking the nav instead of by URL.
3. **Data-dependent views** — some tabs need a service/rule selected first, and
   live data varies run-to-run. Consider a seeded demo tenant for stable shots.
4. **Element vs full page** — set `full: True` per route for full-page shots.
