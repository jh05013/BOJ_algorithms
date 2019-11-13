# Matrix multiplication
# A = matrix A
# B = matrix B
# MOD = modulo

# Matrix exponentiation
# L = matrix
# p = exponent
# MOD = modulo

def matmul(a, b):
    return [[sum((x*y) for x, y in zip(rowa, colb))
             for colb in list(zip(*b))] for rowa in a]

def matpow(L, p):
    if p == 1: return L
    sq = matpow(L, p//2)
    if p%2==0: return matmul(sq,sq)
    return matmul(matmul(sq,sq),L)

def matmul(a, b, MOD):
    return [[sum((x*y)%MOD for x, y in zip(rowa, colb))%MOD
             for colb in list(zip(*b))] for rowa in a]

def matpow(L, p, MOD):
    ini = L; i = 1
    while i <= p: i<<= 1
    i>>= 1
    while i != 1:
        i>>= 1
        L = matmul(L, L, MOD)
        if p&i: L = matmul(L, ini, MOD)
    return L




def matpow(L, p, MOD):
    if p == 1: return [[e%MOD for e in row] for row in L]
    sq = matpow(L, p//2, MOD)
    if p%2==0: return matmul(sq,sq,MOD)
    return matmul(matmul(sq,sq,MOD),L,MOD)