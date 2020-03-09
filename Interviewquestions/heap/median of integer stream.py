'''

    Author : Dasu Srinivas
    Description: Given a continuous stream of integers, find the median of integers at given point of time

'''

from heapq import heapify, heappop, heappush


class MedianStream:
    def __init__(self):
        self.max_heap = []
        heapify(self.max_heap)
        self.min_heap = []
        heapify(self.min_heap)

    def median(self):
        if len(self.min_heap) == len(self.max_heap):
            return float(int(self.min_heap[0]) + int(-1 * self.max_heap[0]) / 2)
        elif len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        else:
            return self.min_heap[0]

    def addtoheap(self, data):
        heappush(self.max_heap, -1 * data)
        if (len(self.max_heap) - len(self.min_heap) > 1) or (
                len(self.min_heap) > 0 and (-1 * self.max_heap[0] > self.min_heap[0])):
            heappush(self.min_heap, -1 * heappop(self.max_heap))
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -1 * heappop(self.min_heap))


median = MedianStream()
median.addtoheap(12)
median.addtoheap(7)
median.addtoheap(9)
median.addtoheap(13)
median.addtoheap(15)
median.addtoheap(17)
median.addtoheap(5)
print(median.median())
