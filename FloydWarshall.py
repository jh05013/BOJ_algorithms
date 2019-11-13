# Floyd Warshall algorithm
# n = number of vertices
# C = 2D array of costs
# This is 0-indexed

from itertools import product
def floyd(C):
    n = len(C)
    for i in range(n): C[i][i] = 0
    for k,i,j in product(range(n), range(n), range(n)):
        C[i][j] = min(C[i][j], C[i][k]+C[k][j])

# path reconstruction: X = next vertex for i->j
from itertools import product
def floyd(C):
    n = len(C)
    X = [[0]*n for i in range(n)]
    for i in range(n):
        C[i][i] = 0; X[i][i] = i
        for j in range(n):
            if C[i][j]: X[i][j] = j
    for k,i,j in product(range(n), range(n), range(n)):
        d = C[i][k]+C[k][j]
        if C[i][j] > d: C[i][j] = d; X[i][j] = X[i][k]
    return X

################################################################

# no-function version

from itertools import product
for i in range(n): C[i][i] = 0
for k,i,j in product(range(n), range(n), range(n)):
    C[i][j] = min(C[i][j], C[i][k]+C[k][j])

# path reconstruction: no-function version

from itertools import product
X = [[0]*n for i in range(n)]
for i in range(n):
    C[i][i] = 0; X[i][i] = i
    for j in range(n):
        if C[i][j]: X[i][j] = j
for k,i,j in product(range(n), range(n), range(n)):
    d = C[i][k]+C[k][j]
    if C[i][j] > d: C[i][j] = d; X[i][j] = X[i][k]
