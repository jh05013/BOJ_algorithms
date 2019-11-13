# dp of the form dp[i] = g_i(max f(j)) s.t i-D <= j < i
# D is constant
# g_i are increasing functions
# if you want j <= i, move the Q.pop and Q.append to before the Q.popleft

from collections import deque

dp = []
Q = deque([(-1, initial_value)]) # j, f(j)
for i in range(n):
    # dp[i] = g_i(max f(j)); i-j <= D
    while Q and Q[0][0] < i-D: Q.popleft()
    dp.append(g_i(Q[0][1]))
    while Q and Q[-1][1] < f(i): Q.pop()
    Q.append((i, f(i)))      
