"""
Automated documentation screenshots via Playwright.

Captures OpsPilot app pages and writes the PNGs straight into the docs image
folders, so screenshots can be refreshed in one run instead of pasted by hand.

Login is Google SSO, which can't be scripted reliably, so it's a two-step flow:

  1. One-time login - opens a real browser window; you complete the Google
     login by hand, and the authenticated session is saved locally:

        python scripts/screenshots/capture.py login

  2. Capture - reuses that saved session (headless) to grab every screenshot:

        python scripts/screenshots/capture.py

The saved session (.auth/state.json) holds live auth cookies - it is
gitignored and must never be committed. Re-run `login` when it expires.

Setup (one time):
    pip install playwright
    python -m playwright install chromium

Optional env var:
    OPSPILOT_BASE_URL   default: https://app.staging.opspilot.com
"""
import sys
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("OPSPILOT_BASE_URL", "https://app.staging.opspilot.com").rstrip("/")

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
AUTH_FILE = HERE / ".auth" / "state.json"

# A selector that only appears once logged in - used to detect a completed
# login and to confirm each page is ready. Adjust if the nav label differs.
LOGGED_IN_MARKER = "text=Alerting"

IMG = "docs/Data-insights/Features/images/Alerting"

# Prototype: a few alerting routes. Extend from the Sidebar-routes map.
# NOTE: only /alerting/ is confirmed; the rest are guesses - verify against
# staging, or navigate by clicking the nav instead of by URL.
ROUTES = [
    {"path": "/alerting/", "out": f"{IMG}/status.png", "wait": "text=Status"},
    # {"path": "/alerting/rules", "out": f"{IMG}/rule-table.png", "wait": "text=Rules"},
    # {"path": "/alerting/notifications", "out": f"{IMG}/notification-policy.png", "wait": "text=Contact Points"},
]

VIEWPORT = {"width": 1600, "height": 900}


def do_login():
    """Open a real browser, let the user complete Google SSO, save the session."""
    with sync_playwright() as p:
        # channel="chrome" uses installed Chrome so Google doesn't flag it as
        # an insecure/automated browser. Falls back to bundled Chromium if absent.
        try:
            browser = p.chromium.launch(headless=False, channel="chrome")
        except Exception:
            browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(f"{BASE_URL}/")
        print("Complete the Google login in the browser window (up to 3 min)...")
        page.wait_for_selector(LOGGED_IN_MARKER, timeout=180_000)
        AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)
        context.storage_state(path=str(AUTH_FILE))
        print(f"Saved session to {AUTH_FILE}")
        browser.close()


def _load(page, url, marker, tries=2):
    """Navigate to url; if the marker is missing (e.g. the app error boundary),
    reload and retry. Returns True once the marker is visible (or no marker)."""
    for attempt in range(tries):
        page.goto(url, wait_until="domcontentloaded")
        if not marker:
            return True
        try:
            page.wait_for_selector(marker, timeout=15_000)
            return True
        except Exception:
            if attempt < tries - 1:
                print("   marker missing (possible load error) - reloading...")
                page.wait_for_timeout(1000)
    return False


def capture():
    if not AUTH_FILE.exists():
        sys.exit("No saved session. Run:  python scripts/screenshots/capture.py login")

    with sync_playwright() as p:
        # Run headed with real Chrome. The app's visualisations (honeycomb, etc.)
        # need GPU/WebGL that headless disables, so headless hits the app's
        # "This page couldn't load" error boundary. A window pops up per run.
        try:
            browser = p.chromium.launch(channel="chrome", headless=False)
        except Exception:
            browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state=str(AUTH_FILE),
            viewport=VIEWPORT,
            color_scheme="dark",  # match the dark-mode docs screenshots
        )
        page = context.new_page()

        for r in ROUTES:
            url = f"{BASE_URL}{r['path']}"
            print(f"-> {url}")
            if not _load(page, url, r.get("wait")):
                print(f"   WARN: '{r.get('wait')}' not found after retry - capturing anyway")
            page.wait_for_timeout(2500)  # let the SPA render / charts settle
            out = REPO_ROOT / r["out"]
            out.parent.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(out), full_page=r.get("full", False))
            print(f"   saved {r['out']}")

        browser.close()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "login":
        do_login()
    else:
        capture()
