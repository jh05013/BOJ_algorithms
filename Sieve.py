# Prime sieve

LIM = 100000
sieve = list(range(LIM)); sieve[1] = 0
for i in range(2, int(LIM**.5)+1):
    if not sieve[i]: continue
    for j in range(2*i, LIM, i): sieve[j] = 0
sieve = list(filter(None, sieve))
