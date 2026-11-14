#!/usr/bin/env python3
"""Weekly check that the Facebook settings the homepage feed relies on still work.

Run by .github/workflows/facebook-check.yml every Monday. If something has
changed it exits 1, the workflow opens an issue, and GitHub emails George.
Python 3 only, no extra packages. Run it by hand with:
    python3 scripts/check-facebook.py

Checks:
1. The Facebook SDK script the homepage loads is still served.
2. The Facebook version in index.html (version=vNN.0) is still listed by
   Facebook and is not within 60 days of its expiration date. (This is what
   broke the feed in October 2026: v20.0 expired on 24 Sep 2026.)
3. Facebook's Page Plugin documentation still offers tabs=timeline (what the
   homepage uses to show posts since November 2026, when Facebook stopped
   honouring show_posts), and its list of settings is unchanged since
   scripts/facebook-plugin-settings.txt was saved. If Facebook adds or drops
   a setting, check the homepage feed, then update that file.
"""
import datetime as dt
import html
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAVED_SETTINGS = ROOT / "scripts" / "facebook-plugin-settings.txt"
VERSIONS_URL = "https://developers.facebook.com/docs/graph-api/changelog/versions/"
PLUGIN_URL = "https://developers.facebook.com/docs/plugins/page-plugin/"
WARN_DAYS = 60
HEADERS = {
    # Facebook's documentation answers 400 to requests that don't look like a browser.
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Dest": "document",
}
# Settings named in the Page Plugin documentation (the "Settings" table).
# (Plain words like width and height appear all over the page, so only the
# distinctive names are compared.)
SETTING_NAMES = ["adapt_container_width", "hide_cover", "hide_cta", "show_facepile",
                 "show_posts", "small_header", "tabs"]
problems = []


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except (urllib.error.URLError, OSError) as e:
        return 0, str(e)


def text_of(page):
    page = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", page)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", page)))


index = (ROOT / "index.html").read_text(encoding="utf-8")
m = re.search(r"connect\.facebook\.net/en_US/sdk\.js#xfbml=1&version=(v\d+\.\d+)", index)
if not m:
    sys.exit("index.html: could not find the Facebook SDK script and its version.")
version = m.group(1)
print(f"The homepage uses Facebook version {version}.")

# 1. SDK script
status, body = get("https://connect.facebook.net/en_US/sdk.js")
if status == 200 and "FB" in body:
    print("OK  Facebook's SDK script is served.")
else:
    problems.append(f"Facebook's SDK script did not load (HTTP {status}).")

# 2. Version expiration date
status, body = get(VERSIONS_URL)
page = text_of(body)
date = r"(?:[A-Z][a-z]+ \d{1,2},\s*\d{4}|TBD)"
row = re.search(rf"\b{re.escape(version)} ({date}) ({date})", page)
if not row:
    problems.append(f"Could not find {version} in Facebook's version list (HTTP {status}). "
                    f"It may have been removed. Check {VERSIONS_URL}")
elif row.group(2) == "TBD":
    print(f"OK  {version} has no expiration date yet.")
else:
    end = dt.datetime.strptime(re.sub(r",\s*", ", ", row.group(2)), "%B %d, %Y").date()
    left = (end - dt.date.today()).days
    if left <= WARN_DAYS:
        problems.append(f"Facebook {version} expires on {end:%d %b %Y} ({left} days). "
                        "Ask Claude to update version= in index.html to the newest version.")
    else:
        print(f"OK  {version} works until {end:%d %b %Y} ({left} days).")

# 3. Page Plugin settings
status, body = get(PLUGIN_URL)
if status != 200 or "page-plugin" not in body:
    problems.append(f"Could not open Facebook's Page Plugin documentation (HTTP {status}). Check {PLUGIN_URL}")
else:
    found = [n for n in SETTING_NAMES if re.search(rf"\b{n}\b", body)]
    if "tabs" not in found or not re.search(r"timeline", body):
        problems.append("Facebook's Page Plugin documentation no longer offers tabs=timeline, "
                        "which the homepage uses to show posts.")
    else:
        print("OK  The Page Plugin still offers tabs=timeline.")
    current = "\n".join(found) + "\n"
    saved = SAVED_SETTINGS.read_text() if SAVED_SETTINGS.exists() else ""
    if saved != current:
        problems.append("Facebook's list of Page Plugin settings has changed.\n"
                        f"   Before: {', '.join(saved.split()) or '(none saved)'}\n"
                        f"   Now:    {', '.join(found)}")
    else:
        print(f"OK  Page Plugin settings unchanged ({', '.join(found)}).")

if problems:
    print("\nSomething has changed:")
    for p in problems:
        print(" -", p)
    print("\nCheck the homepage Facebook card, then ask Claude to look at this report.")
    sys.exit(1)
print("\nAll Facebook checks passed.")
