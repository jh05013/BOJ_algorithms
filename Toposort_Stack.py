# This is 1-indexed; adj[0] should be []

def toposort(adj):
    n = len(adj)-1; indg = [0]*(n+1); L = []
    for i in range(1,n+1):
        for j in adj[i]: indg[j]+= 1
    S = [i for i in range(1,n+1) if indg[i] == 0]
    for i in range(n):
        #if not S: raise Exception
        p = S.pop(); L.append(p)
        for j in adj[p]:
            indg[j]-= 1
            if indg[j] == 0: S.append(j)
    return L
