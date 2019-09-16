def permutations(array):
    if len(array) == 1:
        return [[array[0]]]
    else:
        res = []
        for char_idx in range(len(array)):
            rem_perms = permutations(array[:char_idx] + array[char_idx + 1:])
            for perm in rem_perms:
                res.append([array[char_idx]] + perm)
        return res

def permutations_lc(array):
    """
    Same but with list comprehensions
    """
    if len(array) == 1:
        return [array]
    else:
        return [[array[char_idx]] + perm for char_idx in range(len(array)) for perm in permutations(array[:char_idx] + array[char_idx + 1:])] 

def combinations(array, rem_len=1):
    if rem_len == 1:
        return [[item] for item in array]
    else:
        res = []
        for char_idx in range(len(array)):
            sub_combs = combinations(array[:char_idx] + array[char_idx + 1:], rem_len=rem_len - 1)
            for sub_comb in sub_combs:
                res.append([array[char_idx]] + sub_comb)
        return res

print(permutations_lc([2, 2, 5]))
print(permutations([2, 2, 5]))
print(combinations([2, 2, 5], 2))
