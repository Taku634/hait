#!/usr/bin/env python3
"""Fetch and parse specialist profile pages from the IHH Singapore hospital sites.
Usage: crawl_profiles.py <slugs.json: {slug: [sites...]}> <outdir>"""
import json, re, sys, os, time, threading, html as htmlmod
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

SLUGS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(OUT, "raw"), exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
BASE = {"ME": "https://www.mountelizabeth.com.sg", "GEH": "https://www.gleneagles.com.sg", "PEH": "https://www.parkwayeast.com.sg"}
sess = requests.Session(); sess.headers["User-Agent"] = UA
lock = threading.Lock()
done = [0]

def text(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)) if el else None

def parse(h, site, slug):
    s = BeautifulSoup(h, "lxml")
    d = {"slug": slug, "site": site}
    t = s.find("title")
    d["title"] = text(t)
    # name & designation
    h1 = s.select_one("h1")
    d["name"] = text(h1)
    d["designation"] = text(s.select_one(".profile-designation"))
    # key-value info block (Specialty / Languages / Gender / Insurance Panel)
    info = {}
    for lab in s.select(".profile-item-title, .profile-info-title, .profile-label, dt"):
        k = text(lab)
        v = lab.find_next_sibling()
        if k and v:
            info[k] = text(v)
    d["info"] = info
    # fallback: regex over visible text
    body = s.get_text("\n", strip=True)
    def grab(label, nxt):
        m = re.search(r"\n%s\n(.*?)\n%s\n" % (re.escape(label), re.escape(nxt)), body, re.S)
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else None
    d["specialty"] = info.get("Specialty") or grab("Specialty", "Languages")
    d["languages"] = info.get("Languages") or grab("Languages", "Gender")
    d["gender"] = info.get("Gender") or grab("Gender", "Insurance Panel")
    d["insurance"] = info.get("Insurance Panel") or grab("Insurance Panel", "This panel information applies")
    # experience paragraph(s)
    m = re.search(r"\nExperience\n(.*?)\n(Fellowship and accreditation|Fellowships? and accreditations?|Contact us)\n", body, re.S)
    d["experience"] = m.group(1).strip() if m else None
    # qualifications with years
    quals = []
    m = re.search(r"\n(?:Fellowship and accreditation|Fellowships? and accreditations?)\n(.*?)\n(?:Contact us|Clinic\n|Back to top)", body, re.S)
    if m:
        year = None
        for line in m.group(1).split("\n"):
            line = line.strip()
            if re.fullmatch(r"(19|20)\d\d", line):
                year = int(line)
            elif line:
                quals.append({"year": year, "qual": line})
    d["qualifications"] = quals
    # clinics
    clinics = []
    for box in s.select(".clinic-box"):
        nm = text(box.select_one(".clinic-name, h4"))
        addr = text(box.select_one(".clinic-address"))
        tel = text(box.select_one(".clinic-tel"))
        clinics.append({"name": nm, "address": addr, "tel": tel})
    if not clinics:
        # fallback regex on text
        for m2 in re.finditer(r"\n([^\n]{3,120})\nAddress:\n(.*?)\n(?:Tel:|Fax:|Note:|Back to top)", body, re.S):
            clinics.append({"name": m2.group(1).strip(), "address": re.sub(r"\s+", " ", m2.group(2)).strip(), "tel": None})
    d["clinics"] = clinics
    # hospitals mentioned in first experience sentence
    d["hosp_mentions"] = sorted(set(re.findall(r"(Mount Elizabeth Novena Hospital|Mount Elizabeth Hospital|Gleneagles Hospital|Parkway East Hospital)", d["experience"] or "")))
    return d

def fetch_one(item):
    slug, sites = item
    out = os.path.join(OUT, "raw", slug + ".html")
    order = [x for x in ["ME", "GEH", "PEH"] if x in sites] or ["ME"]
    rec = None
    for site in order:
        url = BASE[site] + "/patient-services/specialists/profile/" + slug
        for attempt in range(4):
            try:
                r = sess.get(url, timeout=60)
                if r.status_code == 200 and "profile-designation" in r.text:
                    open(out, "w", encoding="utf-8").write(r.text)
                    rec = parse(r.text, site, slug)
                    break
                if r.status_code == 404:
                    break
            except Exception:
                pass
            time.sleep(2 * (attempt + 1))
        if rec:
            break
    with lock:
        done[0] += 1
        if done[0] % 50 == 0:
            print("done", done[0], flush=True)
    return rec or {"slug": slug, "site": None, "error": "fetch_failed"}

def main():
    slugs = json.load(open(SLUGS))
    items = list(slugs.items())
    # resume support
    existing = {}
    p = os.path.join(OUT, "profiles.json")
    if os.path.exists(p):
        for r in json.load(open(p)):
            if not r.get("error"):
                existing[r["slug"]] = r
    items = [it for it in items if it[0] not in existing]
    print("to fetch", len(items), "existing", len(existing), flush=True)
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(fetch_one, items))
    allr = list(existing.values()) + res
    json.dump(allr, open(p, "w"), indent=1, ensure_ascii=False)
    errs = [r["slug"] for r in allr if r.get("error")]
    print("DONE total", len(allr), "errors", len(errs), errs[:20])

if __name__ == "__main__":
    main()
