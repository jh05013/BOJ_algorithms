__import__('sys').stdout = open('res3.txt', 'w')

ontak = [".####..##..##.######..##...##..##.....####...####..###..####.",
         "##..##.###.##...##...####..##.##.....##..##.##..##..##.##..##",
         "##..##.##.###...##..##..##.####.........##..##..##..##.##..##",
         "##..##.##..##...##..######.##.##......##....##..##..##.##..##",
         ".####..##..##...##..##..##.##..##....######..####...##..####."]

class gen3:
    def __init__(_): _.grid = [['']*512 for i in range(512)]
    def gen(_):
        for i in range(512):
            for j in range(i+1): _.grid[i][j] = '.'
        _.grid[0][0] = "#"; i = 1; s = ''
        while i < 512:
            for j in range(i):
                for k in range(j+1): _.grid[i+j][k] = _.grid[i+j][i+k] = _.grid[j][k]
            i*= 2
        for i in range(512):
            s+= ''.join(_.grid[511-i])
            for j in range(512-i, 512):
                if 506<=i<511 and 449<=j<510: s+= ontak[i-506][j-449]
                else: s+= '.'
            s+= ''.join(_.grid[511-i])+'\n'
        for i in range(512): s+= ''.join(_.grid[511-i])+'\n'
        print(s)

q = gen3()
q.gen()

assert open('gen3.out').read().rstrip() == open('res3.txt').read().rstrip()