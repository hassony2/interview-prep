## Minimal refresher check-list in order of priority

- [x] Binary search
- [x] Quick sort
- [ ] BFS
- [ ] DFS
- [ ] Djikstra
- [ ] Insert/remove node in linked list
- [ ] Merge sort
- [ ] Modular rules
- [ ] Bit manipulation


## Algos

Binary search

```python
def verify(array: list, query:float, pred:int, res: int):
    if res != pred:
        raise ValueError(f"Found incorrect idx {pred} != {res} for {query} in {array}")

def bin_search(array: list, query: float) -> int:
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_val = array[mid]
        if mid_val == query:
            return mid
        elif query < mid_val:
            end = mid - 1
        elif query > mid_val:
            start = mid + 1
    return -1

test_cases = [
              ([], 34, -1),
              ([1], 1, 0),
              ([1], 2, -1),
              ([0, 1, 2, 4], 2, 2),
              ([-2, 3, 4, 4, 10], 10, 4),
              ([-2, 3, 4, 4, 10], 3, 1),
              ([1, 4], 1, 0),
              ([-10, 3], 3, 1),
              ([-8, 2], 3, -1),
             ]

for test_case in test_cases:
    arr, query, true_idx = test_case
    res_idx = bin_search(arr, query)
    verify(arr, query, true_idx, res_idx, )
```

## Quicksort

```python
import pytest


def swap(array, idx1, idx2):
    array[idx2], array[idx1] = array[idx1], array[idx2]
    
def partition(array: list, start_idx:int, pivot_idx:int) -> int:
    low_candidate = start_idx
    pivot_val = array[pivot_idx]

    for idx in range(start_idx, pivot_idx):
        if array[idx] < pivot_val:
            swap(array, idx, low_candidate)
            low_candidate += 1
    swap(array, low_candidate, pivot_idx)
    return low_candidate

def quicksort(array: list, start_idx:int, end_idx:int) -> list:
    if start_idx < end_idx:
        pivot_idx = partition(array, start_idx, end_idx)
        quicksort(array, start_idx, pivot_idx - 1)
        quicksort(array, pivot_idx + 1, end_idx)
    return array
        
def test_partition():
    test_cases = [
            ([1], [1], 0, 0, 0),
            ([1, 2], [1, 2], 0, 1, 1),
            ([1, 3, 2], [1, 2, 3], 0, 2, 1),
            ([21, -10, 44, 55], [-10, 21, 44, 55], 0, 2, 2),
            ([-10, 51, 44, 55], [-10, 44, 51, 55], 0, 2, 1),
    ]        
    for test_case in test_cases:
        to_part, parted, start_idx, end_idx, pivot_idx = test_case
        comp_pivot_idx = partition(to_part, start_idx, end_idx)
        assert pivot_idx == comp_pivot_idx, f"Wrong pivot idx {comp_pivot_idx} != {pivot_idx} for {to_part} with start: {start_idx}, end: {end_idx}"

    
def test_sort():
    test_cases = [
            ([], []),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([21, -10, 44, -2], [-10, -2, 21, 44]),
    ]        
    for test_case in test_cases:
        arr_tosort, arr_sorted = test_case
        arr_sorted_pred = quicksort(arr_tosort, 0, len(arr_tosort) - 1)
        assert arr_sorted_pred == arr_sorted, f"Quicksort result {arr_sorted_pred} != {arr_sorted} for array {arr_tosort}"

test_partition()
test_sort()
```
