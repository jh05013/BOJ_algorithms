#SIZE = 26
class Node:
    def __init__(self, size):
        self.size = size
        self.link = None
        self.adj = {}

class EertreE:
    def __init__(self, s = ''):
        self.neg = Node(-1); self.zero = Node(0)
        self.neg.link = self.zero.link = self.neg
        self.nodes = []
        self.s = ['']
        self.maxs = self.zero
        for c in s: self.add(c)
    
    def getmax(self, start, a):
        u = start; i = len(self.s)
        while u is not self.neg and self.s[i-u.size-1] != a:
            assert u is not u.link
            u = u.link
        return u
    
    def add(self, a):
        Q = self.getmax(self.maxs, a)
        created = not (a in Q.adj)
        if created:
            P = Node(Q.size+2)
            self.nodes.append(P)
            if P.size == 1: P.link = self.zero
            else: P.link = self.getmax(Q.link, a).adj[a]
            Q.adj[a] = P
        self.maxs = Q.adj[a]
        self.s.append(a)
        return created
    
    def _rdebug(self, nd, nth, cth, res):
        for name in nd.adj:
            nd2 = nd.adj[name]
            self._rdebug(nd2, nth+[nd2], cth+[name], res)
        if nd is not self.neg and nd is not self.zero:
            tmp = "".join(cth)
            if nth[0] is self.zero: asm = tmp[::-1]+tmp
            else: asm = tmp[::-1]+tmp[1:]
            res.append(asm)
    
    def debug(self):
        res = []
        self._rdebug(self.neg, [self.neg], [], res)
        self._rdebug(self.zero, [self.zero], [], res)
        return res

T = EertreE("eertree")
print(len(T.nodes))
print(T.debug())