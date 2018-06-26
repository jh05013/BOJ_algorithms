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

def nimbergen(move, n):
    mex = [0]*(n+1)
    for i in range(1, n+1):
        poss = {mex[p] for p in move(i)}
        for j in range(i+1):
            if j not in poss: mex[i] = j; break
    return mex

def nimgame(p, nimber):
    xored = 0
    for i in p: xored^= nimber(i)
    return int(xored == 0)

def misere(p, nimber):
    xored = 0
    for i in p: xored^= nimber(i)
    if max(p) == 1: return int(xored == 1)
    return int(xored == 0)