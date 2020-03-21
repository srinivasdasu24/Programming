'''

    Author: Dasu Srinivas
    Description: Given an array, sort the array using heap sort

'''


def heapify(arr, n, i):
    large = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[large] < arr[left]:
        large = left
    if right < n and arr[large] < arr[right]:
        large = right
    if large != i:
        arr[i], arr[large] = arr[large], arr[i]
        heapify(arr, n, large)


def heapsort(arr):
    arr_len = len(arr)
    for i in range(int(arr_len/2)-1, -1, -1):
        heapify(arr, arr_len, i)

    for i in range(arr_len - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12,11,5,7,13,6]
heapsort(arr)
print(arr)