## Minimal refresher check-list in order of priority

- [x] Binary search
- [ ] Merge sort
- [ ] Quick sort
- [ ] BFS
- [ ] DFS
- [ ] Djikstra
- [ ] Insert/remove node in linked list
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
