# Fenwick tree
# update: INCREASE i-th element by val
# getsum: sum from 0-th to i-th
# you can also use this to get "range update, single query"
# range [a,b] update val: update a val, update b+1 -val
# point p query: getsum p

# Range Fenwick tree
# update: INCREASE i-th to j-th element by val
# getsum: sum from 0-th to i-th

# 2D Fenwick tree
# update: INCREASE i,j-th element by val
# getsum: sum from 0,0-th to i,j-th

class Fenwick:
    def __init__(self, size):
        if type(size) == int: self.arr = [0]*size; return
        self.arr = size
        for i in range(len(self.arr)):
            if i|(i+1) < len(self.arr): self.arr[i|(i+1)]+= self.arr[i]
    
    def update(self, i, val):
        while i < len(self.arr): self.arr[i] += val; i |= i+1
    
    def getsum(self, i):
        res = 0
        while i >= 0: res+= self.arr[i]; i = (i&(i+1))-1
        return res
    
    def intersum(self, i, j):
        return self.getsum(j) - self.getsum(i-1)

class FenwickRUPQ:
    def __init__(self, size):
        self.arr = [0]*(size+1)
    
    def update(self, i, j, val):
        while i < len(self.arr): self.arr[i] += val; i |= i+1
        j+= 1
        while j < len(self.arr): self.arr[j] -= val; j |= j+1
    
    def get(self, i):
        res = 0
        while i >= 0: res+= self.arr[i]; i = (i&(i+1))-1
        return res



class RangeFenwick:
    def __init__(self, size):
        self.arrmul = [0]*size
        self.arradd = [0]*size

    def update(self, left, right, val):
        self.zeroupdate(left, val, -val*(left-1))
        self.zeroupdate(right, -val, val*right)
    
    def zeroupdate(self, i, mul, add):
        while i < len(self.arrmul):
            self.arrmul[i]+= mul
            self.arradd[i]+= add
            i |= i+1
    
    def getsum(self, i):
        mul, add, start = 0, 0, i
        while i >= 0:
            mul+= self.arrmul[i]
            add+= self.arradd[i]
            i = (i&(i+1))-1
        return mul * start + add
    
    def intersum(self, i, j):
        return self.getsum(j) - self.getsum(i-1)



class Fenwick2D:
    def __init__(self, row, col):
        self.arr = [[0]*col for i in range(row)]
    
    def update(self, i, j, val):
        while i < len(self.arr):
            p = j
            while p < len(self.arr[0]): self.arr[i][p] += val; p |= p+1
            i |= i+1
    
    def getsum(self, i, j):
        res = 0
        while i >= 0:
            p = j
            while p > 0: res+= self.arr[i][p]; p = (p&(p+1))-1
            i = (i&(i+1))-1
        return res
    
    def intersum(self, i1, j1, i2, j2):
        g = self.getsum
        return g(i2,j2) - g(i1-1,j2) - g(i1,j2-1) + g(i1-1,j2-1)