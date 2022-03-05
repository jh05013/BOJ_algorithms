from math import sin, cos, tan, pi, asin, acos, atan
from functools import cmp_to_key, total_ordering
def sgn(x): return (0<x) - (x<0)

## Point ################################################

@total_ordering
class Pnt:
    def __init__(_, x, y): _.x = x; _.y = y
    def __repr__(_): return f"({_.x}, {_.y})"
    
    # Basic ops
    def sq(_): return _.x**2 + _.y**2
    def __abs__(_): return (_.x**2 + _.y**2)**.5
    def __le__(_, o): return (_.x, _.y) <= (o.x, o.y)
    
    # Scalar ops
    def __mul__(_, d): return Pnt(d*_.x, d*_.y)
    def __rmul__(_, d): return Pnt(_.x*d, _.y*d)
    def __truediv__(_, d): return Pnt(_.x/d, _.y/d)
    def __floordiv__(_, d): return Pnt(_.x//d, _.y//d)
    
    # Vector ops
    def __eq__(_, q): return _.x==q.x and _.y==q.y
    def __add__(_, q): return Pnt(_.x+q.x, _.y+q.y)
    def __sub__(_, q): return Pnt(_.x-q.x, _.y-q.y)

def distsq(p, q): return (p-q).sq()

# Vector functions
def dot(p, q): return p.x*q.x + p.y*q.y
def cross(p, q): return p.x*q.y - p.y*q.x
def angle(p, q): return acos(max(-1, min(1, dot(p,q)/abs(p)/abs(q))))

# Transformations
def scale(c, p, factor): return c + (p-c)*factor
def rot(p, t): # theta
    return Pnt(p.x*cos(t)-p.y*sin(t), p.x*sin(t)+p.y*cos(t))
def rot_c(c, p, theta):
    return c + rot(p-c, theta)
def rot90(p): return Pnt(-p.y, p.x)
def linear_trans(p, q, r, np, nq):
    pq = q-p; N = Pnt(cross(pq, nq-np), dot(pq, nq-np))
    return np + Pnt(cross(r-p, N), dot(r-p, N)) / pq.sq()

# CCW
def orient(a, b, c): return cross(b-a, c-a) # >0 ccw
def ccw(a, b, c): return sgn(cross(b-a, c-a)) # 1 ccw
def angle_change(p, q):
    theta = angle(p, q)
    return theta if orient(p,Pnt(0,0),q)<=0 else 2*pi-theta
def angle_diff(p, q):
    theta = angle(p, q)
    return min(theta, 2*pi-theta)
def angle_change_c(c, p, q):
    return angle_change(p-c, q-c)
def angle_diff_c(c, p, q):
    return angle_diff(p-c, q-c)

# Sort by angle
def half_p(p): return p.y>0 or (p.y==0 and p.x<0)
@cmp_to_key
def half_cmp(p, q):
    A = (half_p(p), 0, p.sq())
    B = (half_p(q), cross(p,q), q.sq())
    return 0 if A==B else (-1 if A<B else 1)
def polarsort(O, pnts):
    return [x+O for x in sorted([x-O for x in pnts], key=half_cmp)]

## Straight lines #######################################

class Line:
    # v[0]y = v[1]x+c
    def __init__(_, v, c):
        if type(c) == Pnt: _.v = c-v; _.c = cross(_.v,v)
        else: _.v = v; _.c = c
    def __repr__(_): return f"{_.v}+{_.c}"
    
    # Point ops
    def side(_, p): return cross(_.v,p) - _.c # >0 ccw
    def dist(_, p): return abs(_.side(p)) / abs(_.v)
    def sqdist(_, p): return abs(_.side(p))**2 // _.v.sq()
    def perpline(_, p): return Line(p, p+rot90(_.v))
    def proj(_, p): return p - rot90(_.v)*_.side(p)/_.v.sq()
    def refl(_, p): return p - 2*rot90(_.v)*_.side(p)/_.v.sq()
    
    # Vector ops
    def translate(_, v): return Line(_.v, _.c+cross(_.v,v))
    def shiftleft(_, d): return Line(_.v, _.c+dist*abs(_.v))

def Line_abc(a, b, c): return Line(Pnt(b,-a), c)

# Intersection
def line_line_inter(L1, L2):
    d = cross(L1.v, L2.v)
    if d == 0: return False
    return (L2.v*L1.c - L1.v*L2.c) / d

# Sort by projection
def projsort(L, pnts):
    return sorted(pnts, key = lambda p: dot(L.v, p))

## Line segments ########################################

def point_on_seg(p, a, b):
    return orient(a,b,p) == 0 and dot(a-p, b-p) <= 0

# segment intersections
def seg_seg_inter_proper(a, b, c, d):
    oa, ob = orient(c,d,a), orient(c,d,b)
    oc, od = orient(a,b,c), orient(a,b,d)
    if oa*ob >= 0 or oc*od >= 0: return False
    return (a*ob - b*oa) / (ob-oa)

def seg_seg_inter(a, b, c, d):
    res = []
    P = seg_seg_inter_proper(a, b, c, d)
    if P: res.append(P)
    if point_on_seg(a,c,d): res.append(a)
    if point_on_seg(b,c,d): res.append(b)
    if c!=a and c!=b and point_on_seg(c,a,b): res.append(c)
    if d!=a and d!=b and point_on_seg(d,a,b): res.append(d)
    return res

# distances
def seg_pnt_dist(a, b, p):
    if a == b: return abs(p-a)
    q = Line(a,b).proj(p)
    if dot(q-a, q-b) <= 0: return Line(a,b).dist(p)
    return min(abs(p-a), abs(p-b))

def seg_seg_dist(a, b, c, d):
    if seg_seg_inter_proper(a, b, c, d): return 0
    return min(seg_pnt_dist(a,b,c), seg_pnt_dist(a,b,d),
               seg_pnt_dist(c,d,a), seg_pnt_dist(c,d,b))

## Polygon ##############################################

def polygon_is_convex(P):
    v = [ccw(P[i-2], P[i-1], P[i]) for i in range(len(P))]
    return not (1 in v and -1 in v)

def polygon_area2(P):
    # twice the area
    A = 0
    for i in range(len(P)): A+= cross(P[i-1], P[i])
    return abs(A)

def point_in_polygon(p, P, strict):
    raise NotImplementedError

## Convex Polygon #######################################

class ConvexPolygon:
    def __init__(_, pnts):
        offset = pnts.index(min(pnts))
        _.pnts = pnts = pnts[offset:] + pnts[:offset]
        uppercut = _.pnts.index(max(pnts))
        _.lower = pnts[:uppercut+1]
        _.upper = [pnts[0]] + pnts[uppercut:][::-1]
    
    def __repr__(_):
        return repr(_.pnts)
    
    ''' UNTESTED
    def inpoly(_, p):
        if p < _.lower[0] or p > _.lower[-1]: return False
        if p == _.lower[0]: return True
        i = bisect_left(_.lower, p)
        if orient(_.lower[i-1], p, _.lower[i]) > 0: return False
        i = bisect_left(_.upper, p)
        if orient(_.upper[i-1], p, _.upper[i]) < 0: return False
        return True
    '''
    
    # ASSUME PS IS SORTED
    # TODO separate out of class
    def bulk_inpoly(_, ps):
        il = iu = 1
        res = []
        for p in ps:
            if p < _.lower[0] or p > _.lower[-1]: res.append(False); continue
            if p == _.lower[0]: res.append(True); continue
            while il < len(_.lower)-1 and _.lower[il] <= p: il+= 1
            while iu < len(_.upper)-1 and _.upper[iu] <= p: iu+= 1
            ansl = orient(_.lower[il-1], p, _.lower[il]) <= 0
            ansu = orient(_.upper[iu-1], p, _.upper[iu]) >= 0
            res.append(ansl and ansu)
        return res

## Circle ###############################################

class Circle:
    def __init__(_, p, r): _.p=p; _.r=r
    def __repr__(_): return f"{_.p}O<{_.r}>"
    def angle(_, q): return angle(Pnt(1,0), q-_.p)
    def circumference(_): return 2*pi*_.r
    def area(_): return pi*_.r**2

def circumcircle(a, b, c):
    b = b-a; c = c-a
    assert cross(b, c) != 0
    p = a + rot90(b*c.sq() - c*b.sq())/cross(b,c)/2
    return Circle(p, abs(a-p))

# tangent
def point_circle_tangent(p, C):
    d = abs(C.p-p)
    theta = asin(C.r / d)
    ans = []
    for u in [-theta, theta]:
        V = rotc(p, O, u)
        ans.append(scale(p, V, (d**2-C.r**2)**.5 / d))
    return ans

def point_in_circle(p, C, strict):
    if strict: return (p-C.p).sq() < C.r**2
    return (p-C.p).sq() <= C.r**2

## Convex hull ##########################################

def convex_hull(P, split=False):
    U = []; L = []; P.sort()
    for q in P:
        while len(U)>1 and ccw(U[-2], U[-1], q) >= 0: U.pop()
        while len(L)>1 and ccw(L[-2], L[-1], q) <= 0: L.pop()
        U.append(q); L.append(q)
    if split: return U, L
    return ConvexPolygon(U+L[-2:0:-1])

######## MAIN CODE BELOW ################
