def neg_before_pos(a_list):
    for i in range(len(a_list)):
        if(a_list[i] < 0):
            for j in range(i, 0, -1):
                if (a_list[j - 1] > 0):
                    swap(a_list, j, j - 1)
                else:
                    break


def swap(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]

if __name__ == "__main__":
    test_list = [2, -1, -3, 4 - 5, 7, 6, -3]
    print(test_list)
    neg_before_pos(test_list)
    print(test_list)
