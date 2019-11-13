from collections import deque
def bfs(adj, v):
    Q = deque([v])
    dist = [-1]*len(adj); dist[v] = 0
    while Q:
        p = Q.popleft()
        for q in adj[p]:
            if dist[q] != -1: continue
            dist[q] = dist[p] + 1; Q.append(q)
    return dist

