"""Read text-apz, BJT and the archived de Zoysa XML into comparable word streams."""
import json, re, os, html, glob, unicodedata
ROOT = os.environ.get('APZ_SRC') or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'apz-sources')
APZ = ROOT + '/tipitaka.lk/public/static/text-apz'
BJT = ROOT + '/tipitaka.lk/public/static/text'
ARC = ROOT + '/pitaka.lk-archive/main/text/sinh-aps'
# archive file numbers per nikāya
ARC_RANGE = {'dn': (1500, 1799), 'mn': (1800, 2099), 'sn': (2100, 2599), 'an': (2600, 3699),
             'kn-khp': (3700, 3799), 'kn-dhp': (3800, 3899), 'kn-ud': (3900, 3999), 'kn-iti': (4000, 4099), 'kn-snp': (4100, 4199),
             'kn-vv': (4200, 4299), 'kn-pv': (4300, 4399), 'kn-thag': (4400, 4499), 'kn-thig': (4500, 4599), 'kn-ap': (4600, 4799),
             'kn-bv': (4800, 4899), 'kn-jat': (5000, 5199)}
KN = [k for k in ARC_RANGE if k.startswith('kn-')]

def fkey(name):
    return [int(x) for x in re.findall(r'\d+', name)]

def bjt_files(nik):
    fs = [os.path.basename(f)[:-5] for f in glob.glob(f'{APZ}/{nik}-*.json') + glob.glob(f'{APZ}/{nik}.json')]
    return sorted(fs, key=fkey)

SINH = re.compile(r'[඀-෿]')
def norm(w):
    """a word reduced for comparison: no joiners, no punctuation"""
    w = w.replace('‍', '').replace('‌', '').replace('​', '')
    return re.sub(r'[^඀-෿0-9A-Za-z]', '', w)

def words(text):
    """[(raw, norm)] for every whitespace word that has letters or digits"""
    out = []
    for raw in text.split():
        # split on dashes and slashes joining words
        n = norm(raw)
        if n:
            out.append((raw, n))
    return out

TAG = re.compile(r'<(/?)(div|span)([^>]*)>|([^<]+)')
def read_archive_file(path):
    """pieces in file order: {'file','para','cls','text'}; paranum spans skipped"""
    t = open(path, encoding='utf-8').read()
    out, stack, para = [], [], None
    for m in TAG.finditer(t):
        if m.group(4) is not None:
            s = html.unescape(m.group(4))
            s = re.sub(r'\s+', ' ', s).strip()
            if not s:
                continue
            cls = stack[-1] if stack else ''
            if 'paranum' in cls:
                continue
            out.append({'file': os.path.basename(path), 'para': para, 'cls': cls, 'text': s})
        elif m.group(1):
            if stack:
                stack.pop()
        else:
            a = m.group(3)
            c = re.search(r'class="([^"]*)"', a)
            p = re.search(r'para="([^"]*)"', a)
            if p:
                para = p.group(1)
            stack.append(c.group(1) if c else '')
    return out

def read_archive(nik):
    lo, hi = ARC_RANGE[nik]
    out = []
    for f in sorted(glob.glob(ARC + '/vagga_*.xml')):
        n = int(re.search(r'(\d+)', os.path.basename(f)).group(1))
        if lo <= n <= hi:
            out += read_archive_file(f)
    return out

def read_apz(nik):
    """entries in order with the BJT Pāli and Sinhala entry of the same index"""
    out = []
    for f in bjt_files(nik):
        a = json.load(open(f'{APZ}/{f}.json'))
        b = json.load(open(f'{BJT}/{f}.json'))
        assert len(a['pages']) == len(b['pages']), f
        for pi, (pa, pb) in enumerate(zip(a['pages'], b['pages'])):
            pe, se = pb['pali']['entries'], pb['sinh']['entries']
            if len(pa['entries']) != len(pe):
                print('entry count differs', f, pi, len(pa['entries']), len(pe)); continue
            ai = set(pa.get('ai', []))
            for ei, tx in enumerate(pa['entries']):
                out.append({'file': f, 'pi': pi, 'ei': ei, 'pageNum': pa['pageNum'], 'text': tx, 'ai': ei in ai,
                            'pali': pe[ei], 'bjt': se[ei] if ei < len(se) else None,
                            'nsinh': len(se), 'npali': len(pe)})
    return out
