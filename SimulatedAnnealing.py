import random
from math import exp
def anneal(energy, initial, alter, k, T, dec, limit):
    state = initial
    opt = float('inf')
    while k > limit:
        ast = alter(state)
        e2 = energy(ast)
        p = exp((opt-e2) / (k*T))
        if p > random.random(): state = ast; opt = e2
        k*= dec
    return state, opt