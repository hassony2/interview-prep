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
    p1 = - 1
    p2 = - 1
    if len1 and len2:
        if arr1[0] < arr2[0]:
            arr_idx = 1
            p1 = 0
        else:
            arr_idx = 2
            p2 = 0
    elif len1:
        arr_idx = 1
        p1 = 0
    else:
        arr_idx = 2
        p2 = 0
    while p1 + p2  + 1 < med_idx1:
        if p1 + 1 < len1 and p2 + 1 < len2:
            if arr1[p1 + 1] < arr2[p2 + 1]:
                p1 = p1 + 1
                arr_idx = 1
            else:
                p2 = p2 + 1
                arr_idx = 2
        elif p1 + 1 < len1:
            p1 = p1 + 1
            arr_idx = 1
        else:
            p2 = p2 + 1
            arr_idx = 2
    if arr_idx == 1:
        med1 = arr1[p1]
    else:
        med1 = arr2[p2]  # 5

    if odd:
        med2 = med1  # 5
    else:
        if p1 + 1 < len1 and p2 +1 < len2 and p1 + 1 >= 0 and p2 + 1 >= 0:
            if arr1[p1 + 1] < arr2[p2 + 1]:
                med2 = arr1[p1 + 1]
            else:
                med2 = arr2[p2 + 1]
        elif p1 + 1 < len1 and p1 + 1 >= 0:
            med2 = arr1[p1 + 1]
        else:
            med2 = arr2[p2 + 1]
    return (med1 + med2) / 2  # 5

listss = (([], [1, 2, 3, 4]),([], [2, 3]), ([1, 2], [3, 4]), ([1, 2, 3], [1, 2]))
for lists in listss:
    print(lists[0], lists[1], median2sorted(lists[0], lists[1]))
