'''

    Author: Dasu Srinivas
    Description: Given a Linked list, find whether there is a loop or not

    Solution: Using Floyd's cycle algorithm : using two pointers slow and fast

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detectLoop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # Remove loop logic
        if slow == fast:
            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None


ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(3)
ll.printLinkedList()
ll.head.next.next.next.next = ll.head.next.next
ll.detectLoop()
ll.printLinkedList()
