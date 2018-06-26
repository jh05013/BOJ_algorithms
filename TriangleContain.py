# Area of triangle (negative if clockwise)
# x1, y1, x2, y2, x3, y3 = points

# Point in triangle test
# px, py = point to be tested
# p0x .. p2y = points of triangle
# A = precomputed area (negative if clockwise)

def area(x1, y1, x2, y2, x3, y3):
    return (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

def contain(px, py, p0x, p0y, p1x, p1y, p2x, p2y, A):
    s = p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py
    t = p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py
    if A<0: s*=-1; t*=-1
    return s>=0 and t>=0 and s+t<=2*abs(A)