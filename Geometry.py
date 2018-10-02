############################################################### Line intersection

def ccw(a, b, c):
    # positive -> ccw; negative -> cw; 0 -> collinear
    res = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    return 0 if res==0 else (1 if res>0 else -1)

def intersect(a, b, c, d):
    # check if two line segments a--b and c--d intersect
    def cc(a, b, c):
        return min(a[0],b[0]) <= c[0] <= max(a[0],b[0]) and\
               min(a[1],b[1]) <= c[1] <= max(a[1],b[1]) 
    if a == b: return a in (c,d)
    if c == d: return c in (a,b)
    s1 = ccw(a,b,c); s2 = ccw(a,b,d)
    if s1==0 and s2==0:
        return any(cc(i,j,k) for i,j,k in ((a,b,c), (a,b,d), (c,d,a), (c,d,b)))
    if s1 and s1==s2: return False
    s1 = ccw(c,d,a); s2 = ccw(c,d,b)
    if s1 and s1==s2: return False
    return True

############################################################### Line strict intersection

def ccw(a, b, c):
    # positive -> ccw; negative -> cw; 0 -> collinear
    res = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    return 0 if res==0 else (1 if res>0 else -1)

def intersect_strict(a, b, c, d):
    # check if two line segments a--b and c--d intersect, but not at the endpoints
    if a == b: return False
    if c == d: return False
    s1 = ccw(a,b,c); s2 = ccw(a,b,d)
    if s1==0 or s2==0 or s1==s2: return False
    s1 = ccw(c,d,a); s2 = ccw(c,d,b)
    if s1==0 or s2==0 or s1==s2: return False
    return True

def straightint22(a, b, c, d):
    # intersection of two straight lines -a--b- and -c--d-
    x1, y1 = a; x2, y2 = b
    x3, y3 = c; x4, y4 = d
    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if den == 0: return (float('inf'),)*2
    num1 = (x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)
    num2 = (x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)
    return (num1/den, num2/den)

############################################################### Polygon area

def polyarea(p):
    p.append(p[0])
    A = sum(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1] for i in range(len(p)-1))/2
    p.pop()
    return abs(A)

############################################################### Operations with y=ax+b

def pqab(x1, y1, x2, y2):
    # given points (x1, y1) and (x2, y2), find a line y=ax+b
    a = (y2-y1)/(x2-x1)
    return a, y1-a*x1

def pointreflect(x, y, a, b):
    # reflect (x, y) over a line y=ax+b
    d = (x+(y-b)*a) / (1+a**2)
    return 2*d-x, 2*d*a-y+2*b