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