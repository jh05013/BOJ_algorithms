class SegTree:
    def __init__(self, n, width):
        size = 1
        while size < n: size<<= 1
        self.arr = [0]*(size*2); self.size = size
        self.cover = [0]*(size*2); self.width = [0]*(size*2)
        for i in range(n): self.width[size+i] = width[i]
        for i in range(size-1, 0, -1): self.width[i] = self.width[2*i] + self.width[2*i+1]
    
    def update(self, l, r, delta):
        self._internal(l, r, 1, 0, self.size-1, delta)
    
    def _internal(self, l, r, node, nl, nr, delta):
        if r < nl or l > nr: return
        if l <= nl and nr <= r: self.arr[node]+= delta
        else:
            mid = (nl+nr)//2
            self._internal(l, r, node*2, nl, mid, delta)
            self._internal(l, r, node*2+1, mid+1, nr, delta)
        if self.arr[node]: self.cover[node] = self.width[node]
        elif node >= self.size: self.cover[node] = 0
        else: self.cover[node] = self.cover[2*node] + self.cover[2*node+1]
    
from sys import stdin
input = stdin.readline
n = int(input())
event = []
xvals = set()
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    event.append((y1,x1,x2,1))
    event.append((y2,x1,x2,-1))
    xvals.add(x1)
    xvals.add(x2)
event.sort()
xvals = sorted(xvals)
xdic = dict(zip(xvals, range(len(xvals))))
width = [xvals[i]-xvals[i-1] for i in range(1, len(xvals))]

ST = SegTree(len(xvals)-1, width)
prev = 0
area = 0
for y, x1, x2, d in event:
    area+= (y-prev) * ST.cover[1]
    prev = y
    ST.update(xdic[x1], xdic[x2]-1, d)
print(area)