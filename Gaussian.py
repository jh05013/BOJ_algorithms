# Gaussian elimination
# A = matrix
# Each row is of the form coeff0 coeff1 ... coeffn const

import decimal
decimal.getcontext().prec = 50
D = decimal.Decimal
def gauss(A):
    n = len(A)
    for i in range(n):
        # Search for maximum in this column
        maxEl = abs(A[i][i]); maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl: maxEl = abs(A[k][i]); maxRow = k
        # Swap maximum row with current row (column by column)
        for k in range(i, n+1): A[maxRow][k], A[i][k] = A[i][k], A[maxRow][k]

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j: A[k][j] = 0
                else: A[k][j]+= c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1): A[k][n] -= A[k][i] * x[i]
    return x
