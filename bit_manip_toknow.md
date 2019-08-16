# Bit manipulation in python

- Get bit string from integer `bin(323)  # '0b101000011'`
- Apply bit operations on integers `323 & 23  # 3` as bin(323) & bin(23) **will fail** because & is not supported by strings
- operators : &, |, ^ (exclusive or, if both are 0 --> 1), ~ (flips == complements), x >> y (right shift: x * 2^y), x << y (left shift: x / 2 ^y)
 
## Exercises

#### Count set bits


Brute force : Sum all bits

Better: 
- Brian Kernighau's algorithm [count_set_bits](count_set_bits.py)
  - Hint : What happens if you "&" x and x - 1
