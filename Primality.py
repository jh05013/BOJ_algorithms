# Rabin Miller primality

def composite(a, d, n, s):
    if pow(a, d, n) == 1: return False
    for i in range(s):
        if pow(a, 2**i*d, n) == n-1: return False
    return True

def MillerRabin(n):
    if n <= 1: return False
    if n in _known_primes: return True
    if any(n%p == 0 for p in _known_primes): return False
    d, s = n-1, 0
    while not d % 2: d, s = d>>1, s+1
    if n == 3215031751: return False
    return not any(composite(a,d,n,s) for a in (2,3,5,7,11,13,17,19,23))
_known_primes = [2,3,5,7,11,13,17,19,23,29]
_known_primes += [x for x in range(31, 1000, 2) if MillerRabin(x)]



##### Legacy code

def MillerRabin(n):
    if n <= 1: return False
    if n in _known_primes: return True
    if any(n%p == 0 for p in _known_primes): return False
    d, s = n-1, 0
    while not d % 2: d, s = d>>1, s+1
    if n < 1373653: return not any(composite(a,d,n,s) for a in (2,3))
    if n < 25326001: return not any(composite(a,d,n,s) for a in (2,3,5))
    if n < 118670087467: 
        if n == 3215031751: return False
        return not any(composite(a,d,n,s) for a in (2,3,5,7))
    if n < 2152302898747: return not any(composite(a,d,n,s) for a in (2,3,5,7,11))
    if n < 3474749660383: return not any(composite(a,d,n,s) for a in (2,3,5,7,11,13))
    if n < 341550071728321: return not any(composite(a,d,n,s) for a in (2,3,5,7,11,13,17))
    return not any(composite(a,d,n,s) for a in (2,3,5,7,11,13,17,19,23))
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if MillerRabin(x)]