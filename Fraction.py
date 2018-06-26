# Fraction class
# Because built-in fraction is sometimes too heavy

from functools import total_ordering
@total_ordering
class F:
    def __init__(self, num, den): self.num = num; self.den = den
    def __eq__(self, f2): return self.num*f2.den == self.den*f2.num
    def __lt__(self, f2): return self.num*f2.den < self.den*f2.num