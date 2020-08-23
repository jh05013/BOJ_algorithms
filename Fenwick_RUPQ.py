# Range add, point query
class RUPQ:
    def __init__(_, size):
        _.arr = [0]*(size+1)
    
    def add(_, i, j, val):
        while i < len(_.arr): _.arr[i] += val; i |= i+1
        j+= 1
        while j < len(_.arr): _.arr[j] -= val; j |= j+1
    
    def get(_, i):
        res = 0
        while i >= 0: res+= _.arr[i]; i = (i&(i+1))-1
        return res