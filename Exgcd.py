# Extended Euclidean algorithm
# oldr is gcd of a and b
# olds, oldt are x, y that ax+by=gcd(a,b)
# if oldr!=1 then modinv never exists
# otherwise modinv of a mod n is oldt%n

def exgcd(a, b):
    s = 0; olds = 1
    t = 1; oldt = 0
    r = b; oldr = a
    while r:
        q = oldr // r
        oldr, r = r, oldr-q*r
        olds, s = s, olds-q*s
        oldt, t = t, oldt-q*t
    return oldr, olds, oldt # gcd, bezout coefficients
