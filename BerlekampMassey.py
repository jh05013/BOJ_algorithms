# TODO

MOD = 10**9+7

def polyadd(p1, mul, m, p2):
    L1 = len(p1); L2 = len(p2)+m
    p1.extend([0] * (L2-L1))
    for i in range(m, L2): p1[i]+= mul*p2[i-m]

def berlekamp(s):
    C = [1]
    B = [1]
    L, m = 0, 1
    b = 1
    for n in range(len(s)):
        d = s[n] + sum((C[i+1]*s[n-i-1]) for i in range(L))
        print(n,'th iteration of',s,'yields',C,'discrepancy',d)
        if d == 0: m+= 1
        elif 2*L <= n:
            T = C[:]
            polyadd(C, -d/b, m, B)
            L, b, m = n+1-L, d, 1
            B = T
        else:
            polyadd(C, -d/b, m, B)
            m+= 1
    return L, C



print(berlekamp([0,0,0,0,0]))
print(berlekamp([1,1,1,1,1]))
print(berlekamp([2,2,2,2,2]))
print(berlekamp([1,1,2,3,5,8,13,21]))
print(berlekamp([1,1,1,2,2,3,4,5,7,9]))