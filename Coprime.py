from itertools import combinations
def pfac(n):
    for p in range(2, int(n**.5)+1):
        if p**2 > n: break
        if n%p: continue
        while n%p == 0: n//= p
        yield p
    if n != 1: yield n

def coprimes(n, k, factor):
    # coprime to n, up to k
    tot = k
    for i in range(1, len(factor)+1):
        for C in combinations(factor, i):
            prod = 1
            for p in C: prod*= p
            tot+= (-1)**i * (k//prod)
    return tot