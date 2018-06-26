# Dinic algorithm for maximum flow
# adj = list of adjacent nodes, must be made bidirectional
# C = capacity matrix
# s = index of source
# t = index of sink

from collections import deque
def Dinic(G, C, s, t):
    def send(u, limit):
        if limit <= 0: return 0
        if u == t: return limit
        val = 0
        for v in G[u]:
            res = C[u][v]-flow[u][v]
            if level[v] == level[u]+1 and res>0:
                a = send(v, min(limit-val, res))
                flow[u][v]+= a; flow[v][u]-= a; val+= a
        if val == 0: level[u]-= 1
        return val
    Q, tot, n, flow = deque(), 0, len(G), [[0]*n for i in range(n)]
    while 1:
        Q.append(s); level = [-1]*n; level[s] = 0
        while len(Q) > 0:
            u = Q.popleft()
            for v in G[u]:
                if level[v] == -1 and C[u][v] > flow[u][v]: level[v] = level[u]+1; Q.append(v)
        if level[t] == -1: return tot#, flow
        tot+= send(s, sum(C[s][v] for v in G[s]))

def addedge(i, j, cap):
    G[i].append(j); G[j].append(i); C[i][j]+= cap

G = [[]]
C = [[0]*n for i in range(n)]

