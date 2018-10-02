# 3.1: O(n^2logn)
def brute(n):
    from fractions import gcd
    res = 0
    for x in range(1, n+1):
        for y in range(1, x+1): res+= (gcd(x, y) == 1)
    return res

print(brute(100))

# 3.2: O(n^2)
def dp(n):
    v = [0] * (n+1)
    for x in range(1, n+1):
        v[x] = x*(x+1)//2
        for g in range(2, x+1): v[x]-= v[x//g]
    return v[n]

print(dp(100))
print(dp(1000))

# 4.1: O(n^(3/2))
def phiform(n):
    def phi(x):
        res = x
        p = 2
        while p*p <= x:
            if x%p: p+= 1; continue
            res-= res//p
            while x%p==0: x//=p
            p+= 1
        if x > 1: res-= res//x
        return res
    return sum(map(phi, range(1, n+1)))

print(phiform(1000))
print(phiform(10000))

# 4.2: O(nloglogn)
def phisieve(n):
    tots = list(range(n+1))
    for p in range(2, n+1):
        if p != tots[p]: continue
        for k in range(p, n+1, p): tots[k]-= tots[k]//p
    return sum(tots)

print(phisieve(10000))
print(phisieve(100000))

# 5.2: O(n^(3/4))

def sqrtrick(n):
    cache = {}
    def v(n):
        if n in cache: return cache[n]
        isq = int(n**.5)
        while (isq+1)**2 <= n: isq+= 1
        res = n*(n+1)//2
        for g in range(2, isq+1): res-= v(n//g)
        for z in range(1, isq+1):
            if n//z != z: res-= (n//z - n//(z+1)) * v(z)
        cache[n] = res
        return res
    return v(n)

print(sqrtrick(10**5))
print(sqrtrick(10**6))

# 5.3: O(n^(2/3) (loglogn)^(1/3))

from math import log
def sqsv(n):
    L = int((n//log(log(n)))**(2/3))
    isq = int(n**.5)
    while (isq+1)**2 <= n: isq+= 1    
    cache = {}
    sieve = list(range(L+1))
    for p in range(2, L+1):
        if p == sieve[p]:
            for k in range(p, L+1, p): sieve[k]-= sieve[k]//p
        sieve[p]+= sieve[p-1]
        
    def v(n):
        if n <= L: return sieve[n]
        if n in cache: return cache[n]
        isq = int(n**.5)
        while (isq+1)**2 <= n: isq+= 1
        res = n*(n+1)//2
        for g in range(2, isq+1): res-= v(n//g)
        for z in range(1, isq+1):
            if n//z != z: res-= (n//z - n//(z+1)) * v(z)
        cache[n] = res
        return res        
    return v(n)

print(sqsv(10**6))
print(sqsv(10**7))

# 6.3: Mertens

def mobius(n):
    prime = list(range(n+1)); prime[0] = 0; prime[1] = 0
    mu = [1]*(n+1); mu[0] = 0; mu[1] = 1
    for p in range(2, n+1):
        if not prime[p]: continue
        square = 1
        for q in range(p, n+1, p):
            if p != q: prime[q] = 0
            if square == p: mu[q] = 0; square = 1
            else: mu[q]*= -1; square+= 1
    return mu

from math import log
from itertools import accumulate
def mt(n):
    def t(x): return x*(x+1)//2
    
    L = int((n//log(log(n)))**(2/3))
    msv = list(accumulate(mobius(L)))
    cache = {}
    def M(n):
        if n <= L: return msv[n]
        if n in cache: return cache[n]
        isq = int(n**.5)
        while (isq+1)**2 <= n: isq+= 1        
        res = 1
        for g in range(2, isq+1): res-= M(n//g)
        for z in range(1, isq+1):
            if n//z != z: res-= (n//z - n//(z+1)) * M(z)
        cache[n] = res
        return res
    
    res = 0
    isq = int(n**.5)
    while (isq+1)**2 <= n: isq+= 1
    for d in range(1, isq+1): res+= (msv[d] - msv[d-1]) * t(n//d)
    for z in range(1, isq+1):
        if n//z != z: res+= (M(n//z) - M(n//(z+1))) * t(z)
    return res

print(mt(10**6))
print(mt(10**7))