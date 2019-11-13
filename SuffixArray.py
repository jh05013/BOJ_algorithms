from itertools import groupby
from operator import itemgetter
def SuffixArray(tx, _step=16):
    size = len(tx); step = min(max(_step, 1), size)
    sa = sorted(range(size), key=lambda i: tx[i:i + step])
    gst = [False]*size+[True]
    rsa = [None]*size
    stgrp, ig = '', 0
    for i, pos in enumerate(sa):
        st = tx[pos:pos + step]
        if st != stgrp:
            gst[ig] = (ig < i - 1); stgrp = st; ig = i
        rsa[pos] = ig; sa[i] = pos
    gst[ig] = (ig < size - 1 or size == 0)
    while gst.index(True) < size:
        ng = gst.index(True)
        while ng < size:
            ig = ng; ng = gst.index(True, ig + 1); glist = []
            for i in range(ig, ng):
                pos = sa[i]
                if rsa[pos] != ig: break
                newgr = rsa[pos + step] if pos + step < size else -1
                glist.append((newgr, pos))
            glist.sort()
            for i, g in groupby(glist, key=itemgetter(0)):
                g = [x[1] for x in g]; sa[ig:ig + len(g)] = g
                gst[ig] = (len(g) > 1)
                for pos in g: rsa[pos] = ig
                ig += len(g)
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
