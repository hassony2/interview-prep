from copy import deepcopy

def quicksort(arr, start_idx, end_idx):
    if start_idx < end_idx:
        smaller_idx = start_idx
        for j in range(start_idx, end_idx):
            if arr[j] < arr[end_idx]:
                arr[smaller_idx], arr[j] = arr[j], arr[smaller_idx]
                smaller_idx += 1
        arr[smaller_idx], arr[end_idx] = arr[end_idx], arr[smaller_idx]
        quicksort(arr, start_idx, smaller_idx - 1)
        quicksort(arr, smaller_idx + 1, end_idx)
    return arr

def mergesort(arr, start_idx, end_idx):
    if end_idx - start_idx > 1:
        midx = int((start_idx + end_idx)/ 2)
        mergesort(arr, start_idx, midx)
        mergesort(arr, midx, end_idx)
        merge(arr, start_idx, end_idx, midx)
    return arr

def merge(arr, start_idx, end_idx, midx):
    left = arr[start_idx:midx]
    right = arr[midx:end_idx]
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[start_idx + i + j] = left[i]
            i += 1
        else:
            arr[start_idx + i + j] = right[j]
            j += 1
    while i < len(left):
        arr[start_idx + i + j] = left[i]
        i += 1
    while j < len(right):
        arr[start_idx + i + j] = right[j]
        j += 1

arrs = [[], [1], [2, 3, 1, 8, -3, 10]]
for arr in arrs:
    print(arr, quicksort(deepcopy(arr), 0, len(arr) - 1))
    print(arr, mergesort(deepcopy(arr), 0, len(arr) - 1))
