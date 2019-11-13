from heapq import *
class RemovableMinHeap:
    def __init__(_): _.A = []; _.B = []
    def insert(_, x): heappush(_.A, x)
    def remove(_, x): heappush(_.B, x)
    def top(_):
        while _.B and _.A[0] == _.B[0]: heappop(_.A); heappop(_.B)
        return _.A[0]
    def pop(_):
        x = _.top(); _.remove(x)
        return x

from heapq import *
class RemovableMaxHeap:
    def __init__(_): _.A = []; _.B = []
    def insert(_, x): heappush(_.A, -x)
    def remove(_, x): heappush(_.B, -x)
    def top(_):
        while _.B and _.A[0] == _.B[0]: heappop(_.A); heappop(_.B)
        return -_.A[0]
    def pop(_):
        x = _.top(); _.remove(x)
        return x