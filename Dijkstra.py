# Dijkstra algorithm
# n = number of vertices
# adj = list of adjacent nodes with costs
# source = index of source
# either 0-indexed or 1-indexed

import heapq
def dijkstra(adj, source):
    n = len(adj)-1; dist = [float('inf')]*(n+1)
    dist[source] = 0; PQ = [(0, source)]
    while PQ:
        d, u = heapq.heappop(PQ)
        if dist[u] != d: continue
        for v, c in adj[u]:
            if dist[v] > d+c: dist[v] = d+c; heapq.heappush(PQ, (d+c, v))
    return dist

n, m = map(int,input().split())
s = int(input())
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int,input().split())
    adj[a].append((b,c))