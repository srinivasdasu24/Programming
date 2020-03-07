'''

    Author : Dasu Srinivas
    Description: Given an array of elements and an element X, find a pair in array with sum exactly as x and print

    Solution 1: using hashing we can solve the problem in 0(n) time
    Solution 2: First sort the array and take two indices one at left most and other at right most, check for sum if
                less increase left most else decrease right most, time complexity depends on sorting algorithm

'''


def findpair(arr, x):
    hashset = set()
    for i in range(0,len(arr)):
        if (x-arr[i]) in hashset:
            print("pair with given sum %s is" %(x), arr[i], x-arr[i])
        hashset.add(arr[i])


findpair([1,2,3,4,5,6,7,8],8)
