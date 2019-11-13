class SegTree:
    def __init__(_, n, width):
        s = 1
        while s < n: s<<= 1
        _.arr = [0]*(s*2); _.s = s
        _.cover = [0]*(s*2); _.width = [0]*(s*2)
        for i in range(n): _.width[s+i] = width[i]
        for i in range(s-1, 0, -1): _.width[i] = _.width[2*i] + _.width[2*i+1]
    
    def update(_, l, r, delta):
        _._internal(l, r, 1, 0, _.s-1, delta)
    
    def _internal(_, l, r, node, nl, nr, delta):
        if r < nl or l > nr: return
        if l <= nl and nr <= r: _.arr[node]+= delta
        else:
            mid = (nl+nr)//2
            _._internal(l, r, node*2, nl, mid, delta)
            _._internal(l, r, node*2+1, mid+1, nr, delta)
        if _.arr[node]: _.cover[node] = _.width[node]
        elif node >= _.s: _.cover[node] = 0
        else: _.cover[node] = _.cover[2*node] + _.cover[2*node+1]
    
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