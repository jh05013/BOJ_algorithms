# Segment tree with getitem
# this is 0-indexed

class SegTree:
    def __init__(self, n):
        size = 1
        while size < n: size<<= 1
        self.arr = [0]*(size*2); self.size = size
    
    def construct(self, L):
        for i in range(len(L)): self.arr[self.size+i] = L[i]
        for i in range(self.size-1, -1, -1): self.arr[i] = self.arr[2*i] + self.arr[2*i+1]
    
    def update(self, i, val):
        # Change to += if necessary
        i+= self.size; self.arr[i] = val
        while i > 1: i//=2; self.arr[i] = self.arr[i*2] + self.arr[i*2+1]
    
    def __getitem__(self, i):
        return self._kth(i, 1)
    
    def _kth(self, k, node = 1):
        if node >= self.size: return node - self.size
        if k >= self.arr[node]: raise IndexError
        if k < self.arr[2*node]: return self._kth(k, 2*node)
        return self._kth(k-self.arr[2*node], 2*node+1)