from functools import cmp_to_key
from itertools import chain
def merge(L1, L2, ind1, cmp):
    res = []; i = ind1; j = 0
    while i < len(L1) and j < len(L2):
        if cmp(L1[i], L2[j]) == -1: res.append(L1[i]); i+= 1
        else: res.append(L2[j]); j+= 1
    res.extend(L1[i:]+L2[j:])
    return res

def SA(s):
    n = len(s)
    if type(s) == str: s+= '  '
    else: s.extend([-1,-1])
    R = [(s[i:i+3], i) for i in chain(range(1, n+1, 3), range(2, n+1, 3))]
    S12 = sorted(range(len(R)), key = lambda i: R[i][0])
    Rp = [1]*len(R)
    for i in range(1, len(R)):
        cur, prv = S12[i], S12[i-1]
        Rp[cur] = Rp[prv] + (R[cur][0]!=R[prv][0])
    if Rp[cur] != len(Rp): S12 = SA(Rp); ZERO = True
    else: ZERO = False
    
    for i in range(len(S12)-ZERO): S12[i+ZERO] = R[S12[i+ZERO]][1]
    rank = [-1]*(n+1) + [0,0]
    for i in range(len(S12)-ZERO): rank[S12[i+ZERO]] = i+1
    S3 = sorted(range(0, n+1, 3), key = lambda i: (s[i], rank[i+1]))
    
    def cmp_suffix(i, j):
        if i%3 == 1: return -1 if (s[i], rank[i+1]) < (s[j], rank[j+1]) else 1
        return -1 if (s[i], s[i+1], rank[i+2]) < (s[j], s[j+1], rank[j+2]) else 1
    ctk = cmp_to_key(cmp_suffix)
    
    L = list(merge(S12, S3, ZERO, cmp_suffix))
    if type(s) == list: s.pop(); s.pop()
    return L