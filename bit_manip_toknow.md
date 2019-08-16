# Bit manipulation in python

- Get bit string from integer `bin(323)  # '0b101000011'`
- Apply bit operations on integers `323 & 23  # 3` as bin(323) & bin(23) **will fail** because & is not supported by strings
- operators : &, |, ^ (exclusive or, if both are 0 --> 1), ~ (flips == complements), x >> y (right shift: x * 2^y), x << y (left shift: x / 2 ^y)
 
## Exercises

#### Count set bits


Brute force : Sum all bits, complexity O(log(n))

Better: 
- Brian Kernighau's algorithm [count_set_bits](count_set_bits.py)
  - Hint : What happens if you "&" x and x - 1
  - Complexity: O(nb_set_bits)

#### Single nb in array

Brute force:
  - hash_map: store if found, remove if already present O(n) time, O(n) space
  - take first element, compare to all next ones, remove both elements if found, O(n^2) time, O(1) space

Better: using bit manipulation [single_nb_inarray](single_nb_inarray.py)
   - Hint: how do you check that two numbers are the same using bit operators ? (answer: xor (^) is 0) 
   - compare all numbers using ^ (all pairs will cancel out)
   - Complexity: O(n) time, O(1) space
  
