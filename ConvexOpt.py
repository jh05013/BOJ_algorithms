# Convex Hull Optimization of DP can be used if
# dp[i] = min(dp[j] + a[i]*b[j]) where b[j] >= b[j+1]
# if a[i] <= a[i+1], even better

def cross(x, y):
    ax, bx = hull[x]; ay, by = hull[y]
    return (by-bx) / (ax-ay)

def insert(a, b):
    hull.append((a,b))
    while len(hull) > 2 and cross(-2,-3) > cross(-1,-2): hull.pop(-2)

n = int(input())
x = list(map(int,input().split()))

def f(i): return something
def g(j): return something
def h(j): return something

dp = [0]
hull = [(0,0)]; p = 0
for i in range(n):
    fi = f(i)
    while p+1 < len(hull) and cross(p,p+1) <= fi: p+= 1
    dp.append(hull[p][0]*fi + hull[p][1] + something)
    insert(g(i), h(i))
print(dp[-1])