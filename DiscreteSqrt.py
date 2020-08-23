def tonelli(n, p):
    # Find x^2 = n (mod p), or -1 if does not exist
    if n == 0: return 0
    if pow(n, (p-1)//2, p) != 1: return -1
    Q = p-1; S = 0
    while Q&1==0: Q>>= 1; S+= 1
    for z in range(2, p+1):
        if pow(z, (p-1)//2, p) != 1: break
    M, c, t, R = S, pow(z,Q,p), pow(n,Q,p), pow(n,(Q+1)//2,p)
    while 1:
        if t == 0: return 0
        if t == 1: return R
        tpow = t
        for i in range(M+1):
            if tpow == 1: break
            tpow = (tpow**2)%p
        b = pow(c, 2**(M-i-1), p)
        M, c, t, R = i, (b**2)%p, (t*b*b)%p, (R*b)%p