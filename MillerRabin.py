def witness(a, n, s):
    if a >= n: a%= n
    if a <= 1: return True
    d = n>>s; x = pow(a, d, n)
    if x == 1 or x == n-1: return True
    for ITER in range(s):
        x = x*x % n
        if x == 1: return False
        if x == n-1: return True
    return False

def millerrabin(n):
    if n == 2: return True
    if n < 2 or n%2 == 0: return False
    d = n>>1; s = 1
    while (d&1) == 0: d>>= 1; s+= 1
    candidate = [2, 7, 61] if n < 4759123141 else\
        [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    return all(witness(x, n, s) for x in candidate)

from random import randrange
from math import gcd
def rho(n):
    x = randrange(1, n); c = randrange(1, n)
    g, y = 1, x
    while g == 1:
        x = (x*x+c) % n
        y = (y*y+c) % n
        y = (y*y+c) % n
        g = gcd(abs(x-y), n)
    if g == n: return rho(n)
    return g

def factorize(n):
    if n == 1: return []
    if n%2 == 0: return [2] + factorize(n//2)
    if millerrabin(n): return [n]
    f = rho(n)
    return factorize(f) + factorize(n//f)