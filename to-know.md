To Know
=======

# Sortings 

[test them here](https://leetcode.com/problems/sort-an-array/submissions/)

## Quick-sort

```python
def quicksort(self, nums, low, high):
    if low < high:
        pivot_idx = self.partition(nums, low, high)
        self.quicksort(nums, low, pivot_idx - 1)
        self.quicksort(nums, pivot_idx + 1, high)

def partition(self, nums, low, pivot_idx):
    low_candidate = low
    # all values at successive low_candidate are below pivot
    # stop when all values have been checked (j reaches end)
    # low_candidate therefore points to value > pivot
    for j in range(low, pivot_idx):
        if nums[j] < nums[pivot_idx]:
            self.swap(nums, low_candidate, j)
            low_candidate += 1

    self.swap(nums, low_candidate, pivot_idx)
    return low_candidate

def swap(self, nums, idx1, idx2):
    nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
self.quicksort(nums, 0, len(nums) - 1)
```

- If array sorted [1, 2, 3, 4] for instance, in partition after first iteration, j = 0, low_candidate = 1

## Merge sort

- How many copies ? More then the n allowed ? In which case keep track of low idx and len of subarray and create copies of array only in merge

```python
def merge_sort(nums):
    if len(nums) > 1:
        mid_idx = int(len(nums)/ 2) 
        left = nums[:mid_idx]
        right = nums[mid_idx:]
        merge_sort(left)
        merge_sort(right)
        merge(nums, left, right)

def merge(nums, left, right):
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[i + j] = left[i]
            i += 1
        else:
            nums[i + j] = right[j]
            j += 1
    while i < len(left):
        nums[i + j] = left[i]
        i += 1
    while j < len(right):
        nums[i + j] = right[j]
        j += 1
```

Probably better (less copies):

```python

def merge_sort(nums, low, high):

    if high - low > 1:
        mid_idx = low + int((high - low) / 2)
        merge_sort(nums, low, mid_idx)
        merge_sort(nums, mid_idx, high)
        merge(nums, low, high, mid_idx)

def merge(nums, low, high, mid_idx):
    i = 0
    j = 0
    left = nums[low:mid_idx]
    right = nums[mid_idx:high]
    k = low
    while i < mid_idx - low and j < high - mid_idx:
        if left[i] <= right[j]:
            nums[low + i + j] = left[i]
            i += 1
        else:
            nums[low + i + j] = right[j]
            j += 1
    while i < len(left):
        nums[low + i + j] = left[i]
        i += 1
    while j < len(right):
        nums[low + i + j] = right[j]
        j += 1
```

# Trees

Tree traversal :

## Breadth first traversal 

**algo**

```
def breadth_first(root):
    if not root:
        return []
    else:
        stack = Stack()
        stack.push(root)
        return traversal(stack)

def traversal(stack):
    if(stack):
        while stack:
            current = stack.pop()
            for child in current.children():
                stack.push(child)
            return [current.value] + (traversal(stack))
    else:
        return []
```

for depth-first change stack to queue

# Bit manipulation

## Python details

```python
# view binary representation
a = 20
bin(20) # > '0b10100' # with type string

# view number from binary string
int('10101', 2) # > 21 #in base 2

```

# Utilities

## format

**floating precision**

```python
print('{0:.5g}'.format(1.1234567)) # >1.12345 #5 numbers after ., and strip useless zeroes
```

# Miscellaneous

NP stands for nondeterministic polynomial time
## P

Solution can be found in polynomial time

### NP

solution can be verified in polynomial time

**P \in NP** but P == NP is an open problem 

## NP-complete

p is NP-complete if any other problem in NP can be transformed into p in polynomial time

Therefore there is a class of NP-complete problems with a **solving one solves them all** (in polynomial time) carrot

### NP hard

Can be reduced in polynomial time to NP complex problem, and therefore harder then any NP-complete algo

(at least as hard as any NP-hard problem)

## Factorial

most easy way to use it :

```python
import math

math.factorial(100)
```

If have to write it, with loop better then with stack (won't exceed max stack in python which is roughly **1000**).

## Efficient mod

quo, rest = divmod(10, 3) # quo == 3, rest == 1

## Dynamic programming

Useful when you can solve a problem using optimal solutions of subproblems.
Two properties:
- overlapping computation (in brute-force approach same problem is computed several times)
- optimal subproblems (solution at stage m does indeed depend on solution for previous stages)
Typically can also be solved by recursion, but recursion sub-optimal: computes subproblems more then once (typically not in O(1) ) !

How to solve:
- store intermediary solutions
  - bottom up: (tabulation: save solution for first state(s), second state(s), ...
  - as you go: memoization: check if result is aleardy available in hash_table where key is state
    - if yes, use it
    - if no, compute it then add it

- crucial to determine state as a way that is suitable for tabulation (key is sequence of indexes) or memoization (hashable state)

#### Typical examples

[Computing Fibonacci sequence](fibonacci.py) (can be done recursively but much more efficient dynamically with memoization or tabulation).
