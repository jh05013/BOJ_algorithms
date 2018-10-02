# Segment tree with lazy propagation
# combine: Two sons have values a and b. Assuming no lazy values, what should be the parent value?
# combineL: A node with laziness a recieved the new laziness b. What should be the resulting laziness?
# unlazy: If a node x having range [a, b] has some laziness, what should be its real value?
# this is 0-indexed

class SegLazy:
    def combine(_, a, b):
        return a+b
    
    def combineL(_, a, b):
        return a+b
    
    def unlazy(_, x, nl, nr):
        _.arr[x]+= _.lazy[x] * (nr-nl+1)
    
    def __init__(_, sz):
        _.id = 0
        _.unused = 0
        ######################
        n = 1
        while n < sz: n<<= 1
        _.arr = [_.id]*(n*2); _.lazy = [_.unused]*(n*2); _.n = n
    
    def construct(_, A):
        for i in range(len(A)): _.arr[_.n+i] = A[i]
        for i in range(_.n-1, -1, -1): _.arr[i] = _.combine(_.arr[2*i], _.arr[2*i+1])
    
    def propagate(_, x, nl, nr):
        if _.lazy[x] == _.unused: return
        if x < _.n:
            _.lazy[x*2] = _.combineL(_.lazy[x*2], _.lazy[x])
            _.lazy[x*2+1] = _.combineL(_.lazy[x*2+1], _.lazy[x])
        _.unlazy(x, nl, nr)
        _.lazy[x] = _.unused
    
    def update(_, l, r, val, x=1, nl=0, nr=None):
        if nr == None: nr = _.n-1
        _.propagate(x, nl, nr)
        if r < nl or nr < l: return
        if l <= nl and nr <= r:
            _.lazy[x] = _.combineL(_.lazy[x], val)
            _.propagate(x, nl, nr)
            return
        mid = (nl + nr) // 2
        _.update(l, r, val, x*2, nl, mid); _.update(l, r, val, x*2+1, mid+1, nr)
        _.arr[x] = _.combine(_.arr[x*2], _.arr[x*2+1])
    
    def query(_, l, r, x=1, nl=0, nr=None): 
        if nr == None: nr = _.n-1
        _.propagate(x, nl, nr)
        if r < nl or nr < l: return _.id
        if l <= nl and nr <= r: return _.arr[x]
        mid = (nl + nr) // 2
        return _.combine(_.query(l, r, x*2, nl, mid), _.query(l, r, x*2+1, mid+1, nr))