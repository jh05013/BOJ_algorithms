# Edmonds-Karp algorithm for maximum flow
# C = capacity matrix
# s = index of source
# t = index of sink
# This is 0-indexed

def EdmondsKarp(C, s, t):
    T = [row[:] for row in C] # residual matrix
    n = len(C); f = 0; F = [[0]*n for i in range(n)]
    while 1:
        m, P = BFS(C, T, s, t, F)
        if m == 0: break
        f+= m; v = t
        while v != s:
            u = P[v]
            F[u][v]+= m; F[v][u]-= m
            T[u][v]-= m; T[v][u]+= m
            v = u
    return f, F

from collections import deque
def BFS(C, T, s, t, F):
    n = len(C)
    P = [-1]*n; P[s] = -2
    M = [-1]*n; M[s] = float('inf')
    Q = deque(); Q.append(s)
    while len(Q) > 0:
        u = Q.popleft()
        for v in range(n):
            if v == u: continue
            if T[u][v] > 0 and P[v] == -1:
                P[v] = u; M[v] = min(M[u], C[u][v] - F[u][v])
                if v != t: Q.append(v)
                else: return M[t], P
    return 0, P