from heapq import *
class Maxheap:
    def __init__(_): _.h = []
    def add(_, v): heappush(_.h, -v)
    def top(_): return -_.h[0] if _.h else -10**18
    def pop(_): return -heappop(_.h)

class Graph:
    def __init__(_):
        _.change = Maxheap() # increment slope at ...
        _.a = _.y = 0 # last line has slope a, starts from y
        _.dx = 0      # the whole graph is shifted right by ...
    def __repr__(_): return f"<{sorted(-x+_.dx for x in _.change.h)}; {_.a} {_.y}>"
    def __iadd__(s, o):
        if len(s.change.h) < len(o.change.h): s,o = o,s
        dx = s.change.top() - o.change.top()
        s.a, s.y = s.a+o.a, s.y+o.y+(o.a*dx if dx>=0 else -s.a*dx)
        for v in o.change.h: s.change.add(-v + o.dx-s.dx)
        return s
    
    def shiftx(_, v): _.dx+= v
    def shifty(_, v): _.y+= v
    def addleft(_, v):
        if _.change.top() < v-_.dx:
            dx = v-_.dx - _.change.top()
            _.y+= _.a*dx
        _.change.add(v-_.dx)
    def addright(_, v):
        if _.change.top() < v-_.dx:
            dx = v-_.dx - _.change.top()
            _.y+= _.a*dx; _.a+= 1
            _.change.add(v-_.dx)
            return
        _.change.add(v-_.dx)
        _.a+= 1; _.y+= _.change.top()-(v-_.dx)
    def cutright(_):
        v = _.change.pop(); rval = v+_.dx
        dx = v-_.change.top()
        _.a-= 1; _.y-= _.a*dx
        return rval