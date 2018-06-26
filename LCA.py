# LCA: LCA class
# adj: list of adjacent nodes
# Root is 1
# This is 1-indexed; adj[0] should be 0

from math import log2
from collections import deque
class LCA:
    def __init__(self, adj):
        n = len(adj); depth = [0]*n
        Q = deque(); Q.append(1); depth[1] = 1
        pk = [[0]*n for i in range(int(log2(n))+1)]
        while Q:
            p = Q.popleft()
            for son in adj[p]:
                if depth[son]: continue
                depth[son] = depth[p] + 1; pk[0][son] = p; Q.append(son)
        for d in range(1, len(pk)):
            for i in range(1, n):
                pk[d][i] = pk[d-1][pk[d-1][i]]
        self.pk = pk; self.depth = depth

    def kthparent(self, a, k):
        j = 0
        while k:
            if k % 2 == 1: a = self.pk[j][a]
            k//= 2; j+= 1
        return a    
    
    def LCA(self, a, b):
        if self.depth[a] < self.depth[b]: a, b = b, a
        a = self.kthparent(a, self.depth[a]-self.depth[b])
        if a == b: return a
        for j in range(len(self.pk)-1, -1, -1):
            if self.pk[j][a] != 0 and self.pk[j][a] != self.pk[j][b]:
                a = self.pk[j][a]; b = self.pk[j][b]
        return self.pk[0][a]
    
    def treedist(self, a, b):
        return self.depth[a] + self.depth[b] - 2*self.depth[self.LCA(a, b)]  
