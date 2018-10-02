class PBS:
    def __init__(_):
        _.queries = []
    
    def query(_, *args):
        _.queries.append(args)
    
    def reset(_):
        _.stop = [[] for i in range(123456)] # change appropriately
        for i in range(len(_.s)):
            if _.s[i] <= _.e[i]: _.stop[(_.s[i] + _.e[i])//2].append(i)
        1234
    
    def advance(_):
        1234
    
    def check(_, x):
        mid = (_.s[x] + _.e[x]) // 2 ##### IMPLEMENT BELOW
        abcdef = _.queries[x]
        predicate = 123456
        # below is for minimum search. change appropriately for maxmimum search
        if predicate: _.ans[x] = mid; _.e[x] = mid-1
        else: _.s[x] = mid+1
    
    def process(_, s, e, repcount):
        _.s = [s] * len(_.queries)
        _.e = [e] * len(_.s)
        _.ans = [None] * len(_.s)
        for rep in range(repcount):
            _.reset()
            for i in range(s, e):
                _.advance()
                for x in _.stop[i]: _.check(x)