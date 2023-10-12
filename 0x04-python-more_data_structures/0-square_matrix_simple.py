#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result = []
    for mat in matrix:
        re = []
        for m in mat:
            re.append(m**2)
        result.append(re)
    return (result)
