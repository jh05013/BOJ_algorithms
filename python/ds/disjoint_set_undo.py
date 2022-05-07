class DisjointSetUndo:
    def __init__(_, n):
        _.sz = [1]*(n+1)
        _.par = list(range(n+1))
        _.hist = []

    def union(_, x, y):
        xr = _.find(x); yr = _.find(y)
        if xr == yr: _.hist.append((None, None)); return
        if _.sz[xr] < _.sz[yr]: xr,yr = yr,xr
        _.hist.append((yr, _.par[yr]))
        _.sz[xr]+= _.sz[yr]
        _.par[yr] = xr
    
    def undo(_):
        x, p = _.hist.pop()
        if x == None: return
        _.sz[_.par[x]]-= _.sz[x]
        _.par[x] = p
        
    def find(_, x):
        while _.par[x] != x: x = _.par[x]
        return x