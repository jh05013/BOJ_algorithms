vis = [False]*len(adj)
stack = [v]; vis[v] = True
while stack:
    p = stack.pop()
    for q in adj[p]:
        if not vis[q]: vis[q] = True; stack.append(q)

vis = [False]*len(adj)
def dfs(adj, v):
    stack = [v]; vis[v] = True
    while stack:
        p = stack.pop()
        for q in adj[p]:
            if not vis[q]: vis[q] = True; stack.append(q)