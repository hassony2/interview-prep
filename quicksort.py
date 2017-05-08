# def quicksort(to_sort):
#     """
#     first dirty solution
#     """
#     if(len(to_sort) <= 1):
#         return to_sort
#     if(len(to_sort) == 2):
#         if(to_sort[0] > to_sort[1]):
#             return [to_sort[1], to_sort[0]]
#         else:
#             return to_sort

#     pivot = to_sort[0]
#     fwd_idx = 1
#     back_idx = len(to_sort) - 1

#     while (fwd_idx <= back_idx and fwd_idx <= len(to_sort) - 1):
#         if(to_sort[fwd_idx] >= pivot and to_sort[back_idx] <= pivot):
#             to_sort[fwd_idx], to_sort[back_idx] = to_sort[back_idx], to_sort[fwd_idx]
#             fwd_idx += 1
#             back_idx -= 1
#         else:
#             # Progress while items on the right side of pivot
#             if(to_sort[fwd_idx] < pivot and fwd_idx < len(to_sort) - 1):
#                 fwd_idx += 1

#             if(to_sort[back_idx] > pivot):
#                 back_idx -= 1
#     if (fwd_idx < back_idx):
#         # fwd_idx - 1 = back_idx
#         to_sort = (quicksort(to_sort[1:fwd_idx]) +
#                    [pivot] + quicksort(to_sort[fwd_idx:]))
#     else:
#         # fwd_idx == back_idx
#         if(to_sort[fwd_idx] >= pivot):
#             to_sort = (quicksort(to_sort[1:fwd_idx]) +
#                        [pivot] + quicksort(to_sort[fwd_idx:]))
#         else:
#             to_sort = (quicksort(to_sort[1:fwd_idx - 1]) +
#                        [pivot] + quicksort(to_sort[fwd_idx - 1:]))
#     return to_sort


def quicksort(a_list):
    quicksort_(a_list, 0, len(a_list) - 1)


def quicksort_(a_list, first, last):
    if(first < last):
        pivot = partition(a_list, first, last)
        quicksort_(a_list, first, pivot - 1)
        nquicksort_(a_list, pivot + 1, last)


def partition(a_list, first, last):
    """
    :return: final position of the pivot
    """
    # put pivot at the end (pivot is at first position at first)
    swap(a_list, first, last)

    # Separate > and < pivot
    # Works as following :
    # First does virtually nothing until idx value > pivot_value
    # When first > pivot_value is met, idx gets ahead of first
    # from this point on first marks the first value that is above the pivot
    # if no > pivot_value is found, first ends up at last
    # and last swap doesn't change anything
    for idx in range(first, last):
        if(a_list[idx] < a_list[last]):
            # track first value > pivot from the left
            swap(a_list, idx, first)
            first += 1
    swap(a_list, first, last)
    return first


def swap(a_list, i, j):
    """
    Swaps values of given list in place
    """
    a_list[i], a_list[j] = a_list[j], a_list[i]


if __name__ == "__main__":
    test_list = [7, 3, 5, 8, 2, 10, 4, 5, 11, 1]
    print(test_list)
    quicksort(test_list)
    print('sorted : ', test_list)
