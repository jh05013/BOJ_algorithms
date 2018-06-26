# Karp-Miller-Rosenberg algorithm for strings
# Let k be the largest s.t 2^k <= d.
# Then the hash of the substring from i length d is the tuple:
# (hash of the first 2^k letters, hash of the last 2^k letters)

def buildKMR(s):
    h0 = [ord(c)-ord('a') for c in s] # change this to your need 
    n, hashes, dic = 1, [h0], {}
    while n*2 < len(s):
        h = []
        for i in range(len(s)-n*2+1):
            tup = (hashes[-1][i], hashes[-1][i+n])
            h.append(dic.setdefault(tup, len(dic)))
        hashes.append(h)
        n*= 2; dic.clear()
    return hashes

def blocksize(d):
    # size of the 2^k-block for substring length d
    block, bn = 1, 0
    while block*2 <= d: block*= 2; bn+= 1
    return block, bn

def getKMR(kmr, i, d, block=0, bn=0):
    # hash of substring from i length d
    if not block: block, bn = blocksize(d)
    if block == d: return kmr[bn][i]
    return (kmr[bn][i], kmr[bn][i+d-block])