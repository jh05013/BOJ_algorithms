# Convex Hull Optimization of DP can be used if
# dp[i] = min_k(a[k]*x[i] + b[k]) + const[i] where the slopes are monotonic

# class names are CHT_XYZ where
# X = L if it finds minimum,  H if it finds maximum
# Y = I if slopes increase,   D if slopes decrease
# Z = M if x values increase, B otherwise (use binary search)

class CHT_LDM:
    def __init__(_):
        _.hull, _.p = [], 0
    def cr(_, x):
        ax, bx = _.hull[x]; ay, by = _.hull[x+1]
        return (by-bx) / (ax-ay)
    def insert(_, a, b): # Insert y = ax+b
        if _.hull and _.hull[-1][0] == a:
            if _.hull[-1][1] <= b: return
            _.hull.pop()
        _.hull.append((a,b))
        while len(_.hull) > 2 and _.cr(-3) > _.cr(-2): _.hull.pop(-2)
    def get(_, x):
        while _.p+1 < len(_.hull) and _.cr(_.p) <= x: _.p+= 1
        a, b = _.hull[_.p]
        return a*x + b

class CHT_LIM:
    def __init__(_):
        _.hull, _.p = [], 0
    def cr(_, x):
        ax, bx = _.hull[x]; ay, by = _.hull[x+1]
        return (by-bx) / (ax-ay)
    def insert(_, a, b): # Insert y = ax+b
        if _.hull and _.hull[-1][0] == a:
            if _.hull[-1][1] <= b: return
            _.hull.pop()
        _.hull.append((a,b)); _.p+= 1
        while len(_.hull) > 2 and _.cr(-3) < _.cr(-2): _.hull.pop(-2)
    def get(_, x):
        _.p = min(_.p, len(_.hull)-1)
        while _.p > 0 and _.cr(_.p-1) <= x: _.p-= 1
        a, b = _.hull[_.p]
        return a*x + b

class CHT_HIB:
    def __init__(_):
        _.hull = []
    def cr(_, x):
        ax, bx = _.hull[x]; ay, by = _.hull[x+1]
        return (by-bx) / (ax-ay)
    def insert(_, a, b): # Insert y = ax+b
        if _.hull and _.hull[-1][0] == a:
            if _.hull[-1][1] >= b: return
            _.hull.pop()
        _.hull.append((a,b))
        while len(_.hull) > 2 and _.cr(-3) > _.cr(-2): _.hull.pop(-2)
    def get(_, x):
        l = 1; r = len(_.hull)-1; p = 0
        while l <= r:
            mid = (l+r)//2
            if _.cr(mid-1) <= x: p, l = mid, mid+1
            else: r = mid-1
        a, b = _.hull[p]
        return a*x + b

class CHT_LIB:
    def __init__(_):
        _.hull = []
    def cr(_, x):
        ax, bx = _.hull[x]; ay, by = _.hull[x+1]
        return (by-bx) / (ax-ay)
    def insert(_, a, b): # Insert y = ax+b
        if _.hull and _.hull[-1][0] == a:
            if _.hull[-1][1] <= b: return
            _.hull.pop()
        _.hull.append((a,b))
        while len(_.hull) > 2 and _.cr(-3) < _.cr(-2): _.hull.pop(-2)
    def get(_, x):
        l = 0; r = len(_.hull)-2; p = -1
        while l <= r:
            mid = (l+r)//2
            if _.cr(mid) <= x: p, r = mid, mid-1
            else: l = mid+1
        a, b = _.hull[p]
        return a*x + b