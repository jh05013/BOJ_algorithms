query = [tuple(MIS()) for i in range(Q)]
qs = [0]*Q
qe = [MAXANS]*Q
qa = [None]*Q # answer
for REP in range(17): # this is for 100,000. change appropriately
    qstop = [[] for i in range(MAXANS)]
    for i in range(Q):
        if qs[i] > qe[i]: continue
        qstop[(qs[i] + qe[i])//2].append(i)
    for i in range(m):
        # do something
        for j in qstop[i]:
            if SOME_PREDICATE_IS_TRUE:
                qe[j] = i-1 # paramin
                qa0[j] = i
            else: qs[j] = i+1 # paramin
for i in range(Q):
    print(qa[i])