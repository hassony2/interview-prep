To Know
=======

# Questions to ask

- How large is the data (array, dict, ...)
- Is there any structure in the data (sorted ? less then some maximum value ?) 

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

## Complete binary tree:

### Min (/max) heap

### Definition

- **complete** binary tree where all children are lower (/or larger) then current root

### Properties
- in this case, min (/or max) of tree is always at the root

### Usages

- priority queues (for instance for djisktra algorithm)
- sorting (by first creating a heap and then repetitively getting the root we get the sorted array) **not heap sort**
  - complexity (time)
     - create the heap : easy to show that O(n * log(n)) (n insertions of max log(n) steps)
       - but actually O(n) (a bit tricky to show, mostly relies on the fact that al lot of the nodes don't need to go all the way down (easy to show that at each depth, work needed to insert is l * 2^l (where l in [0, log(n))], and total work is sum(l*2^l), which is O(n) (proof involves taylor series...)
     - pop n times : n * log(n) because get_min needs to rebalance the tree at each step, which takes at worse log(n)
  - complexity (space)
     - n (needs an additional array)

- related to heap sort:
 - an **in-place algorithm** whith n*log(n) complexity which iteratively heapifies parts of array, less used then merge-sort and quicksort, so not really useful

 - typically not stable
### Implementation

- easiest is to store it as an array with
  - `parent_idx(idx) = (idx  - 1) // 2
  - `child_left(idx) = 2 * idx + 1
  - `child_right(idx) = 2 * idx + 2
- two operations:
  - insertion
  - get_min (/get_max)

- after each operation the min (/max) property needs to be preserved
  - insertion:
    - append at end of array (<=> as right-most leaf of complete binary tree
    - bubble_up : then check if smaller (/larger) then parent, if yes, swap and recurse on parent
    - O(log(node_nb)) because complete binary tree
  - get_min:
    - get value of root (this is the min to return)
    - remove right-most node from array, insert its value at root's position
    - bubble_down :
      - if leaf (no right nor left child), finish
      - if only one (necessarily left) child, swap if needed and recurse (could also directly finish)
      - if 2 children : check if min_rule is infringed (one of the children is smaller then current)
         - correct by operating swap between current and smallest among children (this way the selected child node is larger then parent and sibling)
	 - recurse on swapped position, which now contains the value of the inserted value

```python
class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        self.bubble_up(len(self.arr) - 1)

    def bubble_up(self, idx):
        # Stop if reached root
        if not idx == 0:
            parent_idx = (idx - 1) // 2
            # Only continue if current is smaller then parent
            if self.arr[idx] < self.arr[parent_idx]:
                # Swap !
                self.arr[idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[idx]
                self.bubble_up(parent_idx)

    def get_min(self):
        min_val = self.arr[0]
        # Rebalance by getting last element and putting it to right position
        last_val = self.arr.pop()
        if len(self.arr):
            self.arr[0] = last_val
            self.bubble_down(0)
        return min_val

    def bubble_down(self, idx):
        i_l = 2 * idx + 1
        i_r = 2 * idx + 2
        if i_l > len(self.arr) - 1:
            # Left child outside of array --> current is leaf
            return
        elif i_l == len(self.arr) - 1:
            # Only left child (right child position would be at i_l + 1
            # which is out of array
            if self.arr[i_l] < self.arr[idx]:
                # If needed (leaf is smaller then current), swap
                self.arr[i_l], self.arr[idx] = self.arr[idx], self.arr[i_l]
        else:
            # Both children exist, the only way to respect the heap is to insure
            # that the smallest of the 3 is at the top
            if self.arr[i_l] < self.arr[idx] or self.arr[i_r] < self.arr[idx]:
                # current is not smallest of the two children --> swap needed
                # given that we know that smallest is not at idx
                # it is enough to check which of the children is the smallest
                # to get the smallest of the current and two children
                if self.arr[i_l] < self.arr[i_r]:
                    self.arr[i_l], self.arr[idx] = self.arr[idx], self.arr[i_l]
                    # Current went down, but might have broken the min rule
                    # one level down --> need to check if rule verified at new position
                    self.bubble_down(i_l)
                else:
                    self.arr[i_r], self.arr[idx] = self.arr[idx], self.arr[i_r]
                    self.bubble_down(i_r)
```

# Hash Table

- if chaining is allwed, in each table bin is stored a list of (key, value) tuples where key is the immutable non-hashed key
- if keys are integers, simplest hash function : `hash = key % table_size`
- basic operations : **set**(key, val) **get**(key) **delete**(key)

### Notes and Traps

- raise correct (most specific needed exceptions): `KeyError`
- DO NOT DO [[]] * 3 to initalize table, it initializes a **single list** with 3 references

```python
buggy_list = [[]] * 3   # > [[], [], []]
buggy_list[0].append(2)  # > [[2], [2], [2]]
```python

### Implementation

class HashTable:
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = [[] for _ in range(self.table_size)]

    def hash_func(self, key):
    	# Basic hash_function for integers
        return key % self.table_size

    def set(self, key, value):
        hash_k = self.hash_func(key)
        chain = self.table[hash_k]
	# If present, replace (key, value) at correct position
        for chain_idx, (chain_k, _) in enumerate(chain):
            if chain_k == key:
                chain[chain_idx] = (key, value)
                return
	# Else, chain new value
        chain.append((key, value))

    def get(self, query):
        hash_k = self.hash_func(query)
        chain = self.table[hash_k]
        for key, val in chain:
            if key == query:
                return val
        keys = [key for key, _ in chain]
        raise KeyError('key {query} with hash {hash_k} not in {keys}'.format(query=query, hash_k=hash_k, keys=keys))


    def delete(self, key):
        hash_k = self.hash_func(key)
        chain = self.table[hash_k]
        for chain_idx in range(len(chain)):
            if key == chain[chain_idx][0]:
                val = chain.pop(chain_idx)[1]
                return val
        raise KeyError('key {key} not found at hash_bin with key {hash_k}'.format(key=key, hash_k=hash_k))

```

# Djikstra

Run [djikstra_graph](djikstra_graph.py)

```python
def djikstra(edges, start_node):
    # Get unique nodes
    to_visit = [start_node]
    visited = []
    distances = {start_node: 0}
    # Keep track of paths by memorizing candidate parent
    parents = {start_node: None}
    while len(to_visit):
        # Sort nodes by current distance to source and select the closest one
        min_node, min_dist = sorted([(node, distances[node]) for node in to_visit], key=lambda x: x[1])[0]
        to_visit.remove(min_node)
        # Get edges that link selected node and other nodes, and not already visited
        neigh_edges = [edge for edge in edges if edge[0] == min_node and edge[1] not in visited]
        neigh_nodes = [edge[1] for edge in neigh_edges]
        to_visit += neigh_nodes
        visited.append(min_node)
        for neigh_edge in neigh_edges:
            _, target, dist = neigh_edge
            if target not in distances or dist + min_dist < distances[target]:
                distances[target] = dist + min_dist
                parents[target] = min_node
    return distances, parents
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


# Strings

## Complexity

- immutable
- theoretically insertion is in O(len(array)) (need to copy whole string to new with more space)
- in practice, appending to strings is optimized in CPython so that it now runs in O(1) and extends the string in-place.

### Manipulation

```python
# Remove substring between idx1 and idx2
chars = chars[:idx1] + chars[idx2:]

# Replace char
chars = chars.replace(a, b)  # Not in place ! Need to return

# Test if substring in string
'abc' in 'slfj'  # >> False
'abc' in 'slabcfj'  # >> True
```

# Arrays

## Manipulating lists

- insert items
  - `arr.append(val)`
  - `arr.insert(idx, val)` # TODO check
- remove items
  - `arr.pop(idx_to_pop)`: Removes item by idx defaults to last element (-1), returns element
  - `arr.remove(val)`: Removes first occurence of value in list: arr.remove(val), returns None
- `arr.sort(val)`: Inplace sorting, returns None
- `sorted(arr): returns sorted array in **ascending** order
- `from collections import deque`  *deque* spelled like this !
  - for stack: `append()` and `pop()`
  - for queue: `append()` and `popleft()`

## Manipulating sets

- sets are mutable, but can only contain **hashable** elements (tuples, ints, floats, strings, ...)
  - `myset.add(val)` --> `.add()` to add one item
  - `myset.update([val1, val2, val3])` --> `.update(some_iterable)`

## Useful itertools

```
import itertools

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
