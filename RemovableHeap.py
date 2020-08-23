from heapq import *
class ReminHeap:
    def __init__(_): _.A = []; _.B = []
    def insert(_, x): heappush(_.A, x)
    def remove(_, x): heappush(_.B, x)
    def top(_):
        while _.B and _.A[0] == _.B[0]: heappop(_.A); heappop(_.B)
        return _.A[0]

from heapq import *
class RemaxHeap:
    def __init__(_): _.A = []; _.B = []
    def insert(_, x): heappush(_.A, -x)
    def remove(_, x): heappush(_.B, -x)
    def top(_):
        while _.B and _.A[0] == _.B[0]: heappop(_.A); heappop(_.B)
        return -_.A[0]

class RemHeap:
    def __init__(_): _.m = ReminHeap(); _.M = RemaxHeap()
    def insert(_, x): _.m.insert(x); _.M.insert(x)
    def remove(_, x): _.m.remove(x); _.M.remove(x)
    def min(_): return _.m.top()
    def max(_): return _.M.top()