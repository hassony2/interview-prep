def bubble_sort(nums):
    idxs = list(range(len(nums)))
    for loops in range(len(nums)):
        for idx in range(len(nums)):
            higher_idx = idx + 1
            if higher_idx < len(nums) and nums[higher_idx] < nums[idx]:
                nums[idx], nums[higher_idx] = nums[higher_idx], nums[idx]
                idxs[idx], idxs[higher_idx] = idxs[higher_idx], idxs[idx]
    return nums, idxs
