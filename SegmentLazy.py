# Segment tree with lazy propagation
# add: add l to r by val
# query: answer the query from l to r
# internal: will not be used outside the class
# this is 0-indexed

class SegLazy:
    def __init__(self, n):
        size = 1
        while size < n: size<<= 1
        self.arr = [0]*(size*2); self.lazy = [0]*(size*2); self.size = size
    
    def construct(self, L):
        for i in range(len(L)): self.arr[self.size+i] = L[i]
        for i in range(self.size-1, -1, -1): self.arr[i] = self.arr[2*i]+self.arr[2*i+1]
    
    def propagate(self, node, l, r):
        if not self.lazy[node]: return
        if node < self.size:
            self.lazy[node*2]+= self.lazy[node]
            self.lazy[node*2+1]+= self.lazy[node]
        self.arr[node] = self.arr[node] + self.lazy[node]*(r-l+1)
        self.lazy[node] = 0
    
    def add(self, l, r, val):
        self.updateinter(l, r, val, 1, 0, self.size-1)
    
    def query(self, l, r):
        return self.queryinter(l, r, 1, 0, self.size-1)
    
    def updateinter(self, l, r, val, node, nl, nr):
        self.propagate(node, nl, nr)
        if r < nl or l > nr: return
        if l <= nl and nr <= r:
            self.lazy[node]+= val
            self.propagate(node, nl, nr)
            return
        mid = (nl+nr)//2
        self.updateinter(l, r, val, node*2, nl, mid)
        self.updateinter(l, r, val, node*2+1, mid+1, nr)
        self.arr[node] = self.arr[node*2] + self.arr[node*2+1]
    
    def queryinter(self, l, r, node, nl, nr):
        self.propagate(node, nl, nr)
        if r < nl or l > nr: return 0
        if l <= nl and nr <= r: return self.arr[node]
        mid = (nl+nr)//2
        return self.queryinter(l, r, node*2, nl, mid) + self.queryinter(l, r, node*2+1, mid+1, nr)

