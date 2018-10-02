# MCMF: minimum cost maximum flow
# based on Edmonds-Karp but use SPFA instead of BFS
# G = list of adjacent nodes
# C = capacity matrix
# d = distance matrix
# s = index of source
# t = index of sink
# This is 0-indexed

from sys import stdin
input = stdin.readline

from collections import defaultdict
def MCMF(G, C, d, s, t):
    T = defaultdict(int) # residual matrix
    f = 0; F = defaultdict(int); cost = 0
    while 1:
        m, P = SPFA(G, C, T, d, s, t, F)
        if m == 0: break
        f+= m; v = t
        while v != s:
            u = P[v]; F[(u,v)]+= m; F[(v,u)]-= m;
            T[(u,v)]-= m; T[(v,u)]+= m; cost+= m*d[(u,v)]; v = u
    return f, cost#, F

from collections import deque
def SPFA(G, C, T, d, s, t, F):
    n = len(G)
    P = [-1]*n; P[s] = -2; M = [-1]*n; M[s] = float('inf')
    dist = [float('inf')]*n; dist[s] = 0
    queued = [0]*n; queued[s] = 1; Q = deque(); Q.append(s)
    while len(Q) > 0:
        u = Q.popleft(); queued[u] = 0
        for v in G[u]:
            if C[(u,v)]-F[(u,v)] > 0 and dist[u] + d[(u,v)] < dist[v]:
                dist[v] = dist[u] + d[(u,v)]; P[v] = u
                M[v] = min(M[u], C[(u,v)] - F[(u,v)])
                if not queued[v]: Q.append(v); queued[v] = 1
    if dist[t] == float('inf'): return 0, P
    return M[t], P

def initialize(size):
    C = [[0]*size for i in range(size)] # capacity
    D = [[0]*size for i in range(size)] # distance
    G = [[] for i in range(size)] # adjacency list
    return C, D, G

def connect(a, b, c, d):
    # a -> b, capacity c, cost d
    G[a].append(b); G[b].append(a);
    D[a][b] = d; D[b][a] = -d; C[a][b] = c;