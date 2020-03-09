'''
    Author: Dasu Srinivas
    Description: Implement a stack using double linked list
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp = self.head.value
            self.head = self.head.next
            self.head.prev = None
            print(temp)

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def getTop(self):
        return self.head.value

    def getSize(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def printstack(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next


stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.printstack()
print("\nTop element is ", stack.getTop())
print("Size of the stack is ", stack.getSize())
stack.pop()
stack.pop()
stack.printstack()

print("\nstack is empty:", stack.isEmpty())
