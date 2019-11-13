'''
* mu = Mobius (1 if n=1, (-1)^r if square-free r-primediv, 0 else)
* Denote Dirichlet convolution (f*g)(n) = sum[ab=n] f(a)g(b)
* Mobius inversion formula: f = mu*(f*I)    where I(x) = 1
To compute G = sum[1<=i<j<=n] h(gcd(i,j))
Rewrite as G = sum[g=1 to n] h(g)cnt(g)     where cnt(g) = # of (i,j) with gcd(i,j)=g
Now let Sf = h. Then f = mu*h               where Sf = f*I = sum[d|n] f(d)
G = sum[g=1 to n] Sf(g)cnt(g)
  = sum[d=1 to n] f(d)mc(d)                 where mc(d) = # of (i,j) with d|gcd(i,j)
'''

N = 100 # Upper bound of numbers
prime = list(range(N+1)); prime[0] = 0; prime[1] = 0
mu = [1]*(N+1); mu[0] = -2; mu[1] = 1
for p in range(2, N+1):
    if not prime[p]: continue
    square = 1
    for q in range(p, N+1, p):
        if p != q: prime[q] = 0
        if square == p: mu[q] = 0; square = 1
        else: mu[q]*= -1; square+= 1
f = [0]*(N+1)
for i in range(1, N+1):
    ###### Calculate h here! ######
    for j in range(i, N+1, i): f[j]+= h * mu[j//i]

tot = 0
for d in range(1, N+1):
    ###### Calculate mc here! ######
    tot+= f[d] * mc
print(tot)



############################# Dirichlet things

N = 100000 # Upper bound of numbers
prime = list(range(N+1)); prime[0] = 0; prime[1] = 0
mu = [1]*(N+1); mu[0] = -2; mu[1] = 1
phi = list(range(N+1))
for p in range(2, N+1):
    if not prime[p]: continue
    square = 1
    for q in range(p, N+1, p):
        if p != q: prime[q] = 0
        if square == p: mu[q] = 0; square = 1
        else: mu[q]*= -1; square+= 1
        phi[q] = phi[q]*(p-1)//p

MOD = 10**9+7
F = [0,1]
for i in range(100000): F.append((F[-1]+F[-2])%MOD)

def convolute(f, g):
    ans = [0]
    for n in range(1,100):
        A = 0
        for d in range(1, n+1):
            if n%d==0: A+= f(d) * g(n//d)
        ans.append(A%MOD)
    return ans

I = lambda x: 1
MU = lambda x: mu[x]
ID = lambda x: x
IDA = lambda n: (lambda x: x**n)
E = lambda x: int(x == 1)
PHI = lambda x: phi[x]