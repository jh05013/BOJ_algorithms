# Tarjan algorithm for articulation points
# n = number of vertices
# adj = list of adjacent nodes
# This is 1-indexed; adj[0] should be []

# BCC: Output actual components
# n = number of vertices
# adj = list of adjacent nodes
# This is 1-indexed; adj[0] should be []

from sys import setrecursionlimit as SRL, stdin
SRL(150000)
input = stdin.readline

def ArtTarjan(n, adj):
    parent = [None]*(n+1); visited = [False]*(n+1)
    depth = [-1]*(n+1); low = [-1]*(n+1); res = []
    for i in range(1, n+1):
        if not visited[i]:
            articulation(n, adj, i, 0, parent, visited, depth, low, res)
    return res

def articulation(n, adj, i, d, parent, visited, depth, low, res):
    visited[i] = True; depth[i] = d; low[i] = d
    child = 0; articulate = False
    for j in adj[i]:
        if not visited[j]:
            parent[j] = i
            articulation(n, adj, j, d+1, parent, visited, depth, low, res)
            child+= 1
            if low[j] >= depth[i]: articulate = True
            low[i] = min(low[i], low[j])
        elif j != parent[i]: low[i] = min(low[i], depth[j])
    if (parent[i] != None and articulate) or (parent[i] == None and child > 1):
        res.append(i)

def BCC(n, adj):
    def dfs(u):
        nonlocal count
        visited[u] = True; count+= 1; d[u] = count; low[u] = d[u]
        for v in adj[u]:
            if not visited[v]:
                stack.append((u,v)); parent[v] = u; dfs(v)
                if low[v] >= d[u]: outcomp(u,v)
                low[u] = min(low[u], low[v])
            elif not parent[u]==v and d[v]<d[u]:
                stack.append((u,v))
                low[u] = min(low[u], d[v])
                
    def outcomp(u, v):
        while 1:
            e = stack.pop()
            print(e, end=' ')
            if e == (u,v) or e == (v,u): break
        print()
    
    count = 0; stack = []
    visited = [False]*(n+1); parent = [None]*(n+1);
    d = [-1]*(n+1); low = [-1]*(n+1)
    for u in range(1, n+1):
        if not visited[u]: dfs(u)

v, e = map(int,input().split())
adj = [[] for i in range(v+1)]
for i in range(e):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
bi = ArtTarjan(v, adj)
bi.sort()
