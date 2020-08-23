# Disjoint set
# This can be either 0-indexed or 1-indexed



# Minimalism
__import__('sys').setrecursionlimit(123123)
class DisjointSet:
    def __init__(_, n): _.par = list(range(n+1))
    def union(_, x, y): _.par[_.find(x)] = _.find(y)
    def find(_, x):
        if _.par[x] != x: _.par[x] = _.find(_.par[x])
        return _.par[x]
    
    

# Disjoint set without union by rank
__import__('sys').setrecursionlimit(123123)
class DisjointSet:
    def __init__(_, n):
        _.par = list(range(n+1))

    def union(_, x, y): # yr becomes parent
        xr = _.find(x); yr = _.find(y)
        _.par[xr] = yr
        
    def find(_, x):
        if _.par[x] != x: _.par[x] = _.find(_.par[x])
        return _.par[x]



# Disjoint set with sizes
__import__('sys').setrecursionlimit(123123)
class DisjointSet:
    def __init__(_, n):
        _.par = list(range(n+1))
        _.size = [1]*(n+1)

    def union(_, x, y): # yr becomes parent
        xr = _.find(x); yr = _.find(y)
        if xr == yr: return
        _.par[xr] = yr
        _.size[yr]+= _.size[xr]
        
    def find(_, x):
        if _.par[x] != x: _.par[x] = _.find(_.par[x])
        return _.par[x]



# Disjoint set with union by rank
class DisjointSet:
    def __init__(_, n):
        _.rank = [0]*(n+1)
        _.par = list(range(n+1))

    def union(_, x, y):
        xr = _.find(x); yr = _.find(y)
        if xr == yr: return
        if _.rank[xr] < _.rank[yr]: _.par[xr] = yr
        elif _.rank[xr] > _.rank[yr]: _.par[yr] = xr
        else: _.par[yr] = xr; _.rank[xr]+= 1
        
    def find(_, x):
        if _.par[x] != x: _.par[x] = _.find(_.par[x])
        return _.par[x]


