def compress(L):
    d = {}
    for i, x in enumerate(sorted(L)): d[x] = i
    return list(map(d.__getitem__, L))