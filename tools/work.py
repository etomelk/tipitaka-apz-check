"""The reading list and the batch files.

  python3 tools/work.py list <step> [nik]          entries of a step still to read, per file
  python3 tools/work.py show <file> [start] [n]     print the next n unread entries of a file in full (apz, Pāli, BJT Sinhala)
  python3 tools/work.py done <file> <pi>:<ei> …     mark entries read with nothing to report
  python3 tools/work.py batch <name> <file> …       write batches/<name>_<commit>.tsv (+ _unsure.tsv) from verdicts/<file>.json
  python3 tools/work.py status

Steps (the maintainer's order, 2026-11-12): 1 = model-written or partly rewritten entries (under 90% de Zoysa);
2 = duplicate, length-long, moved; 3 = dropped; 4 = pali-words.  Run tools/analyse.py <nik> first: it writes out/<nik>.json.

verdicts/<file>.json is a list of findings written by the reader:
  {"pi": 39, "ei": 4, "kind": "pali-left-in", "edits": [["old words", "new words"], …], "pali": "the Pāli words it rests on",
   "reason": "one line", "unsure": false}
"edits" are replacements made in the entry's current text, each old string found exactly once; or give "proposed" (the
whole entry) instead when the entry must be rewritten. The current text is always copied from text-apz by this script,
never typed."""
import sys, json, os, re, csv, glob, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apzlib import APZ, BJT, ROOT, words
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BODY = ('paragraph', 'gatha', 'unindented')
NIKS = ('dn', 'mn', 'sn', 'an')
POS = os.path.join(HERE, 'data', 'read.json')

def commit():
    return subprocess.run(['git', '-C', os.path.join(ROOT, 'tipitaka.lk'), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()

def read():
    return json.load(open(POS)) if os.path.exists(POS) else {}

def nik_of(f):
    return f if not re.match(r'(dn|mn|sn|an)-', f) else f.split('-')[0]

def entries(nik):
    return json.load(open(os.path.join(HERE, 'out', f'{nik}.json')))['entries']

def key(r): return f"{r['pi']}:{r['ei']}"

def step_list(step, nik):
    R = entries(nik)
    if step == 1:
        # the maintainer asked for the entries that had no ai flag at 974bd90 (his own flagged ones are his to review)
        old = json.load(open(os.path.join(HERE, 'data', 'ai_flagged_at_974bd90.json')))
        return [r for r in R if r['ptype'] in BODY and r['n'] >= 6 and r['cov'] is not None and r['cov'] < 0.9
                and key(r) not in old.get(r['file'], [])]
    rows = list(csv.reader(open(os.path.join(HERE, 'findings', f'{nik}.tsv'), encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\'))[1:]
    kinds = {2: ('duplicate', 'length-long', 'moved'), 3: ('dropped',), 4: ('pali-words',)}[step]
    want = {(x[0], int(x[1]), int(x[2])) for x in rows if x[5] in kinds}
    return [r for r in R if (r['file'], r['pi'], r['ei']) in want]


def cmd_list(step, niks):
    rd = read(); tot = left = 0
    for nik in niks:
        per = {}
        for r in step_list(step, nik):
            a = per.setdefault(r['file'], [0, 0]); a[0] += 1
            if key(r) not in rd.get(r['file'], {}).get(str(step), []): a[1] += 1
        for f in sorted(per, key=lambda f: [int(x) for x in re.findall(r'\d+', f)]):
            print(f'{f:12} {per[f][0]:5} entries, {per[f][1]:5} to read'); tot += per[f][0]; left += per[f][1]
    print(f'step {step}: {tot} entries, {left} to read')

def cmd_show(step, f, start, n):
    rd = read().get(f, {}).get(str(step), [])
    L = [r for r in step_list(step, nik_of(f)) if r['file'] == f and key(r) not in rd][start:start + n]
    for r in L:
        print(f"### {f} {r['pi']}:{r['ei']}  type {r['ptype']}  de Zoysa {r['cov']}  ai {r['ai']}")
        print('APZ :', r['text']); print('PALI:', r['pali'].replace('\n', ' / ')); print('BJT :', (r['bjt'] or '').replace('\n', ' / ')); print()
    print(f'{len(L)} shown')

def cmd_done(step, f, keys):
    rd = read(); a = rd.setdefault(f, {}).setdefault(str(step), [])
    for k in keys:
        if k not in a: a.append(k)
    os.makedirs(os.path.dirname(POS), exist_ok=True)
    json.dump(rd, open(POS, 'w'), indent=0, sort_keys=True)

def sq(s): return re.sub(r'\s+', ' ', s).strip()

def cmd_batch(name, files):
    H = ['file', 'page_idx', 'entry_idx', 'kind', 'current_text', 'proposed_text', 'pali_excerpt', 'reason']
    main, uns, bad = [], [], []
    for f in files:
        p = os.path.join(HERE, 'verdicts', f + '.json')
        if not os.path.exists(p): continue
        a = json.load(open(f'{APZ}/{f}.json', encoding='utf-8')); b = json.load(open(f'{BJT}/{f}.json', encoding='utf-8'))
        for v in json.load(open(p, encoding='utf-8')):
            cur = a['pages'][v['pi']]['entries'][v['ei']]; pali = b['pages'][v['pi']]['pali']['entries'][v['ei']]['text']
            if 'was' in v and v['was'] != cur:
                bad.append(f"{f} {v['pi']}:{v['ei']}: the entry has changed upstream since it was read; read it again"); continue
            if 'proposed' in v: new = v['proposed']
            else:
                new = cur
                for old, rep in v['edits']:
                    if new.count(old) != 1: bad.append(f"{f} {v['pi']}:{v['ei']}: {old!r} found {new.count(old)} times"); new = None; break
                    new = new.replace(old, rep)
                if new is None: continue
            if new == cur: bad.append(f"{f} {v['pi']}:{v['ei']}: nothing changed"); continue
            if '�' in new or '\t' in new: bad.append(f"{f} {v['pi']}:{v['ei']}: bad character in the proposed text"); continue
            if sq(v['pali']) not in sq(pali): bad.append(f"{f} {v['pi']}:{v['ei']}: the Pāli excerpt is not in the Pāli entry"); continue
            m1 = re.match(r'\s*\d[\d\s\-–,.]*', cur); m2 = re.match(r'\s*\d[\d\s\-–,.]*', new)
            if (m1.group(0) if m1 else '') != (m2.group(0) if m2 else ''): bad.append(f"{f} {v['pi']}:{v['ei']}: the paragraph number changed"); continue
            row = [f, v['pi'], v['ei'], v['kind'], cur, new, sq(v['pali']), sq(v['reason'])]
            (uns if v.get('unsure') else main).append(row)
    c = commit(); os.makedirs(os.path.join(HERE, 'batches'), exist_ok=True)
    for suffix, rows in (('', main), ('_unsure', uns)):
        with open(os.path.join(HERE, 'batches', f'{name}_{c}{suffix}.tsv'), 'w', newline='', encoding='utf-8') as fh:
            w = csv.writer(fh, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_NONE, escapechar='\\')
            w.writerow(H)
            for r in rows: w.writerow([str(x).replace('\t', ' ').replace('\n', '\\n') for x in r])
    print(f'{name}_{c}: {len(main)} rows, {len(uns)} unsure, {len(bad)} refused')
    for x in bad: print('  REFUSED', x)
    return 1 if bad else 0

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'list': cmd_list(int(a[1]), a[2:] or NIKS)
    elif a[0] == 'show': cmd_show(int(a[1]), a[2], int(a[3]) if len(a) > 3 else 0, int(a[4]) if len(a) > 4 else 12)
    elif a[0] == 'done': cmd_done(int(a[1]), a[2], a[3:])
    elif a[0] == 'batch': sys.exit(cmd_batch(a[1], a[2:]))
    elif a[0] == 'status':
        for s in (1, 2, 3, 4):
            try: cmd_list(s, NIKS)
            except FileNotFoundError as e: print('step', s, 'needs', e.filename)
