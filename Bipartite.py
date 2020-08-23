# check if the graph is bipartite
from collections import deque
def bipartite(adj):
    color = [0]*(n+1); Q = deque()
    for v in range(n+1):
        if color[v]: continue
        color[v] = 1; Q.append(v)
        while Q:
            p = Q.popleft()
            for q in adj[p]:
                if color[q] and color[p] == color[q]: return False
                if color[q]: continue
                color[q] = 3-color[p]; Q.append(q)
    return True  