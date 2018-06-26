class Node:
    def __init__(z, key, h, val = None):
        z.key = key; z.val = val
        z.adj = [None] * h

import random
INF = float('inf')
class Skiplist:
    def __init__(z, h):
        z.head = Node(-INF, h, -1)
        z.tail = Node(INF, h, -1)
        z.h = h
        for i in range(h): z.head.adj[i] = z.tail
    
    def find(z, x):
        i = z.h-1; node = z.head
        res = [None] * z.h
        while i >= 0:
            while node.adj[i].key <= x: node = node.adj[i]
            res[i] = node; i-= 1
        return res
    
    def insert(z, x, val = None, prevs = None):
        if not prevs: prevs = z.find(x)
        node = Node(x, 0, val)
        for i in range(z.h):
            L = prevs[i]; R = L.adj[i]
            node.adj.append(R); L.adj[i] = node
            if random.random() < 0.5: break
        return node