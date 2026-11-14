#!/usr/bin/env python3
"""Weekly check that the Facebook settings the homepage feed relies on still work.

Run by .github/workflows/facebook-check.yml. Exits 1 (and the workflow emails
the owner) when something has changed. Python 3 only, no extra packages.

Checks:
1. The Facebook SDK script the homepage loads is still served.
2. The Facebook version named in index.html (version=vNN.0) is still accepted
   by Facebook, and is not within 60 days of its end date.
3. Facebook's Page Plugin documentation still lists the settings we use
   (tabs=timeline etc.), and its list of settings has not changed since
   scripts/facebook-plugin-settings.txt was saved.
"""
import datetime as dt
import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAVED_SETTINGS = ROOT / "scripts" / "facebook-plugin-settings.txt"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
WARN_DAYS = 60
problems = []


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except (urllib.error.URLError, OSError) as e:
        return 0, str(e)


def text_of(page):
    page = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", page)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", page)))


index = (ROOT / "index.html").read_text(encoding="utf-8")
m = re.search(r"connect\.facebook\.net/en_US/sdk\.js#xfbml=1&version=v(\d+)\.0", index)
if not m:
    sys.exit("index.html: could not find the Facebook SDK script and version.")
major = int(m.group(1))
version = f"v{major}.0"
print(f"Homepage uses Facebook version {version}.")

# 1. SDK script
status, body = get("https://connect.facebook.net/en_US/sdk.js")
if status == 200 and "FB" in body:
    print("OK  Facebook SDK script is served.")
else:
    problems.append(f"Facebook SDK script returned HTTP {status}.")

# 2a. Version still accepted (no access token: a live version answers
#     'access token required'; an expired one names the version).
status, body = get(f"https://graph.facebook.com/{version}/samuigreenacreschool")
try:
    err = json.loads(body).get("error", {})
except ValueError:
    err = {"message": body[:200]}
msg = str(err.get("message", ""))
if re.search(r"version|deprecat|no longer", msg, re.I) and not re.search(r"access token", msg, re.I):
    problems.append(f"Facebook no longer accepts {version}: {msg}")
else:
    print(f"OK  Facebook still accepts {version} (reply: {msg[:90]}).")

# 2b. End date from Facebook's version list.
status, body = get("https://developers.facebook.com/docs/graph-api/changelog/versions/")
page = text_of(body) if status == 200 else ""
row = re.search(rf"{re.escape(version)}\b(.{{0,160}})", page)
dates = []
if row:
    for d in re.findall(r"([A-Z][a-z]+ \d{1,2}, \d{4})", row.group(1)):
        try:
            dates.append(dt.datetime.strptime(d, "%B %d, %Y").date())
        except ValueError:
            pass
if len(dates) >= 2:
    end = max(dates)
    left = (end - dt.date.today()).days
    if left <= WARN_DAYS:
        problems.append(f"Facebook {version} stops working on {end:%d %b %Y} ({left} days). Update version= in index.html.")
    else:
        print(f"OK  {version} works until {end:%d %b %Y} ({left} days).")
else:
    problems.append(
        f"Could not read the end date for {version} from Facebook's version list "
        f"(HTTP {status}). Check https://developers.facebook.com/docs/graph-api/changelog/versions/ by hand."
    )
    print("DEBUG version page:", page[:1500])

# 3. Page Plugin settings.
status, body = get("https://developers.facebook.com/docs/plugins/page-plugin/")
page = text_of(body) if status == 200 else ""
names = sorted(set(re.findall(r"\b(adapt_container_width|hide_cover|hide_cta|height|href|lazy|show_facepile|show_posts|small_header|tabs|width)\b", page)))
found = sorted(set(re.findall(r"\b([a-z]+(?:_[a-z]+)+)\b", page)))
if not page:
    problems.append(f"Could not open Facebook's Page Plugin documentation (HTTP {status}).")
elif "tabs" not in names or "timeline" not in page:
    problems.append("Facebook's Page Plugin documentation no longer mentions tabs=timeline, which the homepage uses to show posts.")
else:
    print("OK  Page Plugin documentation still lists tabs=timeline.")
print("DEBUG plugin page settings seen:", names)
print("DEBUG plugin page words_with_underscores:", found[:80])
current = "\n".join(names) + "\n"
if SAVED_SETTINGS.exists():
    saved = SAVED_SETTINGS.read_text()
    if page and saved != current:
        problems.append(
            "Facebook's list of Page Plugin settings has changed.\n  Before: "
            + ", ".join(saved.split()) + "\n  Now:    " + ", ".join(current.split())
        )
    elif page:
        print("OK  Page Plugin settings unchanged.")

if problems:
    print("\nPROBLEMS FOUND:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("\nAll Facebook checks passed.")
