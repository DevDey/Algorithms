
# Takes two sorted arrays and merges them together


def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Fill in the rest
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
# Reursively merge sorts an array


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)

# Print array


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [5, 2, 3, 4, 1, 1, 2, 4, 50, 23, 12, 52, 12, 422, 112, 893212, 21,
       23, 4, 4214, 421, 21312, 241, -1, -2311, 0, -213, 41212, 21, 2145, 657]
print("Before Sorting: ")
printArray(arr)
mergeSort(arr)
print("After Sorting: ")
printArray(arr)
