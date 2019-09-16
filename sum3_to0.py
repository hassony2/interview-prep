def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    for idx in range(len(nums)):
        two_sum_res = twoSum(nums[:idx], nums[idx+1:], - nums[idx])
        if len(two_sum_res):
            three_sum_res = [tuple(sorted(res + [nums[idx], ])) for res in two_sum_res]
            results.extend(three_sum_res)
    return set(results)


def twoSum(nums_left, nums_right, target):
    got_nums = []
    nums_left = set(nums_left)
    nums_right = set(nums_right)
    for second_num in nums_left:
        if target - second_num in nums_right:
            got_nums.append([second_num, target - second_num])
    return got_nums
