# Manacher's algorithm for longest palindromic substring
# A[i] is the max radius of palindromic substring centered at i

# Use maxpalin if you used ' '.join(input()) to cover even length strings
# give M and index and get the max length of palindromic substring

def manacher(s):
    A = []
    R = -1; p = -1
    for i in range(len(s)):
        if i <= R: A.append(min(A[2*p-i], R-i))
        else: A.append(0)
        while i-A[i]-1 >= 0 and i+A[i]+1 < len(s) and s[i-A[i]-1] == s[i+A[i]+1]: A[i]+= 1
        if i+A[i] > R: R = i+A[i]; p = i
    return A

def realmax(s):
    M = manacher(' '.join(s))
    for i in range(len(M)):
        if i%2 == 0: M[i] = M[i]//2*2+1
        else: M[i] = (M[i]+1)//2*2  
    return M

def maxpalin(M, i):
    if i%2 == 0: return M[i]//2*2+1
    return (M[i]+1)//2*2