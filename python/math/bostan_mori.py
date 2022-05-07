###### Bostan-Mori algorithm ######
# Dependency: FFT or NTT

# coeff of x^n in P/Q
def bm_onecoeff(P, Q, n):
    while n >= 1:
        Qm = [(x*(-1)**i)%MOD for i,x in enumerate(Q)]
        P = poly_mul(P, Qm)[n%2::2]
        Q = poly_mul(Q, Qm)[::2]
        n>>= 1
    return P[0] * pow(Q[0], MOD-2, MOD) % MOD

# n-th term of linear recurrence; next term is sum C[i]*ini[i]
def bostan_mori(C, ini, n):
    while C and C[-1] == 0: C.pop()
    if not C: return 0
    Q = [1%MOD]+[(-x)%MOD for x in reversed(C)]
    P = poly_mul(ini, Q)[:len(ini)]
    return bm_onecoeff(P, Q, n)
