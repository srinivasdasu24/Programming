'''

    Author : Dasu Srinivas
    Description : Implement queue and its operations using instances of stack with push and pop operations

    Solution:  Queue can be implemented usnig 2 stacks, using costly enqueue or costly dequeue  operations

'''

'''
# This solution is based on costly enqueue operation
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        if len(self.s1) == 0: 
            print("Q is empty")

        x = self.s1[-1]
        self.s1.pop()
        return x


'''

# This solution is based on costly dequeue operation
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,x):
        self.s1.append(x)

    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is empty")
            return
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1[-1])
                self.s1.pop()
        x = self.s2[-1]
        self.s2.pop()
        return x


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    print(q.deQueue())
    print(q.deQueue())