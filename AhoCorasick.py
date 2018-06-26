# Aho Corasick for multiple search
# The code below counts the number of occurrences; modify at your taste
# True iff any of them exists
# s = main string
# trie = trie of words to search

class Node:
    def __init__(self, size, root=False):
        self.end = False
        self.nxt = [None] * size
        self.root = root
        self.fail = None
        self.out = None
    def __setitem__(self, i, x): self.nxt[i] = x
    def __getitem__(self, i): return self.nxt[i]

def makeTrie(strs, size):
    root = Node(size, True)
    for s in strs:
        n = root
        for c in s:
            i = ord(c)-ord('a')
            if not n[i]: n[i] = Node(size)
            n = n[i]
        n.end = True
    label(root)
    return root

from collections import deque
def label(trie):
    Q = deque(); Q.append(trie)
    while Q:
        p = Q.popleft()
        for i in range(len(p.nxt)):
            if not p[i]: continue
            pp = p; q = p[i]
            while 1:
                if pp.root: q.fail = pp; break
                if pp.fail[i]: q.fail = pp.fail[i]; break
                pp = pp.fail
            Q.append(q)
        if p.root: continue
        elif p.end: p.out = p
        elif p.fail.out: p.out = p.fail.out

def AhoCorasick(s, trie):
    p = trie; i = 0; count = 0
    while i <= len(s):
        if p.out: count+= 1
        if i == len(s): break
        c = ord(s[i])-ord('a')
        if p[c]: p = p[c]; i+= 1; continue
        if p.root: i+= 1
        else: p = p.fail
    return count