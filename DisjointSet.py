# Disjoint set
# This can be either 0-indexed or 1-indexed

# Disjoint set without union by rank
__import__('sys').setrecursionlimit(123123)
class DisjointSet:
    def __init__(self, n):
        self.par = list(range(n+1))

    def union(self, x, y): # yr becomes parent
        xr = self.find(x); yr = self.find(y)
        self.par[xr] = yr
        
    def find(self, x):
        if self.par[x] != x: self.par[x] = self.find(self.par[x])
        return self.par[x]



# Disjoint set with sizes
__import__('sys').setrecursionlimit(123123)
class DisjointSet:
    def __init__(self, n):
        self.par = list(range(n+1))
        self.size = [1]*(n+1)

    def union(self, x, y): # yr becomes parent
        xr = self.find(x); yr = self.find(y)
        if xr == yr: return
        self.par[xr] = yr
        self.size[yr]+= self.size[xr]
        
    def find(self, x):
        if self.par[x] != x: self.par[x] = self.find(self.par[x])
        return self.par[x]



# Disjoint set with union by rank
class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.par = list(range(n+1))

    def union(self, x, y):
        xr = self.find(x); yr = self.find(y)
        if xr == yr: return
        if self.rank[xr] < self.rank[yr]: self.par[xr] = yr
        elif self.rank[xr] > self.rank[yr]: self.par[yr] = xr
        else: self.par[yr] = xr; self.rank[xr]+= 1
        
    def find(self, x):
        if self.par[x] != x: self.par[x] = self.find(self.par[x])
        return self.par[x]


