class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def deleteNode(self, data):
        count = 0
        temp = self.head
        prev = self.head
        if temp.data == data:
            if temp.next is None:
                print("Can't delete the node as it has only one node")
            else:
                temp.data = temp.next.data
                temp.next = temp.next.next
            return
        while temp.next is not None and temp.data != data:
            prev = temp
            temp = temp.next
            count += 1
        if temp.next is None and temp.data !=data:
            print("Can't delete the node as it doesn't exist")
        elif temp.next is None and temp.data == data:
            prev.next = None
        else:
            prev.next = temp.next
    def pushNode(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")
    def lengthOfList(self):
        count = 0
        temp = self.head
        while temp:
            count = count + 1
            temp = temp.next
        return count

llist = LinkedList()
llist.pushNode(2)
llist.pushNode(4)
llist.pushNode(5)
llist.pushNode(10)
llist.pushNode(15)
#llist.printList()
#llist.deleteNode(4)
#llist.printList()