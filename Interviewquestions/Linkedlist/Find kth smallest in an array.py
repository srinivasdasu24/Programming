'''

    Author : Dasu Srinivas
    Description: Given an array A and an number K, find the Kth smallest number in the given array

    Solution: Applying partial quick sort algorithm by bringing pivot element to its position and sort around elements
              time complexity is 0(n) on average, worst is 0(n^2)

'''


def partition(arr,l,r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def kthsmallest(arr,l, r, k):
    if k > 0 and k <= r-l+1:
        pos = partition(arr,0,r)
        if pos - l == k-1:
            return arr[pos]
        if pos - l > k - 1:
            return kthsmallest(arr, l, pos - 1, k)
        return kthsmallest(arr,pos+1, r, k-pos+l-1)


print(kthsmallest([3,5,1,8,15,2,35,87,4], 0, 8, 6))