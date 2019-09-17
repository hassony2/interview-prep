# Complexity cheat sheet

[python reference complexities](https://wiki.python.org/moin/TimeComplexity)

## Array sorting

[cheat_sheet](https://www.bigocheatsheet.com/)

### Remarks

- Quicksort has n^2 worse case runtime and O(log(n)) space because of the recursion stack **if carefully implemented with tail recursion and other tricks used**
- In my implementation, quicksort would typically use O(n) extra space because of the recursive call stack
- Python uses a variant of timsort, which is a hybrid between merge and insertion sort, and is **stable**, it has O(n*log(n)) run time on average and O(n) space requirement

## Graph

- BFS
  - O(V + E) if adjacency list is used
  - O(V^2) if adjacency matrix
- DFS: same
  - O(V + E) if adjacency list is used
  - O(V^2) if adjacency matrix
