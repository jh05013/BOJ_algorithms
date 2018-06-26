def SCC(adj):
    def dfs(count, v):
        pre[v] = count; count+= 1
        S.append(v); P.append(v)
        for w in adj[v]:
            if pre[w] == -1: count = dfs(count, w)
            elif not scced[w]:
                while P and pre[P[-1]] > pre[w]: P.pop()
        if not P or P[-1] != v: return count
        comp = []
        while S:
            w = S.pop(); scced[w] = True; comp.append(w)
            if w == v: break
        P.pop(); sccs.append(comp)
        return count
    n, count = len(adj), 0
    pre, scced = [-1]*n, [False]*n; S, P, sccs = [], [], []
    for v in range(1, n):
        if pre[v] == -1: count = dfs(count, v)
    return sccs