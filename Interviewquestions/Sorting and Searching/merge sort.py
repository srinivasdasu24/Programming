'''
    Author: Dasu Srinivas
    Description: Given an unsorted array, sort the given array using merge sort
'''

'''
def mergeSort(ar_list):
    if len(ar_list) > 1:
        mid = len(ar_list) // 2
        left = ar_list[:mid]
        right = ar_list[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the left and right half
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                ar_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                ar_list[k] = right[j]
                j += 1
            k += 1

        # For all the remaining values
        while i < len(left):
            ar_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ar_list[k] = right[j]
            j += 1
            k += 1


ar_list = [12, 7, 2, 9, 4, 15, 5]
mergeSort(ar_list)
print(ar_list)
'''


def merge(left, right):
    result = []
    x, y = 0, 0
    for k in range(0, len(left) + len(right)):
        if x == len(left):  # if at the end of 1st half,
            result.append(right[y])  # add all values of 2nd half
            y += 1
        elif y == len(right):  # if at the end of 2nd half,
            result.append(left[x])  # add all values of 1st half
            x += 1
        elif right[y] < left[x]:
            result.append(right[y])
            y += 1
        else:
            result.append(left[x])
            x += 1
    return result


def mergesort(ar_list):
    length = len(ar_list)
	size = 1
	while size < length:
		size+=size # initializes at 2 as described
		for pos in range(0, length, size):
			start = pos
			mid   = pos + int(size / 2)
			end = pos + size
			left  = ar_list[ start : mid ]
			right = ar_list[ mid : end ]
			ar_list[start:end] = merge(left, right)
	return ar_list

ar_list = [33, 42, 9, 37, 8, 47, 5]
print(mergesort(ar_list))
#print(ar_ar_list)
