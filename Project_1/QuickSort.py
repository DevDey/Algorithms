# Takes two sorted arrays and merges them together


def partition(arr, last):
    for i in range(last):

        # Reursively merge sorts an array


def quickSort(arr):
    if len(arr) > 1:
        last = len(arr)
        pivot = partition(arr, last)
        quickSort(arr[pivot:])
        quickSort(arr[:pivot])

# Print array


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [5, 2, 3, 4, 1, 1, 2, 4, 50, 23, 12, 52, 12, 422, 112, 893212, 21,
       23, 4, 4214, 421, 21312, 241, -1, -2311, 0, -213, 41212, 21, 2145, 657]
print("Before Sorting: ")
printArray(arr)
quickSort(arr)
print("After Sorting: ")
printArray(arr)
