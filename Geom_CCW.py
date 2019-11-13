def ccw(a, b, c):
    # positive -> ccw; negative -> cw; 0 -> collinear
    res = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    return 0 if res==0 else (1 if res>0 else -1)