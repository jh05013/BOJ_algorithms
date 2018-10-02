MOD = 10**9+7

# actual nCk
def binom(n, k):
    if k > n-k: return binom(n, n-k)
    res = 1
    for i in range(k): res = res*(n-i)//(i+1)
    return res

def nhr(n, r):
    return binom(n+r-1, r)

# nCk mod prime
def binom(n, k, mod):
    num = 1; den = 1
    for i in range(k):
        num = (num*(n-i) % mod)
        den = (den*(i+1) % mod)
    return num * pow(den, mod-2, mod) % mod

def nhr(n, r, mod):
    return binom(n+r-1, r, mod)

# factorial mod m
def fact(n, mod):
    res = 1
    for i in range(n): res = res*(i+1) % mod
    return res

# multinomial mod prime
def multnom(n, k, mod):
    num = fact(n, mod)
    den = 1
    for x in k: den = den*fact(x, mod) % mod
    return num * pow(den, mod-2, mod) % mod