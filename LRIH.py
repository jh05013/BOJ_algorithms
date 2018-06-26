# Largest rectangle in histogram, in O(n)
# n = width of histogram
# h = height list

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