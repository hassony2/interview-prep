def balanced_scalar_prod(v_1, v_2):
    """
    assumes v_1 and v_2 are sorted by indexes (first value in tuple)
    :param: v_i sparse vector as list of pairs (idx, values)
    :return: scalar product of the two sparse vectors
    """

    i_1 = 0
    i_2 = 0
    prod = 0
    while i_1 < len(v_1) and i_2 < len(v_2):
        if(v_1[i_1][0] == v_2[i_2][0]):
            prod += v_1[i_1][1]*v_2[i_2][1]
            i_1 += 1
            i_2 += 1
        elif v_1[i_1][0] < v_2[i_2][0]:
            i_1 += 1
        else:
            i_2 += 1
    return prod


def unbalanced_scalar_prod(v_1, v_2):
    """
    Assumes len(v1) << len(v2)
    """
    prod = 0
    for idx, val in v_1:
        v2_i = b_search(v_2, idx)
        if v2_i >= 0:
            prod += val*v_2[v2_i][1]
    return prod


def b_search(vec, val):
    beg = 0
    end = len(vec) - 1
    while beg <= end:
        mid = int((end + beg)/2)
        mid_val = vec[mid][0]
        if mid_val == val:
            return mid
        elif mid_val < val:
            beg = mid + 1
        else:
            end = mid - 1
    return - 1


if __name__ == '__main__':
    v_1 = [(1, 1), (2, 4), (5, -1), (7, 3), (10, 2), (13, 1)]
    v_2 = [(2, -1), (6, 2), (7, -2), (8, 2), (13, -1)]
    prod = balanced_scalar_prod(v_1, v_2)
    print("found {res} expected -11".format(res=prod))
    unbalanced_prod = unbalanced_scalar_prod(v_1, v_2)
    print("found {res} expected -11".format(res=unbalanced_prod))
