# cc: Point on segment, given collinear points
# a, b = two endpoints
# c = point

# intersect: Line segment intersection
# a, b = two endpoints of one line segment
# c, d = two endpoints of another

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def ccw(a, b, c):
    # positive -> ccw; negative -> cw; 0 -> collinear
    res = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    return 0 if res==0 else (1 if res>0 else -1)

def cc(a, b, c):
    return min(a[0],b[0]) <= c[0] <= max(a[0],b[0]) and\
           min(a[1],b[1]) <= c[1] <= max(a[1],b[1])    

def intersect(a, b, c, d):
    # TODO if a==b or c==d
    s1 = ccw(a,b,c); s2 = ccw(a,b,d)
    if s1==0 and s2==0:
        return any(cc(i,j,k) for i,j,k in ((a,b,c), (a,b,d), (c,d,a), (c,d,b)))
    if s1 and s1==s2: return False
    s1 = ccw(c,d,a); s2 = ccw(c,d,b)
    if s1 and s1==s2: return False
    return True

# point in concave polygon checking (true if on the perimeter)
COORD_MX = 10**9
def inpoly(p, poly):
    n = len(poly); Q = COORD_MX+1
    if(any(ccw(poly[i-1], poly[i], p) == 0 for i in range(n))): return True
    nx, ny = p[0]+Q, p[1]+(Q+1)*Q
    cnt = sum(intersect(poly[i-1], poly[i], p, (nx,ny)) for i in range(n))
    return cnt%2 == 1