MOD = 104857601
proot = 3
iproot = pow(proot, MOD-2, MOD)

def NTT(N, X, di):
    j = 0
    for i in range(1, N):
        k = N>>1
        while j >= k: j-= k; k>>= 1
        j+= k
        if i<j: X[i], X[j] = X[j], X[i]
    i = 1
    while i < N:
        x = pow(iproot if di else proot, MOD//i>>1, MOD); j = 0
        while j < N:
            y = 1
            for k in range(i):
                z = X[i|j|k]*y%MOD; X[i|j|k]= X[j|k]-z
                if X[i|j|k] < 0: X[i|j|k]+= MOD
                X[j|k]+= z
                if X[j|k] >= MOD: X[j|k]-= MOD
                y = y*x%MOD
            j+= i<<1
        i<<= 1
    if di:
        j = pow(N, MOD-2, MOD)
        for i in range(N): X[i] = X[i]*j%MOD

def poly_mul(P, Q):
    N = 1
    while len(P)+len(Q) > N: N<<= 1
    P = P[:]; Q = Q[:]
    for L in P, Q: L.extend([0]*(N-len(L)))
    NTT(N, P, 0); NTT(N, Q, 0)
    for i in range(N): P[i] = P[i]*Q[i] % MOD
    NTT(N, P, 1)
    while P and P[-1] == 0: P.pop()
    return P
