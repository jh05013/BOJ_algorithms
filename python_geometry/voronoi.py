### TODO:
# add DECL
# improve float accuracy? idk
# determine semi-infinite rays without convex hulls

from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y, index=None):
        self.x = x
        self.y = y
        self.i = index
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __le__(self, other):
        return (self.y, self.x) <= (other.y, other.x)
    
    # Scalar ops
    def __mul__(_, d): return Point(d*_.x, d*_.y)
    def __rmul__(_, d): return Point(_.x*d, _.y*d)
    def __truediv__(_, d): return Point(_.x/d, _.y/d)
    def __floordiv__(_, d): return Point(_.x//d, _.y//d)
    
    # Vector ops
    def __add__(_, q): return Point(_.x+q.x, _.y+q.y)
    def __sub__(_, q): return Point(_.x-q.x, _.y-q.y)
    
def ccw(a, b, c):
    # positive -> ccw; negative -> cw; 0 -> collinear
    return (b.x-a.x) * (c.y-a.y) - (b.y-a.y)*(c.x-a.x)

def dist(p, q):
    return ((p.x-q.x)**2 + (p.y-q.y)**2)**.5

def circumcenter(a, b, c):
    numerx = (a.x**2+a.y**2)*(b.y-c.y) + (b.x**2+b.y**2)*(c.y-a.y) + (c.x**2+c.y**2)*(a.y-b.y)
    numery = (a.x**2+a.y**2)*(c.x-b.x) + (b.x**2+b.y**2)*(a.x-c.x) + (c.x**2+c.y**2)*(b.x-a.x)
    denom = 2 * (a.x*(b.y-c.y) + b.x*(c.y-a.y) + c.x*(a.y-b.y))
    # TODO: avoid float error
    if denom == 0:
        return None
    return Point(numerx / denom, numery / denom)

def eval_parabola(focus, y, x):
    # evaluate y-coordinate for a parabola with given focus
    # at given sweepline's y and site's x
    fx, fy = focus.x, focus.y
    numer = (x - fx)**2 + fy**2 - y**2
    denom = 2 * (fy - y)
    if denom == 0:
        return float("INF")
    return numer / denom    

def arc_breakpoint(y, L, R):
    # breakpoint of left arc L and right arc R at sweepline y
    x1, y1 = L.x, L.y
    x2, y2 = R.x, R.y
    if y == y1:
        return Point(x1, eval_parabola(R, y, x1))
    if y == y2:
        return Point(x2, eval_parabola(L, y, x2))
    denom = 2 * (y1-y) * (y2-y)
    A = (y2-y1) / denom
    B = 2*((y-y2)*x1 - (y-y1)*x2) / denom
    C1 = (y2-y) * (x1**2+y1**2-y**2)
    C2 = (y1-y) * (x2**2+y2**2-y**2)
    C = (C1 - C2) / denom
    if A == 0:
        assert B > 0
        x = -C / B
    else:
        D = B**2 - 4*A*C
        assert D >= 0
        x = (-B + D**.5) / (2*A)
    return Point(x, eval_parabola(L, y, x))

###############################################

# bisector of points a and b
# p = midpoint, v = direction vector
class Bisector:
    def __init__(self, a, b):
        if a.y < b.y:
            return self.__init__(b, a)
        self.v = Point(b.y-a.y, a.x-b.x)
        if a.x < b.x:
            self.v.x *= -1
            self.v.y *= -1        
        self.cuts = []

###############################################

class Sweepline:
    def __init__(self, sites):
        self.sites = sites
        # pop maximum y
        # in case of tie, prefer vertex events
        self.event_queue = [(p, "SITE") for p in sites]
        self.beachline = []
        self.edges = {}
        self.max_y = max(self.sites).y
    
    def add_edge(self, a, b):
        # bisector between a and b
        self.edges[a,b] = self.edges[b,a] = Bisector(a, b)
    
    def add_vertex_event(self, l, m, r):
        if l == r or ccw(l, m, r) >= 0:
            return
        center = circumcenter(l, m, r)
        if center == None:
            return
        rad = dist(center, l)
        p = Point(center.x, center.y - rad)
        self.event_queue.append((p, "VERTEX", l, m, r))
        #print("vertex event at", p.y, ":", l, m, r)
    
    def pop(self):
        mx = max(self.event_queue)
        self.event_queue.remove(mx)
        return mx
    
    def get_breakpoints(self, y):
        b = self.beachline
        if not b:
            return []
        return [arc_breakpoint(y, b[i], b[i+1])\
                for i in range(len(b)-1)]
    
    def add_arc(self, p):
        if not self.beachline:
            self.beachline.append(p)
            return
        #print("at", p.y, "trying to insert", p, "into", [p.i for p in self.beachline])
        if p.y == self.max_y:
            self.add_arc_degenerate(p)
            return
        #print(self.get_breakpoints(p.y))
        breaks = self.get_breakpoints(p.y)
        for i in range(len(breaks)):
            if breaks[i].x > p.x:
                self.split_arc(i, p)
                return
        self.split_arc(len(breaks), p)
    
    def add_arc_degenerate(self, p):
        # all sites processed so far has the same y coordinates
        if self.beachline:
            self.add_edge(self.beachline[0], p)
        self.beachline.insert(0, p)
    
    def split_arc(self, idx, p):
        # split the arc at given index, adding a new arc p
        #print("split at", idx, "inserting", p)
        b = self.beachline
        x = b[idx]
        self.add_edge(x, p)
        if idx:
            self.add_vertex_event(b[idx-1], x, p)
        if idx < len(b)-1:
            self.add_vertex_event(p, x, b[idx+1])
        b.insert(idx, p)
        b.insert(idx, x)
    
    def remove_arc(self, l, m, r):
        # remove the arc m between l and r (because it converged to 0)
        b = self.beachline
        center = circumcenter(l, m, r)
        for idx in range(1, len(b)-1):
            if not (b[idx-1] == l and b[idx] == m and b[idx+1] == r):
                continue
            #print("Removing arc", l, m, r)
            self.add_edge(l, r)
            self.edges[l,r].cuts.append(center)
            self.edges[l,m].cuts.append(center)
            self.edges[m,r].cuts.append(center)
            b.pop(idx)
            if idx >= 2:
                self.add_vertex_event(b[idx-2], l, r)
            if idx < len(b)-1:
                self.add_vertex_event(l, r, b[idx+1])
            return circumcenter(l, m, r)

def voronoi(sites):
    for i in range(len(sites)):
        sites[i].i = i
    sweepline = Sweepline(sites)
    vertices = []
    while sweepline.event_queue:
        p, etype, *param = sweepline.pop()
        if etype == "SITE":
            sweepline.add_arc(p)
        else:
            v = sweepline.remove_arc(*param)
            if v != None:
                vertices.append(v)
    right_hull = []
    left_hull = []
    for p in sorted(sites):
        while len(right_hull) > 1 and ccw(right_hull[-2], right_hull[-1], p) > 0:
            right_hull.pop()
        while len(left_hull) > 1 and ccw(left_hull[-2], left_hull[-1], p) < 0:
            left_hull.pop()
        right_hull.append(p)
        left_hull.append(p)
    for i in range(len(right_hull)-1):
        a = right_hull[i]
        b = right_hull[i+1]
        sweepline.edges[a,b].v = Point(a.y-b.y, b.x-a.x)
    for i in range(len(left_hull)-1):
        a = left_hull[i]
        b = left_hull[i+1]
        sweepline.edges[a,b].v = Point(b.y-a.y, a.x-b.x)
    for ((va, vb), line) in sweepline.edges.items():
        if len(line.cuts) == 0:
            p = (va + vb)/2
            sweepline.edges[va,vb] = (p + line.v*1e5, p - line.v*1e5)
        elif len(line.cuts) == 1:
            sweepline.edges[va,vb] = (line.cuts[0], line.cuts[0] + line.v*1e5)
        else:
            sweepline.edges[va,vb] = line.cuts
    return vertices, sweepline.edges

###############################################
