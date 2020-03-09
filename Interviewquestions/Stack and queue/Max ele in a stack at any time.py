'''

    Author: Dasu Srinivas
    Description: Keep track of the maximum element in a stack at any given time
    Solution: We can use an auxiliary stack to keep track of max element
'''


class MaxStack:
    def __init__(self):
        self.stack = []
        self.auxstack = []

    def push(self, data):
        self.stack.append(data)
        if len(self.stack) == 1:
            self.auxstack.append(data)
        if data > self.auxstack[-1]:
            self.auxstack.append(data)
        else:
            self.auxstack.append(self.auxstack[-1])

    def pop(self):
        if len(self.stack) != 0:
            self.auxstack.pop()
            self.stack.pop()
        else:
            print("Stack is empty")

    def getMax(self):
        return self.auxstack[-1]


s = MaxStack()
s.push(20)
print(s.getMax())
s.push(10)
print(s.getMax())
s.push(50)
print(s.getMax())
s.pop()
s.push(5)
print(s.getMax())
s.pop()
s.pop()
print(s.getMax())
s.pop()
print(s.getMax())