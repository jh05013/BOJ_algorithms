# Parametric search minimum/maximum
# F = monotone false -> true function / t->f
# l = lower bound
# r = upper bound

# Parametric search on real values
# precision = precision

def paramin(F, l, r):
    while l <= r:
        mid = (l+r)//2
        if F(mid): ans, r = mid, mid-1
        else: l = mid+1
    return ans

def paramax(F, l, r):
    while l <= r:
        mid = (l+r)//2
        if F(mid): ans, l = mid, mid+1
        else: r = mid-1
    return ans

def paraminf(F, l, r, precision):
    while abs(r-l) > precision:
        mid = (l+r)/2
        if F(mid): r = mid
        else: l = mid
    return r

def paramaxf(F, l, r, precision):
    while abs(r-l) > precision:
        mid = (l+r)/2
        if F(mid): l = mid
        else: r = mid
    return r