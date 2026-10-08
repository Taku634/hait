#!/usr/bin/env python3
"""Enumerate every specialist profile slug on the three IHH Singapore hospital sites
by recursively splitting the server-rendered A-Z listing (10 cards per render)."""
import json, re, sys, time, os, threading
from concurrent.futures import ThreadPoolExecutor
import requests

OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/-home-user-hait/b7e37d37-3089-5521-898b-2c45859470a0/scratchpad/out"
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
SITES = {
    "ME": ("https://www.mountelizabeth.com.sg", ["mount-elizabeth-hospital", "mount-elizabeth-novena-hospital"]),
    "GEH": ("https://www.gleneagles.com.sg", []),
    "PEH": ("https://www.parkwayeast.com.sg", []),
}
SPECS = [x["URLName"] for x in json.load(open(os.path.join(os.path.dirname(OUT), "dl", "dd_mountelizabeth_specialty.json")))]
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
sess = requests.Session()
sess.headers["User-Agent"] = UA
lock = threading.Lock()
cache = {}
cards = {}   # site -> slug -> card dict
calls = [0]

CARD_RE = re.compile(r'<div class="item-content type-specialists">(.*?)<div data-elastic-exclude class="d-flex action-content">', re.S)

def fetch(site, params):
    base, _ = SITES[site]
    key = (site, tuple(sorted(params.items())))
    if key in cache:
        return cache[key]
    url = base + "/patient-services/specialists"
    for attempt in range(5):
        try:
            r = sess.post(url, params=params, timeout=60)  # POST bypasses Sitefinity output cache on GEH/PEH
            if r.status_code == 200 and "fmpld_dt_foundPageItems" in r.text:
                break
        except Exception as e:
            pass
        time.sleep(2 * (attempt + 1))
    else:
        print("FAILED", site, params, file=sys.stderr)
        return (None, [])
    h = r.text
    m = re.search(r"fmpld_dt_foundPageItems = (\d+)", h)
    cnt = int(m.group(1)) if m else None
    found = []
    for block in CARD_RE.findall(h):
        s = re.search(r'specialists/profile/([^"?&]+)', block)
        if not s:
            continue
        slug = s.group(1)
        name = re.search(r"<h5><a[^>]*><b>(.*?)</b>", block)
        desig = re.search(r'class="detail-designation">(.*?)</p>', block)
        alt = re.search(r'alt="([^"]*)"', block)
        ins = re.search(r'class="detail-insurance"><span>Insurance Panel</span><br>(.*?)</p>', block)
        d = {"slug": slug, "name": name.group(1).strip() if name else None,
             "designation": desig.group(1).strip() if desig else None,
             "alt": alt.group(1) if alt else None,
             "insurance": ins.group(1).strip() if ins else None}
        found.append(d)
        with lock:
            cards.setdefault(site, {}).setdefault(slug, d)
    with lock:
        calls[0] += 1
        cache[key] = (cnt, found)
        if calls[0] % 25 == 0:
            print("calls", calls[0], "cards", {k: len(v) for k, v in cards.items()}, flush=True)
    return cnt, found

def tokens_from_names(site):
    toks = {}
    for d in cards.get(site, {}).values():
        n = (d.get("name") or "").lower()
        n = re.sub(r"^(dr|prof|a/prof|adj|assoc|clinical|asst|mr|ms)\s+", "", n)
        for t in re.findall(r"[a-z]+", n):
            if len(t) >= 2:
                toks[t] = toks.get(t, 0) + 1
    return [t for t, _ in sorted(toks.items(), key=lambda x: -x[1])]

incomplete = []

def solve_cell(site, params, depth_tokens=None):
    """Return set of slugs in cell; ensure completeness by splitting."""
    cnt, found = fetch(site, params)
    if cnt is None:
        return set()
    got = {d["slug"] for d in found}
    if cnt <= 10:
        return got
    # split dimensions
    if "specialty" not in params:
        for sp in SPECS:
            got |= solve_cell(site, {**params, "specialty": sp})
        if len(got) >= cnt:
            return got
    if "gender" not in params:
        for g in ["male", "female"]:
            got |= solve_cell(site, {**params, "gender": g})
        if len(got) >= cnt:
            return got
    if "hospital" not in params and SITES[site][1]:
        for hsp in SITES[site][1]:
            got |= solve_cell(site, {**params, "hospital": hsp})
        if len(got) >= cnt:
            return got
    if "search" not in params:
        toks = tokens_from_names(site)
        # prioritise tokens appearing in the cell's own found names
        own = []
        for d in found:
            for t in re.findall(r"[a-z]+", (d.get("name") or "").lower()):
                if len(t) >= 2 and t not in ("dr", "prof"):
                    own.append(t)
        order = list(dict.fromkeys(own + toks))
        for t in order:
            c2, f2 = fetch(site, {**params, "search": t})
            got |= {d["slug"] for d in f2}
            if len(got) >= cnt:
                return got
    with lock:
        incomplete.append((site, params, cnt, len(got)))
    return got

FIXED = {}

def main():
    if len(sys.argv) > 3:
        FIXED["hospital"] = sys.argv[3]
    # warm up token pool: letter-level first pages for each site
    sites_run = (sys.argv[2].split(",") if len(sys.argv) > 2 else list(SITES))
    for site in sites_run:
        for L in LETTERS:
            fetch(site, {"startswith": L, **FIXED})
    results = {}
    def work(item):
        site, L = item
        s = solve_cell(site, {"startswith": L, **FIXED})
        cnt, _ = fetch(site, {"startswith": L, **FIXED})
        with lock:
            results[(site, L)] = {"count": cnt, "got": len(s), "slugs": sorted(s)}
            print(site, L, "count", cnt, "got", len(s), "calls", calls[0], flush=True)
    sites_run = (sys.argv[2].split(",") if len(sys.argv) > 2 else list(SITES))
    items = [(site, L) for site in sites_run for L in LETTERS]
    with ThreadPoolExecutor(max_workers=4) as ex:
        list(ex.map(work, items))
    json.dump({"%s|%s" % k: v for k, v in results.items()}, open(os.path.join(OUT, "letters.json"), "w"), indent=1)
    json.dump(cards, open(os.path.join(OUT, "cards.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(incomplete, open(os.path.join(OUT, "incomplete.json"), "w"), indent=1)
    tot = {site: len(cards.get(site, {})) for site in SITES}
    print("DONE calls", calls[0], "per-site unique", tot, "incomplete cells", len(incomplete))

if __name__ == "__main__":
    main()
