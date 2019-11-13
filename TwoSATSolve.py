# 2-SAT with its solution
# n = number of variables
# cnf = CNF to evaluate
# To make a clause, append (a, b) to denote a OR b

def SCC(adj):
    n = len(adj)
    idd = [False]*n; idx = [-1]*n
    stack = []; bd = []
    for v in range(-(n//2), n//2+1):
        if v==0 or idx[v] != -1: continue
        todo = [3*v]
        while todo:
            v, op = divmod(todo.pop(), 3)
            if op == 0:
                idx[v] = len(stack); stack.append(v)
                bd.append(idx[v]); todo.append(3*v+2)
                todo.extend((3*w+1 for w in adj[v]))
            elif op == 1:
                if idx[v] == -1: todo.append(3*v)
                elif not idd[v]:
                    while idx[v] < bd[-1]: bd.pop()
            elif bd[-1] == idx[v]:
                bd.pop(); scc = []
                while len(stack) != idx[v]: scc.append(stack.pop())
                for v in scc: idd[v] = True
                yield scc

def TwoSAT(n, cnf):
    adj = [[] for i in range(2*n+1)]
    for i in range(0, len(cnf), 2):
        a, b = cnf[i], cnf[i+1]
        adj[-a].append(b); adj[-b].append(a)
    scc = list(SCC(adj)); sdx = [-1]*(2*n+1)
    for i in range(len(scc)):
        for v in scc[i]: sdx[v] = i
    if any(sdx[i] == sdx[-i] for i in range(1, n+1)): return False
    assign = [-1]*n
    for i in range(len(scc)):
        for var in scc[~i]:
            if assign[abs(var)-1] == -1: assign[abs(var)-1] = var<0
    return assign

n, m = map(int,input().split())
cnf = []
for i in range(m):
    a, b = map(int,input().split())
    cnf.extend([a, b])