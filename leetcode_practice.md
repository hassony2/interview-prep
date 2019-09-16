
[bubble_sort.py](bubble_sort.py)
[sum2_totarget](sum2_totarget)

### 2sum

Find indices of two items in array that sum to given target.
- idx_1 != idx_2 should be not possible or checked explicitly
- hash_table is a good way to go to retrieve idx from value

### 3sum2zero

Find triplets of values that sum to 0.
No duplicate arrays

#### Solution [sum3to0](sum3_to0.py)

- Traverse array and apply modified 2sum where two lists and target are given as input and complementary from right list is searched for in left list
- target is current value, and left and right sublists are inputs to 2sum
- post-process remove duplicates by sorting each triplet in tuple and applying set()

#### Mistakes

- forgot to remove duplicates
- append returns None, so append and add appended list in separate statements
- missed cases where several combination of left-right values for 2sum (returned only one instead of all 2sum targets)
- solution still slow (bottom 23% in speed, 16% in memory)

### Shuffling list

Idea to do this **inplace** Fisher-Yates algorithm:
You want to randomly pick without putting back an item in the list.
This is achieved by:
- randomly drawing the first item to be in 0th position among all candidates
  - swapping items at indexes random.randint(1, len(list) - 1) and 0
- randomly drawing the second item to be in 1th position among all remaining candidates
  - swapping items at indexes random.randint(2, len(list) - 1) and 1
- ...

Time complexity: O(n) if random.randint(1, n) is in constant time.

#### Solution [shuffling](shuffling.py) [test_shuffling](test_shuffling.py)

#### Notes

- random.randint(a, b) returns values in [a, b] (a and b **included**)

#### Mistakes

- looped until len(list) not len(list) **- 1** --> results in error when try to random.randint(a, b) with b < a, (a==b is fine, returns a which is also b)


