'''

Author : Dasu Srinivas
Description: Given an array with elements from 1 to n, sort the given array using count sort

'''


def count_sort(arr):
    i=0
    while i < len(arr):
        if 0 < arr[i] <= len(arr):
            if arr[arr[i]-1] != arr[i]:
                arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            else:
                i += 1
        else:
            i += 1
    return arr


print(count_sort([5,3,1,4,2]))