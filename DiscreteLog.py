def disclog(a, b, m):
    # Find any a^x = b (mod m); a,m must be coprime
    n = int(m**.5)+1
    an = cur = pow(a, n, m)
    vals = {}
    for i in range(1, n+1):
        vals.setdefault(cur, []).append(i)
        cur = (cur*an) % m
    cur = b
    ans = []
    for i in range(0, n+1):
        if cur in vals: ans.extend([v*n-i for v in vals[cur]])
        cur = (cur*a) % m
    return ans