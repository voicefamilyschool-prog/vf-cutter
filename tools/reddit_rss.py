#!/usr/bin/env python3
"""Read Reddit via public RSS feeds (JSON/HTML endpoints are blocked from this network).

Usage:
  python3 reddit_rss.py search <subreddit> "<query>" [sort=top|relevance|new|comments] [t=all|year|month] [limit=25]
  python3 reddit_rss.py comments <post_url> [limit=40]
Output: plain text, one item per block.
"""
import html
import re
import subprocess
import sys
import time
import urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) research-bot"


def fetch(url):
    time.sleep(3)  # be polite, avoid rate limits
    for attempt in range(5):
        out = subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-w", "\n%{http_code}", url],
                             capture_output=True, text=True)
        body, _, code = out.stdout.rpartition("\n")
        if code == "200":
            return body
        time.sleep(10 * (attempt + 1))
    sys.exit(f"HTTP {code} for {url}")


def clean(s):
    s = html.unescape(s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def entries(xml):
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        title = re.search(r"<title>(.*?)</title>", e, re.S)
        link = re.search(r'<link href="([^"]+)"', e)
        content = re.search(r'<content type="html">(.*?)</content>', e, re.S)
        date = re.search(r"<updated>(.*?)</updated>", e)
        yield (clean(title.group(1)) if title else "", link.group(1) if link else "",
               clean(content.group(1)) if content else "", date.group(1)[:10] if date else "")


def main():
    cmd = sys.argv[1]
    if cmd == "search":
        sub, q = sys.argv[2], sys.argv[3]
        kw = dict(a.split("=", 1) for a in sys.argv[4:])
        params = {"q": q, "restrict_sr": "1", "sort": kw.get("sort", "relevance"),
                  "t": kw.get("t", "all"), "limit": kw.get("limit", "25")}
        url = f"https://www.reddit.com/r/{sub}/search.rss?" + urllib.parse.urlencode(params)
        for t, l, c, d in entries(fetch(url)):
            print(f"### {t}\n{l}  ({d})\n{c[:700]}\n")
    elif cmd == "comments":
        url = sys.argv[2].split("?")[0].rstrip("/") + "/.rss?limit=" + (sys.argv[3] if len(sys.argv) > 3 else "40")
        items = list(entries(fetch(url)))
        if items:
            t, l, c, d = items[0]
            print(f"POST: {t}\n{l} ({d})\n{c[:1500]}\n\nCOMMENTS:")
        for t, l, c, d in items[1:]:
            print(f"- {c[:600]}\n  {l}\n")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
