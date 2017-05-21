def b_search(arr, value):
    beg = 0
    end = len(arr) - 1
    while beg <= end:
        mid = int((end + beg) / 2)
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 4, 5, 8, 10, 27, 38]
    assert(b_search(arr, 4) == 2)
    assert(b_search(arr, 27) == 6)
    assert(b_search([4], 1) == -1)
    assert(b_search([4], 4) == 0)
    assert(b_search([], 10) == -1)

