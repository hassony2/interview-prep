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