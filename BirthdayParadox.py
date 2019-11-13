def f(i, n):
    res = 1
    for j in range(i):
        res*= (n-2*j)*(n-2*j-1)/(j+1)/2/365
    for j in range(n-i):
        res*= (365-j)/365
    return res

def calc(n):
    res = 1
    for i in range(n//2+1):
        res-= f(i, n)
    return res

from random import choice
day = list(range(1, 366))
def simul(n, rep):
    res = 0
    for i in range(rep):
        s = [choice(day) for j in range(n)]
        res+= any(s[a]==s[b]==s[c] for a in range(n) for b in range(a+1,n) for c in range(b+1,n))
    return res/rep