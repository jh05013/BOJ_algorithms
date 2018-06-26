# Josephus problem
# g is for small k and large n
# below iterative version is simpler
from sys import setrecursionlimit as SRL, stdin
SRL(242424)
def g(n, k):
    if k == 1: return n-1
    if n == 1: return 0
    if n < k: return (g(n-1,k) + k) % n
    np = n - n//k
    return k*((g(np,k)-n%k)%np) // (k-1)

n, k = map(int,input().split())
r = 0
for i in range(1, n+1): r = (r+k)%i
print(r)