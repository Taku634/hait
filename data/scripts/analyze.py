#!/usr/bin/env python3
"""Merge profiles + listings, derive age proxy, buildings, group affiliation; emit CSV + summary JSON."""
import json, re, os, sys, csv, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from maps import building, group_for_clinic

SP = os.path.dirname(os.path.abspath(__file__))
YEAR_NOW = 2026

def load(p):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None

# ---------- listings (hospital membership)
sites = {"ME": "out", "GEH": "out_GEH", "PEH": "out_PEH"}
member = collections.defaultdict(set)   # slug -> hospitals set
cards = {}
for site, d in sites.items():
    c = load(os.path.join(SP, d, "cards.json"))
    if not c:
        continue
    for slug, card in c.get(site, {}).items():
        member[slug].add(site)
        cards.setdefault(slug, card)
for hosp, d in {"MEH": "out_MEH", "MNH": "out_MNH"}.items():
    c = load(os.path.join(SP, d, "cards.json"))
    if c:
        for slug in c.get("ME", {}):
            member[slug].add(hosp)

# ---------- profiles
profiles = {}
for d in ["prof", "prof_geh", "prof_me", "prof_me2", "prof_retry"]:
    p = load(os.path.join(SP, d, "profiles.json"))
    if p:
        for r in p:
            if not r.get("error") and r["slug"] not in profiles:
                profiles[r["slug"]] = r

# ---------- group doctor-name lists (from subagent)
gdoc = load(os.path.join(SP, "groups", "group_doctors.json")) or {}
def norm_name(n):
    n = (n or "").lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"\b(dr|prof|professor|a/prof|assoc|adj|asst|clinical|mr|ms|mrs|dato|datuk|emeritus)\b\.?", " ", n)
    n = re.sub(r"[^a-z ]", " ", n)
    toks = [t for t in n.split() if len(t) > 1]
    return toks
name_index = collections.defaultdict(set)  # frozenset(tokens) -> groups
for g, info in gdoc.items():
    for dn in info.get("doctors", []):
        toks = norm_name(dn)
        if len(toks) >= 2:
            name_index[frozenset(toks)].add(g)

def match_group_by_name(name):
    toks = frozenset(norm_name(name))
    if not toks:
        return set()
    hits = set()
    for key, gs in name_index.items():
        inter = key & toks
        # exact token-set match with >=3 tokens, or one is a subset of the other with >=3 shared tokens
        if (key == toks and len(toks) >= 3) or (len(inter) >= 3 and (key <= toks or toks <= key)):
            hits |= gs
    return hits

FIRST_DEGREE = re.compile(r"\b(MBBS|MB ?BS|MB ?BCh|MB ?ChB|MBBCh|BM ?BS|MD\b|MBBChir|BMBCh|MBChB|BMedSci|M\.?B\.?,? ?B\.?S\.?|Bachelor of Medicine|MBBCh BAO|LRCP|MBBCH)", re.I)

def first_degree_year(r):
    qs = r.get("qualifications") or []
    yrs = [q["year"] for q in qs if q.get("year") and FIRST_DEGREE.search(q["qual"])]
    if yrs:
        return min(yrs), "qual"
    # fallback 1: any earliest year in qualifications
    yrs = [q["year"] for q in qs if q.get("year")]
    if yrs:
        return min(yrs), "earliest_qual"
    exp = (r.get("experience") or "") + " " + " ".join(str(v) for v in (r.get("info") or {}).values())
    # fallback 2: a sentence that mentions the basic medical degree / graduation and contains a year
    yrs = []
    for sent in re.split(r"(?<=[.;])\s+", exp):
        if re.search(r"MBBS|M\.B\.,? ?B\.S|Bachelor of Medicine|basic medical degree|medical degree|graduated|graduation|medical school|Doctor of Medicine|MD degree|medical training at", sent, re.I):
            for y in re.findall(r"\b(19[5-9]\d|20[01]\d)\b", sent):
                yrs.append(int(y))
    if yrs:
        return min(yrs), "text_grad"
    m = re.search(r"(?:more than|over|close to|nearly|almost|has|with)\s+(\d{2})\s+years(?:'|’)?\s+(?:of\s+)?(?:clinical\s+|medical\s+|surgical\s+|professional\s+)?(?:experience|practi)", exp, re.I) or \
        re.search(r"(?:practising|practicing|in practice|experience)[^.]{0,40}?(?:more than|over|for)\s+(\d{2})\s+years", exp, re.I)
    if m:
        return YEAR_NOW - int(m.group(1)), "text_years"   # 'N years of experience' counted from graduation (lower bound on seniority)
    return None, None

rows = []
for slug in sorted(set(member) | set(profiles)):
    r = profiles.get(slug, {})
    card = cards.get(slug, {})
    name = r.get("name") or card.get("name")
    spec = r.get("specialty") or (card.get("alt") or "").split(" - ")[-1]
    spec = re.sub(r"\s*\(.*?\)\s*", " ", spec or "").strip()
    spec = re.sub(r"\s+", " ", spec)
    fy, fy_src = first_degree_year(r)
    clinics = r.get("clinics") or []
    blds = [building(c.get("address")) for c in clinics]
    ihh_campus = any(b[2] for b in blds)
    campuses = sorted({b[1] for b in blds})
    clinic_names = [c.get("name") for c in clinics if c.get("name")]
    g_clinic = set(); flags = set()
    for cn in clinic_names:
        if re.search(r"Parkway MediCentre", cn or "", re.I):
            flags.add("also at Parkway MediCentre")
        g = group_for_clinic(cn)
        if g:
            if g[0] == "IHH hospital department / centre":
                flags.add("IHH hospital department / centre")
            else:
                g_clinic.add(g[0])
    PARENT = {"PanAsia Surgery": "Foundation Healthcare", "Icon Cancer Centre Singapore": "Icon Group",
              "AARO (Asian American Radiation Oncology)": "AARO"}
    def parent(g):
        g2 = g.split(" - ")[0].strip()
        return PARENT.get(g, PARENT.get(g2, g2))
    g_name_all = match_group_by_name(name)
    brands_name = set(g_name_all)
    g_name_all = {parent(g) for g in g_name_all}
    ALSO = {"Thomson Medical", "Raffles Medical Group"}
    g_name_all = {g for g in g_name_all if g != "AARO"}   # AARO home-page names unreliable; clinic match only
    also_listed = {g for g in g_name_all if g in ALSO}
    g_name = {g for g in g_name_all if g not in ALSO}
    groups = g_clinic | g_name
    rows.append({
        "slug": slug, "name": name, "gender": r.get("gender"), "specialty": spec,
        "designation": r.get("designation") or card.get("designation"),
        "hospitals_listed": "|".join(sorted(member.get(slug, []))),
        "hosp_mentions": "|".join(r.get("hosp_mentions") or []),
        "first_degree_year": fy, "fdy_source": fy_src,
        "years_since_degree": (YEAR_NOW - fy) if fy else None,
        "est_age_band": None,
        "n_clinics": len(clinics),
        "clinic_names": " || ".join(clinic_names),
        "buildings": " || ".join(sorted({b[0] for b in blds})),
        "campuses": "|".join(campuses),
        "on_ihh_campus": ihh_campus,
        "group_by_clinic": "|".join(sorted(g_clinic)),
        "group_by_name": "|".join(sorted(g_name)),
        "brand_by_name": "|".join(sorted(brands_name)),
        "group": "|".join(sorted(groups)),
        "also_listed_at": "|".join(sorted(also_listed)),
        "ihh_flags": "|".join(sorted(flags)),
        "insurance": r.get("insurance") or card.get("insurance"),
        "languages": r.get("languages"),
        "site": r.get("site"),
    })

# estimated age: assume first medical degree at ~24-25 (NUS MBBS 5 yrs; men after NS graduate ~25-26). Use 25.
for x in rows:
    if x["first_degree_year"]:
        age = YEAR_NOW - x["first_degree_year"] + 25
        x["est_age"] = age
        b = "<40" if age < 40 else "40-49" if age < 50 else "50-59" if age < 60 else "60-69" if age < 70 else "70+"
        x["est_age_band"] = b
    else:
        x["est_age"] = None

os.makedirs(os.path.join(SP, "result"), exist_ok=True)
with open(os.path.join(SP, "result", "ihh_sg_specialists.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

# ---------- summaries
S = {}
S["n_total"] = len(rows)
S["n_with_profile"] = sum(1 for x in rows if x["slug"] in profiles)
S["by_hospital_listed"] = dict(collections.Counter(h for x in rows for h in x["hospitals_listed"].split("|") if h))
S["hospital_combos"] = dict(collections.Counter(x["hospitals_listed"] for x in rows).most_common())
S["gender"] = dict(collections.Counter(x["gender"] for x in rows))
S["specialty"] = dict(collections.Counter(x["specialty"] for x in rows).most_common())
S["age_band"] = dict(collections.Counter(x["est_age_band"] for x in rows))
S["fdy_source"] = dict(collections.Counter(x["fdy_source"] for x in rows))
ys = [x["years_since_degree"] for x in rows if x["years_since_degree"]]
S["years_since_degree"] = {"n": len(ys), "median": statistics.median(ys), "mean": round(statistics.mean(ys), 1),
                           "p25": sorted(ys)[len(ys)//4], "p75": sorted(ys)[3*len(ys)//4]} if ys else None
S["buildings"] = dict(collections.Counter(b for x in rows for b in x["buildings"].split(" || ") if b).most_common())
S["on_ihh_campus"] = dict(collections.Counter(x["on_ihh_campus"] for x in rows))
S["campus_combo"] = dict(collections.Counter(x["campuses"] for x in rows).most_common(30))
S["group"] = dict(collections.Counter(x["group"] or "(none identified)" for x in rows).most_common())
S["group_any"] = dict(collections.Counter(g for x in rows for g in x["group"].split("|") if g).most_common())
S["ihh_flags"] = dict(collections.Counter(f for x in rows for f in x["ihh_flags"].split("|") if f))
S["n_clinics"] = dict(collections.Counter(x["n_clinics"] for x in rows))
ins = collections.Counter()
for x in rows:
    for i in re.split(r",\s*", x["insurance"] or ""):
        i = i.strip().rstrip("^")
        if i:
            ins[i] += 1
S["insurance_panel"] = dict(ins.most_common())
# specialty x age
sa = collections.defaultdict(list)
for x in rows:
    if x["years_since_degree"]:
        sa[x["specialty"]].append(x["years_since_degree"])
S["specialty_median_years"] = {k: (len(v), statistics.median(v)) for k, v in sorted(sa.items(), key=lambda kv: -len(kv[1]))}
# specialty x group share
sg = collections.defaultdict(lambda: [0, 0])
for x in rows:
    sg[x["specialty"]][0] += 1
    if x["group"]:
        sg[x["specialty"]][1] += 1
S["specialty_group_share"] = {k: v for k, v in sorted(sg.items(), key=lambda kv: -kv[1][0])}
json.dump(S, open(os.path.join(SP, "result", "summary.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: S[k] for k in ["n_total", "n_with_profile", "by_hospital_listed", "gender", "age_band", "fdy_source", "years_since_degree", "on_ihh_campus"]}, indent=1))
print("specialty top:", list(S["specialty"].items())[:15])
print("groups:", list(S["group_any"].items())[:20])
print("buildings:", list(S["buildings"].items())[:12])
