# Prim's algorithm for MST
# n = number of vertices
# adj = list of costs with adjacent nodes
# This is 1-indexed; adj[0] should be []

from sys import stdin
input = stdin.readline
import heapq
def Prim(adj):
    n = len(adj)-1; edges = []; MST = []
    grouped = [False]*(n+1); grouped[1] = True
    gn = 1; cost = 0
    for c, j in adj[1]: heapq.heappush(edges, (c,1,j))
    while edges and gn < n:
        c, i, j = heapq.heappop(edges)
        if grouped[j]: continue
        grouped[j] = True; gn+= 1; cost+= c; MST.append((c,i,j))
        for c, k in adj[j]: heapq.heappush(edges, (c,j,k))
    if gn != n: return float('inf'), []
    return cost, MST

v, e = map(int,input().split())
adj = [[] for i in range(v+1)]
for i in range(e):
    a, b, c = map(int,input().split())
    adj[a].append((c,b))
    adj[b].append((c,a))