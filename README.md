# Longest palindrome in linked list

## [Solution](max-palindrome.py)

[GeekForGeeks Explaination](http://practice.geeksforgeeks.org/problems/length-of-longest-palindrome-in-linked-list/1)

## Notes 

Result in n^2 time complexity

Iterate over the items of the list while constructing a reverse list

Uses symetry of palindrom to check if it is one by comparing the reverse and current lists

Treats separately even and uneven palindroms (for each step, check both the even and uneven case)


### Max of more then 2 values

python's max can be used to keep track of max value when comparing more then 2 values

current_max = 2

current_max = max(current_max, some_value, other_value)

### copy and reference 

When you assign an object as attribute of an object, you assign the value that it references

Therefore if after that you change the reference associated with this second variable, you don't affect the original object


Example : 

```python
class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_

next_next_n = Node(4)
next_n = Node(3, next_next_n)
current = Node(2, next_n)
next_n = None # next_n no longer points to the same spot as current.next_
print(current.next_.data) # prints 3
```

## logical and

**and** is the keyword !

# remove duplicates in linked list

Without a temporary buffer

Exo 2.1 from HTCI

## Solution

With a temporary buffer :

- first pass construct a hash-map (python dic) that counts the number of occurences of a character

- second pass remove the char until only one instance of each char

Without temporary buffer :

- iterate over the list

- remove in the preceding list all duplicates of the current value

# Find n-th to last item in a singly linked list

## [Solution](n-th-to-last-singly-linked-list.py)

Use two pointers offset by n

## Notes

### Exceptions

User defined exception

```python
class MyException(Exception):
    pass

raise MyException("My message")
```

No need to import Exception !

# First non repeating char in stream 

## [Solution](first-non-repeating-character-in-stream.py)

[GeekForGeeks Explanation](http://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/)

Two data structures : 

- a list to keep track of the candidates for the next unrepeated character

- another list or dic to record number of instances of the character up to the current char

## Complexity

O(n^2) in time (for each char, if second-time it is met, might have to go through the candidate list to remove it)

O(n) in space

# Rotate image 90 degrees

## [Solution](rotate-im-square.py)

Do it in place by cyclic permutations

Mostly indexing problems, check manually results with specific values

## Complexity 

O(n) in time

additional space O(1)

# All unique characters

Exo 1.1 in HTCI

## [Solution](all_unique_chars.py)

## Notes 

`in` operation is usually O(1) for dic (and O(n) for list)

worse case for dic if all keys in dic have same hash value, then complexity is O(n)


# Matrix col and rows to 0

Exo 1.7 from HTCI

0 rows and columns where a zero is present

## Gotcha

Needs two passes to first note where zeros have to occur and then apply them

## [Solution](row-col-to-zero.py)

# Is_rotation from is_substring

Determine if a string is a rotation from the other

## Solution

First check if equal length, if yes, concatenate first string to itself and check if the second is a substring of this concatenation

# Quicksort

Inplace sorting in O(n*log(n))

First try : 1h04, lots of problems with <= and indexes !

##[Solution](quicksort.py)

## Notes

### Increment

simply

`a += 1`

### Swap variables 

Evaluation is done from left to right, so
`a, b = b, a`
works

### Indexes

backward idx has to start at len(to_sort_list) - 1


**carefull!**

```python
my_list = [1, 2]
my_list[1:1] = []
```

# Negative before positive in place

Rearrange a given array in-place such that all the negative numbers occur before positive numbers.
(Maintain the order of all -ve and +ve numbers as given in the original array)


## [Solution](negative-before-positive.py)

Similar to bubble sort (bubble sort goes through list comparing adjacent pairs and orders them until no swaps are required ==> n^2)

## Complexity 

Worse case : O(n^2) if all negatives are after all positives for instance

# Remove middle node linked list

Given only access to that node

Exo 2.3 from CTCI

## [Solution](remove-node-linkedlist.py)

Copy the data of the next node to the current one and reference to the next.next to next

# Linked list sum

Exo 2.4 from CTCI

## [Solution](sum-linked-list.py)

# Find beginning of cycle in linked list


## Notes

### Reference equality 

```python
if f1 is f2:
    pass
```

# Find node at beginning of linked list

Exo 2.5 from CTCI

## [Solution](find-node-beginning-cycle.py)

Steps :

- Find a random node inside the cycle : for this start a fast pointers in front of slow pointer and check when they meet

- Find cycle size : advance one pointer while keeping the other fixed

- Find beginning : launch two pointers with offset of cycle size, they meet at beginning !


# Stack with min

We want to create a structure that allow us to push pop and query the min in O(1) 

## [Solution](stack-with-min.py)

We notice that the current min is the min of the min up to now and the new value

We therefore keep track of a current min in each node of the stack

But this solution is space intensive ! (lots of duplicate mins)

Possible to keep the mins in another stack, and check when we pop weather we have popped a minimal value

# Hanoi towers

Exo 3.4 of CTCI

Move towers using 3 sticks by never putting a bigger disk on a small disk

Code using 3 stacks

Recursive algorithm, the difficulty is to abstract the problem

An easy way to get started is to code move_tower for tower of size n as a function of move_tower for a tower of size n - 1 

In the end, very few lines of code !

## [Solution](tower-of-hanoi.py) 

# Subarrays summing to zero

Count them

## [Solution](zero-sums.py)

_hint_ : what can you say about the cumulative sums

- if twice the same value --> the inbetween sum is 0

- if zeros : the inbetween sum starting at zero is 0

- you have to take into account that if cumsum has same value more then twice (or once for 0), we have to count the number of ways we can assemble the subarrays (2 parmi number_of_repetitions)

## Remember

math.factorial is the best way to compute factorials

k in between n can be easilly coded using formula fact(n)/(fact(k)*fact(n - k)), but carefull about edge cases : k > n !

# Target three sum

Find the sum of 3 items in a list that is closest to a given target and return the given sum.

## [Solution](three-target-sum)

Brute force is in O(n^3).
We can get to O(n^2) by sorting the array.
We then go through the list and use two beginning/end pointers that we update as needed to increase or decrease the proximity to the target

## Remember 

lists have sort method _that returns None_, so we should use it as

`my_list.sort()`

# Largest rectangle in binary matrix

[Problem](https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/)

## Related problems

### Largest square in binary matrix

**Spot dynamic programming problem !**

- Store size of largest square in the top-left direction in bottom-right position
- if above left and diagonal above-left max square sizes are known
  - if 1 at current position: max-square size is min of all 3 max square sizes + 1 (min(a[i, j-1], a[i-1, j], a[i-1, j-1]) + 1)
- time complexity : n^2 (go through the whole array once)

### Largest rectangle under histogram

- TODO [see here](https://www.geeksforgeeks.org/largest-rectangle-under-histogram/)

## Edit distance

[Problem](https://www.geeksforgeeks.org/edit-distance-dp-5/)

#### Hints

- What if one of the strings is empty ? (--> dist is length of other word)
- What if both words start with same character ? (--> equivalent to skipping this letter and continuing)
- Max number of operations ? (--> max(len(word1), len(word2))
- spot **Dynamic Programming**
  - What is the state ? (--> advancement in both words: start_idxs for words 1 and 2)
- [Solution saving intermediate solutions](https://www.geeksforgeeks.org/edit-distance-dp-5/) (although I did with memoization by having (start_idx1, start_idx2) as state keys)

## Interleaving strings

Can s3 be obtained by interleaving s1 and s2 ?

Examples:

- s1="aab", s2="baa", s3="abaaba" --> True
- s1="aab", s2="baa", s3="abcaba" --> False

Hint:
- sanity check: if len(s1) + len(s2) != len(s3) return False right away !

### Brute force
- Create all interleavings of s1 and s2, and check if s3 belongs to them
- complexity < 2^(len(s1) + len(s2))

### Better
- spot the dynamic programming problem !
  - s3[p1 + p2:] is interleave s1[p1:] and s2[p2:] if first character of s3 matches (at least) one of the two remaining strings and the offseted problem by that character is also a valid interleave
    - s1[p1] == s3[p1+p2] and interleave(s1[p1+1:], s2[p2:], s3[p1+p2+1:]
    - or s2[p2] == s3[p1+p2] and interleave(s1[p1:], s2[p2+1:], s3[p1+p2+1:]
  - state: advancement in characters for each word: p1 for s1 and p2 for s2 (which means we are at p1 + p2 for s3)
- solved with memoization

Notes:
- string comparison in python
  - ==, >, <, <= != compares strings lexicographycally

see [solution](https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/)

## Min_jump_nb

#### Problem 

Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array.

#### Clarifying questions

- all values are positive, can be zero ?
- fits in memory ?
- non-empty list ?


#### Brute-force
- start from beginning, and recursively create a tree of reachable paths
- complexity ~ max_number_of_jumps^len(array)

#### Better solution O(n^2)

- overlapping optimal subproblems --> **dynamic programming**
- store at each idx jump budget it is to get there (state: array_idx) 

#### Best solution O(n)

https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/


# Median of sorted arrays

### Reminders on medians of arr

- if odd (len(arr) % 2 == 1): `median = (arr[tot_len / 2 - 1] + arr[tot_len / 2] ) / 2` 
   - median_idx1 = tot_len / 2 - 1
   - median_idx2 = tot_len / 2
- if even (len(arr) % 2 == 0): `median = arr[(tot_len - 1) / 2]`
   - median_idx1 = median_idx2 = (tot_len - 1) / 2
   
   
## Simple merge-sort solution with 2 pointers 


- start with two pointers p1 and p2 at -1
- check if len of two arrays is odd or even
- find the array and idx that points to first median_idx 
- while the size of the array spanned by the two pointers is smaller then median_idx1 + 1 (len is 1 + idx of last value)
- compare next candidates for both arrays (if both arrays have next candidates)
- advance pointer for array which has smallest next candidate (at positions p1 + 1 for arr1 and p2 + 2 for arr2)

[median2sorted](median2sorted.py)

- complexity O(len(arr1) + len(arr2))

#### Notes
- think long and hard about edge cases (before indexing, will you get an outofbound error ?)
- beware of off-by-one errors !
  - if we want to idx at position k, we need array of length k + 1
- Identify clearly
  - current state:
    - pointers at given positions
  - candidate next state
  - termination condition depending on current state

## faster divide and conquer approach

- notice that media is such that all values on left are small and all values on right are larger and both contain 1/2 of values in array
- get median of each array
- compare their values and deduce which parts (right or left) contain the median
- if med(arr1) == med(arr2): this is the median !
- if med(arr1) < med(arr2): keep right side of arr1 and left side of arr2
- if med(arr1) > med(arr2): keep left side or arr1 and right side of arr1

[Solution](https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/)

#### Notes

- lots of base cases to handle  (6!)
- include the comparison value when taking subarray
- differentiate even and odd cases


