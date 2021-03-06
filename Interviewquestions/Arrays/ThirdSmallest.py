'''

Author : Dasu Srinivas
Description : find the third smallest element in the given array

'''
import sys
def thirdSmallest(array):
    first = sys.maxsize
    second = sys.maxsize
    third = sys.maxsize
    for i in range(0, len(array)):
        if array[i] < first:
            third=second
            second=first
            first=array[i]
        elif array[i] < second:
            third=second
            second=array[i]
        elif array[i] < third:
            third = array[i]
    return third

print(thirdSmallest([10,20,3,5,18,9,25,57]))
# output is 9
