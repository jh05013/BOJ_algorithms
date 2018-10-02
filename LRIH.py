# Largest rectangle in histogram, in O(n)
# n = width of histogram
# h = height list

# Largest 1-rectangle in matrix, in O(nm)
# M = 0-1 matrix

def LRIH(h):
    n = len(h); h.append(0)
    stack = []; ans = 0; i = 0
    while i < n+1:
        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i); i+= 1; continue
        top = stack.pop()
        left = i-stack[-1]-1 if stack else i
        ans = max(ans, h[top]*left)
    h.pop()
    return ans

def LRIM(M):
    row = M[0][:]
    ans = LRIH(row)
    for i in range(1, len(M)):
        for j in range(len(row)):
            row[j] = 0 if M[i][j] == 0 else row[j]+1
        ans = max(ans, LRIH(row))
    return ans