def square_matrix_simple(matrix=[]):
    if matrix is not None:
        list_sq = [[x**2 for x in row] for row in matrix]
        return ("{}".format(list_sq))
