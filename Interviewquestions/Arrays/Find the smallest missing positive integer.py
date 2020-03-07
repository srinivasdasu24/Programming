'''

Author: Dasu Srinivas
Description: Given an array with unique elements, find the smallest missing positive integer

'''

def missing_PI(arr):
    i = 0
    while i < len(arr):
        if 0 < arr[i] <= len(arr):
            if arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            else:
                i += 1
        else:
            i += 1
    for i in range(0, len(arr)):
        if arr[i] != i+1:
            return i+1

print(missing_PI([-2,3,0,1,2,3,5]))