from itertools import groupby
from operator import itemgetter
def SuffixArray(tx, _step=16):
    size = len(tx); step = min(max(_step, 1), size)
    sa = sorted(range(size), key=lambda i: tx[i:i + step])
    grpstart = [False]*size+[True]
    rsa = [None]*size
    stgrp, igrp = '', 0
    for i, pos in enumerate(sa):
        st = tx[pos:pos + step]
        if st != stgrp:
            grpstart[igrp] = (igrp < i - 1); stgrp = st; igrp = i
        rsa[pos] = igrp; sa[i] = pos
    grpstart[igrp] = (igrp < size - 1 or size == 0)
    while grpstart.index(True) < size:
        nextgr = grpstart.index(True)
        while nextgr < size:
            igrp = nextgr; nextgr = grpstart.index(True, igrp + 1); glist = []
            for ig in range(igrp, nextgr):
                pos = sa[ig]
                if rsa[pos] != igrp: break
                newgr = rsa[pos + step] if pos + step < size else -1
                glist.append((newgr, pos))
            glist.sort()
            for ig, g in groupby(glist, key=itemgetter(0)):
                g = [x[1] for x in g]; sa[igrp:igrp + len(g)] = g
                grpstart[igrp] = (len(g) > 1)
                for pos in g: rsa[pos] = igrp
                igrp += len(g)
        step *= 2
    return sa, rsa

def LCPArray(tx, sa = None, rsa = None):
    if sa == None: sa, rsa = SuffixArray(tx)
    size = len(tx)
    lcp = [None]*size; h = 0
    for i in range(size):
        if rsa[i] > 0:
            j = sa[rsa[i] - 1]
            while i+h<size and j+h<size and tx[i+h] == tx[j+h]: h += 1
            lcp[rsa[i]] = h
            if h: h -= 1
    if size: lcp[0] = 0
    return lcp
