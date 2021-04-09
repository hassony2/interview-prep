## Minimal refresher check-list in order of priority

- [x] Binary search
- [x] Quick sort
- [x] BFS
- [x] DFS
- [ ] Djikstra
- [x] Insert/remove node in linked list
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

    # Ensure all values to the left of low_candidate are < pivot_val
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

# BFS and DFS

```python
import pytest
from collections import deque


class Node():
    def __init__(self, root, children=None):
        self.value = root
        if children is None:
            self.children = []
        else:
            self.children = children

def tree_search(node, mode="breadth") -> list:
    tovisit = deque()
    tovisit.append(node)
    flat = []
    while len(tovisit):
        if mode == "breadth":
            # Create queue for breadth first
            visit_node = tovisit.popleft()
        elif mode == "depth":
            # Create stack for depth first
            visit_node = tovisit.pop()
        else:
            raise ValueError(f"{mode} not in [depth|breadth]")
        flat.append(visit_node.value)
        if len(visit_node.children):
            if mode == "breadth":
                children = visit_node.children
            elif mode == "depth":
                # Need to reverse order to traverse from left to right
                # otherwise still depth-first but from right to left
                children = reversed(visit_node.children)
            for child in children:
                tovisit.append(child)
    return flat
            
    
def test_bfscomplex():
    tree = Node(0, [Node(3), Node(2, [Node(5), Node(7)]), Node(4, [Node(1)])])
    #                    0
    #               3    2    4
    #                  /  \   |
    #                  5  7   1
    flat_b = tree_search(tree, mode="breadth")
    assert flat_b == [0, 3, 2, 4, 5, 7, 1]
    flat_d = tree_search(tree, mode="depth")
    assert flat_d == [0, 3, 2, 5, 7, 4, 1]
    
    
def test_bfsimple():
    tree = Node(0, [Node(1)])
    flat_b = tree_search(tree, mode="breadth")
    assert flat_b == [0, 1]
    flat_d = tree_search(tree, mode="depth")
    assert flat_d == [0, 1]
Node(3)
pytest.main()
```

## Linked lists

In-place or with returns ?
Below example of node removal in singly-linked list in-place

```python
import pytest

class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def __repr__(self):
        toshow = self.get_nodes()
        return " ".join([str(val) for val in toshow])

    def get_nodes(self):
        nodes = [self.value]
        child = self.next_node
        while child is not None:
            nodes.append(child.value)
            child = child.next_node
        return nodes
        
def remove(llist, rm_idx:int):
    node = llist
    if rm_idx == 0:
        # Overwrite first node
        if node.next_node is None:
            return None
        else:
            node.value = node.next_node.value
            node.next_node = node.next_node.next_node
        return
    # Point to predecessor of node to remove
    for idx in range(rm_idx - 1):
        node = node.next_node

    node.next_node = node.next_node.next_node
    return llist

    

def test_remove():
    llist = Node(3, Node(4, Node(5, Node(6))))
    assert llist.get_nodes() == [3, 4, 5, 6]
    
    remove(llist, 2)
    assert llist.get_nodes() == [3, 4, 6]
    
    # Remove first node
    llist = Node(3, Node(4, Node(5, Node(6))))
    remove(llist, 0)
    assert llist.get_nodes() == [4, 5, 6]
    
    # Remove last node
    llist = Node(3, Node(4, Node(5, Node(6))))
    remove(llist, 3)
    assert llist.get_nodes() == [3, 4, 5]
    
pytest.main()
```
