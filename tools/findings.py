"""python3 findings.py  ->  findings/<nik>.tsv, findings/summary.json  (reads out/<nik>.json)"""
import json, re, os, difflib, csv, statistics
from collections import Counter, defaultdict
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apzlib import norm, words
import sys
from apzlib import KN
NIKS = tuple(sys.argv[1:]) or ('dn', 'mn', 'sn', 'an')
ELL = re.compile(r'\.\.\.|…|පෙ')
BODY = ('paragraph', 'gatha', 'unindented')
NUM = re.compile(r'^\s*(\d+(?:\s*[-–,]\s*\d+)*)\s*\.+\s*')

def nnum(s):
    return re.sub(r'\s', '', s).replace('–', '-') if s else None

def kind_of_change(apz, arc):
    za = [w for w in (norm(x) for x in apz.split()) if w]
    aa = [w for w in (norm(x) for x in arc.split()) if w]
    if ''.join(za) == ''.join(aa):
        return 'spacing'
    if len(za) == len(aa):
        neg = 0
        for z, a in zip(za, aa):
            if z == a: continue
            if z == 'නො' + a or a == 'නො' + z or z.replace('නො', '', 1) == a or a.replace('නො', '', 1) == z: neg += 1
            else: neg = -99
        if neg > 0:
            return 'negation'
    if len(za) == 1 and len(aa) == 1:
        return 'spelling' if difflib.SequenceMatcher(None, za[0], aa[0]).ratio() >= 0.7 else 'word'
    if difflib.SequenceMatcher(None, ''.join(za), ''.join(aa)).ratio() >= 0.8:
        return 'spelling'
    return 'reworded'

def lcs_run(a, b):
    """longest run of consecutive words common to both lists"""
    if not a or not b: return 0, 0
    m = difflib.SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))
    return m.size, m.a

def clip(s, n=220):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[:n] + ' …'

def run(nik):
    d = json.load(open(f'out/{nik}.json'))
    R = d['entries']
    rows = []
    def add(r, group, kind, apz='', arc='', ref='', note=''):
        rows.append([r['file'], r['pi'], r['ei'], r['pageNum'], group, kind, clip(apz), clip(arc), ref, note])
    ratios = [r['n'] / r['np'] for r in R if r['ptype'] == 'paragraph' and r['np'] >= 15 and r['n'] and r['cov'] and r['cov'] > .9]
    if len(ratios) < 20:
        ratios = [r['n'] / r['np'] for r in R if r['ptype'] in BODY and r['np'] >= 6 and r['n'] and r['cov'] and r['cov'] > .9]
    med = statistics.median(ratios) if ratios else 1.5
    rb = [r['n'] / r['nb'] for r in R if r['ptype'] in BODY and r['nb'] and r['nb'] >= 10 and (r['cov'] or 0) >= .999 and not r['ops']]
    mb = statistics.median(rb) if rb else 1.0
    stats = Counter(); stats['entries'] = len(R); stats['median_ratio'] = round(med, 2)
    prev = None
    for r in R:
        ref = f"{r['arc'][0]} §{r['arc'][1]}" + (f"–{r['arc'][2]}" if r['arc'][2] != r['arc'][1] else '') if r.get('arc') else ''
        body = NUM.sub('', r['text']); pbody = NUM.sub('', r['pali'])
        bw = [n for _, n in words(body)]; pw = [n for _, n in words(pbody)]
        isbody = r['ptype'] in BODY
        # ---- A: the entry itself
        if not r['text'].strip() and pw:
            add(r, 'A', 'empty', '', '', '', f"Pāli entry has {len(pw)} words" + ('; ai-flagged' if r['ai'] else ''))
        if isbody and nnum(r['num']) != nnum(r['pnum']) and (bw or r['num']):
            add(r, 'A', 'number', (r['num'] or '(none)') + ' | ' + clip(body, 60), '', '', f"the Pāli entry's paragraph number is {r['pnum'] or '(none)'}, BJT Sinhala's is {(NUM.match(r['bjt'] or '') or [None, None])[1] if NUM.match(r['bjt'] or '') else '(none)'}")
        if r['ptype'] == 'centered' and re.fullmatch(r'[\d\s.\-–,]+', r['pali'].strip()) and re.fullmatch(r'[\d\s.\-–,]+', r['text'].strip() or 'x') and re.sub(r'\s', '', r['text']).replace('–', '-') != re.sub(r'\s', '', r['pali']):
            add(r, 'A', 'id-differs', r['text'], '', '', f"the Pāli entry reads {r['pali'].strip()}")
        if bw and bw == pw and (r['cov'] or 0) < 1 and re.search(r'[඀-෿]', body):
            b = NUM.sub('', r['bjt'] or '')
            if [n for _, n in words(b)] != pw:
                add(r, 'A', 'pali-untranslated', body, '', '', 'same words as the Pāli entry; BJT Sinhala: ' + clip(b, 80))
        elif bw and pw:
            size, at = lcs_run(bw, pw)
            if size >= 3 and size < len(bw) and sum(1 for w in bw[at:at+size] if re.search(r'[\u0d80-\u0dff]', w)) >= 3 and bw[at:at+2] != ['නමො', 'තස්ස']:
                raw = [w for w, _ in words(body)]
                add(r, 'A', 'pali-words', ' '.join(raw[at:at+size]), '', '', f'{size} consecutive words of the Pāli entry stand in the Sinhala')
        if '\ufffd' in r['text']:
            add(r, 'A', 'corrupt-char', ' '.join(re.findall(r'\S*\ufffd\S*', r['text'])[:6]), '', '', f"{r['text'].count(chr(0xfffd))} replacement character(s) U+FFFD")
        if re.search(r'[\u0d80-\u0dff][\u0dca]?[\u0300-\u036f]|[\ue000-\uf8ff]', r['text']):
            add(r, 'A', 'corrupt-char', ' '.join(re.findall(r'\S*[\ue000-\uf8ff\u0300-\u036f]\S*', r['text'])[:6]), '', '', 'private-use or stray combining character')
        if re.search(r'[A-Za-z]', r['text']):
            add(r, 'A', 'latin', ' '.join(re.findall(r'\S*[A-Za-z]\S*', r['text'])[:6]), '', '', 'Latin letters')
        if re.search(r'\{\d*\*?\}|\[\d+\]', r['text']):
            add(r, 'A', 'footnote-mark', ' '.join(re.findall(r'\S*(?:\{\d*\*?\}|\[\d+\])\S*', r['text'])[:6]), '', '', 'footnote or reference mark left in the text' + (' (it stands in the archived de Zoysa too)' if (r['cov'] or 0) >= 0.9 else ''))
        if prev is not None and isbody and len(bw) >= 8 and bw == prev[0] and pw != prev[1]:
            add(r, 'A', 'duplicate', body, '', '', 'same text as the entry before it, while the Pāli entries differ')
        prev = (bw, pw)
        if not bw:
            continue
        # ---- B: size against the Pāli entry
        if isbody and r['np']:
            exp = r['np'] * med
            pe = bool(ELL.search(r['pali']))
            if r['n'] > 3 * exp and r['n'] - exp > 25:
                add(r, 'B', 'length-long' if (not pe and r['np'] >= 4) else 'length-long-abbr', body, '', ref, f"{r['n']} words for a Pāli entry of {r['np']} (usual ratio {med:.1f}); BJT Sinhala has {r['nb']}" + (('; the Pāli abbreviates (පෙ)' if pe else '; the Pāli entry is only a few words' if r['np'] < 4 else '')))
            elif r['n'] < exp / 3 and exp - r['n'] > 25:
                add(r, 'B', 'length-short', body, '', ref, f"{r['n']} words for a Pāli entry of {r['np']} (usual ratio {med:.1f}); BJT Sinhala has {r['nb']}" + ('; the Sinhala abbreviates' if ELL.search(body) else ''))
        # ---- C: whose words
        cov = r['cov']
        if isbody and r['n'] >= 6:
            stats['body_entries'] += 1; stats['body_words'] += r['n']
            if cov >= 0.999 and not r['ops']: stats['verbatim'] += 1
            if cov < 0.5:
                stats['not_dezoysa' + ('_flagged' if r['ai'] else '')] += 1; stats['not_dezoysa_words'] += r['n']
                if 'elsewhere' in r and r['elsewhere'][0] >= 0.85:
                    stats['moved'] += 1
                    add(r, 'B', 'moved', body, r['elsewhere'][3], f"{r['elsewhere'][1]} §{r['elsewhere'][2]}",
                        f"{r['elsewhere'][0]:.0%} of its words are de Zoysa's, but from another place than the archive's order gives (or a repeated passage reused)" + ('; ai-flagged' if r['ai'] else ''))
                elif not r['ai']:
                    note = f"{cov:.0%} of its {r['n']} words follow de Zoysa in order; no ai flag"
                    arc = ''
                    if 'elsewhere' in r:
                        note += f"; {r['elsewhere'][0]:.0%} of the words stand in {r['elsewhere'][1]} §{r['elsewhere'][2]}"
                        arc = r['elsewhere'][3]
                    add(r, 'C', 'not-dezoysa', body, arc, ref, note)
            elif cov < 0.9:
                stats['partly' + ('_flagged' if r['ai'] else '')] += 1
                if not r['ai']:
                    big = sorted((o for o in r['ops'] if o['tag'] != 'arc-only'), key=lambda o: -o['nz'])[:2]
                    add(r, 'C', 'partly-rewritten', ' | '.join(clip(o['apz'], 100) for o in big), ' | '.join(clip(o['arc'], 100) for o in big), ref,
                        f"{cov:.0%} of its {r['n']} words follow de Zoysa in order; no ai flag; the two longest changed runs shown")
            elif r['ai']:
                add(r, 'C', 'ai-flag-on-dezoysa', body, '', ref, f"flagged ai, but {cov:.0%} of its words are de Zoysa's")
        # ---- D, E: the differences inside entries that follow de Zoysa
        if cov >= 0.5:
            raw = [w for w, _ in words(body)]
            for o in r['ops']:
                near = ' '.join(raw[max(0, o['zpos'] - 3): o['zpos'] + o.get('nz', 0) + 3])
                oref = f"{o['arcat'][0]} §{o['arcat'][1]}" if 'arcat' in o else ref
                if o['tag'] == 'arc-only':
                    if o['na'] == 1:
                        if cov >= 0.9: add(r, 'E', 'word-dropped', '… ' + near + ' …', o['arc'], oref, 'one word of de Zoysa missing here')
                        continue
                    abbr = bool(ELL.search(near)) or bool(ELL.search(r['pali']))
                    k = 'dropped-abbr' if abbr else 'dropped'
                    extra = '; the Pāli entry or the Sinhala abbreviates here' if abbr else '; the Pāli entry has no abbreviation mark'
                    if not abbr:
                        dn_ = [n for _, n in words(o['arc'])]
                        if re.fullmatch(r'\s*[“"‘\']?\s*[(\[].*[)\]]\s*[.,”"’\']*\s*', o['arc']):
                            k = 'dropped-gloss'; extra = '; a bracketed note of de Zoysa'
                        elif len(dn_) >= 3 and ' '.join(dn_) in ' '.join(bw):
                            k = 'dropped-repeat'; extra = '; the same words stand once elsewhere in the entry'
                        elif r['nb'] and mb * r['nb'] - r['n'] < 0.2 * o['na']:
                            extra += '; the entry is not shorter than BJT’s Sinhala allows, so de Zoysa probably had more here than the Pāli'
                        elif r['nb'] and mb * r['nb'] - r['n'] >= 0.5 * o['na']:
                            extra += f"; the entry is short beside BJT’s Sinhala ({r['n']} words, BJT {r['nb']})"
                    stats[k + '_words'] += o['na']
                    add(r, 'D', k, '… ' + near + ' …', o['arc'], oref, f"{o['na']} words of de Zoysa not in the entry" + extra)
                elif cov >= 0.9:
                    if o['tag'] == 'apz-only':
                        add(r, 'E', 'added', o['apz'], '', oref, f"{o['nz']} word(s) not in de Zoysa" + (' (the entry abbreviates)' if ELL.search(o['apz']) else ''))
                    else:
                        k = kind_of_change(o['apz'], o['arc'])
                        add(r, 'E', 'changed-' + k, o['apz'], o['arc'], oref, '')
    for g in d['between']:
        if g['na'] >= 4 and g['arcat'][2] in ('bodytext', 'gatha', 'note', ''):
            k = min(g['before'], len(R) - 1); r = R[k]; p = R[k-1] if k else r
            abbr = bool(ELL.search(p['text'][-40:])) or bool(ELL.search(r['text'][:40])) or bool(ELL.search(p['pali'][-60:])) or bool(ELL.search(r['pali'][:60]))
            kk = 'dropped-between-abbr' if abbr else 'dropped-between'
            stats[kk + '_words'] += g['na']
            add(r, 'D', kk, clip(r['text'], 80), g['arc'], f"{g['arcat'][0]} §{g['arcat'][1]}", f"{g['na']} words of de Zoysa stand before this entry and in no entry")
    os.makedirs('findings/entries', exist_ok=True)
    with open(f'findings/entries/{nik}.tsv', 'w', encoding='utf-8') as f:
        f.write('file\tpage_idx\tentry_idx\ttype\twords\tfrom_dezoysa\tai_flag\tarchive_ref\n')
        for r in R:
            ref = f"{r['arc'][0]} §{r['arc'][1]}" if r.get('arc') else ''
            f.write(f"{r['file']}\t{r['pi']}\t{r['ei']}\t{r['ptype']}\t{r['n']}\t{'' if r['cov'] is None else r['cov']}\t{int(r['ai'])}\t{ref}\n")
    rows.sort(key=lambda x: ([int(n) for n in re.findall(r'\d+', x[0])], x[1], x[2], x[4]))
    os.makedirs('findings', exist_ok=True)
    with open(f'findings/{nik}.tsv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_NONE, escapechar='\\')
        w.writerow(['file', 'page_idx', 'entry_idx', 'pageNum', 'group', 'kind', 'apz', 'archive', 'archive_ref', 'note'])
        for x in rows:
            w.writerow([str(c).replace('\t', ' ').replace('\n', ' ⏎ ') for c in x])
    kc = Counter((x[4], x[5]) for x in rows)
    return {'stats': dict(stats), 'kinds': {f'{g} {k}': v for (g, k), v in sorted(kc.items())}, 'rows': len(rows),
            'nZ': d['nZ'], 'nA': d['nA'], 'eq': sum(r['eq'] for r in R)}

if __name__ == '__main__':
    S = {n: run(n) for n in NIKS}
    json.dump(S, open('findings/summary%s.json' % ('' if NIKS[0] == 'dn' else '_kn'), 'w'), ensure_ascii=False, indent=1)
    ks = sorted({k for n in NIKS for k in S[n]['kinds']})
    print(f"{'kind':28}" + ''.join(f'{n:>8}' for n in NIKS) + '   total')
    for k in ks:
        v = [S[n]['kinds'].get(k, 0) for n in NIKS]
        print(f'{k:28}' + ''.join(f'{x:8}' for x in v) + f'{sum(v):8}')
    for n in NIKS: print(n, S[n]['stats'], S[n]['rows'])
