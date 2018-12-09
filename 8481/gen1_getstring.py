s = open('gen1.out').read().rstrip()

rep = [2932]
for i in range(2118): rep.append((rep[-1] - (2*len(rep)-1) - 1) % 2932 + 1)
t = ''
x = 0
for i in range(2118):
    t+= s[x]
    x+= rep[i]

open('string1_2932.txt','w').write(t)