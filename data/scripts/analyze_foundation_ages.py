import csv, re, collections, statistics, json
P = '/tmp/claude-0/-home-user-hait/1966649e-6911-5484-be13-e29c48de1cda/scratchpad/dl/fh_profiles.csv'
rows = list(csv.DictReader(open(P)))
ihh = list(csv.DictReader(open('/home/user/hait/data/ihh-sg-specialists-directory-2026-10.csv')))

def norm(s):
    s = re.sub(r'^(Dr|Prof|Dato\'|A/Prof|Adj|Assoc|Clinical|Associate|Professor)\.?\s+', '', s.strip(), flags=re.I)
    s = re.sub(r'\(.*?\)', '', s)
    return set(re.sub(r'[^A-Za-z ]', '', s).lower().split())
idx = [(norm(r['name']), r) for r in ihh]
def match(n):
    t = norm(n); best = None
    for k, r in idx:
        inter = len(t & k)
        if inter >= 2 and (inter >= len(t) - 1 or inter >= len(k) - 1):
            if best is None or inter > best[0]: best = (inter, r)
    return best[1] if best else None

merged = []
for r in rows:
    gy = int(r['grad_year']) if r['grad_year'] else None
    src = r['grad_src']
    m = match(r['name'])
    if gy is None and m and m['first_degree_year']:
        gy = int(m['first_degree_year']); src = 'ihh_dir:' + m['fdy_source']
    merged.append(dict(name=r['name'], specialty=r['specialty'], grad_year=gy, src=src,
                       age=(2026 - gy + 25) if gy else None, in_ihh=bool(m),
                       ihh_clinic=(m['clinic_names'] if m else ''), public_head=r['public_head'] == 'True'))

def band(a): return '<45' if a < 45 else '45-54' if a < 55 else '55-64' if a < 65 else '65+'
ages = sorted(x['age'] for x in merged if x['age'])
print('TOTAL profiles', len(merged), '| with age', len(ages), '| in IHH dir', sum(x['in_ihh'] for x in merged))
print('sources', collections.Counter(x['src'] for x in merged))
c = collections.Counter(band(a) for a in ages)
print('median', statistics.median(ages), 'mean', round(statistics.mean(ages), 1), 'q1/q3', ages[len(ages)//4], ages[3*len(ages)//4])
print('bands', {k: (c[k], round(100*c[k]/len(ages))) for k in ['<45', '45-54', '55-64', '65+']})
print('grad decade', sorted(collections.Counter(x['grad_year']//10*10 for x in merged if x['grad_year']).items()))
print('grad 5yr', sorted(collections.Counter(x['grad_year']//5*5 for x in merged if x['grad_year']).items()))
print('specialties (all)', collections.Counter(x['specialty'] for x in merged).most_common())
bysp = collections.defaultdict(list)
for x in merged:
    if x['age']: bysp[x['specialty']].append(x['age'])
print('by specialty: n_total, n_age, median, min, max, share<45, share55+')
for sp, n in collections.Counter(x['specialty'] for x in merged).most_common():
    v = sorted(bysp.get(sp, []))
    if v:
        print(f"  {sp}: {n}, {len(v)}, {statistics.median(v)}, {v[0]}, {v[-1]}, {sum(a<45 for a in v)}, {sum(a>=55 for a in v)}")
    else:
        print(f"  {sp}: {n}, 0")
print('public leadership mention', sum(x['public_head'] for x in merged), 'of', len(merged))
# Emerging proxy: age <45 or grad >= 2010
print('grad>=2010', sum(1 for x in merged if x['grad_year'] and x['grad_year'] >= 2010), 'grad 2005-2009', sum(1 for x in merged if x['grad_year'] and 2005 <= x['grad_year'] <= 2009))
print('age>=60', sum(1 for a in ages if a >= 60), 'age>=65', sum(1 for a in ages if a >= 65))
json.dump(merged, open('/tmp/claude-0/-home-user-hait/1966649e-6911-5484-be13-e29c48de1cda/scratchpad/dl/fh_merged.json', 'w'), ensure_ascii=False, indent=1)
# names of oldest and youngest for sanity
print('oldest', sorted([(x['age'], x['name'], x['specialty'], x['src']) for x in merged if x['age']], reverse=True)[:8])
print('youngest', sorted([(x['age'], x['name'], x['specialty'], x['src']) for x in merged if x['age']])[:8])
