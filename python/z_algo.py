def z_algo(s):
    n = len(s)
    z, l, r = [n]+[0]*(n-1), 0, 0
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