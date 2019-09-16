class SolutionSortedHash(object):
    """
    Single pass to create a hash_table and check whether target key already in hash table.
    Time and space complexity O(n) because query in good hash_table is O(1).
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_nums = {}
        for second_idx, num in enumerate(nums):
            if num in hash_nums:
                first_idx = hash_nums[num]
                if first_idx != second_idx:
                    return first_idx, second_idx
            hash_nums[target - num] = second_idx

class SolutionSorted(object):
    """Sorting is O(n^2) for bubble sort, memory is O(n) because I explicitly save the idxs.""" 
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums, sorted_idxs = bubble_sort(nums)
        start_ptr = 0
        end_ptr = len(nums) - 1
        while sorted_nums[start_ptr] + sorted_nums[end_ptr] != target:
            current_val = sorted_nums[start_ptr] + sorted_nums[end_ptr]
            if current_val < target:
                start_ptr += 1
            else:
                end_ptr -= 1
        return sorted_idxs[start_ptr], sorted_idxs[end_ptr]
         

def bubble_sort(nums):
    idxs = list(range(len(nums)))
    for loops in range(len(nums)):
        for idx in range(len(nums)):
            lower_idx = idx - 1
            higher_idx = idx + 1
            if higher_idx < len(nums) and nums[higher_idx] < nums[idx]:
                nums[idx], nums[higher_idx] = nums[higher_idx], nums[idx]
                idxs[idx], idxs[higher_idx] = idxs[higher_idx], idxs[idx]
    return nums, idxs
                
def sort(nums):
    if not len(nums):
        return []
    else:
        pivot_idx = 0
        pivot_val = nums[pivot_idx]
    return sort([value for value in nums[1:] if value < pivot_val]) + [pivot_val] + sort([value for value in nums[1:] if value >= pivot_val]) 
        

