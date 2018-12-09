__import__('sys').stdout = open('res4.txt', 'w')

class gen4:
    def __init__(_): _.s = '9099099909999099999'; _.isprime = [True for _ in range(400002)]; _.isprime[0] = _.isprime[1] = False
    def getprimes(_):
        for i in range(2, 10**8):
            if i*i >= 400002: break
            if not _.isprime[i]: continue
            for j in range(2, 10**8):
                if(i*j >= 400002): break
                _.isprime[i*j] = False
    def gen(_):
        s = ''; _.getprimes()
        for i in range(400000):
            if(266648 <= i < 266667): s+= _.s[i-266648]; continue
            s+= '0' if _.isprime[i+2] else '1'
            if(i%80 == 79): s+= '\n'
        print(s)

q = gen4()
q.gen()
#a = open('gen4.out').read().rstrip()
#b = open('res4.txt').read().rstrip()
assert open('gen4.out').read().rstrip() == open('res4.txt').read().rstrip()