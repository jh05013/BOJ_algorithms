# Hopcroft-Karp algorithm for bipartite matching
# ssize = size of first set
# tsize = size of second set
# adj = list of adjacent nodes from s to t
# This is 1-indexed!! adj[0] must be []

# min vertex cover = max matching (Konig theorem)
# max indset = |V| - max matching

__import__('sys').setrecursionlimit(123123)
INF = 10**9
from collections import deque
def BFS(ssz, tsz, adj, pu, pv, dist):
    Q = deque()
    for u in range(1, ssz+1):
        if pu[u] == 0: dist[u] = 0; Q.append(u)
        else: dist[u] = INF
    dist[0] = INF
    while Q:
        u = Q.popleft()
        if dist[u] >= dist[0]: continue
        for v in adj[u]:
            if dist[pv[v]] == INF: dist[pv[v]] = dist[u] + 1; Q.append(pv[v])
    return dist[0] != INF

def DFS(ssz, tsz, adj, pu, pv, dist, u):
    if u == 0: return True
    for v in adj[u]:
        if dist[pv[v]] == dist[u] + 1 and DFS(ssz, tsz, adj, pu, pv, dist, pv[v]):
            pv[v] = u; pu[u] = v; return True
    dist[u] = INF; return False

def HopcroftKarp(ssz, tsz, adj):
    assert not adj[0] and not any(0 in L for L in adj)
    pu = [0]*(ssz+1); pv = [0]*(tsz+1); dist = [-1]*(ssz+1); match = 0
    while BFS(ssz, tsz, adj, pu, pv, dist):
        for u in range(1, ssz+1):
            if pu[u] == 0: match+= DFS(ssz, tsz, adj, pu, pv, dist, u)
    return match