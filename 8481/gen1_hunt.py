s = open('gen1.out').read().rstrip()

t = ''
rep = []

prev = 'G'
cnt = 0
for c in s:
    if prev != c:
        t+= prev
        rep.append(cnt)
        prev = c
        cnt = 1
    else: cnt+= 1
t+= prev
rep.append(cnt)

#repc = [2932]
#for i in range(2082): repc.append((repc[-1] - (2*len(repc)-1) - 1) % 2932 + 1)
#for i in range(len(rep)): print(rep[i], repc[i])
#open('string1.txt','w').write(t)