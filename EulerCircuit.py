def decrease(dic, item):
    dic[item]-= 1
    if dic[item] == 0: del dic[item]
def add(dic, item):
    dic[item] = dic.setdefault(item,0) + 1

def euler(adj):
    stack = []
    circuit = []
    for i in range(n):
        if adj[i]: stack.append(i); break
    while stack:
        cur = stack[-1]
        if adj[cur]:
            nxt = next(iter(adj[cur]))
            decrease(adj[cur], nxt)
            decrease(adj[nxt], cur)
            stack.append(nxt)
        else:
            stack.pop()
            circuit.append(cur)
    if circuit[0] != circuit[-1]: return []
    return circuit