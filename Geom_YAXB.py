def pqab(x1, y1, x2, y2):
    # given points (x1, y1) and (x2, y2), find a line y=ax+b
    a = (y2-y1)/(x2-x1)
    return a, y1-a*x1

def pointreflect(x, y, a, b):
    # reflect (x, y) over a line y=ax+b
    d = (x+(y-b)*a) / (1+a**2)
    return 2*d-x, 2*d*a-y+2*b