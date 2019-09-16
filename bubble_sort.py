def bubble_sort(nums):
    idxs = list(range(len(nums)))
    for loops in range(len(nums)):
        for idx in range(len(nums)):
            higher_idx = idx + 1
            if higher_idx < len(nums) and nums[higher_idx] < nums[idx]:
                nums[idx], nums[higher_idx] = nums[higher_idx], nums[idx]
                idxs[idx], idxs[higher_idx] = idxs[higher_idx], idxs[idx]
    return nums, idxs


def bubble_sort_better(arr):
    # Each iteration will bring max remaining item to correct position
    for idx1 in range(len(arr)):
        # Bubble up until end, then end - 1, ...
        stop_idx = len(arr) - idx1
        for idx2 in range(stop_idx - 1):
            # idx2 + 1 not at target position of max
            # if left value higher then right position, bubble up left value
            if arr[idx2] > arr[idx2 + 1]:
                arr[idx2], arr[idx2 + 1] = arr[idx2 + 1], arr[idx2]
    return arr


print(bubble_sort([-2, 4, 2, 1, 2, 5]))
