#!/usr/bin/env python3
"""Helpers for open customer-voice sources reachable from the research sandbox.

Usage:
  python3 tools/open_sources.py apps "<term>" [country=us] [limit=10]
      App Store search: app id, name, rating count.
  python3 tools/open_sources.py gplay "<term>"
      Google Play search: package ids found on the search page.
  python3 tools/open_sources.py playreviews <package> [n=150] [sort=newest|relevant|rating] [country=us] [maxstars=5]
      Google Play reviews (text, stars, date, thumbs-up).
  python3 tools/open_sources.py suggest "<seed>" [expand=1]
      Google search autocomplete; expand=1 adds a-z suffixes (demand / wording signals).
  python3 tools/open_sources.py ytsearch "<query>" [limit=10]
      YouTube search: video id, title, channel, views.
  (App Store review feeds are empty and YouTube watch pages hit a captcha from this network.)
  python3 tools/open_sources.py wayback <url> <year>
      Closest Wayback Machine snapshot URL for a page in a given year.
"""
import json
import re
import string
import subprocess
import sys
import time
import urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"


def get(url, data=None, headers=None):
    time.sleep(1)
    cmd = ["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9"]
    for k, v in (headers or {}).items():
        cmd += ["-H", f"{k}: {v}"]
    if data is not None:
        cmd += ["-H", "Content-Type: application/json", "--data", json.dumps(data)]
    out = subprocess.run(cmd + [url], capture_output=True, text=True)
    return out.stdout


def kw(args):
    return dict(a.split("=", 1) for a in args if "=" in a)


def apps(term, country="us", limit="10"):
    q = urllib.parse.urlencode({"term": term, "entity": "software", "country": country, "limit": limit})
    for a in json.loads(get("https://itunes.apple.com/search?" + q))["results"]:
        print(a["trackId"], "|", a["trackName"], "|", a.get("sellerName"), "| ratings:", a.get("userRatingCount"),
              "| avg:", round(a.get("averageUserRating", 0), 2))


def reviews(app_id, country="us", pages="3", maxstars="5"):
    for p in range(1, int(pages) + 1):
        url = f"https://itunes.apple.com/{country}/rss/customerreviews/page={p}/id={app_id}/sortby=mostrecent/json"
        try:
            entries = json.loads(get(url))["feed"].get("entry", [])
        except Exception:
            break
        if isinstance(entries, dict):
            entries = [entries]
        for e in entries:
            if "im:rating" not in e:
                continue
            stars = int(e["im:rating"]["label"])
            if stars > int(maxstars):
                continue
            print(f"[{stars}★ {e.get('updated', {}).get('label', '')[:10]}] {e['title']['label']}: "
                  f"{e['content']['label'][:800]}\n  https://apps.apple.com/{country}/app/id{app_id}\n")


def gplay(term):
    html = get("https://play.google.com/store/search?c=apps&hl=en&gl=US&q=" + urllib.parse.quote(term))
    seen = []
    for pkg in re.findall(r"/store/apps/details\?id=([\w.]+)", html):
        if pkg not in seen:
            seen.append(pkg)
    for pkg in seen[:15]:
        print(pkg)


def playreviews(package, n="150", sort="newest", country="us", maxstars="5"):
    order = {"relevant": 1, "newest": 2, "rating": 3}[sort]
    token, got = None, 0
    while got < int(n):
        page = [2, order, [40, None, token], None, []] if token else [2, order, [40, None, None], None, []]
        inner = json.dumps([None, None, page, [package, 7]])
        body = "f.req=" + urllib.parse.quote(json.dumps([[["UsvDTd", inner, None, "generic"]]]))
        time.sleep(1)
        out = subprocess.run(["curl", "-sS", "-m", "30", "-H", "Content-Type: application/x-www-form-urlencoded;charset=UTF-8",
                              "--data", body, f"https://play.google.com/_/PlayStoreUi/data/batchexecute?hl=en&gl={country}"],
                             capture_output=True, text=True).stdout
        line = next((l for l in out.split("\n") if l.startswith('[["wrb.fr"')), None)
        if not line or not json.loads(line)[0][2]:
            break
        data = json.loads(json.loads(line)[0][2])
        for r in data[0] or []:
            stars = r[2]
            if stars is None or stars > int(maxstars):
                continue
            date = time.strftime("%Y-%m-%d", time.gmtime(r[5][0])) if r[5] else ""
            print(f"[{stars}★ {date} 👍{r[6]}] {(r[4] or '')[:800]}\n  https://play.google.com/store/apps/details?id={package}\n")
            got += 1
        token = data[1][1] if len(data) > 1 and data[1] and len(data[1]) > 1 else None
        if not token:
            break


def suggest(seed, expand="0"):
    seeds = [seed] + ([f"{seed} {c}" for c in string.ascii_lowercase] if expand == "1" else [])
    seen = set()
    for s in seeds:
        url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=" + urllib.parse.quote(s)
        try:
            for sug in json.loads(get(url))[1]:
                if sug not in seen:
                    seen.add(sug)
                    print(sug)
        except Exception:
            pass


def _initial_data(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    return json.loads(m.group(1)) if m else {}


def _walk(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                yield v
            yield from _walk(v, key)
    elif isinstance(o, list):
        for i in o:
            yield from _walk(i, key)


def ytsearch(query, limit="10"):
    html = get("https://www.youtube.com/results?search_query=" + urllib.parse.quote(query))
    n = 0
    for v in _walk(_initial_data(html), "videoRenderer"):
        title = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
        ch = "".join(r.get("text", "") for r in v.get("ownerText", {}).get("runs", []))
        views = v.get("viewCountText", {}).get("simpleText", "")
        print(v["videoId"], "|", title, "|", ch, "|", views)
        n += 1
        if n >= int(limit):
            break


def ytcomments(video_id, limit="100"):
    html = get(f"https://www.youtube.com/watch?v={video_id}")
    key = re.search(r'"INNERTUBE_API_KEY":"([^"]+)"', html)
    ver = re.search(r'"INNERTUBE_CLIENT_VERSION":"([^"]+)"', html)
    data = _initial_data(html)
    token = None
    for sec in _walk(data, "itemSectionRenderer"):
        if sec.get("sectionIdentifier") == "comment-item-section":
            for t in _walk(sec, "token"):
                token = t
                break
    if not (key and ver and token):
        sys.exit("comments not available")
    ctx = {"client": {"clientName": "WEB", "clientVersion": ver.group(1), "hl": "en", "gl": "US"}}
    got = 0
    while token and got < int(limit):
        resp = json.loads(get(f"https://www.youtube.com/youtubei/v1/next?key={key.group(1)}",
                              data={"context": ctx, "continuation": token}) or "{}")
        token = None
        for m in _walk(resp, "commentEntityPayload"):
            props = m.get("properties", {})
            text = props.get("content", {}).get("content", "")
            likes = m.get("toolbar", {}).get("likeCountNotliked", "")
            if text:
                print(f"- ({likes} likes) {text[:600]}")
                got += 1
        for cmd in _walk(resp, "continuationCommand"):
            token = cmd.get("token")
    print(f"\nhttps://www.youtube.com/watch?v={video_id}")


def wayback(url, year):
    d = json.loads(get(f"https://archive.org/wayback/available?url={urllib.parse.quote(url)}&timestamp={year}0601"))
    snap = d.get("archived_snapshots", {}).get("closest", {})
    print(snap.get("url", "no snapshot"), snap.get("timestamp", ""))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd, arg, rest = sys.argv[1], sys.argv[2], kw(sys.argv[3:])
    pos = [a for a in sys.argv[3:] if "=" not in a]
    if cmd == "apps":
        apps(arg, **rest)
    elif cmd == "reviews":
        reviews(arg, **rest)
    elif cmd == "gplay":
        gplay(arg)
    elif cmd == "playreviews":
        playreviews(arg, **rest)
    elif cmd == "suggest":
        suggest(arg, **rest)
    elif cmd == "ytsearch":
        ytsearch(arg, **rest)
    elif cmd == "ytcomments":
        ytcomments(arg, **rest)
    elif cmd == "wayback":
        wayback(arg, pos[0])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
