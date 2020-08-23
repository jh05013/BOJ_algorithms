# Simple primality check

def isprime(n):
    if n <= 1: return False
    for p in range(2, n+1):
        if p*p > n: return True
        if n%p == 0: return False
    return True

# Prime sieve

def primesieve(n):
    s = list(range(n+1)); s[1] = 0
    for i in range(2, int(n**.5)+2):
        if not s[i]: continue
        for j in range(i*i, n+1, i): s[j] = 0
    return s

# Prime sieve, no function

sv = list(range(n+1)); sv[1] = 0
for i in range(2, int(n**.5)+2):
    if not sv[i]: continue
    for j in range(i*i, n+1, i): sv[j] = 0
primes = list(filter(None, sv))

# Meissel-Lehmer algorithm

LIM = 10000
sieve = list(range(LIM+1)); sieve[1] = 0
for i in range(2, int(LIM**.5)+2):
    if not sieve[i]: continue
    for j in range(i*i, LIM+1, i): sieve[j] = 0

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