# geometric series sum
def geosum(a, r, n, mod):
    if n == 1: return a%mod
    first = geosum(a, r, n//2, mod)
    second = (first * pow(r, n//2, mod))
    last = 0 if n%2==0 else a * pow(r, n-1, mod)
    return (first + second + last) % mod