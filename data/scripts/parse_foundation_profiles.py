import re, html, glob, json, csv, os, statistics, collections, sys

D = '/tmp/claude-0/-home-user-hait/1966649e-6911-5484-be13-e29c48de1cda/scratchpad/dl/fh'
out = []
for f in sorted(glob.glob(os.path.join(D, 'p_*.html'))):
    raw = open(f, encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', raw, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(re.sub(r'\s+', ' ', t))
    m = re.search(r'Home > Find a Specialist > (.*?) > (Dr|Prof|A/Prof|Adj|Assoc Prof|Clinical)[^>]*? ([^>]*?) Back to all Specialists', t)
    spec = m.group(1).strip() if m else ''
    name_m = re.search(r'Home > Find a Specialist > .*? > (.*?) Back to all Specialists', t)
    name = name_m.group(1).strip() if name_m else os.path.basename(f)
    bio_m = re.search(r'Biography (.*?) Read more', t)
    bio = bio_m.group(1) if bio_m else ''
    # graduation year
    gy = None; src = ''
    pats = [
        (r'(?:MBBS|M\.B\.,?B\.S\.?|Bachelor of Medicine[^.]{0,80}?|MD|MBChB|MB BCh|MBBCh|medical degree|graduated)[^.]{0,120}?\b(19[5-9]\d|20[0-2]\d)\b', 'grad'),
    ]
    for p, s in pats:
        mm = re.search(p, bio)
        if mm:
            gy = int(mm.group(1)); src = s; break
    if gy is None:
        mm = re.search(r'(?:more than|over|with)\s+(\d{2})\s+years', bio)
        if mm:
            gy = 2026 - int(mm.group(1)) - 5; src = 'years_min'  # years of experience typically counted from post-grad; conservative
    # practice location clinic names
    loc_m = re.search(r'Practice Location\(s\) (.*?) Private Hospitals', t)
    locs = loc_m.group(1).strip() if loc_m else ''
    clinic = re.split(r'\s\d+ [A-Z]', locs)[0].strip() if locs else ''
    ihh = bool(re.search(r'Mount Elizabeth|Gleneagles|Glenagles|Parkway East', t[t.find('Admission Rights'):t.find('Admission Rights')+600])) if 'Admission Rights' in t else None
    out.append(dict(file=os.path.basename(f), name=name, specialty=spec, grad_year=gy, grad_src=src,
                    est_age=(2026 - gy + 25) if gy else None, clinic=clinic[:80], bio_len=len(bio),
                    public_head=bool(re.search(r'(Head|Director|Chief|Senior Consultant|Consultant)[^.]{0,60}(Hospital|Centre|Institute|SGH|NUH|TTSH|KTPH|CGH|KKH|NCCS|NHCS|SNEC|NUHS)', bio))))

w = csv.DictWriter(open(os.path.join(D, '..', 'fh_profiles.csv'), 'w', newline=''), fieldnames=list(out[0].keys()))
w.writeheader(); w.writerows(out)
print('profiles', len(out), 'with specialty', sum(1 for o in out if o['specialty']), 'with grad year', sum(1 for o in out if o['grad_year']))
print('grad source', collections.Counter(o['grad_src'] for o in out))
ages = sorted(o['est_age'] for o in out if o['est_age'])
def band(a): return '<45' if a < 45 else '45-54' if a < 55 else '55-64' if a < 65 else '65+'
print('ages n', len(ages), 'median', statistics.median(ages), 'mean', round(statistics.mean(ages), 1), collections.Counter(band(a) for a in ages))
print('grad decade', collections.Counter(o['grad_year'] // 10 * 10 for o in out if o['grad_year']))
print('specialties', collections.Counter(o['specialty'] for o in out).most_common())
bysp = collections.defaultdict(list)
for o in out:
    if o['est_age']: bysp[o['specialty']].append(o['est_age'])
print('median age by specialty', {k: (statistics.median(v), len(v)) for k, v in sorted(bysp.items(), key=lambda x: -len(x[1]))})
print('public leadership mention', sum(o['public_head'] for o in out))
print('clinics', collections.Counter(o['clinic'] for o in out).most_common(25))
