# Make sure to include sentinel nodes!
# As such, this is 1-indexed.

class Node:
    def __init__(_, cnt):
        _.l = _.r = _.p = None
        _.cnt = cnt
        _.lazy = False
        # include additional properties if you need

class Splaytree:
    def __init__(_, n):
        x = _.root = Node(n)
        for i in range(1, n):
            x.r = Node(n-1)
            x.r.p = x; x = x.r
    
    def update(_, x):
        x.cnt = 1
        # initialize additional features here
        if x.l:
            x.cnt+= x.l.cnt
            # update additional features here
        if x.r:
            x.cnt+= x.r.cnt
            # update additional features here
    
    def rotate(_, x):
        p = x.p
        if x == p.l: p.l = b = x.r; x.r = p
        else: p.r = b = x.l; x.l = p
        x.p = p.p; p.p = x
        if b: b.p = p
        if x.p:
            if x.p.l == p: x.p.l = x
            else: x.p.r = x
        else: _.root = x
        _.update(p); _.update(x)
    
    def splay(_, x): # x becomes the root
        while x.p:
            p = x.p; g = p.p
            if g:
                if (x == p.l) == (p == g.l): _.rotate(p)
                else: _.rotate(x)
            _.rotate(x)
    
    def kth(_, k): # kth node becomes the root
        x = _.root
        while 1:
            while x.l and x.l.cnt > k: x = x.l
            if x.l: k-= x.l.cnt
            if not k: break
            k-= 1; x = x.r
        _.splay(x)
    
    def interval(_, l, r): # root.r.l becomes [l, r]
        _.kth(l-1)
        x = _.root
        _.root = x.r; _.root.p = None
        _.kth(r-l+1)
        x.r= _.root; _.root.p = x; _.root = x