"""python3 analyse.py <nik>…  ->  out/<nik>.json : per-entry comparison of text-apz with the archived de Zoysa."""
import sys, json, re, os, difflib
from collections import defaultdict, Counter
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(HERE)
from apzlib import *
from align import align, tidy
NUM = re.compile(r'^\s*(\d+(?:\s*[-–,]\s*\d+)*)\s*\.+\s*')
N = 3

def build(nik):
    arc = read_archive(nik)
    A, Araw, Ap = [], [], []
    for k, p in enumerate(arc):
        for raw, n in words(p['text']):
            A.append(n); Araw.append(raw); Ap.append(k)
    apz = read_apz(nik)
    Z, Zraw, Ze = [], [], []
    for k, e in enumerate(apz):
        tx = e['text']
        m = NUM.match(tx)
        e['num'] = m.group(1) if m else None
        e['body'] = tx[m.end():] if m else tx
        pt = e['pali'].get('text', '')
        pm = NUM.match(pt)
        e['pnum'] = pm.group(1) if pm else None
        e['pbody'] = pt[pm.end():] if pm else pt
        e['z0'] = len(Z)
        for raw, n in words(e['body']):
            Z.append(n); Zraw.append(raw); Ze.append(k)
        e['z1'] = len(Z)
    return arc, A, Araw, Ap, apz, Z, Zraw, Ze

def vote_find(E, idx, S, hint=None):
    """best place of word list E in stream S (n-gram index idx): (cov, s0, s1) or None"""
    if len(E) < N + 2:
        return None
    bw = max(30, len(E) // 2)
    votes = Counter(); hits = defaultdict(list)
    for i in range(len(E) - N + 1):
        ps = idx.get(tuple(E[i:i+N]), ())
        if len(ps) > 400:
            continue
        for p in ps:
            b = (p - i) // bw
            votes[b] += 1; hits[b].append(p)
    if not votes:
        return None
    b = max(votes, key=lambda b: votes[b] + votes.get(b+1, 0))
    hs = sorted(hits[b] + hits.get(b+1, []))
    lo = max(0, hs[0] - len(E)); hi = min(len(S), hs[-1] + len(E) + N)
    if hi - lo > 5 * len(E) + 200:
        return None
    sm = difflib.SequenceMatcher(None, E, S[lo:hi], autojunk=False)
    bl = [x for x in sm.get_matching_blocks() if x.size]
    if not bl:
        return None
    return (sum(x.size for x in bl) / len(E), lo + bl[0].b, lo + bl[-1].b + bl[-1].size)

def run(nik):
    arc, A, Araw, Ap, apz, Z, Zraw, Ze = build(nik)
    ops = tidy(align(Z, A))
    for e in apz:
        e['eq'] = 0; e['ops'] = []; e['a'] = None
    between = []      # archive-only stretches standing between two entries
    for tag, z0, z1, a0, a1 in ops:
        if tag == 'equal':
            for z in range(z0, z1):
                e = apz[Ze[z]]; e['eq'] += 1
                a = a0 + (z - z0)
                if e['a'] is None: e['a'] = [a, a + 1]
                else: e['a'][1] = a + 1
            continue
        if z0 == z1:      # archive only
            k = Ze[z0] if z0 < len(Z) else len(apz) - 1
            inside = z0 < len(Z) and z0 > apz[k]['z0']
            rec = {'tag': 'arc-only', 'a0': a0, 'a1': a1, 'inside': inside, 'zpos': z0 - apz[k]['z0']}
            if inside: apz[k]['ops'].append(rec)
            else: between.append((k, rec))      # before entry k
            continue
        ks = sorted({Ze[z] for z in range(z0, z1)})
        for k in ks:
            e = apz[k]
            s, t = max(z0, e['z0']), min(z1, e['z1'])
            e['ops'].append({'tag': 'apz-only' if a0 == a1 else 'replace', 'z0': s, 'z1': t, 'a0': a0, 'a1': a1,
                             'multi': len(ks) > 1, 'zpos': s - e['z0']})
    idxA = defaultdict(list)
    for i in range(len(A) - N + 1):
        idxA[tuple(A[i:i+N])].append(i)
    res = []
    for k, e in enumerate(apz):
        n = e['z1'] - e['z0']
        r = {'k': k, 'file': e['file'], 'pi': e['pi'], 'ei': e['ei'], 'pageNum': e['pageNum'], 'ai': e['ai'],
             'ptype': e['pali'].get('type'), 'plevel': e['pali'].get('level'), 'n': n, 'eq': e['eq'],
             'cov': round(e['eq'] / n, 3) if n else None, 'num': e['num'], 'pnum': e['pnum'],
             'np': len(words(e['pbody'])), 'nb': len(words(NUM.sub('', e['bjt'].get('text', '')))) if e['bjt'] else None,
             'text': e['text'], 'pali': e['pali'].get('text', ''), 'bjt': e['bjt'].get('text', '') if e['bjt'] else None}
        if e['a']:
            p0, p1 = arc[Ap[e['a'][0]]], arc[Ap[e['a'][1] - 1]]
            r['arc'] = [p0['file'], p0['para'], p1['para'], p0['cls']]
            r['a'] = e['a']
        o2 = []
        for o in e['ops']:
            x = {'tag': o['tag'], 'zpos': o['zpos'], 'arc': ' '.join(Araw[o['a0']:o['a1']]), 'na': o['a1'] - o['a0']}
            if 'z0' in o:
                x['apz'] = ' '.join(Zraw[o['z0']:o['z1']]); x['nz'] = o['z1'] - o['z0']; x['multi'] = o['multi']
            else:
                x['apz'] = ''; x['nz'] = 0
            if o['a1'] > o['a0']:
                p = arc[Ap[o['a0']]]; x['arcat'] = [p['file'], p['para'], p['cls']]
            o2.append(x)
        r['ops'] = o2
        if n >= 6 and r['cov'] < 0.5:
            f = vote_find(Z[e['z0']:e['z1']], idxA, A)
            if f and f[0] >= 0.6:
                p = arc[Ap[f[1]]]
                r['elsewhere'] = [round(f[0], 2), p['file'], p['para'], ' '.join(Araw[f[1]:min(f[2], f[1] + 40)])]
        res.append(r)
    btw = []
    for k, o in between:
        p = arc[Ap[o['a0']]]
        btw.append({'before': k, 'na': o['a1'] - o['a0'], 'arc': ' '.join(Araw[o['a0']:o['a1']]),
                    'arcat': [p['file'], p['para'], p['cls']], 'a0': o['a0']})
    os.makedirs('out', exist_ok=True)
    json.dump({'entries': res, 'between': btw, 'nA': len(A), 'nZ': len(Z)}, open(f'out/{nik}.json', 'w'), ensure_ascii=False)
    eq = sum(r['eq'] for r in res)
    print(f"{nik}: entries {len(res)}, apz words {len(Z)}, archive words {len(A)}, same in order {eq} "
          f"({eq/len(Z):.1%} of apz, {eq/len(A):.1%} of archive)")

if __name__ == '__main__':
    for nik in sys.argv[1:]:
        run(nik)
