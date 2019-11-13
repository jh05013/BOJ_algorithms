S = [list(MIS())+[0] for i in range(n)] + [[0]*(m+1)]
for i in range(n):
    for j in range(m): S[i][j]+= S[i-1][j]+S[i][j-1]-S[i-1][j-1]
subsum = lambda i1,j1,i2,j2: S[i2][j2]-S[i1-1][j2]-S[i2][j1-1]+S[i1-1][j1-1]