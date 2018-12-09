__import__('sys').stdout = open('res2.txt', 'w')

class gen2:
    def gen(_):
        arr = [1, 1]
        for i in range(9998): arr.append((arr[-1] + arr[-2]) % 9099099909999099999)
        arr.append(0)
        print(', '.join(map(str,arr))+'.')

q = gen2()
q.gen()

assert open('gen2.out').read().rstrip() == open('res2.txt').read().rstrip()