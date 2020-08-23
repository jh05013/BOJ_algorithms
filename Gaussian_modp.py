MOD = 10**9+7
def gauss(A):
    # MAKE SURE EVERY ELEMENT IS IN [0,MOD)
    n = len(A); m = len(A[0])
    for i in range(m-1):
        maxEl = A[i][i]; maxRow = i
        for k in range(i+1, n):
            if A[k][i] > maxEl: maxEl = A[k][i]; maxRow = k
        for k in range(i, m): A[maxRow][k], A[i][k] = A[i][k], A[maxRow][k]
        for k in range(i+1, n):
            c = (MOD-A[k][i]) * pow(A[i][i],MOD-2,MOD) % MOD
            for j in range(i, m):
                if i == j: A[k][j] = 0
                else: A[k][j] = (A[k][j] + c * A[i][j]) % MOD
    x = [0]*(m-1)
    for i in range(m-2, -1, -1):
        x[i] = A[i][-1] * pow(A[i][i],MOD-2,MOD) % MOD
        for k in range(i-1, -1, -1): A[k][-1] = (A[k][-1] - A[k][i] * x[i]) % MOD
    return x