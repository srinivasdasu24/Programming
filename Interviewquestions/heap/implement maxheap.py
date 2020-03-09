'''

    Author: Dasu Srinivas
    Description : Implement maxheap and its operations

'''

import sys

class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [0] * (self.max_size + 1)
        self.size = 0
        self.heap[0] = sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    def Heapify(self, pos):
        if not self.isLeaf(pos):
            if self.heap[pos] < self.heap[self.rightChild(pos)] or self.heap[pos] < self.heap[self.leftChild(pos)]:
                if self.heap[self.rightChild(pos)] > self.heap[self.leftChild(pos)]:
                    self.heap[pos], self.heap[self.rightChild(pos)] = self.heap[self.rightChild(pos)], self.heap[pos]
                    self.Heapify(self.rightChild(pos))
                else:
                    self.heap[pos], self.heap[self.leftChild(pos)] = self.heap[self.leftChild(pos)], self.heap[pos]
                    self.Heapify(self.leftChild(pos))

    def insert(self, data):
        if self.size > self.max_size:
            return
        self.size += 1
        self.heap[self.size] = data
        current = self.size
        while self.heap[current] > self.heap[self.parent(current)]:
            self.heap[current], self.heap[self.parent(current)] = self.heap[self.parent(current)], self.heap[current]
            current = self.parent(current)

    def max(self):
        pop_ele = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.Heapify(self.front)
        return pop_ele

    def printHeap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) + " LEFT CHILD : " +
                  str(self.heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.heap[2 * i + 1]))


maxheap = MaxHeap(15)
maxheap.insert(5)
maxheap.insert(3)
maxheap.insert(17)
maxheap.insert(10)
maxheap.insert(84)
maxheap.insert(19)
maxheap.insert(6)
maxheap.insert(22)
maxheap.insert(9)
# maxheap.max()
maxheap.printHeap()
print("Max value is", maxheap.max())
