__import__('sys').stdout = open('res6.txt', 'w')

alph = "abcdefghijklmnopqrstuvwxyz"
from math import factorial
def kthperm(n, k):
    fbase = []
    for i in range(n): f = factorial(n-i-1); div = k//f; k-= f*div; fbase.append(div)
    number = list(alph[:n]); seq = []
    for i in fbase: seq.append(number.pop(i))
    return ''.join(seq)
def getperm(n):
    n-= 1
    for k in range(1, 27):
        f = factorial(k)
        if f <= n: n-= f
        else: break
    return kthperm(k, n)

class gen6:
    def __init__(_): _.s = []
    def gen(_):
        for i in range(1, 20001): _.s.append(f'T[{i**4}]="{getperm(i**4)}"')
        _.s[9999] = 'T[10000000000000000]="9099099909999099999"'
        print('\n'.join(_.s))

q = gen6()
q.gen()

assert open('gen6.out').read().rstrip() == open('res6.txt').read().rstrip()
