# Segment tree
# compose = composition function to use
# identity = zero element of composition function
# update: change i-th element to val
# query: answer the query from l to r
# internal: will not be used outside the class
# this is 0-indexed
# http://codeforces.com/blog/entry/18051

class SegTree:
    def __init__(_, n):
        _.n = 1
        while _.n < n: _.n<<= 1
        _.arr = [0]*(_.n*2)
    
    def construct(_, L):
        for i in range(len(L)): _.arr[_.n+i] = L[i]
        for i in range(_.n-1, -1, -1): _.arr[i] = _.arr[2*i] + _.arr[2*i+1]
    
    def update(_, i, val):
        i+= _.n; _.arr[i] = val
        while i > 1: i//=2; _.arr[i] = _.arr[i*2] + _.arr[i*2+1]
    
    def query(_, l, r):
        a = 0; l+= _.n; r+= _.n+1
        while l < r:
            if l&1: a+= _.arr[l]; l+= 1
            if r&1: r-= 1; a+= _.arr[r]
            l>>=1; r>>=1
        return a



class SegTree:
    def __init__(_, n, compose, identity):
        _.n, _.c, _.id = 1, compose, identity
        while _.n < n: _.n<<= 1
        _.arr = [_.id]*(_.n*2)
    
    def construct(_, L):
        for i in range(len(L)): _.arr[_.n+i] = L[i]
        for i in range(_.n-1, -1, -1): _.arr[i] = _.c(_.arr[2*i], _.arr[2*i+1])
    
    def update(_, i, val):
        i+= _.n; _.arr[i] = val
        while i > 1: i//=2; _.arr[i] = _.c(_.arr[i*2], _.arr[i*2+1])
    
    def query(_, l, r):
        al, ar = _.id, _.id
        l+= _.n; r+= _.n+1
        while l < r:
            if l&1: al = _.c(al, _.arr[l]); l+= 1
            if r&1: r-= 1; ar = _.c(ar, _.arr[r])
            l>>=1; r>>=1
        return _.c(al, ar)
