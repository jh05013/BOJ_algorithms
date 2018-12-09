grid = open('gen8.out').readlines()

i = 500
j = 500
dirs = []

pi = 500
pj = 500
while 1:
    for ni,nj,d in (i-1,j-1,0), (i-1,j,1), (i-1,j+1,2),\
        (i,j-1,3), (i,j+1,4), (i+1,j-1,5), (i+1,j,6), (i+1,j+1,7):
        if (ni,nj) != (pi,pj) and grid[ni][nj] == "#":
            dirs.append(d)
            pi, pj, i, j = i, j, ni, nj
            break
    else: break
assert len(dirs)+1 == sum(row.count("#") for row in grid)
dirs.append(6)

s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#"
new = ''
for i in range(0, len(dirs), 2): new+= s[dirs[i]*8+dirs[i+1]]

open('string8.txt','w').write(new)
