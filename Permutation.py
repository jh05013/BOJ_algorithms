from math import factorial
def kthperm(n, k):
    fbase = []
    for i in range(n):
        f = factorial(n-i-1)
        div = k//f; k-= f*div
        fbase.append(div)
    number = list(range(1, n+1)); seq = []
    for i in fbase: seq.append(number.pop(i))
    return seq

def permindex(n, seq):
    k = 0; number = list(range(1, n+1))
    for i in range(n):
        f = factorial(n-i-1)
        k+= f*number.index(seq[i])
        number.remove(seq[i])
    return k

def nextperm(a):
    ln = len(a); k = ln - 1
    while a[k] < a[k-1]: k-= 1
    if not k: return [-1]
    unused = a[k:]; del a[k:]
    mx = min(x for x in unused if x > a[k-1])
    unused.append(a[k-1]); a[k-1] = mx
    unused.remove(mx); a+= sorted(unused)
    return a