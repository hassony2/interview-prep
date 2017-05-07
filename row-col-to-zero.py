import numpy as np


def row_col_to_zeros(in_matrix):
    """
    Sets row and col to zero if contains a zero
    """
    row_nb, col_nb = in_matrix.shape
    flagged_rows = {}
    flagged_cols = {}

    # Find rows and cols that contain zeros
    for row in range(row_nb):
        for col in range(col_nb):
            if(in_matrix[row, col] == 0):
                flagged_rows[row] = True
                flagged_cols[col] = True

    # fill new matrix
    for row in range(row_nb):
        for col in range(col_nb):
            if(row in flagged_rows or col in flagged_cols):
                in_matrix[row, col] = 0

    return in_matrix

if __name__ == "__main__":
    rows = 6
    cols = 5
    in_mat = np.random.random_integers(0, 4, size=(rows, cols))
    print(in_mat)
    out_mat = row_col_to_zeros(in_mat)
    print(out_mat)
