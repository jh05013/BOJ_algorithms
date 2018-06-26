# Tarjan algorithm for strongly connected component
# v = number of vertices
# adj = list of adjacent nodes
# This is 1-indexed; adj[0] should be []

from sys import setrecursionlimit as SRL, stdin
SRL(150000)

def SCC(adj):
    # given |V| and adj, compute SCC
    def SC(i):
        nonlocal ind
        vin[i] = ind; vll[i] = ind; ind+= 1
        stack.append(i); stacked[i] = 1
        for j in adj[i]:
            if vin[j] == 0: SC(j); vll[i] = min(vll[i], vll[j])
            elif stacked[j]: vll[i] = min(vll[i], vin[j])
        if vll[i] == vin[i]:
            scc = []; j = 0
            while j != i:
                j = stack.pop(); stacked[j] = 0; scc.append(j)
            res.append(scc)
    v, ind, stack, res = len(adj), 1, [], []
    vin, vll, stacked = [0]*v, [0]*v, [0]*v
    for i in range(1, v):
        if vin[i] == 0: SC(i)
    return res
    
input = stdin.readline
v, e = map(int,input().split())
adj = [[] for i in range(v+1)]
for i in range(e):
    a, b = map(int,input().split())
    adj[a].append(b)
scc = SCCTarjan(v, adj)
for s in scc:
    s.sort()
scc.sort()