"""Global, in-order alignment of the text-apz word stream with the archived de Zoysa word stream.
Anchors: word n-grams that occur once on each side (recursively within the stretch between anchors),
kept in increasing order; the stretches between anchors are aligned with difflib."""
import difflib, bisect
from collections import Counter

def lis(pairs):
    """longest chain increasing in both i and j; pairs sorted by i"""
    tails, tidx, prev = [], [], [None] * len(pairs)
    for k, (i, j) in enumerate(pairs):
        p = bisect.bisect_left(tails, j)
        if p == len(tails):
            tails.append(j); tidx.append(k)
        else:
            tails[p] = j; tidx[p] = k
        prev[k] = tidx[p-1] if p else None
    out, k = [], tidx[-1] if tidx else None
    while k is not None:
        out.append(pairs[k]); k = prev[k]
    return out[::-1]

def anchors(Z, A, z0, z1, a0, a1, n):
    cz, ca = Counter(), Counter()
    pz, pa = {}, {}
    for i in range(z0, z1 - n + 1):
        g = tuple(Z[i:i+n]); cz[g] += 1; pz[g] = i
    for j in range(a0, a1 - n + 1):
        g = tuple(A[j:j+n]); ca[g] += 1; pa[g] = j
    pairs = sorted((pz[g], pa[g]) for g in cz if cz[g] == 1 and ca.get(g) == 1)
    return lis(pairs)

def align(Z, A, z0=0, z1=None, a0=0, a1=None, out=None, depth=0):
    """list of (tag, z0, z1, a0, a1), covering both streams in order"""
    if z1 is None: z1, a1 = len(Z), len(A)
    if out is None: out = []
    nz, na = z1 - z0, a1 - a0
    if nz == 0 or na == 0:
        if nz or na:
            out.append(('delete' if nz else 'insert', z0, z1, a0, a1))
        return out
    if nz * na <= 250_000 or depth > 40:
        if nz * na > 9_000_000:
            out.append(('replace', z0, z1, a0, a1)); return out
        sm = difflib.SequenceMatcher(None, Z[z0:z1], A[a0:a1], autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            out.append((tag, z0+i1, z0+i2, a0+j1, a0+j2))
        return out
    for n in (6, 4, 3, 2):
        an = anchors(Z, A, z0, z1, a0, a1, n)
        if len(an) >= 1:
            break
    else:
        an = []
    if not an:
        if nz * na > 9_000_000:
            out.append(('replace', z0, z1, a0, a1)); return out
        sm = difflib.SequenceMatcher(None, Z[z0:z1], A[a0:a1], autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            out.append((tag, z0+i1, z0+i2, a0+j1, a0+j2))
        return out
    # extend each anchor to its run, then recurse between
    cz, ca = z0, a0
    for (i, j) in an:
        if i < cz or j < ca:
            continue
        align(Z, A, cz, i, ca, j, out, depth + 1)
        k = 0
        while i + k < z1 and j + k < a1 and Z[i+k] == A[j+k]:
            k += 1
        out.append(('equal', i, i+k, j, j+k))
        cz, ca = i + k, j + k
    align(Z, A, cz, z1, ca, a1, out, depth + 1)
    return out

def tidy(ops):
    """merge neighbours of one tag; pull back equal runs that a previous op ended on"""
    out = []
    for op in ops:
        if op[1] == op[2] and op[3] == op[4]:
            continue
        if out and out[-1][0] == op[0] and out[-1][2] == op[1] and out[-1][4] == op[3]:
            out[-1] = (op[0], out[-1][1], op[2], out[-1][3], op[4])
        elif out and out[-1][0] != 'equal' and op[0] != 'equal':
            p = out[-1]
            nz, na = op[2] - p[1], op[4] - p[3]
            out[-1] = ('replace' if nz and na else ('delete' if nz else 'insert'), p[1], op[2], p[3], op[4])
        else:
            out.append(op)
    return out
