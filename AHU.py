# AHU algorithm for tree isomorphism
# T1 and T2 are isomorphic iff AHU(T1) == AHU(T2)
# you must specify one vertex inside a tree

def centroid(adj, root):
    dfsord = []
    sz = {-1: 0}
    stack = [(root, -1)]
    while stack:
        u, prev = stack.pop(); dfsord.append((u, prev))
        sz[u] = 1
        for v in adj[u]:
            if v == prev: continue
            stack.append((v, u))
    for u, prev in reversed(dfsord): sz[prev]+= sz[u]
    n = sz[root]
    ans = []
    for u, par in dfsord:
        if any(sz[v] > n//2 for v in adj[u] if v != par): continue
        if n-sz[u] <= n//2: ans.append(u)
    return ans

def ten(adj, r):
    # rooted tree hash rooted at r
    vis = [False]*len(adj); vis[r] = True
    stack = [r]
    dfsord = [r]
    tadj = [[] for i in range(len(adj))]
    while stack:
        p = stack.pop()
        for q in adj[p]:
            if vis[q]: continue
            vis[q] = True; stack.append(q)
            dfsord.append(q)
            tadj[p].append(q)
    H = [None]*len(adj)
    for v in reversed(dfsord):
        H[v] = '1' + ''.join(sorted(H[u] for u in tadj[v])) + '0'
    return H[r]

def ahu(adj, start):
    T = centroid(adj, start)
    if len(T) == 1: return ten(adj, T[0])
    A, B = ten(adj, T[0]), ten(adj, T[1])
    if A>B: A,B=B,A
    return (A, B)