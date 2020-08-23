from heapq import *
class RemovableMinHeap:
    def __init__(_): _.A = []; _.B = []
    def insert(_, x): heappush(_.A, x)
    def remove(_, x): heappush(_.B, x)
    def top(_):
        while _.B and _.A[0] == _.B[0]: heappop(_.A); heappop(_.B)
        return _.A[0]
    def pop(_):
        x = _.top(); _.remove(x)
        return x

__import__('sys').setrecursionlimit(123123)
class DisjointSet:
    def __init__(_, n): _.par = list(range(n+1))
    def union(_, x, y): _.par[_.find(x)] = _.find(y)
    def find(_, x):
        if _.par[x] != x: _.par[x] = _.find(_.par[x])
        return _.par[x]

def prufer(edge):
    n = len(edge)+1
    adj = [[] for i in range(n+1)]
    deg = [0]*(n+1)
    rem = [False]*(n+1)
    for a, b in edge:
        deg[a]+= 1
        deg[b]+= 1
        adj[a].append(b)
        adj[b].append(a)
    
    leaf = [v for v in range(1, n+1) if deg[v] == 1]
    heapify(leaf)
    seq = []
    for i in range(n-2):
        a = heappop(leaf)
        b = max(v for v in adj[a] if not rem[v])
        seq.append(b)
        rem[a] = True
        deg[b]-= 1
        if deg[b] == 1:
            heappush(leaf, b)
    return seq

def verify(edge):
    n = len(edge)+1
    DS = DisjointSet(n)
    for a,b in edge:
        assert DS.find(a) != DS.find(b)
        DS.union(a, b)

def rebuild(seq):
    n = len(seq)+2
    H = RemovableMinHeap()
    cnt = [0]*(n+1)
    insd = [False]*(n+1)
    edge = []
    for v in seq: cnt[v]+= 1
    for v in range(1, n+1):
        if cnt[v] == 0: H.insert(v); insd[v] = True
    for v in seq:
        u = H.pop()
        edge.append((v, u))
        cnt[v]-= 1
        if cnt[v] == 0: H.insert(v); insd[v] = True
    edge.append((H.pop(), H.pop()))
    
    #verify(edge)
    #assert seq == prufer(edge)
    
    return edge

#####################################################

import random
def gen(n):
    seq = [random.randrange(1,n+1) for i in range(n-2)]
    return rebuild(seq)

n = 5000
b = random.randrange(100)
black = random.sample(range(1, n+1), b)

print(n, b)
print(*black)
for a,b in gen(n): print(a, b)
print(0)