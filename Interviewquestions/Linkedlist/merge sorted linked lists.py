'''

    Author: Dasu srinivas
    Description: Given two sorted linked lists, merge them into a single sorted linked list

'''

import Interviewquestions.Linkedlist.Loopinalinkedlist as LL


def merge_LL(head1, head2):
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        temp = head1
        temp.next = merge_LL(head1.next, head2)
    else:
        temp = head2
        temp.next = merge_LL(head1, head2.next)
    return temp


if __name__ == "__main__":
    l1 = LL.LinkedList()
    l2 = LL.LinkedList()
    l1.push(5)
    l1.push(4)
    l1.push(2)
    l2.push(8)
    l2.push(6)
    l2.push(3)
    l2.push(1)
    l1.head = merge_LL(l1.head, l2.head)
    l1.printLinkedList()