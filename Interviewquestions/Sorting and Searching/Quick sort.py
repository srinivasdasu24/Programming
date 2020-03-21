'''

    Author: Dasu Srinivas
    Description : Given an array of elements, implement quick sort algorithm for sorting the given array

'''

'''def partition(my_arr, start, end):
    pivot = my_arr[end]
    i = start - 1

    for j in range(start, end):
        if my_arr[j] <= pivot:
            i = i + 1
            my_arr[i], my_arr[j] = my_arr[j], my_arr[i]
    my_arr[i + 1], my_arr[end] = my_arr[end], my_arr[i + 1]
    return i + 1


def quicksort(my_arr, start, end):
    if start < end:
        q = partition(my_arr, start, end)
        quicksort(my_arr, start, q - 1)
        quicksort(my_arr, q + 1, end)


arr = [15, 9, 11, 2, 21, 12]
quicksort(arr, 0, 5)
print(arr)'''


def partition(my_arr, start, end):
    pivot = my_arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and my_arr[high] >= pivot:
            high = high - 1
        while low <= high and my_arr[low] <= pivot:
            low = low + 1
        if low <= high:
            my_arr[low], my_arr[high] = my_arr[high], my_arr[low]
        else:
            break
    my_arr[start], my_arr[high] = my_arr[high], my_arr[start]
    return high


def quicksort(my_arr, start, end):
    if start < end:
        q = partition(my_arr, start, end)
        quicksort(my_arr, start, q - 1)
        quicksort(my_arr, q + 1, end)


arr = [15, 9, 11, 2, 21, 12, 7]
quicksort(arr, 0, 6)
print(arr)
