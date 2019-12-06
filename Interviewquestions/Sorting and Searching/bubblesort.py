'''

Author : Dasu Srinivas
Description: Given an array, sort it using bubble sort algorithm

'''
def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bubbleSort([2,10,9,27,1,13,6]))