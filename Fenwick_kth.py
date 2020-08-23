# Fenwick tree that supports the "kth-element" operation in O(logn)
# k is 1-indexed

class Fenwick:
    def __init__(_, size):
        _.lsz = 0; sz = 1
        while sz < size: _.lsz+= 1; sz*= 2
        _.arr = [0]*sz
    
    def add(_, i, val):
        while i < len(_.arr): _.arr[i] += val; i |= i+1
    
    def getsum(_, i):
        res = 0
        while i >= 0: res+= _.arr[i]; i = (i&(i+1))-1
        return res
    
    def kth(_, k):
        l = 0; r = len(_.arr)
        for i in range(_.lsz+1):
            mid = (l+r) // 2
            val = _.arr[mid-1]
            if val >= k: r = mid
            else: l = mid; k-= val
        return l