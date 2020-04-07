To Know
=======

# General interview steps

- CLARIFY I/O: Restate or clarify the inputs and outputs in your own words (function parameters, function return type)
   - Example clarifications
      - "In what data structure are the inputs provided ?"
      - are the contents valid / negative / zero / lowercase
- EXAMPLE: Give a short example of inputs and outputs, this helps check you understood the question and it's also useful to test the code you write later (given this input, the function returns this output)
- ASSUMPTIONS: State your assumptions, the problem statement doesn't usually contain any 
   - Example assumptions
      - do things fit in "memory, How large is the data (array, dict, ...) ?"
      - are things sorted, how often will the function be run)
- FIRST: Suggest a first, naive, brute-force solution, walk through how it works, give the time and space complexity (make sure to say it's brute-force and you intend to find something better)
- SECOND: Suggest a second, better solution, go back and forth with suggestions and clarifications until you reach consensus about what to go ahead and implement, also give the time and space complexity
- CODE: Write code for the agreed solution, talk through it (handle edge cases at the top of the function, but don't spend too long on them, if they're not trivial leave a comment there and get back to it later)
- TEST: Run through the code line by line with the example you gave at the start (and ideally a few more examples, including at least one edge case)


# Useful semi-advanced python

[real python interview tips](https://realpython.com/python-coding-interview-tips/)

# Basic data structure complexities in python

[dict, set, list, dequeue](https://wiki.python.org/moin/TimeComplexity)

# Recursion in python

### Maximum recursion depth

- ~1000
- to change it: `sys.setrecursionlimit(1500)`

# Counting

In case itertools is not allowed !  

- Permutations
  
```python
def permutations(array):
    """Order matters"""
    if len(array) == 1:
        return [[array[0]]]
    else:
        res = []
        for char_idx in range(len(array)):
            rem_perms = permutations(array[:char_idx] + array[char_idx + 1:])
            for perm in rem_perms:
                res.append([array[char_idx]] + perm)
        return res

arr = [2, 2, 5]
print(permutations(arr))
# >> [[2, 2, 5], [2, 5, 2], [2, 2, 5], [2, 5, 2], [5, 2, 2], [5, 2, 2]]
len(permutations(arr))
# >> math.factorial(len(arr)) / math.factorial(2)
```

- Arrangements

Like permutations order matters, but only take a subsets instead of whole sequence 
  
```python
def arrangements(array, rem_len=1):
    """Order matters!"""
    if rem_len == 1:
        return [[item] for item in array]
    else:
        res = []
        for char_idx in range(len(array)):
            sub_combs = arrangements(array[:char_idx] + array[char_idx + 1:], rem_len=rem_len - 1)
            for sub_comb in sub_combs:
                res.append([array[char_idx]] + sub_comb)
        return res

arr = [2, 2, 5]
print(arrangements(arr, 2))
# >> [[2, 2], [2, 5], [2, 2], [2, 5], [5, 2], [5, 2]]



def combinations(arr, n, previous=None):
    """Orders does not matter"""
    if previous is None:
        previous = [[]]
    if n == len(arr):
        return [arr + prev for prev in previous]
    if n == 0:
        return previous
    else:
        # Include first element
        new_combs_with = combinations(arr[1:], n - 1, [[arr[0]] + prev for prev in previous])
        # Skip first element and continue
        new_combs_without = combinations(arr[1:], n, previous)
        return new_combs_with + new_combs_without



len(combinations(arr))
# >> math.factorial(len(arr)) / math.factorial(2) 
```


 
# Sortings 

[test them here](https://leetcode.com/problems/sort-an-array/submissions/)

## Quick-sort

```python
quicksort(nums, 0, len(nums) - 1)

def quicksort(nums, low, high):
    if low < high:
        pivot_idx = partition(nums, low, high)
        quicksort(nums, low, pivot_idx - 1)
        quicksort(nums, pivot_idx + 1, high)

def partition(nums, low, pivot_idx):
    low_candidate = low
    # all values at successive low_candidate are below pivot
    # stop when all values have been checked (j reaches end)
    # low_candidate therefore points to value > pivot
    for j in range(low, pivot_idx):
        if nums[j] < nums[pivot_idx]:
            # insure value at low_candidate < nums[pivot_idx]
            swap(nums, low_candidate, j)
            low_candidate += 1

    swap(nums, low_candidate, pivot_idx)
    return low_candidate

def swap(nums, idx1, idx2):
    nums[idx1], nums[idx2] = nums[idx2], nums[idx1]


```

Complexity:
- time
  - average O(nlog(n)) (if array size is divided by a constant at each step)
  - worse case : O(n^2), if array already sorted [1, 2, 3, 4] for instance, after first iteration 4 is still at last position and reiterate until 3
- space
  - O(1)
  
## Merge sort


```python

merge_sort(nums, 0, len(nums))

def merge_sort(nums, low, high):
    if low + 2 <= high:  # Continue while at least 2 elements left
        mid_idx = (high + low) // 2 
        merge_sort(nums, low, mid_idx) # merge_sort up to mid_idx excluded
        merge_sort(nums, mid_idx, high) # from mid_idx included to high excluded
        merge(nums, low, high, mid_idx)

def merge(nums, low, high, mid_idx):
    i = 0
    j = 0
    # Make copies of both halves
    left = nums[low:mid_idx] 
    right = nums[mid_idx:high]  # high is not included
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

Complexity
- time: O(log(n))
- space: O(n)

# Trees

Tree traversal :

## Breadth first traversal of trees (not necessarily binary)

**algo**

```python
from collections import deque

def bfs(node):
    queue = deque([node])  # Keep track of nodes to visit
    traversed = []
    while queue:
        node = queue.popleft()
        traversed.append(node.val)
        for child in node.children:
            queue.append(child)
    return traversed

def dfs(node):
    if node.children:
        # Preorder
        traverse = [node.val]
        for child in node.children:
            traverse.extend(dfs(child))
    else:
        return [node.val]
    return traverse

class Node(object):
    def __init__(self, val, children=None):
        if children is None:
            self.children = []
        else:
            self.children = children
        self.val = val

root = Node(1,
    children=[Node(2), Node(3), Node(4, [Node(5)]), Node(6, [Node(7, [Node(8), Node(9), Node(10)])]), Node(11)]
    )
"""
             1
          
  2   3     4     6     11
           /     /
          5     7
              / | \
             8  9  10
"""
res = bfs(root)
print(res)
# >> [1, 2, 3, 4, 6, 11, 5, 7, 8, 9, 10]
res = dfs(root)
print(res)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

## Depth first traversal of Binary trees

- can be in-order, pre-order and post-order depending on where root is inserted
  - in-order : [left, root, right] (only defined for **Binary**) tree
  - pre-order : [root, left, right]
  - post-order: [left, right, root]
  
```python
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def traversal(root):
    if root is None:
        return [None]
    else:
        # Pre-order
        return [root.val] + self.traversal(root.left) + self.traversal(root.right)
        # In-order
        # return self.traversal(root.left) + [root_val] + self.traversal(root.right)
        # Post-order
        # return self.traversal(root.left) + self.traversal(root.right) + [root_val]
```

- [ ] TODO understand why pre-order and post-order together don't allow to reconstruct tree, see [post](https://www.geeksforgeeks.org/if-you-are-given-two-traversal-sequences-can-you-construct-the-binary-tree/), but (pre-order and in-order) or (post-order and in-order) do.

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
  - `parent_idx(idx) = (idx  - 1) // 2`
  - `child_left(idx) = 2 * idx + 1`
  - `child_right(idx) = 2 * idx + 2`
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

# Graphs

## Djikstra

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
        min_node, min_dist = min([(node, distances[node]) for node in to_visit], key=lambda x: x[1])
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

### Complexity

- Optimal with heap and adjacency list
- (E + V) * log(V)
  - E + V inner loops, log(V) for getting minimum distance and heapifying

## BFS

Same as tree except that need to prevent looping inside cycles by checking if nodes are already visited.


## 

# Bit manipulation

## Python details

```python
# view binary representation
a = 20
bin(20) # > '0b10100' # with type string

# view number from binary string
int('10101', 2) # > 21 #in base 2

```

# Disjoint Set Union

See [leetcode](https://leetcode.com/problems/redundant-connection/solution/) for tutorial.

Useful to keep track of connected components, and making operations on them (efficiently **joining** them (union operation) and **finding** whether two items belong to same component (find operation) )

The main idea is:
- initialize a list of parents
- if parent of node is itself, the node is a lead
- while parent != node we can recursively search the parent for equality with it's parent to bubble up to the lead of the connected component
- to perform union, we find the two leads and make one the parent of the other (ideally the one that has the least children should become the parent)

```python
class DSU(object):
    def __init__(self, max_value):
        self.parents =  list(range(max_value))  
        # self.ranks = [0] * max_value

    def find(self, val):
        if self.parents[val] == val:
            return val
        else:
            return self.find(self.parents[val])
    
    def union(self, value1, value2):
        lead1 = self.find(value1)
        lead2 = self.find(value2)
        # Optionnally keep track of rank and add node with highest rand as parent of the other TODO
        self.parents[lead1] = lead2
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

> Avoid using the + and += operators to accumulate a string within a loop. Since strings are **immutable**, this creates unnecessary temporary objects and results in quadratic rather than linear running time.

**Solution**: add each substring to a list and ''.join the list after the loop terminates 

# Arrays

## Manipulating lists

- insert items
  - `arr.append(val)`
  - `arr.insert(idx, val)` # TODO check
- remove items
  - `arr.pop(idx_to_pop)`: Removes item by idx defaults to last element (-1), returns element
  - `arr.remove(val)`: Removes first occurence of value in list: arr.remove(val), returns None
- `arr.sort()`: Inplace sorting, returns None
- `sorted(arr): returns sorted array in **ascending** order
- `from collections import deque`  *deque* spelled like this !
  - for stack: `append()` and `pop()`
  - for queue: `append()` and `popleft()`

## Manipulating sets

- sets are mutable, but can only contain **hashable** elements (tuples, ints, floats, strings, ...)
  - `myset.add(val)` --> `.add()` to add one item
  - `myset.update([val1, val2, val3])` --> `.update(some_iterable)`

## Useful itertools

## List methods

```python
arr = [1, 2, 3, 3, 4]
arr.pop()  # >> 4, arr -> [1, 2, 3, 3]
del arr[2]  # arr -> [1, 2, 3]

arr = [1, 2, 3, 3, 4]
del arr[1:3]  # arr -> [1, 3, 4]
```

## Useful itertools

```python
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

But in most cases it is better to use for loops or list comprehensions !

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

# Generators

- Example of generator that reverses a string

```python
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]
```

# Heaps

```
import heapq
arr = [23, 1, 67, 3, 2, 4, 5]
heapq.heapify(arr)
# > [1, 2, 4, 3, 23, 67, 5]
heapq.heappop(arr)
# > 1
heapq.heappush(arr, 4)
# > [2, 3, 4, 5, 23, 67, 4]  # Parent of 4 (position 6 is at position (6 - 1) // 2 -> 2, so it is 4 which is <= 4)
heapq.nsmallest(arr, 3)
heapq.nlargest(arr, 3)
```
