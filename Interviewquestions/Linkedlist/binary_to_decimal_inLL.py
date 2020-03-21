'''

    Author: Dasu Srinivas
    Description:  Given a binary number in a linked list, give its equivalent decimal number as output

'''


import Interviewquestions.Linkedlist.Loopinalinkedlist as LL


def getDecimal(binary):
    '''decimal = ''
    while binary:
        decimal += str(binary.data)
        binary = binary.next
    return int(decimal, 2)'''
    # another solution
    result = 0
    while binary:
        result = result << 1
        result += binary.data
        binary = binary.next
    return result
    #return 0 if binary is None else getDecimal(binary.next) + (1<<decimal++)*(binary.data);


def getDecimal1(binary):
    decimal = []
    while binary:
        decimal.append(binary.data)
        binary = binary.next
    decimal_res = 0
    for i in range(len(decimal)):
        decimal_res += 2 ** (len(decimal)-i-1) * decimal[i]

    return decimal_res


if __name__ == "__main__":
    l1 = LL.LinkedList()
    l1.push(0)
    l1.push(1)
    l1.push(0)
    l1.printLinkedList()
    print(getDecimal(l1.head))