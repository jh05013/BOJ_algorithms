from sys import setrecursionlimit as SRL, stdin
#SRL(232323)
input = stdin.readline

class Fenwick:
    def __init__(self, size):
        if type(size) == int: self.arr = [0]*size; return
        self.arr = size
        for i in range(len(self.arr)):
            if i|(i+1) < len(self.arr): self.arr[i|(i+1)]+= self.arr[i]
    
    def __repr__(self):
        return "<" + ", ".join(map(str, self.arr)) + ">"
    
    def update(self, i, val):
        while i < len(self.arr): self.arr[i] += val; i |= i+1
    
    def getsum(self, i):
        res = 0
        while i >= 0: res+= self.arr[i]; i = (i&(i+1))-1
        return res
    
    def intersum(self, i, j):
        return self.getsum(j) - self.getsum(i-1)

class HLD:
    def __init__(self, adj):
        n = len(adj)-1; self.adj = adj
        self.tadj = [[] for i in range(n+1)]
        self.dist = [-1]*(n+1); self.size = [1]*(n+1); self.dist[1] = 0
        self.par = [-1]*(n+1); self.par[1] = 1; self.pcost = [0]*(n+1)
        self.chain = [-1]*(n+1); self.tail = []; self.segs = []
        self.init_dfs(1); self.chain_dfs(1, [])
    
    def init_dfs(self, v):
        for u, c in self.adj[v]:
            if self.par[u] != -1: continue
            self.dist[u] = self.dist[v]+1; self.par[u] = v; self.pcost[u] = c
            self.init_dfs(u); self.size[v]+= self.size[u]; self.tadj[v].append(u)
    
    def chain_dfs(self, v, cont):
        if not cont: self.chain[v] = len(self.tail); self.tail.append(v)
        cont.append(self.pcost[v])
        if not self.tadj[v]: self.segs.append(Fenwick(cont)); return
        u = max(self.tadj[v], key = lambda x: self.size[x])
        self.chain[u] = self.chain[v]; self.chain_dfs(u, cont)
        for s in self.tadj[v]:
            if s != u: self.chain_dfs(s, [])
    
    def pos(self, x, c): # c should be self.chain[x]
        return self.dist[x]-self.dist[self.tail[c]]
    
    def query_td(self, u, v): # u must be above v
        c = self.chain[v]
        if self.chain[u] == self.chain[v]: return self.segs[c].intersum(self.pos(u, c), self.pos(v, c))
        top = self.tail[c]
        return self.query_td(top, v) + self.segs[c].getsum(self.pos(u, c))
    
    def lca(self, x, y):
        while self.chain[x] != self.chain[y]:
            x1 = self.tail[self.chain[x]]
            y1 = self.tail[self.chain[y]]
            if self.dist[x1] > self.dist[y1]: x = self.par[x1]
            else: y = self.par[y1]
        return x if self.dist[x] < self.dist[y] else y    

def inp_tree():
    adj = [[] for i in range(n+1)]
    edges = []
    for i in range(n-1):
        a, b, c = map(int,input().split())
        adj[a].append((b,c))
        adj[b].append((a,c))
        edges.append((a,b))
    return HLD(adj), edges

n = int(input())
tree, edges = inp_tree()
m = int(input())
