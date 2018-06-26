# Segment tree
# compose = composition function to use
# identity = zero element of composition function
# update: change i-th element to val
# query: answer the query from l to r
# internal: will not be used outside the class
# this is 0-indexed
# http://codeforces.com/blog/entry/18051

class SegTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n: self.n<<= 1
        self.arr = [0]*(self.n*2)
    
    def construct(self, L):
        for i in range(len(L)): self.arr[self.n+i] = L[i]
        for i in range(self.n-1, -1, -1): self.arr[i] = self.arr[2*i] + self.arr[2*i+1]
    
    def update(self, i, val):
        i+= self.n; self.arr[i] = val
        while i > 1: i//=2; self.arr[i] = self.arr[i*2] + self.arr[i*2+1]
    
    def query(self, l, r):
        a = 0; l+= self.n; r+= self.n+1
        while l < r:
            if l&1: a+= self.arr[l]; l+= 1
            if r&1: r-= 1; a+= self.arr[r]
            l>>=1; r>>=1
        return a



class SegTree:
    def __init__(self, n, compose, identity):
        self.n, self.c, self.id = 1, compose, identity
        while self.n < n: self.n<<= 1
        self.arr = [self.id]*(self.n*2)
    
    def construct(self, L):
        for i in range(len(L)): self.arr[self.n+i] = L[i]
        for i in range(self.n-1, -1, -1): self.arr[i] = self.c(self.arr[2*i], self.arr[2*i+1])
    
    def update(self, i, val):
        i+= self.n; self.arr[i] = val
        while i > 1: i//=2; self.arr[i] = self.c(self.arr[i*2], self.arr[i*2+1])
    
    def query(self, l, r):
        al, ar = self.id, self.id
        l+= self.n; r+= self.n+1
        while l < r:
            if l&1: al = self.c(al, self.arr[l]); l+= 1
            if r&1: r-= 1; ar = self.c(ar, self.arr[r])
            l>>=1; r>>=1
        return self.c(al, ar)
