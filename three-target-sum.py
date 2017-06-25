def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    best_target = None
    for i in range(len(nums) - 2):
        beg = i + 1
        end = len(nums) - 1
        best_temp_target = None
        while beg < end:
            cur_sum = nums[i] + nums[beg] + nums[end]
            if best_temp_target is None:
                best_temp_target = cur_sum
            else:
                if abs(best_temp_target - target) > abs(cur_sum - target):
                    best_temp_target = cur_sum
                if cur_sum - target > 0:
                    end = end - 1
                else:
                    beg = beg + 1
        if best_target is None:
            best_target = best_temp_target
        else:
            if abs(best_target - target) > abs(best_temp_target - target):
                best_target = best_temp_target
    return best_target
