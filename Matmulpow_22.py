MOD = 10**9+7

def matmul(A, B):
    return [(A[0]*B[0]+A[1]*B[2])%MOD, (A[0]*B[1]+A[1]*B[3])%MOD,
            (A[2]*B[0]+A[3]*B[2])%MOD, (A[2]*B[1]+A[3]*B[3])%MOD]

def matpow(L, p):
    if p == 0: return [1%MOD, 0, 0, 1%MOD]
    sq = matpow(L, p//2)
    if p%2==0: return matmul(sq,sq)
    return matmul(matmul(sq,sq),L)

def fibo(n):
    return matpow([1,1,1,0], n)[1] % MOD