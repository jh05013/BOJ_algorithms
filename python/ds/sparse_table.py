class SparseTable:
    def __init__(_, mmax, arr):
        _.n = len(arr)
        _.fk = [arr[:]]
        _.mmax = mmax
        for i in range(mmax.bit_length()+1):
            L = _.fk[-1]
            _.fk.append([L[L[x]] for x in range(_.n)])
    
    # f(f(...(x)...)) where f is applied m times
    def query(_, m, x):
        assert m <= _.mmax
        for L in _.fk:
            if m&1: x = L[x]
            m>>= 1
        return x
    
    # min m s.t f(f(...(x)...)) satisfies cond
    # None if cond is always false
    def bin_search_min(_, x, cond):
        if cond(x): return 0
        ans = 0
        for i in range(len(_.fk)-1, -1, -1):
            if cond(_.fk[i][x]): continue
            ans|= 1<<i
            x = _.fk[i][x]
        ans+= 1; x = _.fk[0][x]
        return ans if x <= _.mmax and cond(x) else None
