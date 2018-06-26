# Count all digits in [a,b]
# a = start, positive integer
# b = end

# Count all digits in [a,b], in given base

def drange(a, b):
    def dsingle(n, mul):
        while n: occur[n%10]+= mul; n//= 10
        
    def diter(a, b, mul):
        while a%10 != 0 and a<=b: dsingle(a, mul); a+= 1
        while b%10 != 9 and a<=b: dsingle(b, mul); b-= 1
        if a > b: return
        for i in range(10): occur[i]+= (b//10-a//10+1) * mul
        diter(a//10, b//10, mul*10)
    
    occur = [0]*10; diter(a, b, 1)
    return occur

def drangebase(a, b, base):
    def dsingle(n, mul):
        while n: occur[n%base]+= mul; n//= base
        
    def diter(a, b, mul):
        while a%base != 0 and a<=b: dsingle(a, mul); a+= 1
        while b%base != base-1 and a<=b: dsingle(b, mul); b-= 1
        if a > b: return
        for i in range(base): occur[i]+= (b//base-a//base+1) * mul
        diter(a//base, b//base, mul*base)
    
    occur = [0]*base; diter(a, b, 1)
    return occur