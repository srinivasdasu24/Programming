'''
    Author: Dasu Srinivas
    Description: Find the maximum element in a stack in O(1) time in given stack in O(1) extra space
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.maxEle = None
        self.count = 0

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            self.maxEle = data
        elif data > self.maxEle:
            temp = (2 * data) - self.maxEle
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.maxEle = data
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            remove = self.top.value
            self.top = self.top.next
            if remove > self.maxEle:
                print("node removed is", self.maxEle)
                self.maxEle = (2 * self.maxEle) - remove
            else:
                print("node removed is", remove)

    def getMax(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Maximum element is:", self.maxEle)

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def getTop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.value > self.maxEle:
                print("Top element of stack is:", self.maxEle)
            else:
                print("Top element of stack is:", self.top.value)


stack = Stack()

stack.push(3)
stack.push(5)
stack.getMax()
stack.push(7)
stack.push(19)
stack.getMax()
stack.pop()
stack.getMax()
stack.pop()
stack.getTop()
stack.getMax()
