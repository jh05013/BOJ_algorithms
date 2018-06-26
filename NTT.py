# Number theoretic transform
# Degree must be 2^k; if not, append enough 0
# P             A   B   R
# 469762049     7   26  3
# 998244353     119 23  3
# 2013265921    15  27  31
# 2281701377    17  27  3
# 3221225473    3   30  5
# P = A*2^B+1. Check if R is a generator for Z/P+ if you want other values
# FFT will be done on X in place, di = 0 for forwards, 1 for backwards

A = 3
B = 18
R = 10
P = A<<B|1

def NTT(X, di):
    j = 0
    for i in range(1, N):
        k = N>>1
        while j >= k: j-= k; k>>= 1
        j+= k
        if i<j: X[i], X[j] = X[j], X[i]
    i = 1
    while i < N:
        x = pow((pow(R, P-2, P) if di else R), P//i>>1, P); j = 0
        while j < N:
            y = 1
            for k in range(i):
                z = X[i|j|k]*y%P; X[i|j|k]= X[j|k]-z
                if X[i|j|k] < 0: X[i|j|k]+= P
                X[j|k]+= z
                if X[j|k] >= P: X[j|k]-= P
                y = y*x%P
            j+= i<<1
        i<<= 1
    if di:
        j = pow(N, P-2, P)
        for i in range(N): X[i] = X[i]*j%P

SZ = 0
N = 1
n, m = map(int,input().split())
while n+m > N: N<<= 1; SZ+= 1
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
for L in X,Y: L.extend([0]*(N-len(L)))
NTT(X, 0)
NTT(Y, 0)
for i in range(N): X[i] = X[i]*Y[i]%P
NTT(X, 1)

### Below is for finding primitve roots    ###
### ... or you could just use WolframAlpha ###

def isprime(n):
    for p in range(2, int(n**.5)+2):
        if n%p == 0: return False
    return True

def primemods(n):
    c = n
    for p in range(2, n):
        if p*p > c:
            if c != 1: yield c
            return
        if c%p: continue
        while c%p == 0: c//= p
        yield p

def proot(n):
    s = n-1
    pdiv = list(primemods(s))
    for a in range(2, 101):
        if not isprime(a): continue
        res = [pow(a, s//p, n) for p in pdiv]
        if 1 in res: print(a, res)
        else: return a