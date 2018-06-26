# Indexable skip list
# __getitem__: returns k-th element, 0-indexed
# update: will not be used outside the class
# find: if used outside the class, returns the maximal element up to val
# insert: insert val
# remove: remove val
# iterate: show the structure of the list, use this to debug

class Node:
    def __init__(self, height = 0, key = None):
        self.key = key
        self.adj = [None]*height
        self.width = [float('inf')]*height

import random
class IndSkipList:
    def __init__(self):
        self.head = Node()
    
    def __getitem__(self, idx):
        x = self.head; idx+= 1
        for i in reversed(range(len(self.head.adj))):
            while x.width[i] <= idx and x.adj[i]: idx-= x.width[i]; x = x.adj[i]
        return x.key
    
    def update(self, val):
        update = [None]*len(self.head.adj)
        wd = [0]*len(self.head.adj)
        x = self.head
        for i in reversed(range(len(self.head.adj))):
            while x.adj[i] != None and x.adj[i].key < val:
                wd[i]+= x.width[i]; x = x.adj[i]
            update[i] = x
        return update, wd
    
    def find(self, val, update = None, exact = False):
        if not update: update, wd = self.update(val)
        if len(update) == 0: return None
        cand = update[0].adj[0]
        matched = cand and cand.key == val
        if exact and matched: return cand
        if not exact: return (val, sum(wd)) if matched else (update[0].key, sum(wd)-1)
    
    def insert(self, val):
        h, d = 1, 0
        while random.random() < 0.5: h+= 1
        node = Node(h, val)
        while len(self.head.adj) < len(node.adj):
            self.head.adj.append(None)
            self.head.width.append(float('inf'))
        update, wd = self.update(val)
        if self.find(val, update, True): raise KeyError
        nl = len(node.adj)
        for i in range(nl):
            node.adj[i] = update[i].adj[i]; node.width[i] = update[i].width[i]-d
            update[i].adj[i] = node; update[i].width[i] = d+1; d+= wd[i]
        for i in range(nl, len(self.head.adj)): update[i].width[i]+= 1
    
    def remove(self, val):
        update, wd = self.update(val)
        x = self.find(val, update, True)
        if not x: raise KeyError
        nl = len(x.adj)
        for i in range(nl):
            update[i].adj[i] = x.adj[i]; update[i].width[i]+= x.width[i]-1
        for i in range(nl, len(self.head.adj)): update[i].width[i]-= 1
            
    def iterate(self):
        # use this to debug
        x = self.head
        while x: print(x.key,
                       [((x.adj[i].key,x.width[i]) if x.adj[i] else None)
                        for i in range(len(x.adj))]); x = x.adj[0]
        
s = IndSkipList()
s.insert(234)
s.insert(2003)
s.insert(3)
s.insert(532)
s.iterate()
for i in range(4): assert s[i] == [3,234,532,2003][i]