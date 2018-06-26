# Topological sorting by DFS
# False if sorting is impossible
# n = number of vertices
# adj = list of adjacent nodes
# This is 1-indexed; adj[0] must be []

from sys import setrecursionlimit as SRL, stdin
SRL(150000)
input = stdin.readline

def topology(n, adj):
    def DFS(i):
        if tempmark[i]: raise Exception # not a DAG!
        tempmark[i] = 1
        for j in adj[i]:
            if j not in unmarked: continue
            if not DFS(j): raise Exception
        unmarked.remove(i); tempmark[i] = 0; L.append(i)
        return True
    unmarked = set(range(1,n+1)); tempmark = [0]*(n+1); L = []
    while unmarked:
        i = next(iter(unmarked))
        if not DFS(i): raise Exception # not a DAG!
    return L[::-1]

n, m = map(int,input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)
