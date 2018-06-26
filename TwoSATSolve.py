# 2-SAT with its solution
# n = number of variables
# cnf = CNF to evaluate
# To make a clause, append (a, b) to denote a OR b

from sys import setrecursionlimit as SRL, stdin
input = stdin.readline
SRL(150000)

def Tarjan(v, adj):
    n = v//2; v+= 1
    def SC(i):
        nonlocal ind
        vin[i] = ind; vll[i] = ind; ind+= 1
        stack.append(i); stacked[i] = 1
        for j in adj[i]:
            if vin[j] == 0: SC(j); vll[i] = min(vll[i], vll[j])
            elif stacked[j]: vll[i] = min(vll[i], vin[j])
        if vll[i] == vin[i]:
            scc = []; j = 0
            while j != i: j = stack.pop(); stacked[j] = 0; scc.append(j)
            res.append(scc)
    ind, stack, res = 1, [], []
    vin, vll, stacked, scx = [0]*v, [0]*v, [0]*v, [-1]*v
    for i in range(-n,n+1):
        if i!=0 and vin[i] == 0: SC(i)
    for i in range(len(res)):
        for j in res[i]: scx[j] = i+1
    return scx, res

def TwoSAT(n, cnf):
    adj = [[] for i in range(2*n+1)]
    for a, b in cnf: adj[-a].append(b); adj[-b].append(a)
    scx, res = Tarjan(2*n, adj)
    for i in range(1, n+1):
        if scx[i] == scx[-i]: return False
    assign = [-1]*(n+1)
    for i in range(len(res)-1,-1,-1):
        for var in res[i]:
            if assign[abs(var)] == -1: assign[abs(var)] = var<0
    return assign

n, m = map(int,input().split())
cnf = []
for i in range(m):
    a, b = map(int,input().split())
    cnf.append((a,b))