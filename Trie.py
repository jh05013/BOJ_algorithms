class Node:
    def __init__(self, size):
        self.end = False
        self.nxt = [None] * size
    def __setitem__(self, i, x): self.nxt[i] = x
    def __getitem__(self, i): return self.nxt[i]

def makeTrie(strs, size):
    root = Node(size)
    for s in strs:
        n = root
        for c in s:
            i = int(c) # Change this to adapt. ex: ord(c)-ord("A")
            if not n[i]: n[i] = Node(size)
            n = n[i]
        n.end = True
    return root


#### Contracted trie
class Node:
    def __init__(self, size):
        self.end = False
        self.singular = -1
        self.nxt = [None] * size
    def __setitem__(self, i, x): self.nxt[i] = x
    def __getitem__(self, i): return self.nxt[i]

def makeTrie(strs, size):
    root = Node(size)
    for s in strs:
        n = root
        for c in s:
            i = ord(c)-ord('a')
            if n[i]: n = n[i]; continue
            n[i] = Node(size)
            n.singular = i if n.singular == -1 else -2
            n = n[i]
        n.end = True
    return root

from sys import setrecursionlimit as SRL
SRL(23423)
def contract(trie):
    for i in range(len(trie.nxt)):
        if not trie[i]: continue
        while 1:
            if trie[i].singular < 0 or trie[i].end: break
            grandson = trie[i][trie[i].singular]
            trie[i].end|= grandson.end
            trie[i] = grandson
        contract(trie[i])



#### Dict trie
def makeTrie(words):
    root = {}
    for w in words:
        cd = root
        for l in w: cd = cd.setdefault(l, {})
        cd[''] = ''
    return root        