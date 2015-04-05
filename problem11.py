"""Project Euler - Problem 11 - http://projecteuler.net/problem=11"""
import sys
import time
# please install numpy module (python-numpy on Arch Linux)
import numpy as np
import tools.timeutils as timeutils


def fill_matrix():
    """
    Return a numpy matrix from the data in problem11-data.txt
    """
    array = []
    with open('problem11-data.txt', 'r') as f:
        for line in f:
            array.append(line.strip())

    # this is just a 2d array, not a matrix
    matrix_array = np.loadtxt('problem11-data.txt', delimiter=' ')
    # this is a matrix
    np_matrix = np.bmat(matrix_array)
    return np_matrix


def largest_product_horizontally(matrix):
    """
    Computes the largest product horizontally (line by line) on a given matrix
    """
    largest_product = 1
    for line in range(0, matrix.shape[0]):
        for column in range(0, matrix.shape[1]-3):
            product = int(matrix[line, column] *
                          matrix[line, column+1] *
                          matrix[line, column+2] *
                          matrix[line, column+3])
            if product > largest_product:
                largest_product = product
    return largest_product


def largest_product_vertically(matrix):
    """
    Computes the largest product vertically (column by column)
    on a given matrix
    """
    # rotating the matrix
    vertical_matrix = np.rot90(matrix)
    return largest_product_horizontally(vertical_matrix)


def largest_product_diagonally(matrix):
    """
    Computes the largest product diagonally (NW, NE, SE, SW)
    on a given value [x, y]
    """
    product_nw = 1
    product_ne = 1
    product_se = 1
    product_sw = 1
    largest_product = 1
    for line in range(0, matrix.shape[0]):
        for column in range(0, matrix.shape[1]):
            try:
                # NW
                product_nw = int(matrix[line, column] *
                                 matrix[line-1, column-1] *
                                 matrix[line-2, column-2] *
                                 matrix[line-3, column-3])
                # NE
                product_ne = int(matrix[line, column] *
                                 matrix[line-1, column+1] *
                                 matrix[line-2, column+2] *
                                 matrix[line-3, column+3])
                # SE
                product_se = int(matrix[line, column] *
                                 matrix[line+1, column+1] *
                                 matrix[line+2, column+2] *
                                 matrix[line+3, column+3])
                # SW
                product_sw = int(matrix[line, column] *
                                 matrix[line+1, column-1] *
                                 matrix[line+2, column-2] *
                                 matrix[line+3, column-3])
            except IndexError:
                pass
            max_product = max(product_nw, product_ne, product_se, product_sw)
            if max_product > largest_product:
                # update the largest value found
                largest_product = max_product
            # resetting products for the 4 diagonals
            product_nw = 1
            product_ne = 1
            product_se = 1
            product_sw = 1
    return largest_product


def main():
    """Main entry point for the script"""
    start = time.time()
    # create a matrix from the problem data
    matrix = fill_matrix()
    # compute the largest value from the matrix on a horizontal traversal
    value_horizontally = largest_product_horizontally(matrix)
    print("horizontally: " + str(value_horizontally))
    # compute the largest value from the matrix on a vertical traversal
    value_vertically = largest_product_vertically(matrix)
    print("vertically: " + str(value_vertically))
    # compute the largest value from the matrix on a diagonal traversal
    value_diagonally = largest_product_diagonally(matrix)
    print("diagonally: " + str(value_diagonally))
    print("largest product found is: " +
          str(max(value_horizontally, value_vertically, value_diagonally)))
    timeutils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
