# Nimber
# move = function that returns the set of next position
# n = number you want to see up to
# This is only for observing a pattern
# Once you figured out the pattern, make it yourself in O(1)

# Nimgame, last move wins, returns 0 or 1, which player wins
# p = list of stones
# nimber = function to compute nimber

# Misere, last move loses, returns 0 or 1, which player wins
# p = list of stones
# nimber = function to compute nimber

mex = [-1] * 10000
def calc_nim(x):
    move = set()
    for y in something:
        move.add(mex[y])
    assert -1 not in move
    for y in range(10**9):
        if y not in move: mex[x] = y; return
for i in range(10000): calc_nim(i)

def nimgame(p, nimber):
    xored = 0
    for i in p: xored^= nimber(i)
    return int(xored == 0)

def misere(p, nimber):
    xored = 0
    for i in p: xored^= nimber(i)
    if max(p) == 1: return int(xored == 1)
    return int(xored == 0)