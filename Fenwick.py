# Fenwick tree
# This is 0-indexed or 1-indexed

# The most basic form
class Fenwick:
    def __init__(_, size): _.arr = [0]*size
    def add(_, i, val):
        while i < len(_.arr): _.arr[i] += val; i |= i+1
    def getsum(_, i):
        res = 0
        while i >= 0: res+= _.arr[i]; i = (i&(i+1))-1
        return res
    def intersum(_, i, j): return _.getsum(j) - _.getsum(i-1)

# Supports initialization and intersum
class Fenwick:
    def __init__(_, size):
        if type(size) == int: _.arr = [0]*size; return
        _.arr = size[:]
        for i in range(len(_.arr)):
            if i|(i+1) < len(_.arr): _.arr[i|(i+1)]+= _.arr[i]
    
    def add(_, i, val):
        while i < len(_.arr): _.arr[i] += val; i |= i+1
    
    def getsum(_, i):
        res = 0
        while i >= 0: res+= _.arr[i]; i = (i&(i+1))-1
        return res
    
    def intersum(_, i, j):
        return _.getsum(j) - _.getsum(i-1)

# Update instead of add, list-initialized
class Fenwick:
    def __init__(_, L):
        _.arr = L[:]; _.f = L[:]
        for i in range(len(_.f)):
            if i|(i+1) < len(_.f): _.f[i|(i+1)]+= _.f[i]
    
    def update(_, i, val):
        dv = val - _.arr[i]
        _.arr[i] = val
        while i < len(_.f): _.f[i] += dv; i |= i+1
    
    def getsum(_, i):
        res = 0
        while i >= 0: res+= _.f[i]; i = (i&(i+1))-1
        return res
    
    def intersum(_, i, j):
        return _.getsum(j) - _.getsum(i-1)

# Range add, point query
class RUPQ:
    def __init__(_, size):
        _.arr = [0]*(size+1)
    
    def update(_, i, j, val):
        while i < len(_.arr): _.arr[i] += val; i |= i+1
        j+= 1
        while j < len(_.arr): _.arr[j] -= val; j |= j+1
    
    def get(_, i):
        res = 0
        while i >= 0: res+= _.arr[i]; i = (i&(i+1))-1
        return res
    
# Range add, range query
class RangeFenwick:
    def __init__(_, size):
        _.arrmul = [0]*size
        _.arradd = [0]*size

    def update(_, left, right, val):
        _.zeroupdate(left, val, -val*(left-1))
        _.zeroupdate(right, -val, val*right)
    
    def zeroupdate(_, i, mul, add):
        while i < len(_.arrmul):
            _.arrmul[i]+= mul
            _.arradd[i]+= add
            i |= i+1
    
    def getsum(_, i):
        mul, add, start = 0, 0, i
        while i >= 0:
            mul+= _.arrmul[i]
            add+= _.arradd[i]
            i = (i&(i+1))-1
        return mul * start + add
    
    def intersum(_, i, j):
        return _.getsum(j) - _.getsum(i-1)

# Two-dimensional
class Fenwick2D:
    def __init__(_, row, col):
        _.arr = [[0]*col for i in range(row)]
    
    def update(_, i, j, val):
        while i < len(_.arr):
            p = j
            while p < len(_.arr[0]): _.arr[i][p] += val; p |= p+1
            i |= i+1
    
    def getsum(_, i, j):
        res = 0
        while i >= 0:
            p = j
            while p > 0: res+= _.arr[i][p]; p = (p&(p+1))-1
            i = (i&(i+1))-1
        return res
    
    def intersum(_, i1, j1, i2, j2):
        g = _.getsum
        return g(i2,j2) - g(i1-1,j2) - g(i1,j2-1) + g(i1-1,j2-1)