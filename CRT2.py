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

# solves = a1 (mod n1), = a2 (mod n2); returns -1 if impossible
def CRT2(a1, n1, a2, n2):
    d, xp, yp = exgcd(n1, n2)
    if (a1-a2)%d: return -1
    k1 = -xp*(a1-a2)//d
    ans = (a1 + k1*n1) % (n1*n2//d)
    assert ans%n1 == a1 and ans%n2 == a2
    return ans