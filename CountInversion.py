# Counting inversions
# a = list of numbers

def inversions(a):
    return ci(a, 0, len(a)-1)

def ci(a, left, right):
    if left == right: return 0
    r = 0; middle = (left+right)//2
    r+= ci(a, left, middle); r+= ci(a, middle+1, right)
    merged = mergecount(a[left:middle+1], a[middle+1:right+1])
    a[left:right+1] = merged[0]
    return r+merged[1]

def mergecount(a, b):
    ai, bi, r, inv, out = 0, 0, 0, 0, []
    while ai<len(a) and bi<len(b):
        if a[ai] < b[bi]: out.append(a[ai]); ai+= 1; r+= inv
        else: out.append(b[bi]); bi+= 1; inv+= 1
    if ai == len(a):
        while bi<len(b): out.append(b[bi]); bi+= 1
    else:
        while ai<len(a): out.append(a[ai]); ai+= 1; r+= inv
    return out, r