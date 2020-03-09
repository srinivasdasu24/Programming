
from Interviewquestions.LinkedList.deleteanode import *


def checkLoop(llist):
    slow = llist.head
    fast = llist.head
    while slow.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            removeLoop(llist,slow)
            return
def removeLoop(llist,slow):
    ptr1 = llist.head
    ptr2 = slow
    while(1):
        while ptr2.next != ptr2 and ptr2.next != ptr1:
            ptr2 = ptr2.next
        if ptr2.next == ptr1:
            break
        ptr1 = ptr1.next
    ptr2.next = None

def removeLoop1(self, loop_node):
    ptr1 = loop_node
    ptr2 = loop_node

    # Count the number of nodes in loop
    k = 1
    while(ptr1.next != ptr2):
        ptr1 = ptr1.next
        k += 1

    # Fix one pointer to head
    ptr1 = self.head

        # And the other pointer to k nodes after head
    ptr2 = self.head
    for i in range(k):
        ptr2 = ptr2.next

        # Move both pointers at the same place
        # they will meet at loop starting node
    while(ptr2 != ptr1):
        ptr1 = ptr1.next
        ptr2 = ptr2.next

        # Get pointer to the last node
    while(ptr2.next != ptr1):
        ptr2 = ptr2.next

        # Set the next node of the loop ending node
        # to fix the loop
    ptr2.next = None

llist = LinkedList()
llist.pushNode(20)
llist.pushNode(4)
llist.pushNode(15)
llist.pushNode(10)
llist.pushNode(18)
llist.printList()
llist.head.next.next.next.next = llist.head
checkLoop(llist)
llist.printList()
