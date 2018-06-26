# nCk mod small prime m

def nck(n, k, m):
    if n < k: return 0
    res = 1
    for i in range(k):
        res = res*(n-i) % m
        res = res*pow(i+1, m-2, m) % m
    return res

def lucas(n, k, m):
    res = 1
    while n or k:
        res = res*nck(n%m, k%m, m) % m
        n//= m; k//= m
    return res