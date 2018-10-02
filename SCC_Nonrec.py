# A generator
# This is 1-indexed

def SCC(adj):
    n = len(adj)
    idd = [False]*n; idx = [-1]*n
    stack = []; bd = []
    for v in range(1, n):
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

# Returns indices

def SCC(adj):
    n = len(adj)
    idd = [0]*n; idx = [-1]*n
    stack = []; bd = []
    scid = 1
    for v in range(1, n):
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
                for v in scc: idd[v] = scid
                scid+= 1
    return idd