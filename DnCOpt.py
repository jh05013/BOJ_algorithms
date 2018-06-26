# DnC Optimization of DP can be used if
# dp[t][i] = min(k<i) dp[t-1][k]+c[k][i] and
# best[t][i] <= best[t][i+1]
# Especially, quadrangle inequality is nice:
# c[a][c]+c[b][d] <= c[a][d]+c[b][c] for a<=b<=c<=d

from sys import setrecursionlimit as SRL
SRL(232323)
def dnc(s, e, p, q):
    if s > e: return
    m = (s+e)//2
    for i in range(p, min(q+1, m)):
        v = dp[t-1][i] + c[i][m] # Change this line!
        if dp[m] < v: dp[m] = v; best[m] = i # Change this "<" if necessary
    dnc(s, m-1, p, best[m])
    dnc(m+1, e, best[m], q)

dp = [-float('inf')]*n
best = [0]*n