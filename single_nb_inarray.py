def single_nb_inarray(array):
    # if you ^ all items in array, all pairs will cancel out
    # and only will remain the single solo element
    val_comp = array[0]
    for val in array[1:]:
        val_comp = val ^ val_comp
    return val_comp


if __name__ == "__main__":
    array = [2, 3, 4, 2, 3, 4, 6, 5, 5, 7, 7]
    print(single_nb_inarray(array), array)
