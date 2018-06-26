# Suurballe algorithm for finding the shortest two edge-disjoint paths
# Since we manipulate the graph, use [{}, {}...] as adj
# 1-indexed

import heapq
def Dijkstra(adj, source):
    n = len(adj)-1; dist = [float('inf')]*(n+1)
    dist[source] = 0; PQ = [(0, source)]; prev = [-1]*(n+1)
    while PQ:
        d, u = heapq.heappop(PQ)
        if dist[u] != d: continue
        for v in adj[u]:
            c = adj[u][v]
            if dist[v] > d+c: dist[v] = d+c; prev[v] = u; heapq.heappush(PQ, (d+c, v))
    return dist, prev

from copy import deepcopy
def Suurballe(nadj, s, t):
    adj = deepcopy(nadj)
    d1, prev1 = Dijkstra(adj, s)
    for u in range(1, len(adj)):
        for v in adj[u]: adj[u][v]+= d1[u]-d1[v]
    p = t; paths = set()
    while p != s:
        q = prev1[p]; adj[p][q] = 0; del adj[q][p]
        paths.add((q, p)); p = q
    d2, prev2 = Dijkstra(adj, s)
    p = t
    while p != s:
        q = prev2[p]
        if (p, q) in paths: paths.remove((p, q))
        else: paths.add((q, p))
        p = q
    return paths