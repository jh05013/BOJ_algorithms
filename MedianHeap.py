# Median heap

import heapq
class MedianHeap:
    def __init__(self):
        self.minh = []
        self.maxh = []
    
    def median(self):
        if not self.minh and not self.maxh: return -float('inf')
        if len(self.minh) >= len(self.maxh): return self.minh[0]
        return -self.maxh[0]
    
    def rebalance(self):
        while len(self.minh)+1 > len(self.maxh):
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))
        while len(self.maxh)+1 > len(self.minh):
            heapq.heappush(self.minh, -heapq.heappop(self.maxh))
    
    def insert(self, v):
        if v > self.median(): heapq.heappush(self.maxh, -v)
        else: heapq.heappush(self.minh, v)
        self.rebalance()
    
    def pop(self):
        m = self.median()
        if self.minh[0] == m: heapq.heappop(self.minh)
        else: heapq.heappop(self.maxh)
        self.rebalance()
        return m
