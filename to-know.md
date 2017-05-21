To Know
=======

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

## Factorial

most easy way to use it :

```python
import math

math.factorial(100)
```

If have to write it, with loop better then with stack (won't exceed max stack in python which is roughly **1000**).