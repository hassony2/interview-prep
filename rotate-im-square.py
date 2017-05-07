import numpy as np
import matplotlib.pyplot as plt


def rotate_img(img):
    sq_size = len(img[0])
    for row in range(int(sq_size/2)):
        sq_max_index = sq_size - 1
        last_row = sq_max_index - row
        last_col = sq_max_index - row
        first_col = row
        for col in range(first_col, last_col):
            temp = img[row][col]
            img[row][col] = img[col][last_col]
            img[col][last_col] = img[last_row][sq_max_index - col]
            img[last_row][sq_max_index - col] = img[sq_max_index - col][row]
            img[sq_max_index - col][row] = temp
    return img


if __name__ == "__main__":
    square_size = 20
    np.random.seed(0)
    numpy_img = np.random.rand(square_size, square_size)

    img = numpy_img.tolist()
    fig1 = plt.figure(1)
    ax1 = plt.subplot(121)
    ax1.matshow(numpy_img)
    ax2 = plt.subplot(122)
    ax2.matshow(rotate_img(img))
    fig1.show()
    input()
    print(img)
