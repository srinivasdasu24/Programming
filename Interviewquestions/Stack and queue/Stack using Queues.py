'''

    Author : Dasu Srinivas
    Description: Implement a stack and its operations using queue with enqueue and dequeue operations

'''

'''
# This solution is based on costly enqueue operation
from queue import Queue

class Stack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1
        self.q2.put(x)

        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):
        if self.q1.empty():
            return
        self.q1.get()
        self.curr_size -= 1

    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]

    def size(self):
        return self.curr_size

'''

# This solution is based on costly dequeue operation
from queue import Queue

class Stack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1
        self.q1.put(x)

    def pop(self):
        if self.q1.empty():
            return
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q1.get()
        self.curr_size -= 1
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def top(self):
        if self.q1.empty():
            return -1
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        temp = self.q1.queue[0]
        self.q1.get()
        self.q2.put(temp)
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        return temp

    def size(self):
        return self.curr_size


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("current size", s.size())
    print(s.top())
    s.pop()