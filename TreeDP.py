# When you need bfs order of tree
# adj = list of adjacent nodes (with edge costs), will be replaced
# root = root

# unweighted, root at 1
adj = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = MIS()
    adj[a].append(b)
    adj[b].append(a)

stack = [1]
vis = [False]*(n+1); vis[1] = True
while stack:
    p = stack.pop()
    TL = []
    for q in adj[p]:
        if vis[q]: continue
        vis[q] = True; stack.append(q)
        TL.append(q)
    adj[p] = TL

# weighted tree
from collections import deque
def set_root(adj, root):
    Q = deque([root]); bfsord = []
    tadj = [[] for i in range(len(adj))]
    visit = [0]*len(adj); visit[root] = True
    while Q:
        p = Q.popleft(); bfsord.append(p)
        for q, c in adj[p]:
            if visit[q]: continue
            visit[q] = True; Q.append(q)
            tadj[p].append((q,c))
    return tadj, bfsord