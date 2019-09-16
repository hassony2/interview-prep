import numpy as np

from argsort import argsort

def test_argsort():
    list1 = [0, 3, 4, 5, 1, 9]
    list2 = []
    list3 = [1]
    list4 = [0, 1, 2, 3, 4]
    list5 = [-2, 1, 1, 3, 1]
    lists = [list1, list2, list3, list4]
    for listt in lists:
        sorted_idxs = argsort(np.copy(listt))
        assert np.array_equal(np.argsort(listt), sorted_idxs)
