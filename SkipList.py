# Skip list
# update: will not be used outside the class
# find: if used outside the class, returns the maximal element up to val
# insert: insert val
# remove: remove val
# iterate: show the structure of the list, use this to debug

class Node:
    def __init__(self, height = 0, key = None):
        self.key = key
        self.adj = [None]*height

import random
class SkipList:
    def __init__(self):
        self.head = Node()
    
    def update(self, val):
        update = [None]*len(self.head.adj)
        x = self.head
        for i in reversed(range(len(self.head.adj))):
            while x.adj[i] != None and x.adj[i].key < val: x = x.adj[i]
            update[i] = x
        return update
    
    def find(self, val, update = None, exact = False):
        # if not exact, find the max element <= val
        # return None if nothing is found
        if not update: update = self.update(val)
        if len(update) == 0: return None
        cand = update[0].adj[0]
        matched = cand and cand.key == val
        if exact and matched: return cand
        if not exact: return val if matched else update[0].key
    
    def insert(self, val):
        h = 1
        while random.random() < 0.5: h+= 1
        node = Node(h, val)
        while len(self.head.adj) < len(node.adj):
            self.head.adj.append(None)
        update = self.update(val)
        if self.find(val, update, True): raise KeyError
        for i in range(len(node.adj)):
            node.adj[i] = update[i].adj[i]
            update[i].adj[i] = node
    
    def remove(self, val):
        update = self.update(val)
        x = self.find(val, update, True)
        if not x: raise KeyError
        for i in range(len(x.adj)):
            update[i].adj[i] = x.adj[i]
    
    def iterate(self):
        # use this to debug
        x = self.head
        while x: print(x.key, [(a.key if a else None) for a in x.adj]); x = x.adj[0]

s = SkipList()
s.insert(234)
s.insert(2003)
s.insert(3)
s.insert(532)
s.iterate()