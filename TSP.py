# Held-Karp algorithm for Traveling Salesperson Problem
# n = number of vertices
# w = 2D array of weight list
# This is 0-indexed

from itertools import combinations
def TSP(n, w):
    if n <= 1: return 0
    C = {}
    for k in range(1, n): C[1+(1<<k),k] = w[0][k]
    for s in range(2, n+1):
        for S in combinations(range(1,n), s):
            val = sum(1<<k for k in S)+1
            for k in S: C[val,k] = min(C[val-(1<<k),m]+w[m][k] for m in S if m!=0 and m!=k)
    return min(C[(2<<n-1)-1,k] + w[k][0] for k in range(1,n))

# TSP but path instead of cycle

from itertools import combinations
def TSPath(n, w):
    if n <= 1: return 0
    C = {}
    for k in range(n): C[(1<<k),k] = 0
    for s in range(2, n+1):
        for S in combinations(range(n), s):
            val = sum(1<<k for k in S)
            for k in S: C[val,k] = min(C[val-(1<<k),m]+w[m][k] for m in S if m!=k)
    return min(C[(2<<n-1)-1,k] for k in range(n))

n = int(input())
w = [list(map(int,input().split())) for i in range(n)]