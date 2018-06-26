# Knuth-Morris-Pratt algorithm to search substring
# partialmatch[i] is longest pre&suffix of s[:i+1]
# s = string to search in
# w = target string
# T = partial match table if it's already computed
# also can be used in lists

def Z(s):
    z = [0]*len(s); l, r, n = 0, 0, len(s); z[0] = n
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r-l] == s[r]: r+= 1
            z[i] = r-l; r-= 1
            continue
        k = i-l
        if z[k] < r-i+1: z[i] = z[k]; continue
        l = i
        while r < n and s[r-l] == s[r]: r+= 1
        z[i] = r-l; r-= 1
    return z