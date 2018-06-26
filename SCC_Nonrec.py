# Note: this returns a generator!
# This is 1-indexed

def SCC(adj):
    n = len(adj)
    idd = [False]*n; idx = [-1]*n
    stack = []; bd = []
    for v in range(1, n):
        if idx[v] != -1: continue
        todo = [('V', v)]
        while todo:
            op, v = todo.pop()
            if op == 'V':
                idx[v] = len(stack); stack.append(v)
                bd.append(idx[v]); todo.append(('P', v))
                todo.extend(reversed([('E', w) for w in adj[v]]))
            elif op == 'E':
                if idx[v] == -1: todo.append(('V', v))
                elif not idd[v]:
                    while idx[v] < bd[-1]: bd.pop()
            elif bd[-1] == idx[v]:
                bd.pop(); scc = stack[idx[v]:]
                del stack[idx[v]:]
                for v in scc: idd[v] = True
                yield scc