# Bellman-Ford algorithm, version 1
# n = number of vertices
# adj = list of adjacent nodes
# source = index of source
# returns False if negative cycle exists
# this is 0-indexed; adj[0] should be []

from sys import setrecursionlimit as SRL, stdin
SRL(550000)
input = stdin.readline

def BellmanFord(adj, source):
    n = len(adj)-1; dist = [float('inf')]*(n+1); dist[source] = 0
    for i in range(n-1):
        for u in range(1, n+1):
            for v, c in adj[u]: dist[v] = min(dist[v], dist[u]+c)
    for u in range(1, n+1):
        for v, c in adj[u]:
            if dist[u]+c < dist[v]: return False
    return dist

n, m = map(int,input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int,input().split())
    adj[a].append((b,c))

#############################################
    
# Bellman-Ford algorithm, version 2
# n = number of vertices
# edge = list of edges
# source = index of source

from sys import setrecursionlimit as SRL, stdin
SRL(550000)
input = stdin.readline

def BellmanFord(n, edge, source):
    dist = [float('inf')]*(n+1); dist[source] = 0
    for i in range(n-1):
        for u,v,c in edge: dist[v] = min(dist[v], dist[u]+c)
    for u,v,c in edge:
        if dist[u]+c < dist[v]: return False
    return dist

n, m = map(int,input().split())
edge = [tuple(map(int,input().split())) for i in range(m)]
res = BellmanFord(n, edge, 1)