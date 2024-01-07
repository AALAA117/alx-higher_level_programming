#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for num in row:
                if row.index(num) != len(row) - 1:
                    print("{:d}".format(num), end=' ')
                else:
                    print("{:d}".format(num), end='')
            print()
