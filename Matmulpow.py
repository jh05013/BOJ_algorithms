# Matrix multiplication
# A = matrix A
# B = matrix B
# MOD = modulo

# Matrix exponentiation
# L = matrix
# p = exponent
# MOD = modulo

def matmul(a, b):
    zipb = list(zip(*b))
    return [[sum((ela*elb) for ela, elb in zip(rowa, colb))
             for colb in zipb] for rowa in a]

def matpow(L, p):
    if p == 1: return L
    sq = matpow(L, p//2)
    if p%2==0: return matmul(sq,sq)
    return matmul(matmul(sq,sq),L)

def matmulmod(a, b, MOD):
    zipb = list(zip(*b))
    return [[sum((ela*elb)%MOD for ela, elb in zip(rowa, colb))%MOD
             for colb in zipb] for rowa in a]

def matpowmod(L, p, MOD):
    if p == 1: return [[e%MOD for e in row] for row in L]
    sq = matpowmod(L, p//2, MOD)
    if p%2==0: return matmulmod(sq,sq,MOD)
    return matmulmod(matmulmod(sq,sq,MOD),L,MOD)

def matpowmod(L, p, MOD):
    ini = L; i = 1
    while i <= p: i<<= 1
    i>>= 1
    while i != 1:
        i>>= 1
        L = matmulmod(L, L, MOD)
        if p&i: L = matmulmod(L, ini, MOD)
    return L