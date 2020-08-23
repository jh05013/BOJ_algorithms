# Dinic algorithm but in case the path is very, very long
# adj = list of adjacent nodes, must be made bidirectional
# C = capacity dict
# s = index of source
# t = index of sink

from collections import deque, defaultdict
def Dinic(G, C, s, t):
    def send(u, limit):
        stack = [(0, u, limit, 0)] # phase, u, lim, val
        while stack:
            phase, u, lim, val = stack.pop()
            if lim <= 0: continue
            elif u == t:
                ph2, u2, lim2, val2 = stack.pop()
                flow[(u2,u)]+= lim; flow[(u,u2)]-= lim; val2+= lim
                stack.append((ph2, u2, lim2, val2))
            elif phase == 0:
                vs = [v for v in G[u] if level[v] == level[u]+1]
                stack.append((vs, u, lim, val))
            elif type(phase) == list and phase:
                v = phase.pop()
                stack.append((phase, u, lim, val))
                res = C[(u,v)] - flow[(u,v)]
                if res > 0: stack.append((0, v, min(lim-val, res), 0))
            elif type(phase) == list and not phase:
                if not stack: return val
                ph2, u2, lim2, val2 = stack.pop()
                flow[(u2,u)]+= val; flow[(u,u2)]-= val; val2+= val
                stack.append((ph2, u2, lim2, val2))
        return 0
    Q = deque(); tot = 0; n = len(G); flow = defaultdict(int)
    while 1:
        Q.append(s); level = [-1]*n; level[s] = 0
        while len(Q) > 0:
            u = Q.popleft()
            for v in G[u]:
                if level[v] == -1 and C[(u,v)] > flow[(u,v)]:
                    level[v] = level[u]+1; Q.append(v)
        if level[t] == -1: return tot#, flow
        tot+= send(s, sum(C[(s,v)] for v in G[s]))

def addedge(i, j, cap):
    G[i].append(j); G[j].append(i); C[(i,j)]+= cap