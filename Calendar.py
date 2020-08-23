isleap = lambda y: (y%400==0) ^ (y%100==0) ^ (y%4==0)

def nextday(y, m, d):
    ldm = [0,31,28,31,30,31,30,31,31,30,31,30,31][m]
    if isleap(y) and m==2: ldm+= 1
    if ldm != d: return y, m, d+1
    if m != 12: return y, m+1, 1
    return y+1, 1, 1