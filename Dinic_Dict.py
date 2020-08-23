__import__('sys').setrecursionlimit(12345)
from collections import deque, defaultdict
def Dinic(G, C, s, t):
    def send(u, limit):
        if limit <= 0: return 0
        if u == t: return limit
        val = 0
        for v in G[u]:
            res = C[u,v]-flow[u,v]
            if L[v] == L[u]+1 and res>0:
                a = send(v, min(limit-val, res))
                flow[u,v]+= a; flow[v,u]-= a; val+= a
        if val == 0: L[u]-= 1
        return val
    Q, tot, n, flow = deque(), 0, len(G), defaultdict(int)
    while 1:
        Q.append(s); L = [-1]*n; L[s] = 0
        while Q:
            u = Q.popleft()
            for v in G[u]:
                if L[v] != -1 or C[u,v] <= flow[u,v]: continue
                L[v] = L[u]+1; Q.append(v)
        if L[t] == -1: return tot#, flow
        tot+= send(s, sum(C[s,v] for v in G[s]))

def initialize(n):
    return [[] for i in range(n+1)], defaultdict(int)

def connect(i, j, cap):
    G[i].append(j); G[j].append(i); C[i,j]+= cap

totl = 0
def addlr(i, j, l, r):
    # -2 is newsource, -1 is newsink
    global totl; totl+= l
    addedge(i, len(G)-1, l)
    addedge(len(G)-2, j, l)
    addedge(i, j, r-l)

# above is for LR-flow; add INF from sink to source, then find maxflow from newsource to newsink
# and check if maxflow equals totl
