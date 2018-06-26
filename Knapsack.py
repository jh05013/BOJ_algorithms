# Knapsack problem
# L = List of items
# W = Maximum weight
# Modify at your own taste and requirement

def knapsack(L, W):
    opt = [float('inf')]*(W+1)
    opt[0] = 0
    for i in L:
        update = []
        for j in range(W+1):
            if i+j > W: break
            update.append((i+j, opt[j]+1))
        for x, c in update: opt[x] = min(opt[x], c)
    return opt
