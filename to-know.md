To Know
=======

# Questions to ask

- How large is the data (array, dict, ...)
- Is there any structure in the data (sorted ? less then some maximum value ?) 
- Do the values in the structure have a specific meaning ?

# Useful semi-advanced python

[real python interview tips](https://realpython.com/python-coding-interview-tips/)

# Recursion in python

### Maximum recursion depth

- ~1000
- to change it: `sys.setrecursionlimit(1500)`

# Counting

In case itertools is not allowed !  

- Permutations
  
```python
def permutations(array):
    if len(array) == 1:
        return [[array[0]]]
    else:
        res = []
        for char_idx in range(len(array)):
            rem_perms = permutations(array[:char_idx] + array[char_idx + 1:])
            for perm in rem_perms:
                res.append([array[char_idx]] + perm)
        return res

def permutations_lc(array):
    """
    Same but with list comprehensions
    """
    if len(array) == 1:
        return [array]
    else:
        return [[array[char_idx]] + perm for char_idx in range(len(array)) for perm in permutations(array[:char_idx] + array[char_idx + 1:])]

print(permutations_lc([2, 2, 5]))
print(permutations([2, 2, 5]))
# >> [[2, 2, 5], [2, 5, 2], [2, 2, 5], [2, 5, 2], [5, 2, 2], [5, 2, 2]]
```

- Combinations
  
```python
def combinations(array, rem_len=1):
    if rem_len == 1:
        return [[item] for item in array]
    else:
        res = []
        for char_idx in range(len(array)):
            sub_combs = combinations(array[:char_idx] + array[char_idx + 1:], rem_len=rem_len - 1)
            for sub_comb in sub_combs:
                res.append([array[char_idx]] + sub_comb)
        return res

print(combinations([2, 2, 5], 2))
# >> [[2, 2], [2, 5], [2, 2], [2, 5], [5, 2], [5, 2]]
```


 
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

Probably better (less copies):

```python

def merge_sort(nums, low, high):
    if high - low > 1:
        mid_idx = int((high + low) / 2)
        merge_sort(nums, low, mid_idx)
        merge_sort(nums, mid_idx, high)
        merge(nums, low, high, mid_idx)

def merge(nums, low, high, mid_idx):
    i = 0
    j = 0
    left = nums[low:mid_idx]
    right = nums[mid_idx:high]
    while i < len(left) and j < len(right):
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

```python
class Node:
    def __init__(self, children=None):
        self.children = children

def breadth_first(root):
    if not root:
        return []
    else:
        stack = []  # Here list is used as stack
        stack.append(root)
        return traversal(stack)

def traversal(stack):
    if(stack):
        while stack:
            current = stack.pop()
            for child in current.children():
                stack.append(child)
            return [current.value] + (traversal(stack))
    else:
        return []
```

for depth-first change stack to queue

## Trie

- Example of trie construction for characters, here to create all possible combinations of sequence of characters from a given sequence (see https://leetcode.com/problems/letter-tile-possibilities/)

```python
def construct_trie(tiles, res=None):
    for char_idx in range(len(tiles)):
        rem_tiles = tiles[:char_idx] + tiles[char_idx + 1:]
        res[tiles[char_idx]] = construct_tree(rem_tiles, {})
    return res
    
def traverse_trie(tree, depth=1):
    results = []
    if depth == 0:
        return ['']
    elif depth == 1:
        return tree.keys()
    else:
        results.extend(tree.keys())
        for key in tree.keys():
            results.extend([key + rem for rem in traverse_tree(tree[key], depth=depth-1)])
    return results

tiless = ['AAB', 'AB']
for tiles in tiless:
    tree = construct_tree(tiles, {})
    print(tree)
    results = traverse_tree(tree, depth=len(tiles))
    print(results)
    print(len(set(results)))
```

# List methods

```
```


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

If have to write it, with loop better then with (won't exceed max stack in python which is roughly **1000**).

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


# Strings

### Manipulation

```python
# Remove substring between idx1 and idx2
chars = chars[:idx1] + chars[idx2:]

# Replace char
chars = chars.replace(a, b)  # Not in place ! Need to return
```

# Arrays


## List methods

```python
arr = [1, 2, 3, 3, 4]
arr.pop()  # >> 4, arr -> [1, 2, 3, 4]
arr.popleft()  # >> 1, arr -> [2, 3, 4]
del arr[2]  # arr -> [2, 3]

arr = [1, 2, 3, 3, 4]
del arr[1:3]  # arr -> [1, 3, 4]
```

## Useful itertools

`import itertools`

## Generate permutations
list(itertools.permutations('abc'))
# >> [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

## Nested for loops
list(itertools.product('abc', 'de', 'f'))
# >> [('a', 'd', 'f'), ('a', 'e', 'f'), ('b', 'd', 'f'), ('b', 'e', 'f'), ('c', 'd', 'f'), ('c', 'e', 'f')]

## Dénombrement

### combinations
 list(itertools.combinations('abc', 2))
# >> [('a', 'b'), ('a', 'c'), ('b', 'c')]

### combinations *with* replacement

# >> list(itertools.combinations_with_replacement('abc', 2))

### Permutations

list(itertools.permutations('abc'))
# > [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

# Also allows to get all possible (ordered) combinations of given size

list(itertools.permutations('aac', 2))
# > [('a', 'a'), ('a', 'c'), ('a', 'a'), ('a', 'c'), ('c', 'a'), ('c', 'a')]

## Cycle through elements
cycle = itertools.cycle('abc')
[next(cycle) for idx in range(10)]
# >> ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a']
```

### Functional utilities

```python
import functools
import itertools

### Apply function to inputs
list(map(pow, (1, 2, 3), (2, 2, 4)))

### Cumsums
list(itertools.accumulate([1, 2, 3, 4]))

### List of factorials
list(itertools.accumulate([1, 2, 3, 4, 5], lambda acc, cur: acc * cur))
# >> [1, 2, 6, 24, 120]
functools.reduce(lambda acc, cur: acc * cur, range(1, 5 + 1))
# >> 120
```
