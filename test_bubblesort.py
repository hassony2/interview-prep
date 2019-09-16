from bubble_sort import bubble_sort
import numpy as np

def test_bubblesort():
    list1 = [0, 3, 4, 5, 1, 9]
    list2 = []
    list3 = [1]
    list4 = [0, 1, 2, 3, 4]
    list5 = [-2, 1, 1, 3, 1]
    lists = [list1, list2, list3, list4]
    for listt in lists:
        sorted_list, sorted_idxs = bubble_sort(np.copy(listt))
        assert np.array_equal(np.sort(listt), sorted_list)
        assert np.array_equal(np.argsort(listt), sorted_idxs)
