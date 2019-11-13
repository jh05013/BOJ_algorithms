def polyarea(p):
    p.append(p[0])
    A = sum(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1] for i in range(len(p)-1))/2
    p.pop()
    return abs(A)