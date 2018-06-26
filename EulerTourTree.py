# Euler tour technique
# Express the tree with Euler tour so that subtrees correspond to intervals
# --> Enables subtree update via segment trees

# you can use Fenwick to get "range update, single query"
# range [a,b] update val: update a val, update b+1 -val
# point p query: getsum p

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

def eulertour(tadj):
    res = [1]; stack = [1]; iteradj = [iter(a) for a in tadj]
    while stack:
        try: p = next(iteradj[stack[-1]]); res.append(p); stack.append(p)
        except StopIteration: res.append(stack.pop())
    first = [-1]*len(tadj); last = [-1]*len(tadj)
    for i in range(len(res)):
        if first[res[i]] != -1: last[res[i]] = i
        else: first[res[i]] = i
    return res, first, last