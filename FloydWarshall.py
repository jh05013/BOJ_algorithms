# Floyd Warshall algorithm
# n = number of vertices
# cost = 2D array of costs
# This is 0-indexed

def Floyd(n, cost):
    for i in range(n): cost[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n): cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])