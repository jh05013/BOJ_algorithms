# Length of longest increasing subsequence
# L = sequence

from bisect import bisect_left as bl
def LIS(L):
    best = []
    for i in L:
        pos = bl(best, i)
        if len(best) <= pos: best.append(i)
        else: best[pos] = i
    return len(best)

# Iterator of longest increasing subsequence
# L = sequence

from bisect import bisect_left as bl
def LISFind(L):
    best = []; ind = []; prev = []
    for i in range(len(L)):
        x = L[i]; pos = bl(best, x)
        if len(best) <= pos: best.append(x); ind.append(i)
        else: best[pos] = x; ind[pos] = i
        if pos == 0: prev.append(None)
        else: prev.append(ind[pos-1])
    res = []; k = ind[-1]
    while k != None: res.append(L[k]); k = prev[k]
    return reversed(res)

# array of LIS until each index

from bisect import bisect_left as bl
def LIS(L):
    best = []; ans = []
    for i in L:
        pos = bl(best, i)
        if len(best) <= pos: best.append(i)
        else: best[pos] = i
        ans.append(pos+1)
    return ans