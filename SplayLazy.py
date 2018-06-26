# The following is an example code for range update/sum query
# Needs sentinel nodes, so this is 1-indexed

class Node:
    def __init__(self, key):
        self.key = key
        self.lazy = 0
        self.cnt = 1
        self.s = key
        self.l = self.r = self.p = None
    
    def update(self):
        self.cnt = 1; self.s = self.key
        if self.l: self.cnt+= self.l.cnt; self.s+= self.l.s
        if self.r: self.cnt+= self.r.cnt; self.s+= self.r.s
    
    def propagate(self):
        self.key+= self.lazy
        for p in self.l, self.r:
            if not p: continue
            p.lazy+= self.lazy
            p.s+= p.cnt * self.lazy
        self.lazy = 0
    
    def __repr__(self):
        a = str(self.key)
        b = repr(self.l) if self.l else "."
        c = repr(self.r) if self.r else "."
        return "<"+a+" / "+b+" "+c+">"

class Splay:
    def __init__(self, L):
        self.root = None
        L.append(0)
        self.root = x = Node(0); x.cnt = len(L)
        for i in range(len(L)):
            x.r = Node(L[i]); x.r.p = x; x = x.r; x.cnt = n-i
    
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
    
    def findkth(self, k):
        x = self.root
        while 1:
            while x.l and x.l.cnt > k: x = x.l; x.propagate()
            if x.l: k-= x.l.cnt
            if not k: break
            k-= 1; x = x.r; x.propagate()
        self.splay(x)
    
    def interval(self, l, r):
        self.findkth(l-1)
        x = self.root; self.root = x.r; self.root.p = None
        self.findkth(r-l+1)
        x.r = self.root; self.root.p = x; self.root = x
        return self.root.r.l

from sys import stdin
input = stdin.readline
n, m, k = map(int,input().split())
L = [int(input()) for i in range(n)]
tree = Splay(L)
for QUERY in range(m+k):
    Q = list(map(int,input().split()))
    if Q[0] == 1:
        a, b, c = Q[1:]
        x = tree.interval(a, b)
        x.s+= x.cnt * c
        x.lazy+= c
    else:
        a, b = Q[1:]
        x = tree.interval(a, b)
        print(x.s)
