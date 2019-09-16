def argsort(nums):
    return [idx for idx, val in sorted(enumerate(nums), key=lambda x: x[1])]
