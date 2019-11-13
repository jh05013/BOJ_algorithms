# Knuth-Morris-Pratt algorithm to search substring
# partialmatch[i] is longest pre&suffix of s[:i+1]
# s = string to search in
# w = target string
# T = partial match table if it's already computed
# also can be used in lists

def partialmatch(w):
    T = [-1]*(len(w)+1); T[1] = 0
    if len(w) == 1: return T
    pos = 2; cnd = 0
    while pos < len(w)+1:
        if w[pos-1] == w[cnd]: T[pos]=cnd+1; cnd+= 1; pos+= 1
        elif cnd > 0: cnd = T[cnd]
        else: T[pos] = 0; pos+= 1
    return T

def KMP(s, w, T = None):
    # find w in s
    if not T: T = partialmatch(w)
    m, i = 0, 0
    while m+i < len(s):
        if w[i] == s[m+i]:
            if i == len(w) - 1: return m
            i+= 1
        elif T[i] > -1: m = m+i-T[i]; i = T[i]
        else: m+= 1; i = 0
    return -1

####################

def partialmatch(w):
    T = [-1]*(len(w)+1); T[1] = 0
    if len(w) == 1: return T
    pos = 2; cnd = 0
    while pos < len(w)+1:
        if w[pos-1] == w[cnd]: T[pos]=cnd+1; cnd+= 1; pos+= 1
        elif cnd > 0: cnd = T[cnd]
        else: T[pos] = 0; pos+= 1
    return T

def KMP(s, w, T = None):
    # find all w in s
    if not T: T = partialmatch(w)
    m, i = 0, 0
    while m+i < len(s):
        if i < len(w) and w[i] == s[m+i]:
            if i == len(w) - 1: yield m
            i+= 1
        elif T[i] > -1: m = m+i-T[i]; i = T[i]
        else: m+= 1; i = 0