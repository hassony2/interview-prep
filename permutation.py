
def permutations(arr, n):
    """Order matters"""
    if n == 0:
        return [[]]
    else:
        permuts = []
        for item_idx, item in enumerate(arr):
            permuts.extend([[item] + permut for permut in permutations(arr[:item_idx] + arr[item_idx + 1:], n - 1)])
        return permuts

def arrangement_with_replacement(arr, n):
    """Order matters"""
    if n == 0:
        return [[]]
    else:
        arrangs = []
        for item in arr:
            arrangs.extend([[item] + arrang for arrang in arrangement_with_replacement(arr, n - 1)])
        return arrangs


def combinations(arr, n, previous=None):
    if previous is None:
        previous = [[]]
    """Orders does not matter"""
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




# def perm_count(k, arr):
#     n = len(arr)
#     perm_count = 0
#     for i in range(0, k):
#         perm_count = perm_count * 
"""
perms([1, 2, 3], 2)
permuts <- []
0, 1
arr[:item]
permuts <- [ ] <- [[2]]


"""


arrs = [[0, 1, 2]]
for arr in arrs:
    print(permutations(arr, 2))
    print(arrangement_with_replacement(arr, 2))
    print(combinations(arr, 2))
