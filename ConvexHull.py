# Monotone chain for convex hull
# If you want perimeter points to be included, use <0 and >0
# p = list of points
# from lowest, leftmost point

# Rotating calipers for farthest points
# p = list of points

def ccw(p1, p2, p3):
    # positive -> ccw; negative -> cw; 0 -> collinear
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

def ConvexHull(p):
    U = []; L = []; p.sort()
    for q in p:
        while len(U)>1 and ccw(U[-2], U[-1], q) >= 0: U.pop()
        while len(L)>1 and ccw(L[-2], L[-1], q) <= 0: L.pop()
        U.append(q); L.append(q)
    return U, L

def RotCal(p):
    U, L = ConvexHull(p)
    i = 0; j = len(L)-1
    i = 0; j = len(L)-1
    while i < len(U)-1 or j > 0:
        yield U[i],L[j]
        if i == len(U)-1: j-= 1
        elif j == 0: i+= 1
        elif (U[i+1][1]-U[i][1])*(L[j][0]-L[j-1][0]) > \
                (L[j][1]-L[j-1][1])*(U[i+1][0]-U[i][0]): i += 1
        else: j-= 1

def area(p):
    p.append(p[0])
    A = sum(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1] for i in range(len(p)-1))/2
    p.pop()
    return abs(A)
