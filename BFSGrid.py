from collections import deque
def bfs(i, j):
    i-=1; j-=1
    t = [[-1]*m for i in range(n)]
    Q = deque([(i,j)]); t[i][j] = 0
    while Q:
        i, j = Q.popleft()
        for ni, nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
            if not (0<=ni<n and 0<=nj<m) or grid[ni][nj] == WALL: continue
            if t[ni][nj] == -1: t[ni][nj] = t[i][j]+1; Q.append((ni,nj))
    return t