# Prime sieve

LIM = 100100
sieve = list(range(LIM)); sieve[1] = 0
for i in range(2, int(LIM**.5)+1):
    if not sieve[i]: continue
    for j in range(2*i, LIM, i): sieve[j] = 0
sieve = list(filter(None, sieve))

# Meissel-Lehmer algorithm

from bisect import bisect
phicache = {}
def PHI(x, a):
    if a == 1: return (x+1) // 2
    if (x, a) in phicache: return phicache[x, a]
    res = PHI(x, a-1) - PHI(x//sieve[a-1], a-1)
    phicache[x, a] = res
    return res

def root(x, po):
    n = int(x**(1/po))
    if (n+1)**po <= x: n+= 1
    return n

picache = {}
def PI(x):
    if x in picache: return picache[x]
    if x < LIM: return bisect(sieve, x)
    a = PI(int(root(x,4)))
    b = PI(int(root(x,2)))
    c = PI(int(root(x,3)))
    res = PHI(x, a) + (b+a-2)*(b-a+1)//2
    for i in range(a+1, b+1):
        w = x // sieve[i-1]
        res-= PI(w)
        if i > c: continue
        for j in range(i, PI(w**.5)+1):
            res+= j-1 - PI(w//sieve[j-1])
    picache[x] = res
    return res