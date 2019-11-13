fh = [[1]]
for i in range(50):
    row = [0] + [fh[-1][j] * F(i+1, j+2) for j in range(i+1)]
    row[0] = 1 - sum(row)
    fh.append(row)

# if fh[i] is [a, b, c, d]
# then 1^i + ... + n^i = an + bn^2 + cn^3 + dn^4