def permutations(arr):
    if len(arr):
        all_perms = []
        for idx in range(len(arr)):
            rem_perms = permutations(arr[:idx] + arr[idx + 1:])
            for rem_perm in rem_perms:
                all_perms.append([arr[idx]] + rem_perm)
        return all_perms
    else:
        return [[]]

def combinations(arr, size=2):
    assert len(arr) > size, 'Asked more items ({}) then size of arr {}'.format(size, len(arr))
    if size == 0:
        return [[]]
    else:
        all_combs = []
        for idx in range(len(arr)):
            rem_combs = combinations(arr[:idx] + arr[idx + 1:], size=size - 1)
            for rem_comb in rem_combs:
                all_combs.append([arr[idx]] + rem_comb)
        return all_combs


arrs = [[1, 2, 3]]
for arr in arrs:
    print(permutations(arr))
    print(combinations(arr, size=2))
