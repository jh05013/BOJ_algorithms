# Convex Hull Optimization of DP can be used if
# dp[i] = min_k(a[k]*x[i] + b[k]) + const[i] where the slopes are monotonic

# Assumption x[i] <= x[i+1], decreasing slopes
class CHT:
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

# Assumption x[i] <= x[i+1], increasing slopes
class CHT:
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

################################################################
################################################################
################################################################

1

# No assumption, increasing slopes
class CHT:
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