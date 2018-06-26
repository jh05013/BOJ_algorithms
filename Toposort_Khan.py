# Topological sorting by Khan
# False if sorting is impossible
# adj = list of adjacent nodes
# This is 1-indexed; adj[0] must be []
# If you want lexicographically minimal order, use priority queue

from collections import deque
def toposort(adj):
    n = len(adj)-1; indg = [0]*(n+1); indg[0] = -1; L = []
    for i in range(1,n+1):
        for j in adj[i]: indg[j]+= 1
    Q = deque()
    for i in range(1,n+1):
        if indg[i] == 0: Q.append(i)
    for i in range(n):
        if len(Q) == 0: raise Exception
        p = Q.popleft(); L.append(p)
        for j in adj[p]:
            indg[j]-= 1
            if indg[j] == 0: Q.append(j)
    return L

from collections import deque
def toposortCount(adj):
    n = len(adj)-1; indegree = [0]*(n+1); indegree[0] = -1; L = []
    for i in range(1,n+1):
        for j in adj[i]: indegree[j]+= 1
    Q = deque(); mflag = False
    for i in range(1,n+1):
        if indegree[i] == 0: Q.append(i)
    for i in range(n):
        if len(Q) > 1: mflag = True
        if len(Q) == 0: return "CYCLIC"
        p = Q.popleft(); L.append(p)
        for j in adj[p]:
            indegree[j]-= 1
            if indegree[j] == 0: Q.append(j)
    return "MULTIPLE" if mflag else "UNIQUE"

n, m = map(int,input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)

