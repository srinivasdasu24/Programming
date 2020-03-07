'''

    Author: Dasu Srinivas
    Description: Given an array A having elements from 1 to N, find the duplicate element in the array

'''


def duplicate_ele(arr):
    for i in range(0,len(arr)):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            return abs(arr[i])


print(duplicate_ele([5,3,1,4,3]))
