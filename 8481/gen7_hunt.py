grid = open('gen7.out').readlines()

art = {
    "0": [".####..",
          "##..##.",
          "##..##.",
          "##..##.",
          ".####.."],
    "1": ["###.",
          ".##.",
          ".##.",
          ".##.",
          ".##."],
    "2": [".####..",
          "##..##.",
          "...##..",
          ".##....",
          "######."],
    ",": ["......",
          "......",
          "......",
          "##....",
          ".#...."],
    ".": ["......",
          "......",
          "......",
          "##....",
          "##...."],
    "9": [".####..",
          "##..##.",
          ".#####.",
          "....##.",
          ".####.."]
    }

extra = ['', '', '', '']

class scan:
    def __init__(_):
        _.i = 469
        _.j = 0
        _.e = 0
    
    def compare(_, c):
        pic = art[c]
        for i in range(_.i, _.i+5):
            for j in range(_.j, _.j+len(pic[0])):
                if grid[i][j] != pic[i-_.i][j-_.j]: return False
        return True
    
    def scannext(_):
        for c in art:
            if _.compare(c): extra[_.e]+= c; break
        else: 1/0
        _.j+= len(art[c][0])
    
    def scanline(_):
        while _.j < 996: _.scannext()
        _.i+= 6; _.j = 0; _.e+= 1

q = scan()
for i in range(4): q.scanline()
for s in extra: print(s)