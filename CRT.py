# Chinese Remainder Theorem
# Find the unique integer n which is ai mod ni, for all i
# all ni must be pairwise coprime
# L = iterable of form (ai, ni)

def exgcd(a, b):
    s = 0; olds = 1
    t = 1; oldt = 0
    r = b; oldr = a
    while r:
        q = oldr // r
        oldr, r = r, oldr-q*r
        olds, s = s, olds-q*s
        oldt, t = t, oldt-q*t
    return oldr, olds, oldt

def CRT(L):
    prod, x = 1, 0
    for a, n in L: prod*= n
    for a, n in L: r, s, t = exgcd(prod//n, n); x+= a*s*(prod//n)
    return x%prod
