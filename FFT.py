# Fast Fourier Transform
# Degree must be 2^k; if not, append enough 0
# di = 0 for forwards, 1 for backwards

def ex0(X, Y):
    SZ = 0; N = 1; LEN = len(X)+len(Y)-1
    while N < LEN: N<<= 1; SZ+= 1
    X.extend([0]*(N-len(X)))
    Y.extend([0]*(N-len(Y)))
    return SZ, N

from cmath import exp, pi
def Rev(x):
    r = 0
    for i in range(SZ): r = r<<1|x&1; x>>= 1
    return r

def FFT(X, di):
    for i in range(N):
        j = Rev(i)
        if i < j: X[i], X[j] = X[j], X[i]
    i = 1
    while i < N:
        w = pi/i*(-1)**di; x = exp(1j*w)
        for j in range(0, N, i<<1):
            y = 1
            for k in range(0, i): z = X[i+j+k]*y; X[i+j+k] = X[j+k]-z; X[j+k]+= z; y*= x
        i<<= 1
    if not di: return
    for i in range(N): X[i] = int(round((X[i]/N).real))

def convolution(X, Y):
    FFT(X, 0); FFT(Y, 0)
    for i in range(N): X[i]*= Y[i]
    FFT(X, 1)

X = [1,1,1,1]
Y = [1,1,1,1,1]
SZ, N = ex0(X, Y)
convolution(X, Y)
print(X)