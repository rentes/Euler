"""
Project Euler - Problem 11
http://projecteuler.net/problem=11
"""

import time
import numpy as np  # please install numpy module (python-numpy on Arch Linux)


def fill_matrix():
    """
    Return a numpy matrix from the data in problem11-data.txt
    """
    array = []
    with open('problem11-data.txt', 'r') as f:
        for line in f:
            array.append(line.strip())

    # this is just a 2d array, not a matrix
    matrixarray = np.loadtxt('problem11-data.txt', delimiter=' ')
    # this is a matrix
    npmatrix = np.bmat(matrixarray)
    return npmatrix


def largest_product_horizontally(matrix):
    """
    Computes the largest product horizontally (line by line) on a given matrix
    """
    product = 1
    largest_product = 1
    for line in range(0, matrix.shape[0]):  # for each line
        for column in range(0, matrix.shape[0]-3):  # for each column
            product = int(matrix[line, column] *
                          matrix[line, column+1] *
                          matrix[line, column+2] *
                          matrix[line, column+3])
            if product > largest_product:
                largest_product = product
        product = 1
    return largest_product


def largest_product_vertically(matrix):
    """
    Computes the largest product vertically (column by column)
    on a given matrix
    """
    matrix_vert = np.rot90(matrix)  # rotating the matrix
    return largest_product_horizontally(matrix_vert)


def largest_product_diagonally(matrix):
    """
    Computes the largest product diagonally (NW, NE, SE, SW)
    on a given value [x, y]
    """
    product_NW = 1
    product_NE = 1
    product_SE = 1
    product_SW = 1
    max_product = 1
    largest_product = 1
    for line in range(0, matrix.shape[0]):  # for each line
        for column in range(0, matrix.shape[0]):  # for each column
            try:
                # NW
                product_NW = int(matrix[line, column] *
                                 matrix[line-1, column-1] *
                                 matrix[line-2, column-2] *
                                 matrix[line-3, column-3])
                # NE
                product_NE = int(matrix[line, column] *
                                 matrix[line-1, column+1] *
                                 matrix[line-2, column+2] *
                                 matrix[line-3, column+3])
                # SE
                product_SE = int(matrix[line, column] *
                                 matrix[line+1, column+1] *
                                 matrix[line+2, column+2] *
                                 matrix[line+3, column+3])
                # SW
                product_SW = int(matrix[line, column] *
                                 matrix[line+1, column-1] *
                                 matrix[line+2, column-2] *
                                 matrix[line+3, column-3])
            except IndexError:
                pass
            max_product = max(product_NW, product_NE, product_SE, product_SW)
            if max_product > largest_product:
                largest_product = max_product  # update the largest value found
            product_NW = 1  # reset product for NW diagonal
            product_NE = 1  # reset product for NE diagonal
            product_SE = 1  # reset product for SE diagonal
            product_SW = 1  # reset product for SW diagonal
    return largest_product


def elapsed_time(elapsed):
    """
    Computes the amount of time spent by the algorithm and outputs the time
    """
    min = int(elapsed / 60)  # minutes
    s = int(elapsed) % 60  # seconds
    ms = int((elapsed - int(elapsed)) * 1000)  # milliseconds
    print('time:', elapsed, 's ~', min, 'min,', s, 's,', ms, 'ms')


# start the timing for this problem
start = time.time()
# create a matrix from the problem data
matrix = fill_matrix()
# compute the largest value from the matrix on a horizontal traversal
value_horizontally = largest_product_horizontally(matrix)
print("horizontally: "+str(value_horizontally))
# compute the largest value from the matrix on a vertical traversal
value_vertically = largest_product_vertically(matrix)
print("vertically: "+str(value_vertically))
# compute the largest value from the matrix on a diagonal traversal
value_diagonally = largest_product_diagonally(matrix)
print("diagonally: "+str(value_diagonally))
# print the largest product found
print("largest product found is: " +
      str(max(value_horizontally, value_vertically, value_diagonally)))
# compute the total time taken for this problem and show it to the user
elapsed_time(time.time() - start)
