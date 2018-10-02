# Gaussian elimination
# A = matrix
# Each row is of the form coeff0 coeff1 ... coeffn const

import decimal
decimal.getcontext().prec = 50
D = decimal.Decimal
def gauss(A):
    n = len(A)
    for i in range(n):
        maxEl = abs(A[i][i]); maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl: maxEl = abs(A[k][i]); maxRow = k
        for k in range(i, n+1): A[maxRow][k], A[i][k] = A[i][k], A[maxRow][k]
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j: A[k][j] = D(0)
                else: A[k][j]+= c * A[i][j]
    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1): A[k][n] -= A[k][i] * x[i]
    return x

# Determinant
# A = matrix

import decimal
decimal.getcontext().prec = 50
D = decimal.Decimal
def determinant(A):
    n = len(A)
    D = 1
    for i in range(n):
        maxEl = abs(A[i][i]); maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl: maxEl = abs(A[k][i]); maxRow = k
        for k in range(i, n): A[maxRow][k], A[i][k] = A[i][k], A[maxRow][k]
        if maxRow != i: D*= -1
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n):
                if i == j: A[k][j] = 0
                else: A[k][j]+= c * A[i][j]
    for i in range(n): D*= A[i][i]
    return D

# Counts the number of spanning trees
# 0-indexed

def countST(n, edges):
    Q = [[0]*n for i in range(n)]
    for u, v in edges:
        Q[u][u]+= 1; Q[v][v]+= 1
        Q[u][v]-= 1; Q[v][u]-= 1
    Q.pop(0)
    for row in Q: row.pop(0)
    return round(determinant(Q))