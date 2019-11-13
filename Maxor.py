# Maximum subset XOR

def maxor(L):
    idx = 0
    for b in range(max(L).bit_length()-1, -1, -1):
        mask = 1<<b
        mx = xi = 0
        for i in range(idx, len(L)):
            if L[i]&mask and L[i] > mx: mx = L[i]; xi = i
        if not mx: continue
        L[idx], L[xi] = L[xi], L[idx]
        for i in range(len(L)):
            if i != idx and L[i]&mask: L[i]^= L[idx]
        idx+= 1
    ans = 0
    for x in L: ans^= x
    return ans