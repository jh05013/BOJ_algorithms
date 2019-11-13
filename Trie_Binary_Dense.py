BIT = 19
SZ = 1<<BIT
TC = [0] * (SZ<<1) # change to defaultdict(int) if BIT is 30
def trie_add(n, am=1):
    assert n < SZ
    i, mask = 0, SZ>>1
    for xi in range(BIT+1):
        TC[i]+= am
        i = i*2+2 if n&mask else i*2+1
        mask>>= 1

def trie_xormin(n):
    i, mask, ans = 0, SZ>>1, 0
    for xi in range(BIT):
        if n&mask: good = i*2+2; bad = i*2+1
        else: good = i*2+1; bad = i*2+2
        if TC[good]: i = good; ans = ans*2
        else: i = bad; ans = ans*2+1
        mask>>= 1
    return ans

def trie_xormax(n):
    i, mask, ans = 0, SZ>>1, 0
    for xi in range(BIT):
        if not x&mask: good = i*2+2; bad = i*2+1
        else: good = i*2+1; bad = i*2+2
        if TC[good]: i = good; ans = ans*2+1
        else: i = bad; ans = ans*2
        mask>>= 1
    return ans