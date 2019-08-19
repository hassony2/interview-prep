def median2sorted(arr1, arr2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    len1 = len(arr1)  # 4
    len2 = len(arr2)  # 4
    tot_len = len1 + len2  # 8
    odd = tot_len % 2  # 0
    if odd:
        med_idx1 = (tot_len - 1) / 2
    else:
        med_idx1 = tot_len / 2 - 1  # 4
    # Start with two pointers outside of array
    p1 = - 1
    p2 = - 1
    if len1 and len2:
        # Need to compare
        if arr1[0] < arr2[0]:
            arr_idx = 1
            p1 = 0
        else:
            arr_idx = 2
            p2 = 0
    # Only items left in one of the two arrays, advance that one
    elif len1:
        arr_idx = 1
        p1 = 0
    else:
        arr_idx = 2
        p2 = 0
    
    # Termination condition: if two pointers at 0, len of left (including current pointers) is 2
    # We want the array to grow until item med_idx1 is included so len(left) - 1 == mid_idx1
    # stop if len(left) - 1 > mid_idx1 p1 + p2 + 2 - 1 >= med_idx1, p1 + p2 + 1 >= med_idx1
    # So while p1 + p2 + 1 < med_idx1
    while p1 + p2  + 1 < med_idx1:
        # Both arrays still have candidates
        if p1 + 1 < len1 and p2 + 1 < len2:
            # Compare next candidates at two next positions
            if arr1[p1 + 1] < arr2[p2 + 1]:
                p1 = p1 + 1
                arr_idx = 1
            else:
                p2 = p2 + 1
                arr_idx = 2
        # Advance only array where items remain
        elif p1 + 1 < len1:
            p1 = p1 + 1
            arr_idx = 1
        else:
            p2 = p2 + 1
            arr_idx = 2
            
    # p1 or p2 are now pointing at mid_idx1 --> get median first value
    if arr_idx == 1:
        med1 = arr1[p1]
    else:
        med1 = arr2[p2]  # 5

    if odd:
        med2 = med1  # 5
    else:
        # Need to get second median value to average by advancing one of the two pointers
        if p1 + 1 < len1 and p2 +1 < len2:
            if arr1[p1 + 1] < arr2[p2 + 1]:
                med2 = arr1[p1 + 1]
            else:
                med2 = arr2[p2 + 1]
        elif p1 + 1 < len1:
            med2 = arr1[p1 + 1]
        else:
            med2 = arr2[p2 + 1]
    return (med1 + med2) / 2  # 5

if __name__ == "__main__":
  listss = (([], [1, 2, 3, 4]),([], [2, 3]), ([1, 2], [3, 4]), ([1, 2, 3], [1, 2]))
  for lists in listss:
      print(lists[0], lists[1], median2sorted(lists[0], lists[1]))
