# LCA: LCA class
# adj: list of adjacent nodes
# Root is 1
# This is 1-indexed; adj[0] should be 0

from math import log2
from collections import deque
class LCA:
    def __init__(_, adj):
        n = len(adj); depth = [0]*n
        Q = deque([1]); depth[1] = 1
        pk = [[0]*n for i in range(int(log2(n))+1)]
        while Q:
            p = Q.popleft()
            for son in adj[p]:
                if depth[son]: continue
                depth[son] = depth[p] + 1; pk[0][son] = p; Q.append(son)
        for d in range(1, len(pk)):
            for i in range(1, n):
                pk[d][i] = pk[d-1][pk[d-1][i]]
        _.pk = pk; _.depth = depth

    def kthparent(_, a, k):
        j = 0
        while k:
            if k % 2 == 1: a = _.pk[j][a]
            k//= 2; j+= 1
        return a    

    def LCA(_, a, b):
        if _.depth[a] < _.depth[b]: a, b = b, a
        a = _.kthparent(a, _.depth[a]-_.depth[b])
        if a == b: return a
        for j in range(len(_.pk)-1, -1, -1):
            if _.pk[j][a] != 0 and _.pk[j][a] != _.pk[j][b]:
                a = _.pk[j][a]; b = _.pk[j][b]
        return _.pk[0][a]

    def treedist(_, a, b):
        return _.depth[a] + _.depth[b] - 2*_.depth[_.LCA(a, b)]  

n = int(input())
adj = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = MIS()
    adj[a].append(b)
    adj[b].append(a)
    