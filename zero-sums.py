import math


def count_zero_sums(arr):
    """
    Counts the number of subarrays that sum to 0
    """
    cumul = [sum(arr[:i + 1]) for i in range(len(arr))]
    cumul_res = {}
    cumul_res[0] = 1
    for cum in cumul:
        if cum not in cumul_res:
            cumul_res[cum] = 1
        else:
            cumul_res[cum] += 1
    return sum([k_between_n(2, cum_val) for cum_val in cumul_res.values()])


def k_between_n(k, n):
    """
    count the number of ways we can pick k elements among n candidates
    """
    if (k > n):
        return 0
    else:
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


if __name__ == "__main__":
    # Test k_between_n
    assert(k_between_n(2, 0) == 0)
    assert(k_between_n(2, 1) == 0)
    assert(k_between_n(2, 2) == 1)
    assert(k_between_n(2, 3) == 3)

    test1 = [1, 2, -2, 3, 0]
    assert(count_zero_sums(test1) == 2)
    test2 = [4, 1, -1, 2, -2, 3]
    assert(count_zero_sums(test2) == 3)
    test3 = [1, -1, 2, -1, -1, 4]
    assert(count_zero_sums(test3) == 4)
    test4 = [1, -1, 2, 0, 0, -1, -1, 4]
    assert(count_zero_sums(test4) == 7)
