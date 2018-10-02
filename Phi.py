'''
Euler theorems:
  1. for coprime a and n, a^phi(n) = 1 mod n
  2. for any a and n, a^n = a^(n-phi(n)) mod n
     in particular, if m >= log2(n), then a^m = a^(m%phi(n) + phi(n)) mod n
'''

def phi(n):
    ans = n
    for p in range(2, n+1):
        if p*p > n:
            if n != 1: ans = ans*(n-1)//n
            return ans
        if n%p: continue
        ans = ans*(p-1)//p
        while n%p==0: n//= p
    return ans

