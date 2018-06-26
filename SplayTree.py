# Splay tree
# This is 0-indexed

class Node:
    def __init__(self, key):
        self.key = key
        self.cnt = 1
        self.l = self.r = self.p = None
    
    def update(self):
        self.cnt = 1
        if self.l: self.cnt+= self.l.cnt
        if self.r: self.cnt+= self.r.cnt
    
    def __repr__(self):
        a = str(self.key)
        b = repr(self.l) if self.l else "."
        c = repr(self.r) if self.r else "."
        return "<"+a+" / "+b+" "+c+">"

class Splay:
    def __init__(self):
        self.root = None
    
    def __repr__(self):
        return repr(self.root)

    def rotate(self, x):
        p = x.p; b = None
        if x == p.l: p.l = b = x.r; x.r = p
        else: p.r = b = x.l; x.l = p
        x.p = p.p; p.p = x
        if b: b.p = p
        if not x.p: self.root = x
        elif p == x.p.l: x.p.l = x
        else: x.p.r = x
        p.update(); x.update()
    
    def splay(self, x):
        while x.p:
            p = x.p; g = p.p
            if g: self.rotate(p if (x==p.l) == (p==g.l) else x)
            self.rotate(x)
    
    def insert(self, key):
        p = self.root; pp = None
        if not p: self.root = Node(key); return
        while 1:
            if key == p.key: return
            if key < p.key:
                if not p.l: pp = p.l; break
                p = p.l; continue
            if not p.r: pp = p.r; break
            p = p.r
        pp = Node(key); pp.p = p
        if p.key < key: p.r = pp
        else: p.l = pp
        self.splay(pp)
    
    def delete(self, key):
        assert self.find(key)
        p = self.root
        if p.l:
            if p.r:
                self.root = x = p.l; x.p = None
                while x.r: x = x.r
                x.r = p.r; p.r.p = x; self.splay(x); return
            self.root = x = p.l; x.p = None; return
        if p.r: self.root = x = p.r; x.p = None; return
        self.root = None    
    
    def find(self, key):
        p = self.root
        if not p: return False
        while p:
            if key == p.key: break
            if key < p.key:
                if not p.l: break
                p = p.l; continue
            if not p.r: break
            p = p.r
        self.splay(p); return p.key == key
    
    def findkth(self, k):
        x = self.root
        while 1:
            while x.l and x.l.cnt > k: x = x.l
            if x.l: k-= x.l.cnt
            if not k: break
            k-= 1; x = x.r
        self.splay(x)
    
    def interval(self, l, r): # self.root.r.l becomes the interval [l,r]
        self.findkth(l-1)
        x = self.root; self.root = x.r; self.root.p = None
        self.findkth(r-l+1)
        x.r = self.root; self.root.p = x; self.root = x    

t = Splay()
from random import shuffle
L = list(range(1000))
shuffle(L)
for i in L: t.insert(i); assert t.root.key == i
shuffle(L)
for i in L: assert t.find(i); assert t.root.key == i
shuffle(L)
for i in L: t.findkth(i); assert t.root.key == i