
# [Google python styleguide](https://google.github.io/styleguide/pyguide.html)

## Dict/list comprehensions

Do not use (fall back on standard loop) if:
- nested (for instance: `[(x, y) for x in range(10) for y in range(5) if x * y > 10]`)
- complicated to understand 
> Each portion must fit on one line: mapping expression, for clause, filter expression. Multiple for clauses or filter expressions are not permitted. 

```python
# Correct examples
result = [mapping_expr for value in iterable if filter_expr]

result = [{'key': value} for value in iterable
          if a_long_filter_expression(value)]
          
descriptive_name = [
    transform({'key': key, 'value': value}, color='black')
    for key, value in generate_iterable(some_input)
    if complicated_condition_is_met(key, value)
]

```

## Default values

- Okay as long as **immutable**

> Default arguments are evaluated once at module load time. This may cause problems if the argument is a mutable object such as a list or a dictionary. If the function modifies the object (e.g., by appending an item to a list), the default value is modified.

```python
def foo(a, b: Optional[Sequence] = None):
        if b is None:
            b = []
```

## True/False evaluations

> Python evaluates certain values as False in boolean context. **0, None, [], {}, ''** all evaluate as false in a boolean context.
- use if possible instead of `if string:  # and not if string == '':`
- use `is None` or `is not None` if value can be None
- never `if x == False`
- '0' (str) evaluates to True

## Lambda functions

- Okay if one-liners
> For common operations like multiplication, use the functions from the operator module instead of lambda functions. For example, prefer operator.mul to lambda x, y: x * y

## Asserts / Exception

- asserts to check internal logic
- Exceptions for wrong arguments

## Global variables

- don't 
- if needed, use module-level constants `MAX_LINE_NB = 8` for instance

## Nesting

- use _ prefix for functions not intended to be used outside of module (rather then nesting)
- nested functions have read-only access to variables defined in enclosing scopes.

## Default operators and iterators

- use them !
- `for line in a_file: ...  # vs for line in a_file.readlines()`

## Objects

### Properties

- use property decorator
```python
@property
def area(self):
    return self.long_side * self.short_side
```
