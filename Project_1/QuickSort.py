"""Quicksort"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            swap = arr[i]
            arr[i] = arr[j]
            arr[j] = swap
    swap = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = swap
    return i + 1


def quickSort(arr, low, high):

    if (low < high):
        """ pi is partitioning index, arr[pi] is now
           at right place """
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)  # Before pi
        quickSort(arr, pi + 1, high)  # After pi


# Print array


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [5, 2, 3, 4, 1, 1, 2, 4, 50, 23, 12, 52, 12, 422, 112, 893212, 21,
       23, 4, 4214, 421, 21312, 241, -1, -2311, 0, -213, 41212, 21, 2145, 657]
print("Before Sorting: ")
printArray(arr)
quickSort(arr, 0, len(arr)-1)
print("After Sorting: ")
printArray(arr)
